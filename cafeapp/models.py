from app import app, db 


""" Models """ 
class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, index = True)
    email = db.Column(db.String(100), unique = True, index = True)
    subject = db.Column(db.String(50), unique = False, index = False)
    message = db.Column(db.String(300), unique = False, index = False)

class Review(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, index = True)
    review = db.Column(db.String(1000), unique = True, index = False)


