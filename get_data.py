import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
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
    
    def csv_to_json_convertor(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            record=list(json.loads(df.T.to_json()).values())
            return record
        except Exception as e:
            raise HeartDiseaseException(e,sys)
        
    def pushing_data_to_mongodb(self,record,database,collection):
        try:
            self.database=database
            self.record=record
            self.collection=collection
            
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.record)
            return len(self.record)
        except Exception as e:
            raise HeartDiseaseException(e,sys)
        
if __name__=='__main__':
    file_path="./Heart_Diseases_Data/heart (1).csv"
    DATABASE="ayush_project"
    COLLECTION="HEART_DISEASE_DATA"
    disease=HeartDataExtract()
    record=disease.csv_to_json_convertor(file_path)
    disease.pushing_data_to_mongodb(record,DATABASE,COLLECTION)
        