🩺 HealthGuard – Flask + MySQL App










📌 Overview

HealthGuard is a Flask-based web application that allows users to record health entries and automatically predict symptom probabilities using a dummy AI model (powered by NumPy). Data is stored in a MySQL database for retrieval and analysis.

This project is designed as a foundation for integrating an actual machine learning model (e.g., TensorFlow Lite) in the future.

🚀 Features

📝 Add health entries through a form.

🤖 AI-powered dummy symptom predictions (Fever, Cough, Headache, Fatigue).

💾 Store entries in a MySQL database.

📊 Fetch & display all saved entries via API.

🌐 Ready for deployment with Gunicorn and Nginx.

🛠️ Tech Stack

Backend: Python (Flask)

Database: MySQL

AI Simulation: NumPy (random probabilities)

Server: Gunicorn (production-ready WSGI server)

Frontend: Flask Templates (Jinja2, HTML)

Deployment: Render / PythonAnywhere

📂 Project Structure
healthguard/
│── app.py              # Main Flask application
│── requirements.txt    # Dependencies
│── Procfile            # For deployment (Gunicorn start command)
│── templates/
│   └── index.html      # Frontend template

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/healthguard-flask.git
cd healthguard-flask

2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Database

Make sure you have MySQL running and create a database:

CREATE DATABASE healthguard;


Create table:

CREATE TABLE health_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entry_text TEXT,
    fever FLOAT,
    cough FLOAT,
    headache FLOAT,
    fatigue FLOAT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


Update DB credentials in app.py:

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="healthguard"
)

5. Run Locally
python app.py


Visit: http://localhost:5000

🌍 Deployment (Render Example)

Add a Procfile:

web: gunicorn app:app


Push to GitHub.

Deploy on Render
 → new Web Service.

You’ll get a live demo link like:

https://healthguard.onrender.com

📡 API Endpoints

GET / → Home page

POST /add_entry → Add entry (saves to DB)

GET /get_entries → Fetch all entries

Example request:

curl -X POST -F "entry=Feeling tired today" http://localhost:5000/add_entry

📸 Screenshots
🏠 Homepage

📊 API Response

(You can place screenshots in a screenshots/ folder and reference them here.)

📝 Future Improvements

🔮 Integrate real AI model (TensorFlow Lite).

🔐 Add user authentication (login system).

📊 Create dashboard with charts for symptom tracking.

🐳 Deploy with Docker for portability.

👨‍💻 Author

Developed by James Njuguna
📧 Contact: jamesnjugunamuturi847@gmail.com
