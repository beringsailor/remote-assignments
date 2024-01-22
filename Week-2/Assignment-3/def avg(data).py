def avg(data):
    data = data['products']
    average_price = 0
    product_num = 0
    for item in data:
        if item not in data:
            return None
        else: 
            average_price += item['price']
            product_num += 1
    return round(float(average_price / product_num), 3)

print(
    avg({
        "products": [
            {
                "name": "Product 1",
                "price": 100
            },
            {
                "name": "Product 2",
                "price": 700
            },
            {
                "name": "Product 3",
                "price": 300
            }
        ]
    })
) # print the average price of all products (round to 3 decimal)

# ---------------------------
# i = {"products": [
#             {
#                 "name": "Product 1",
#                 "price": 100
#             },
#             {
#                 "name": "Product 2",
#                 "price": 700
#             },
#             {
#                 "name": "Product 3",
#                 "price": 300
#             }
#         ]
#     }
# print(i['products'])