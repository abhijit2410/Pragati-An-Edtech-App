import pymongo
from bson.objectid import ObjectId


def userauth(no):
    client = pymongo.MongoClient(
        "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
    mydb = client["user_authentication"]
    mycol = mydb["User"]

    filcol = mycol.find()
    for z in filcol:
        if (z['phn_no'] == no):
            return 'user exists'

    mydb["User"].insert_one({
                'phn_no': no
            })
    return 'new User'

def check(type):
    client = pymongo.MongoClient(
        "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
    mydb = client["workflow"]
    mycol = mydb["flow_control"]

    filcol = mycol.find()
    for z in filcol:
        if(type=='flow'):
            return z['flow']
        elif(type=='num'):
            return z['num']
        elif(type=='currtime'):
            return z['currtime']
        elif(type=='posttime'):
            return z['posttime']
        else:
            return 'invalid'

def update(param,curr,new):
    client = pymongo.MongoClient(
        "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
    mydb = client["workflow"]
    mycol = mydb["flow_control"]
    filcol = mycol.find()

    
    myquery = { param: curr }
    newvalues = { "$set": { param: new } }
    mycol.update_one(myquery, newvalues)

def update_feedback(str):
    client = pymongo.MongoClient(
        "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
    mydb = client["Feedback"]
    mycol = mydb["info"]

    filcol = mycol.find()
    for z in filcol:
  
        if(str == "Yes, I am satisfied."):
            mycol.update_one({},{'$set':{"pos":z['pos']+1}})

        elif(str == "No, Could be better."):
            mycol.update_one({},{'$set':{"neg":z['neg']+1}})

