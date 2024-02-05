from importlib.resources import path
from flask import Flask , render_template , request
import numpy as np
import pickle
from pathlib import Path
import joblib
import os
import itertools

# location = 'C:\Flask\Snapulse'
# fullpath = os.path.join(location, 'heartmodeltest.pkl')

app = Flask(__name__ , template_folder='template')
# model = joblib.load(fullpath)
filename = 'heartmodeltest.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route("/",)
def hello():
    return render_template("index.html")


@app.route("/detail", methods = ["POST"])
def submit():
    # Html to py
    if request.method == "POST":
        name = request.form["Username"]

    return render_template("detail.html", n = name)


@app.route('/result', methods = ["POST"])
def predict():
    if request.method == "POST":
        
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        bp = int(request.form['bp'])
        chol = int(request.form['chol'])
        ecg = int(request.form['ecg'])
        mhr = int(request.form['mhr'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slp = int(request.form['slp'])
        caa = int(request.form['caa'])
        thall = int(request.form['thall'])

        sex_0,sex_1,cp_0,cp_1,cp_2,cp_3,ecg_0,ecg_1,ecg_2,exang_0,exang_1,slp_0,slp_1,slp_2,caa_0,caa_1,caa_2,thall_1,thall_2,thall_3=itertools.repeat(0,20)

        if sex==1:
            sex_1=1
        else:
            sex_0=1
        
        if cp==0:
            cp_0=1
        elif cp==1:
            cp_1=1
        elif cp==2:
            cp_2=1
        else:
            cp_3=1

        if ecg==0:
            ecg_0=1
        elif ecg==1:
            ecg_1=1
        else:
            ecg_2=1
        
        if slp==0:
            slp_0=1
        elif slp==1:
            slp_1=1
        else:
            slp_2=1

        if exang==1:
            exang_1=1
        else:
            exang_0=1

        if caa==0:
            caa_0=1
        elif caa==1:
            caa_1=1
        else:
            caa_2=1

        if thall==1:
            thall_1=1
        elif thall==2:
            thall_2=1
        else:
            thall_3=1
      

        values = np.array([[age,sex_0,sex_1,cp_0,cp_1,cp_2,cp_3,bp,chol,ecg_0,ecg_1,ecg_2,mhr,exang_0,exang_1,oldpeak,slp_0,slp_1,slp_2,caa_0,caa_1,caa_2,thall_1,thall_2,thall_3]])
        prediction = model.predict(values)
        

    


        return render_template('result.html', prediction=prediction)



if __name__=="__main__":
    app.run(debug=True)
    
