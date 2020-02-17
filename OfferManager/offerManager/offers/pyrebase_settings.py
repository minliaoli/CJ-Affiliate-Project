import pyrebase

config = {
  "apiKey": "AIzaSyDL6UUpJ7qER1QHQCEMUEmZZb4UA30rqQo",
  "authDomain": "greatfantasticteam.firebaseapp.com",
  "databaseURL": "https://greatfantasticteam.firebaseio.com",
  "projectId": "greatfantasticteam",
  "storageBucket": "greatfantasticteam.appspot.com",
  "messagingSenderId": "788329565631",
  "appId": "1:788329565631:web:b567b32228019ef28be50a",
  "measurementId": "G-TZQ86ZQMDZ"
}

# initialize app with config
firebase = pyrebase.initialize_app(config)

''' # authenticate a user
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("nguan@ucsb.edu", "Ng5668253")'''


db = firebase.database()