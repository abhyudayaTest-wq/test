from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    data = {
        'name': name,
        'email': email,
        'course': course
    }

    db.collection('students').add(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
