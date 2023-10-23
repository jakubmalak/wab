import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/wba_4")
print(f'''Databases: {client.list_database_names()}''')

client

db = client.get_database('wab_4')

print(f''''Collections: {db.list_collection_names()}''')
collection = db.get_collection('rabbit')
print(f'{collection.name} objects: {collection}')