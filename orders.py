import requests
import re
import xmltodict,json

# 1. open xml and convert to json in order to easly handle the data structure
with open('employee_orders.xml', 'r') as xmlfile:
    employee_orders= xmltodict.parse(xmlfile.read())

# 2. format the order in a the employee orders in the desired format for request body
order_dict = []
for employee in employee_orders["Employees"]["Employee"]:
    
    # mapping meal to id
    map_id = {' Kebap':13, ' Pizza Quattro Formaggi':3, ' Fried Chicken':23, ' Caesar Salad':42}

    # apply regex to get orders separatly and correct amount
    orders_items = re.split(",", employee["Order"])
    
    items = []
    for i in orders_items:
        # apply parsing for tranlating the order text into correct id
        text = [i.split('x')[1]]
        item = {
            'id': int([map_id[x] for x in text][0]),
            'amount':int(i.split('x')[0])
        } 
        items.append(item)

    # add data only for attending employee
    is_attending = employee["IsAttending"]

    if is_attending=="true":
        order = {
            'customer' : {
                'name' : employee["Name"],
                'address' : { 
                    'street':  employee["Address"]["Street"],
                    'city':  employee["Address"]["City"],
                    'postal_code':  employee["Address"]["PostalCode"],
                }
            },
            'items': items
        }

    order_dict.append(order)
    


# 3. send the request

url = 'https://nhna.com/api/v1/bulk/order'
body = {'orders':order_dict}

'''
orders = {
    'orders': [
        {
            'customer': {
            'name': "Max Mustermann",
                'address': {
                    'street': "Musterweg 3",
                    'city': "Musterhausen",
                    'postal_code': "12345"
                }
            },
            'items': [ 
                {
                    'id': 3,
                    'amount': 3
                },
            ]
        },
    ]
}
'''
response = requests.post(url, json = body)

#print the response
if r and r.status_code == 201:
    print("Order sent successfully")
else:
    print("Error while posting the orders")