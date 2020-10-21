from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predict')
def predict():
    return render_template('predict.html')





@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form
        gdp = float(input['gdp'])
        soc = float(input['soc'])
        health = float(input['health'])
        freedom = float(input['freedom'])
        generosity = float(input['generosity'])
        trust = float(input['trust'])
                  
        col = ['gdp', 'soc', 'health', 'freedom', 'generosity', 'trust']
        data = [[gdp, soc, health, freedom, generosity, trust]]
        pred = Model.predict(pd.DataFrame(data=data, columns=col)).round()
        return render_template('result.html', data=input, pred=pred)


   


if __name__ == '__main__':
    with open('happiness_rank_pred', 'rb') as model:
        Model = pickle.load(model)
    app.run(debug=True)

# @app.route('/plots')