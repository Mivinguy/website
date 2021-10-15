import pymongo

db_username = 'heroku-flask-react'
db_password = '9eaInX3583tSK66N'
db_name = 'Cluster0'

connect_string = "mongodb+srv://{db_username}:{db_password}@cluster0.pxgvr.mongodb.net/{db_name}?retryWrites=true&w=majority"
client = pymongo.MongoClient(connect_string)
db = client.get_default_database()

# get user by name
def get_user_by_name(name):
    return db.user.find_one({"name": name})

# add new user
def add_user(name):

    ret = get_user_by_name(name)

    if ret is None:
        new_user = {"name": name}
        x = db.user.insert_one(new_user)
        ret = x.inserted_id

    return ret