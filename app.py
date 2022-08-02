from flask import Flask , render_template, request
import pickle
import joblib
import numpy as np
model = joblib.load('test_jlib')

app=Flask(__name__)
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    min_diameter = request.form['est_diameter_min']
    max_diameter = request.form['est_diameter_max']
    velocity = request.form['relative_velocity']
    dif_diameter = request.form['est_diameter_diff']
    miss_distance= request.form['miss_distance']
    magnitude= request.form['absolute_magnitude']
    arr = np.array([[min_diameter, max_diameter, velocity, dif_diameter,miss_distance,magnitude]])
    pred = model.predict(arr)
    val=int(pred)
    if val==0:
        return render_template('nonhaz.html')
    else:
        return render_template('haz.html')


if __name__=="__main__":
    app.run(debug=True)