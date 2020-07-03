import json
import random

def lambda_handler(event, context):
    print('Function loaded successfully');
    orderID = event['Order']
    print('Checking stock')
    # Generate a random number to determine there is stock of the products.
    min = 0
    max = 1
    stockStatus = random.randint(min, max)
    if stockStatus == 1:
        tempStr = 'Products are in stock'
    else:
        tempStr = 'Products are out of stock'
    response = {
        'Order': orderID,
        'Status': stockStatus,
        'Message': tempStr
    }
    print('Returning response: ')
    print(response)
    return response
