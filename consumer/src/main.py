import pika
import pymongo

# 1. Fixing the IP address
conn_params = pika.ConnectionParameters(host='127.0.0.1')
conn = pika.BlockingConnection(conn_params)

# 2. and 3. Correcting the method name and variable spelling
channel = conn.channel()


client = pymongo.MongoClient("mongodb://localhost:27017/wba_4")
print(f'''Databases: {client.list_database_names()}''')

client

db = client.get_database('wab_4')

print(f''''Collections: {db.list_collection_names()}''')
collection = db.get_collection('rabbit')
print(f'{collection.name} objects: {collection}')

def on_message_callback(channel, method, properties, body):
    print(f'''channel:{channel},
     method:{method},
      properties:{properties},
       body:{body}''')

    try:
        data = body.decode('utf-8')  # Decoding bytes to string
        collection.insert_one({"message": data})
    except Exception as e:
        print(f"Error while inserting to MongoDB: {e}")


channel.basic_consume(
    queue="wab_4",
    auto_ack=True,
    on_message_callback=on_message_callback
)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()