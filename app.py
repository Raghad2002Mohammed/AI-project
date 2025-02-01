from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

with open("M1","rb") as file:
    load_model=pickle.load(file)

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # استلام البيانات كـ JSON
        carat = float(data['carat'])
        depth = float(data['depth'])
       
        # تنفيذ التنبؤ
        prediction = load_model.predict(np.array([[carat, depth]]))

        return jsonify({'predict_price': prediction[0]})
    except Exception as e:
        return jsonify({'Error': str(e)}), 400  # إرجاع خطأ واضح

if __name__ == '__main__':
    app.run(debug=True)
