# -*- coding:utf-8 -*-
import os
import win32gui,win32con,win32api
from PIL import Image
import tempfile
import requests as rr
import datetime

class WallpaperSetting():
    def __init__(self,API="http://115.28.228.126/externalInterFace/bingpic.php",specFolder=None):
        """
        可选参数: API地址
        可选参数: 存放的文件夹specFolder
        如果指定一个文件夹,壁纸将被存放在该文件夹中
        """
        self.specFolder = specFolder
        self.API = API

    def __setBMPWallpaper(self,imagepath):
        k = win32api.RegOpenKeyEx(
            win32con.HKEY_CURRENT_USER, "Control Panel\\\\Desktop", 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(
            win32con.SPI_SETDESKWALLPAPER, imagepath, 1 + 2)
        print('Today\'s wallpaper have been setted!')

    def __pic2BmpIntoTempFile(self,oldpic,newname='bing',newExt='.bmp'):
        """
        将图像转换为bmp格式,并返回存储它另存为后的名字
        """
        oldpath_withoutExt = os.path.splitext(oldpic)[0]
        newpath = oldpath_withoutExt + newExt
        with Image.open(oldpic) as bmpImage:
            bmpImage.save(newpath, "BMP")
        return newpath

    def __pic2BmpIntoTempFile_fd(self,pic_fd):
        """
        把打开着的图片文件, 转换成bmp
        """
        fd ,tempf = tempfile.mkstemp()
        temppath = os.path.split(tempf)[0]
        newpath = os.path.join(temppath,'bing.bmp')
        
        with Image.open(pic_fd) as bmpImage:
            bmpImage.save(newpath, "BMP")
        return newpath

    def __downloadIntoSpecFolder(self,url):
        """
        下载url中的资源,储存到临时文件中,返回临时文件的路径
        """
        r = rr.get(url)
        picbytes = r.content
        picname = os.path.split(r.url)[-1]

        if self.specFolder == None:
            fd,picpath = tempfile.mkstemp()
        else:
            picpath = os.path.join(self.specFolder,picname)

        with open(picpath,'wb') as f:
            f.write(picbytes)
        return picname,picpath

    def setWallpaper(self):
        """
        对用户开放的方法,直接使用即可设置壁纸
        """
        picname,picpath = self.__downloadIntoSpecFolder(self.API)
        bmppath = self.__pic2BmpIntoTempFile(picpath, newExt='.bmp')
        self.__setBMPWallpaper(bmppath)

        os.remove(bmppath)
        print(datetime.date.today())

    def setWallpaper_bytes(self,picbytes):
        """
        对第三方用例开放的方法,通过图像的二进制来设置壁纸
        """
        from io import BytesIO
        pic_fd = BytesIO()
        pic_fd.write(picbytes)
        bmppath = self.__pic2BmpIntoTempFile_fd(pic_fd)
        self.__setBMPWallpaper(bmppath)
        os.remove(bmppath)

if __name__ == "__main__":
    WallpaperSetting().setWallpaper()
