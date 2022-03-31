


from kafka import KafkaProducer, KafkaConsumer
from time import sleep
import json
from datetime import datetime
from confluent_kafka import Producer
from pymongo import MongoClient, ASCENDING, DESCENDING
from pprint import pprint
from itertools import combinations, combinations_with_replacement
from kafka.admin import KafkaAdminClient, NewTopic
from EtudeBinance import getpairs




producerconnect = Producer({'bootstrap.servers': 'localhost:9092'})
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,10,2))
read = KafkaConsumer(
    'ProjetDDS',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     auto_commit_interval_ms=300,
     enable_auto_commit=True,
     group_id='my-group')

client = MongoClient("localhost", 27017)
db = client.Binance
collection = db.myCollection
db.myCollection.delete_many({})




def SupprimeTOPIC():
    server_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
    title = ['ProjetDDS']
    def create_topics(title):

        existing_topic_list = read2.topics()
        print(list(read2.topics()))
        topic_list = []
        for topic in title:
            if topic not in existing_topic_list:
                print('Topic : {} added '.format(topic))
                topic_list.append(NewTopic(name=topic))
            else:
                print('Topic : {} already exist '.format(topic))
        try:
            if topic_list:
                server_client.create_topics(new_topics=topic_list, validate_only=False)
                print("Topic Created Successfully")
            else:
                print("Topic Exist")
                delete_topics(title)
        except Exception as e:
            print(e)

    def delete_topics(title):
        try:
            server_client.delete_topics(topics=title)
            print("Topic Deleted Successfully")
            create_topics(title)
        except Exception as e:
            print(e)


    read2 = KafkaConsumer(
        bootstrap_servers = ['localhost:9092'],
        )
    create_topics(title)





def ApacheRemplissage():
	listeInsertion=[]
	SupprimeTOPIC()
	get_ipython().run_line_magic('run', "'/home/alexis/DDS/EtudeBinance.py'")
	with open("result.txt", "r") as fichier:
		
		lines = fichier.readlines()
		for line in lines:
			listeInsertion.append(line)

	list1=[]
	list1=listeInsertion[0].split(',AZ')

	del list1[-1]

	jsone=[]
	compteurgenerale=len(list1)
	for i in list1:
		try:
			jsone.append(json.loads(i))
		except ValueError:
			print("error for",i,ValueError)

	for i in jsone:
		producer.send('ProjetDDS',bytes(str(i), encoding='utf-8'))
		sleep(0.5)
	return compteurgenerale





from confluent_kafka import Consumer, KafkaError

def conso(compteur,compteurgenerale):
    cc=1
    settings = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup2',
        'client.id': 'client-'+str(compteur),
        'enable.auto.commit': True,
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'}
    }

    c = Consumer(settings)

    c.subscribe(['ProjetDDS'])
    db.myCollection.delete_many({})
    go=True
    try:
        while go:
            msg = c.poll(0.1)
            if msg is None:
                continue
            elif not msg.error():
                #print('Received message: {0}'.format(msg.value()))
                inputdonnee=collection.insert_one(json.loads(msg.value().decode('utf-8').replace("'", '"')))
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                #print("New input in our collection at "+dt_string)
                cc+=1
                if cc==compteurgenerale:
                    go=False
                    break 
            elif msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition reached {0}/{1}'
                    .format(msg.topic(), msg.partition()))
            else:
                print('Error occured: {0}'.format(msg.error().str()))

    except KeyboardInterrupt:
        pass

    finally:
        c.close()



def hacked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))

def TerminalProducer():
    p = Producer({'bootstrap.servers': 'localhost:9092'})
    cursor = collection.find()
    try:
        for record in cursor:
            p.produce('ProjetDDS', record, callback=hacked)
            p.poll(0.5)

    except KeyboardInterrupt:
        pass

    p.flush(30)
    db.myCollection.delete_many({})
    conso()



symbolList=["BTC","ETH","USDT","USDC","BNB","DOGE","LTC","AVAX","DOT","MATIC","AAVE","UNI","APE"]

def requetesMongoDB():
    index=True
    while index:
        case=input("Do you want to read to read all the data (Press 1)" + '\n' + "Read the data order by the volume (Press 2)" + '\n' + "Read the data order by the high price (Press 3)" + '\n' 
        + "Read the data order by the low price  (Press 4)" + '\n' + "Read the data order by the Number of trades (Press 5)" + '\n'
        + "Read the new command (Press 6)" + '\n'+ "Read the new command 2 (Press 7)" + '\n'+"or  exit (Press 8) > ")
        print("\n")
    
        if case == "1":
            print('Start - Read all data')
            print('\n')
            cursor = collection.find({})
            for record in cursor:
                pprint(record)
            print('\n')
            print('End - Read all data')
            print('\n')

        elif case =="2":
            print('Start - Read the data order by the volume')
            print('\n')
            cursor = collection.find({"Volume":{"$gt":0}}, {"ID":1,"Volume":1, "_id":0}).sort("Volume",DESCENDING)
            for record in cursor:
                print(record)
            print('\n')
            print('End - Read the data order by the volume')
            print('\n')

        elif case =="3":
            print('Start - Read the data order by the high price')
            print('\n')
            cursor = collection.find({"High":{"$gt":0}}, {"ID":1,"High":1, "_id":0}).sort("High",DESCENDING)   
            for record in cursor:
                print(record)
            print('\n')
            print('End - Read the data order by the high price')
            print('\n')
        elif case =="4":
            print('Start - Read the data order by the low price')
            print('\n')
            cursor = collection.find({"Low" : {"$gt":0}}, {"ID":1,"Low":1, "_id":0}).sort("Low",DESCENDING)   
            for record in cursor:
                print(record)
            print('\n')
            print('End - Read the data order by the low price')
            print('\n')

        elif case =="5":
            print('Start - Read the data order by the Number of trades')
            print('\n')
            cursor = collection.find({"Number of trades" : {"$gt":0}}, {"ID":1,"Number of trades":1, "_id":0}).sort("Number of trades",DESCENDING)   
            for record in cursor:
                print(record)
            print('\n')
            print('End - Read the data order by the Number of trades')
            print('\n')
        elif case =="6":
            print('Start - new command 2')
            print('\n')
            cursor = collection.find({"$or": [{"Close": {"$gt": 1}}, {"High": {"$gt": 2}}]}, {"_id":0, "ID":1, "Close":1, "High":1}) 
            for record in cursor:
                print(record)
            print('\n')
            print('End - new command 2')
            print('\n')

        elif case =="7":
            print('Start - new command')
            print('\n')
            cursor = collection.find({"$and": [{"Number of trades": {"$gt": 100}}, {"Low": {"$lt": 2}}]}, {"_id":0})
            for record in cursor:
                print(record)
            print('\n')
            print('End - new command')
            print('\n')  
        elif case =="8":
            index=False
            print("Au revoir !")
        else:
            print("Something, you don't press an avalaible numbers, please restart")




print("Bonjour, bienvenue dans le menu du Projet Apache-MongoDB (Ici via l'API Binance, on traite du sujet des cryptomonnaies notamment les trades des paires de cryptomonnaies) : ")
index=True
compteur=100
while index:
    print("\n")
    print("-------------start-------------")
    print("\n")
    case=input("Do you want to read the data in the Apache topic and MongoDB (in this case, the database will be filled automatically)(Press 1) or execute some request to MongoDB (Press 2) or  exit (Press 3) > ")
    print("\n")
    if case == "1":
        compteurgenerale=ApacheRemplissage()
        conso(compteur,compteurgenerale)
        compteur+=1
    elif case =="2":
        requetesMongoDB()
    elif case =="3":
        index=False
        print("Au revoir !")
    else:
        print("Something, you don't press an avalaible numbers, please restart")
       
    print("-------------end---------------")

