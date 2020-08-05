from app import app, db 


""" Models """ 

class Sales(db.Model): 
    transaction_id = db.Column()
    transaction_date = db.Column()
    transaction_time = db.Column()
    sales_outlet_id = db.Column()
    staff_id = db.Column() 
    customer_id = db.Column()
    product_id = db.Column()
    quantity = db.Column()
    unit_price = db.Column()

class Staff(db.Model): 
    staff_id = db.Column() 
    first_name = db.Column()
    last_name = db.Column() 
    position = db.Column()
    start_date = db.Column() 
    location = db.Column()

class Products(db.Model): 
    product_id = db.Column()
    product_group = db.Column()
    product_category = db.Column()
    product = db.Column()
    product_description = db.Column()
    current_wholesale_price = db.Column()
    current_retail_price = db.Column()

class Locations(db.Model):
    sales_outlet_id = db.Column()
    sales_outlet_type = db.Column()
    store_address = db.Column()
    store_city = db.Column()
    store_state = db.Column()
    store_telephone = db.Column()
    store_postal_code = db.Column()
    manager = db.Column()
    neighborhood = db.Column()

class Customer(db.Model): 
    customer_id = db.Column()
    first_name = db.Column()
    loyalty_card_number = db.Column()
    email = db.Column()
    birthday = db.Column()
    gender = db.Column()
