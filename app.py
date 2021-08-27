from flask import Flask, render_template, request
import requests
import pickle
import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('insurance.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        age = (request.form['age'])
        sex=request.form['sex']
        if(sex=='male'):
            sex_male=1
        else:
            sex_male=0
        bmi=(request.form['bmi'])
        children=int(request.form['children'])
        smoker=request.form['smoker']
        if(smoker=='yes'):
            smoker_yes=1
        else:
            smoker_yes=0
            
        region =(request.form["region"])
        if(region=='southwest'):
               region_southwest = 1
               region_southeast = 0
               region_northwest = 0
               region_northeast = 0
            

        elif (region=='southeast'):
                region_southwest = 0
                region_southeast = 1
                region_northwest = 0
                region_northeast = 0

        elif (region=='northwest'):
                region_southwest = 0
                region_southeast = 0
                region_northwest = 1
                region_northeast = 0
        elif (region=='northeast'):
                region_southwest = 0
                region_southeast = 0
                region_northwest = 0
                region_northeast = 1
            
            
        
            
       

        else:
                southwest = 0
                southeast = 0
                northwest = 0
                northeast = 0
            
            

        
        	
        
        prediction=model.predict([[age,sex_male,bmi,children,smoker_yes,region_southwest,region_southeast,region_northwest]])
        output=(prediction)
        return render_template('index.html',prediction_text="Your insurance amount is {}".format(output))
    
    return render_template("index.html")

    

    
if __name__=="__main__":
    

    
    
     app.run(debug=True)





