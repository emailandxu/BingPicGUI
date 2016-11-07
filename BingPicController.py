# -*- coding:utf-8 -*-
import sys
import BingPicView as UI
from PyQt4 import QtCore, QtGui
from SpiderOrm import BingPic,BingPicDB
from Wallpaper import WallpaperSetting
from BingPicSpider import addUninsertedPicToDB,addTodayPicToDB

app = QtGui.QApplication(sys.argv) 

class myui(UI.Ui_Form):
    def __init__(self):
        self.bing_db = self.initDB()

        super(myui,self).__init__()
        self.initUI()
        self.initSlot()

        self.current_PreviewRowIndex = 0
        self.picsList = self.refreshPicsListAndTable()

        self.previewPicBytes = None

        self.setPreviwByRowIndex(0)

    def initDB(self):
        """
        初始化数据库模块
        """
        self.bing_db = BingPicDB()
        return self.bing_db

    def initUI(self):
        """
        初始化ui控件
        """
        self.form = QtGui.QWidget()
        self.setupUi(self.form)

    def refreshPicsListAndTable(self):
        """
        从数据库取出所有数据, 刷新壁纸信息数组, 并且填充进UI表格
        """
        self.picsList = list(self.bing_db.getAll())
        self.fillImagesInfoTable()
        
        return self.picsList
    
    def initSlot(self):
        """
        初始化交互组件的槽函数
        """
        self.images_table.itemClicked.connect(self.on_itemClick)
        self.apply_btn.clicked.connect(self.on_applybtnClick)
        self.update_btn.clicked.connect(self.on_updatebtnClick)
        self.confirm_btn.clicked.connect(self.on_confirmClick)


    def __setCurrentPreviewRowIndex(self,rowindex):
        """
        改变当前的预览行号,并更新预览图片
        """
        self.current_PreviewRowIndex = rowindex
        self.setPreviwByRowIndex(rowindex)
        
    def __setImagePixmapToIamgeLabel(self,img,bytesblag=True):
        """
        设置预览图片,强行定义其大小为768,432
        """
        pixmap = QtGui.QPixmap()
        if bytesblag == True:
            pixmap.loadFromData(img)
        else:
            pixmap.load(img)
        pixmap = pixmap.scaled(768,432)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def fillImagesInfoTable(self):
        """
        填充图片信息表,根据填充信息自动追加行
        """
        table = self.picsList
        self.images_table.setRowCount(len(table))#根据数据行数改变UI表格行数
        for rowIndex,row in enumerate(table):
            for columnIndex,column in enumerate(row):
                if columnIndex > self.images_table.columnCount()-1:
                    break
                newItem = QtGui.QTableWidgetItem(column)  
                self.images_table.setItem(rowIndex, columnIndex, newItem)
                self.images_table.horizontalHeader().resizeSection(1,72)

    def setPreviwByRowIndex(self,index):
        """
        根据图片信息表的行号,更新图片标签控件的图片
        """
        if self.bing_db.isEmpty():
        	return
        pic_bytes = self.bing_db.getPicBinary(self.picsList[index][-1])
        self.previewPicBytes = pic_bytes
        self.__setImagePixmapToIamgeLabel(pic_bytes)

    def on_itemClick(self,item):
        """
        单击单元格时,改变目前的预览行号
        """
        self.__setCurrentPreviewRowIndex(item.row())

    def on_confirmClick(self):
        """
        设置壁纸,并退出
        """
        self.on_applybtnClick()
        QtCore.QCoreApplication.quit()

    def on_applybtnClick(self):
        """
        设置壁纸
        """
        target=WallpaperSetting().setWallpaper_bytes(self.previewPicBytes,)

    def on_updatebtnClick(self):
        """
        更新数据库中的数据,和UI中的表格,并把预览行号设成第0行
        """
        QtGui.QMessageBox.warning(self.form,"warning", "Got to take a few time to update pictures!")
        try:
            addUninsertedPicToDB()
        except Exception as e:
            msg = QtGui.QMessageBox.warning(self.form,"warning", "Noting to update!")
            print(e)
        else:
            self.refreshPicsListAndTable()
            self.setPreviwByRowIndex(0)

if __name__ == '__main__':
    ui = myui()
    ui.form.show()
    sys.exit(app.exec_())
