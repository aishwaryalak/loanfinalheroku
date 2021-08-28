# save this as app.py
from flask import Flask,request, render_template
import pickle
import numpy as np



app = Flask(__name__)
dt = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method ==  'POST':
        Gender_n = request.form['Gender']
        Married_n = request.form['Married']
        Dependents = request.form['Dependents']
        Education_n = request.form['Education']
        Self_Employed_n = request.form['Self_Employed']
        Credit_History = float(request.form['Credit_History'])
        Property_Area = request.form['Property_Area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        

            
        # gender
        if (Gender_n == "Male"):
            Gender_n=1
        else:
            Gender_n=0
        
        # married
        if(Married_n=="Yes"):
            Married_n = 1
        else:
            Married_n=0

        # dependents
        if(Dependents=='1'):
            Dependents_1 = 1
            Dependents_2 = 0
            Dependents_3 = 0
        elif(Dependents == '2'):
            Dependents_1 = 0
            Dependents_2 = 1
            Dependents_3 = 0
        elif(Dependents=='3+'):
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 1
        else:
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 0  

        # education
        if (Education_n=="Graduate"):
            Education_n=1
        else:
            Education_n=0

        # employed
        if (Self_Employed_n == "Yes"):
            Self_Employed_n = 1
        else:
            Self_Employed_n = 0

        # property area

        if(Property_Area=="Semiurban"):
            Semiurban=1
            Urban=0
        elif(Property_Area=="Urban"):
            Semiurban=0
            Urban=1
        else:
            Semiurban=0
            Urban=0

        log_Total_Income = np.log(ApplicantIncome+CoapplicantIncome)

        prediction = dt.predict([[log_Total_Income,Credit_History,Semiurban,Education_n,Married_n,Dependents_2]])
        #print(prediction)

        if(prediction=="N"):
            prediction="Not Eligible"
        else:
            prediction="Eligible"
            


        return render_template("prediction.html", prediction_text="Customer is {}".format(prediction))




    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
