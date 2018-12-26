dataset = {
        "bob@kpi.ua": {
            "person": {
                "name": "Bob",
                "email": "bob@kpi.ua"
            },
            "food": {
                "apple": [1.3, 12.1],
                "milk": [45]
            }
        },
        "boba@kpi@ua": {
            "person": {
                "name": "Boba",
                "email": "boba@kpi.ua"
            },
            "food": {"milk": [45]}
        }
    }

def getFood(dataset,result={}):
    for i in list(dataset.keys()):
        foods = dataset[i]["food"]
        for food in list(foods.keys()):
            if food in result:
                result[food] +=1
            else:
                result[food] = 1
    print(result)
getFood(dataset)