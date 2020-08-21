import seaborn as sns
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import shutil 

staff = pd.read_csv('./data/staff.csv')
sales = pd.read_csv('./data/201904salesreciepts.csv')
inventory = pd.read_csv('./data/pastry_inventory.csv')
products = pd.read_csv('./data/product.csv')

def generateDailySales(): 
    sns.barplot(
        data = sales, 
        x = 'transaction_date', 
        y = 'unit_price', 
        estimator = sum 
    )
    plt.show()

def generateInventoryWasteByProductId(id): 

    # Filter Locations 
    outlet1 = inventory[inventory.sales_outlet_id == 3]
    outlet2 = inventory[inventory.sales_outlet_id == 5]
    outlet3 = inventory[inventory.sales_outlet_id == 8]
    # Filter by Id 
    inventory1 = outlet1[outlet1.product_id == id]
    inventory2 = outlet2[outlet2.product_id == id]
    inventory3 = outlet3[outlet3.product_id == id]
    
    """ Location 1 Plot """
    plt.figure(figsize=(18,10))
    outletinventory1 = sns.barplot(
        data = inventory1, 
        x = 'transaction_date', 
        y = 'waste', 
        ci = None 
    )
    # Labels 
    outletinventory1.set(xlabel = "Date", ylabel = "Waste")
    outletinventory1.set_xticklabels(labels = inventory1.transaction_date, rotation = 45)
    outletinventory1.set_title('{} Waste: Location 1'.format(products.loc[id][4]))
    # Save figure 
    fig = outletinventory1.get_figure()
    fig.tight_layout()
    fig.savefig('MonthlyWasteLocation1{}'.format(id))
    # Move to Directory 
    shutil.move('MonthlyWasteLocation1{}.png'.format(id), './static/Graphs/MonthlyWaste')

    """ Location 2 Plot """ 
    plt.figure(figsize=(18,10))
    outletinventory2 = sns.barplot(
        data = inventory2, 
        x = 'transaction_date', 
        y = 'waste', 
        ci = None 
    )
    # Labels 
    outletinventory2.set(xlabel = "Date", ylabel = "Waste")
    outletinventory2.set_xticklabels(labels = inventory2.transaction_date, rotation = 45)
    outletinventory2.set_title('{} Waste: Location 2'.format(products.loc[id][4]))
    # Save figure 
    fig = outletinventory2.get_figure()
    fig.tight_layout()
    fig.savefig('MonthlyWasteLocation2{}'.format(id))
    # Move to directory
    shutil.move('MonthlyWasteLocation2{}.png'.format(id), './static/Graphs/MonthlyWaste')

    """ Location 3 Plot """
    plt.figure(figsize=(18,10))
    outletinventory3 = sns.barplot(
        data = inventory3, 
        x = 'transaction_date', 
        y = 'waste', 
        ci = None 
    )
    # Labels 
    outletinventory3.set(xlabel = "Date", ylabel = "Waste")
    outletinventory3.set_xticklabels(labels = inventory3.transaction_date, rotation = 45)
    outletinventory3.set_title('{} Waste: Location 3'.format(products.loc[id][4]))
    # Save figure 
    fig = outletinventory3.get_figure()
    fig.tight_layout()
    fig.savefig('MonthlyWasteLocation3{}'.format(id))
    # Move to Directory 
    shutil.move('MonthlyWasteLocation3{}.png'.format(id), './static/Graphs/MonthlyWaste')
    

def generateAllStaff(): 
    output = []
    for index, row in staff.iterrows(): 
        output.append(
            {
                'firstname': row['first_name'],
                'lastname': row['last_name'], 
                'position': row['position']
            }
        )

    return output

def generateStaffRoasters(): 
    roasters = staff[staff.position == "Roaster"]
    output = [] 

    for index, row in roasters.iterrows(): 
        output.append(
            {
                'firstname': row['first_name'],
                'lastname': row['last_name'], 
                'position': row['position'],
            }
        )

    return output

def generateStaffStoreManagers(): 
    storemanagers = staff[staff.position == "Store Manager"]
    output = [] 

    for index, row in storemanagers.iterrows(): 
        output.append(
            {
                'firstname': row['first_name'], 
                'lastname': row['last_name'], 
                'position': row['position'],
            }
        )
    return output

def generateStaffCoffeeWranglers(): 
    coffeewranglers = staff[staff.position == "Coffee Wrangler"]
    output = [] 

    for index, row in coffeewranglers.iterrows(): 
        output.append(
            {
                'firstname': row['first_name'],
                'lastname': row['last_name'], 
                'position': row['position'],
            }
        )

    return output
    

# generateDailySales()
# generateInventoryWasteByProductId(69)
# generateInventoryWasteByProductId(70)
# generateInventoryWasteByProductId(71)
# generateInventoryWasteByProductId(72)
# generateAllStaff()
