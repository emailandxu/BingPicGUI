import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.types import TEXT,BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
import datetime
import os
import sys
import platform
from path import Path

DBNAME = "bingpic"

if not 'Windows' in platform.platform():
    __filepath__ = '/root/%s'%DBNAME
else:
    __filepath__ = os.path.split(sys.argv[0])[0]
    print(__filepath__)

os.chdir(__filepath__)

DB_CONNECT_STRING = 'sqlite:///%s.db'%DBNAME
DB_PATH = './%s.db'%DBNAME
BASEMODEL = declarative_base()

class BingPic(BASEMODEL):
    __tablename__='bingpic'
    title = Column(TEXT,nullable=False)
    picurl = Column(TEXT,primary_key=True)
    picbinary = Column(BLOB,nullable=False)
    date = Column(TEXT,nullable=False)

    def parseDatetime(self,datetime_str):
        return datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S.%f')
    def parseDate(self,date_str):
        return datetime.strptime(date_str, '%Y-%m-%d')


class DB():
    def __init__(self):
        self.initFlag= Path(DB_PATH).exists()

        self.engine = self.__createEngine()
        self.session = self.__createSession(self.engine)
        
        if self.initFlag == False:
            self.init_db()


    def __createEngine(self):
        engine = sqlalchemy.create_engine(DB_CONNECT_STRING,echo=False)
        return engine    

    def __createSession(self,engine):
        session = sessionmaker(bind=engine)()
        return session

    def add(self,orm_obj):
        self.session.add(orm_obj)
        self.session.commit()

    def init_db(self):
        BASEMODEL.metadata.create_all(self.engine)

    def drop_db(self):
        BASEMODEL.metadata.drop_all(self.engine)
        
class BingPicDB(DB):
    def __init__(self):
        super(BingPicDB,self).__init__()
        self.q = self.initquery()

    def initquery(self):
        q = self.session.query(BingPic)
        return q
    
    def isEmpty(self):
        try:
            self.getLatest()        
        except NoResultFound as e:
            return True
        else:
            return False   
        
    def order_by_date(self):
        return self.q.order_by(BingPic.date.desc())
    
    def getN(self,n):
        for pic in self.order_by_date().limit(n).all():
            yield [pic.title,pic.date,pic.picurl]
            
    def getAll(self):
        for pic in self.order_by_date().all():
            yield [pic.title,pic.date,pic.picurl]

    def getPicBinary(self,pk_picurl):
        return self.q.get(pk_picurl).picbinary
    
    def getLatest(self):
        return self.order_by_date().limit(1).one()

    def findUnInsertedDayIndex(self):
        latest_18_rows = self.order_by_date().limit(18).all()
        latest_18_date_in_rows = list(map(lambda row:row.date,latest_18_rows))
        latest_18_date_in_real = [(datetime.date.today()-datetime.timedelta(i)).strftime('%Y%m%d') for i in range(18)]
        for day in latest_18_date_in_real:
            if day not in latest_18_date_in_rows:
                yield latest_18_date_in_real.index(day)

        

if __name__ == '__main__':
    db = BingPicDB()
