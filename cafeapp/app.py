from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_sqlalchemy import SQLAlchemy 
from wtforms.validators import DataRequired 
import os, sorts


app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'MY_SECRET_KEY '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' 

db = SQLAlchemy(app)

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home(): 
    return render_template("home.html")

@app.route('/gallery')
def gallery(): 

    cafeimages = sorts.mergeSort(os.listdir('./static/CafeImgs'))
    coffeeimages = sorts.mergeSort(os.listdir('./static/CoffImgs'))
    cakeimages = sorts.mergeSort(os.listdir('./static/CakeImgs'))

    return render_template("gallery.html", 
        cafeimages=cafeimages, 
        cakeimages=cakeimages, 
        coffeeimages=coffeeimages, 
    )

@app.route('/menu')
def menu(): 
    return render_template("menus.html")

@app.route('/menu/<int:menu_id>')
def singlemenu(menu_id):
    return render_template("menu.html", id=menu_id)

@app.route('/locations')
def location(): 
    
    locations = [
        {
            'city': 'San Francisco',
            'address': '201 Fell St, CA 94102', 
            'number': '+14154372734',
            'image': 'static/LocImgs/sanfran1.jpg'
        }, 
        {
            'city': 'Seoul',
            'address': '10 Hongik-ro, Seogyo-dong, Mapo-gu, Seoul', 
            'number': '+82 2-332-7470',
            'image': 'static/LocImgs/korea1.jpg',
        }, 
        {
            'city': 'Tokyo',
            'address': '〒 103-0027 Tokyo, Chuo City, Nihonbashi, 2 Chome−11−2 日', 
            'number': '+81 3-6262-3439',
            'image': 'static/LocImgs/tokyo1.jpg'
        }, 
    ]

    return render_template("locations.html",
        locations=locations, 
    )

@app.route('/contact', methods=["GET", "POST"])
def contact(): 

    contactform = ContactForm()
    applicationform = ApplicationForm()
    reviewform = ReviewForm()

    if contactform.validate_on_submit(): 
        print(contactform.name.data)
        print(contactform.email.data)
        print(contactform.subject.data)
        print(contactform.message.data)

    if applicationform.validate_on_submit(): 
        print(applicationform.name.data)
        print(applicationform.number.data)
        print(applicationform.description.data)

    if reviewform.validate_on_submit(): 
        print(reviewform.name.data)
        print(reviewform.review.data)


    return render_template("contact.html", 
        contactform=contactform,
        applicationform=applicationform,
        reviewform=reviewform,
    )


""" Form Classes """ 
class ContactForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ReviewForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    review = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Add Review")

class ApplicationForm(FlaskForm): 
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    number = StringField("Number", validators=[DataRequired()])
    submit = SubmitField("Submit")


