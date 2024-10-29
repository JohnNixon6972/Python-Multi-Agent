from db import personal_data_collection, notes_collection

def get_values(_id):
    return {
        "_id": _id,
        "general":{
            "name":"",
            "age":30,
            "weight":60,
            "height":170,
            "activity_level":"Sedentary (little or no exercise)",
            "gender":"Male"
        },
        "goals":["Muscle Gain"],
        "nutrition":{
            "calories":2000,
            "protein":100,
            "carbs":200,
            "fat":50
        },
    }

def create_profile(_id):
    profile_values = get_values(_id)
    result = personal_data_collection.insert_one(profile_values)

    return result.inserted_id, result

def get_profile(_id):
    profile = personal_data_collection.find_one({"_id":{"$eq":_id}})
    return profile


def get_notes(_id):
    return list(notes_collection.find({"_id":{"$eq":_id}}))