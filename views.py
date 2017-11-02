from flask import render_template

from app import app
from fn import recipe

yum = recipe('name', 'password', 'email')

@app.route('/')
def signup():
    return render_templates('signup.html')

@app.route('/login', methods = ['POST','GET'])
@yum.login
    

@app.route('/register', methods = ['POST','GET'])
@yum.register
    

@app.route('/login_view')
@yum.login_view

@app.route('/register_view')
@yum.register_view

@app.route('/recipe_view')
@yum.recipe_view

