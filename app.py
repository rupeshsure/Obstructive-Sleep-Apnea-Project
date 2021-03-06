from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_classifier_BalancedData1_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('valid.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        BQ= int(request.form['BQ'])
        ESS=int(request.form['ESS'])
        BMI=float(request.form['BMI'])
        #Kms_Driven2=np.log(Kms_Driven)
        Weight=int(request.form['Weight'])
        Height=int(request.form['Height'])
        Head=float(request.form['Head'])
        Neck=int(request.form['Neck'])
        Waist=int(request.form['Waist'])
        Buttock=int(request.form['Buttock'])
        Age=int(request.form['Age'])
        M=int(request.form['M'])
        prediction=model.predict([[BQ,ESS,BMI,Weight,Height,Head,Neck,Waist,Buttock,Age,M
]])
        prediction=round(prediction[0],4)
        if prediction<0:
            return render_template('valid.html',prediction_texts="No{}") 
        elif prediction==0:
            return render_template('normal.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : NORMAL") 
        elif prediction==1:
            return render_template('mild.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : MILD ")   
        elif prediction==2:
            return render_template('moderate.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : MODERATE ")
        elif prediction ==3:
            return render_template('severe.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : SEVERE")  
    else:
        return render_template('valid.html')

if __name__=="__main__":
    app.run(debug=True)