from flask import Flask, request, jsonify, render_template
import mysql.connector, numpy as np

app = Flask(__name__)

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="healthguard"
)
cursor = db.cursor(dictionary=True)

# Dummy AI Model (replace with TFLite later)
def predict_symptoms(text):
    return {
        "fever": np.random.rand(),
        "cough": np.random.rand(),
        "headache": np.random.rand(),
        "fatigue": np.random.rand()
    }

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_entry', methods=['POST'])
def add_entry():
    text = request.form['entry']
    symptoms = predict_symptoms(text)

    cursor.execute(
        "INSERT INTO health_entries (entry_text, fever, cough, headache, fatigue) VALUES (%s, %s, %s, %s, %s)",
        (text, symptoms['fever'], symptoms['cough'], symptoms['headache'], symptoms['fatigue'])
    )
    db.commit()

    return jsonify({"message": "Saved!", "symptoms": symptoms})

@app.route('/get_entries')
def get_entries():
    cursor.execute("SELECT * FROM health_entries ORDER BY date_created ASC")
    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)
