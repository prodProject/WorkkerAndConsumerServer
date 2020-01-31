import os

import pyrebase as pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCHyTXyqa0B8f-bsCPQgCAd22d17Mehmko",
    "authDomain": "prod-project-c3a7b.firebaseapp.com",
    "databaseURL": "https://prod-project-c3a7b.firebaseio.com",
    "projectId": "prod-project-c3a7b",
    "storageBucket": "prod-project-c3a7b.appspot.com",
    "messagingSenderId": "516316079832",
    "appId": "1:516316079832:web:c55590b87b110f61b059ad",
    "measurementId": "G-EWTKPFRJTV"
}

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database();
print(database.child("users").child("Morty").set("hello"))
