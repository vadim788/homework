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
def getNames(dataset, last_names = list(dataset.keys())):
    if last_names == []:
        return
    last_name = last_names[0]
    student_name = dataset[last_name]["person"]["name"]
    print(student_name)
    getNames(dataset, last_names[1:])
getNames(dataset)