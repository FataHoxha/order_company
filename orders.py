import requests
import xmltodict,json

# 1. open xml and convert to json in order to easly handle the data structure
with open('employee_orders.xml', 'r') as xmlfile:
    json_res= xmltodict.parse(xmlfile.read())

# check if result is correct
#print(json.dumps(json_res))

# 2. format the order in a the employee orders in the desired format for request body


# 3. send the request

url = 'https://nhna.com/api/v1/bulk/order'
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

response = requests.post(url, json = orders)

#print the result
print(response)