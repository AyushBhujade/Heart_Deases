import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)
import certifi
ca=certifi.where()

import pandas as pd
import numpy as  np
import pymongo

from heart_disease.exception.exception import HeartDiseaseException
from heart_disease.logger.logger import logging

class HeartDataExtract():
    def __ini__(self):
        try:
            pass
        except Exception as e:
            raise HeartDiseaseException(e,sys)
    
    def csv_to_json_convertor(self):
        try:
            pass
        except Exception as e:
            raise HeartDiseaseException(e,sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise HeartDiseaseException(e,sys)
        
if __name__=='__main__':
    pass
        