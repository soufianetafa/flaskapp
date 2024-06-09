from flask import Flask, request, render_template
import joblib
import pandas as pd

# Charger le modèle et les encoders
model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

app = Flask(__name__)

# Fonction de prédiction
def predict_quantity(area, continent, region, year, item, element):
    input_data = {
        'Area': [label_encoders['Area'].transform([area])[0]],
        'Continent': [label_encoders['Continent'].transform([continent])[0]],
        'Region': [label_encoders['Region'].transform([region])[0]],
        'YEAR': [year],
        'item': [label_encoders['item'].transform([item])[0]],
        'Type': [0],  # Par exemple, si vous ne considérez qu'un seul type
        'Element': [label_encoders['Element'].transform([element])[0]]
    }
    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)
    return prediction[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pred_africa', methods=['GET', 'POST'])
def pred_africa():
    if request.method == 'POST':
        area = request.form['area']
        region = request.form['region']
        year = int(request.form['year'])
        item = request.form['item']
        element = request.form['element']
        prediction = predict_quantity(area, 'Africa', region, year, item, element)
        return render_template('pred_africa.html', prediction=prediction, element=element)
    return render_template('pred_africa.html')

@app.route('/pred_america', methods=['GET', 'POST'])
def pred_america():
    if request.method == 'POST':
        area = request.form['area']
        region = request.form['region']
        year = int(request.form['year'])
        item = request.form['item']
        element = request.form['element']
        prediction = predict_quantity(area, 'Americas', region, year, item, element)
        return render_template('pred_america.html', prediction=prediction, element=element)
    return render_template('pred_america.html')

@app.route('/pred_asie', methods=['GET', 'POST'])
def pred_asie():
    if request.method == 'POST':
        area = request.form['area']
        region = request.form['region']
        year = int(request.form['year'])
        item = request.form['item']
        element = request.form['element']
        prediction = predict_quantity(area, 'Asia', region, year, item, element)
        return render_template('pred_asie.html', prediction=prediction, element=element)
    return render_template('pred_asie.html')

@app.route('/pred_europe', methods=['GET', 'POST'])
def pred_europe():
    if request.method == 'POST':
        area = request.form['area']
        region = request.form['region']
        year = int(request.form['year'])
        item = request.form['item']
        element = request.form['element']
        prediction = predict_quantity(area, 'Europe', region, year, item, element)
        return render_template('pred_europe.html', prediction=prediction, element=element)
    return render_template('pred_europe.html')

if __name__ == '__main__':
    app.run(debug=True)
