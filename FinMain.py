# -*- coding: utf-8 -*-
#First Website
from flask import Flask, render_template
# import the Flask class from flask Library
# import render_template from flask Library to find and render html
app = Flask(__name__) # Instantiate the Flask Class, for current folder it is __main__

@app.route('/')     #This is a decorator, that routes the function home to route '/'
def home():
    return render_template('home.html')  #Return content for the request

@app.route('/help')  # This decorator routes the /about route to the about method
def help():
    return "Help content goes here!" 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__': # This returns true here only if it is from same file
    app.run(port=5001, debug=True, )
