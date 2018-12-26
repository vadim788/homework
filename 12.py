dataset = {
    "bob@kpi.ua": {
                    "person":{
                        "name":"Bob",
                        "email":"bob@kpi.ua"
                    },
                    "food": {
                        "apple":[1.3,12.1],
                        "milk":[45]
                    }
                },
    "boba@kpi@ua":{
        "person":{
            "name": "Boba",
            "email": "boba@kpi.ua"
        },
        "food":{"milk":[45]}
    }
}
result = {}
for i in list(dataset.keys()):
    persons= dataset[i]["person"]["name"]
for x in list(dataset.keys()):
    price = dataset[x]["food"]
    for z in list(price.values()):

        if persons in result:
            result[persons] = sum(z)
        else:
            result[persons] = 0
print(result)