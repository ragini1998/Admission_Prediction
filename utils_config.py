from distutils.command.config import config
from flask import  Flask
import numpy as np
import pandas as pd
import pickle
import json
import config
app=Flask(__name__)

app.route("/")
class predication_model():
    def __init__(self,GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research):
        self.GRE_Score =GRE_Score
        self.TOEFL_Score =TOEFL_Score
        self.University_Rating =University_Rating
        self.SOP =SOP 
        self.LOR =LOR
        self.CGPA =CGPA
        self.Research =Research

    def Predication(self):
        with open(config.MODEL_PATH,'rb') as f:
            self.data=pickle.load(f)
            
    def Admission_Predication(self):
        self.Predication()
        test_array=np.zeros(7)
        test_array[0]=self.GRE_Score
        test_array[1]=self.TOEFL_Score
        test_array[2]=self.University_Rating
        test_array[3]=self.SOP
        test_array[4]=self.LOR
        test_array[5]=self.CGPA
        test_array[6]=self.Research
        test_array

        print("Test Array: ",test_array)    
        admission_prediction=self.data.predict([test_array])
        print("Admission predication : ",admission_prediction)
        return admission_prediction

if __name__=="__main__":
        GRE_Score = 322.0
        TOEFL_Score = 110.0
        University_Rating = 3.0
        SOP = 3
        LOR = 2.50
        CGPA = 8.67
        Research = 1
        adm_prd=predication_model(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research)
        adm_prd.Admission_Predication()