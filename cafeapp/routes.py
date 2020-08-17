from app import app, db
from flask import Flask, render_template, request
from app import ContactForm, ReviewForm, ApplicationForm
from app import Contact, Review, Application
import os, sorts

""" Home Route """
@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home(): 
    bestphotos = [
        'static/CoffImgs/coffee1-4.jpeg',
        'static/CakeImgs/cake1-5.jpg',
        'static/CafeImgs/cafeaesth1-1.jpg',
        'static/CafeImgs/cafeaesth1-2.jpg'
    ] 
    bestreviews = Review.query.all()[1:4]


    return render_template("home.html", 
        photos = bestphotos, 
        reviews = bestreviews,
    )


""" Gallery Route """
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

""" Menus Route """
@app.route('/menu')
def menu(): 
    return render_template("menus.html")

""" Single Menu Route """
@app.route('/menu/<int:menu_id>')
def singlemenu(menu_id):
    return render_template("menu.html", id=menu_id)

""" Locations Route """
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

""" Contact Route """
@app.route('/contact', methods=["GET", "POST"])
def contact(): 

    contactform = ContactForm()
    applicationform = ApplicationForm()
    reviewform = ReviewForm()

    if contactform.validate_on_submit(): 
        newcontact = Contact(
            name = contactform.name.data, 
            email = contactform.email.data, 
            subject = contactform.subject.data, 
            message = contactform.message.data
        )
        db.session.add(newcontact)
        try: 
            db.session.commit()
        except: 
            db.session.rollback()

    if applicationform.validate_on_submit(): 
        newapp = Application(
            name = applicationform.name.data, 
            number = applicationform.number.data,
            description = applicationform.description.data
        )
        db.session.add(newapp)
        try: 
            db.session.commit()
        except: 
            db.session.rollback()

    if reviewform.validate_on_submit(): 
        newreview = Review(
            name = reviewform.name.data, 
            review = reviewform.review.data
        )
        db.session.add(newreview)
        try: 
            db.session.commit()
        except: 
            db.session.rollback()


    return render_template("contact.html", 
        contactform=contactform,
        applicationform=applicationform,
        reviewform=reviewform,
    )


@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    return render_template(
        "reviews.html", 
        reviews=reviews, totalreviews=len(reviews), 
    )

@app.route('/contacts')
def contacts(): 
    contacts = Contact.query.all()
    return render_template(
        "contacts.html", 
        contacts=contacts, totalcontacts=len(contacts), 
    )

@app.route('/applications')
def applications(): 
    applications = Application.query.all()
    return render_template(
        "applications.html", 
        applications=applications, totalapplications=len(applications),
    )

