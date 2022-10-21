from flask import Flask, jsonify,render_template,request
import numpy as np
import pandas as pd
#from utils import adm_prd
from utils import load_model


app=Flask(__name__)

@app.route("/test")

def Admission_Predication():
    data=request.form
    #data=dict(data)
    print("data",data)
    GRE_Score=eval(data['GRE Score'])
    TOEFL_Score=eval(data['TOEFL Score'])
    University_Rating= eval(data['University Rating'])
    SOP= eval(data['SOP']) 
    LOR=eval(data['LOR'])
    CGPA=eval(data['CGPA'])
    Research=eval(data['Research'])

    adm_prd=load_model(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research)
    chance=adm_prd.Admission_Predication()
    print(chance)


    return f"admission predication {chance}"

if __name__=='__main__':
    app.run()
