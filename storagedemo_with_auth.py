import urllib
import pyrebase

#setting up firebase
firebaseConfig={"apiKey": "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
    "authDomain": "trialauth-7eea1.firebaseapp.com",
    "databaseURL": "https://trialauth-7eea1.firebaseio.com",
    "projectId": "trialauth-7eea1",
    "storageBucket": "trialauth-7eea1.appspot.com",
    "messagingSenderId": "441088628124",
    "appId": "1:441088628124:web:e894968e55f29cd52f2459",
    "measurementId": "G-P4Y5QEDVXH"}

firebase=pyrebase.initialize_app(firebaseConfig)

#define storage
storage=firebase.storage()

#define auth
auth=firebase.auth()
#login
email=input("Enter your email")
password=input("Enter password")
try:
    login = auth.sign_in_with_email_and_password(email, password)
    # upload a file
    file = input("Enter the name of the file you want to upload to storage")
    cloudfilename = input("Enter the name for the file in storage")
    storage.child(cloudfilename).put(file, login['idToken'])

except:
    print("Invalid credentials")


