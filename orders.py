import requests

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