from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home(): 
    return "Hello World!"

@app.route('/gallery')
def gallery(): 
    pass

@app.route('/menu')
def menu(): 
    pass 

@app.route('/menu/<int: menu_id>')
def singlemenu(menu_id): 
    pass

@app.route('/location')
def location(): 
    pass 

