from flask import Flask, render_template, request, redirect
import mysql.connector
import uuid

mydb=mysql.connector.connect(
    host="localhost",
    database="",
    username="",
    password=""
)

cursor=mydb.cursor()

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 

@app.route('/login')
def login():
    return render_template('login.html')