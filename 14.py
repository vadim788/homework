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
result = dict ()
def getLen(data, last_names = list(dataset.keys())):
    for name in last_names:
        comp = data[name]["food"]
        for i in comp:
            if i in result:
                result[i]+=1
            else:
                result[i]=1
                print(result)
getLen(dataset)