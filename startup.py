import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import sqlite3

# configuration
DATABASE = '/tmp/personal_site.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('SITE_SETTINGS', silent=True)

@app.route('/')
def site():
    return redirect(url_for('about'))

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/personal')
def personal():
	return render_template('personal.html')