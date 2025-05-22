

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.preprocessing import normalize


stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def clean_doc(document_data):
    words = document_data.split()
    punct_table = str.maketrans('', '', punctuation)
    words = [w.translate(punct_table) for w in words]
    words = [word for word in words if word.isalpha()]
    words = [w for w in words if not w in stop_words]
    words = [ps.stem(word) for word in words if len(word) > 5]
    words = ' '.join(words)
    return words


cv = pickle.load(open('cv.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("index.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signup.html")


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        text = request.form['message']
        data = [text]
        news = cv.transform(data).toarray() 
        predict = model.predict(news) 
        print(predict)
        if predict == 0:
            return render_template('result.html',pred=f'Input statement classified as Positive')
        elif predict == 1:
            return render_template('result.html',pred=f'Input statement classified as Negative')
        


@app.route('/note')
def note():
	return render_template('notebook.html')





if __name__ == '__main__':
    app.run(debug=False)