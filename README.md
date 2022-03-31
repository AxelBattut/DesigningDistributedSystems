# Welcome to our Designing-Distributed-Systems Project.

In this project you will be abe to use at the same time the MongoDB, Apache and Kafka Connect to retrieve data from the Binance API and do some queries on it.
First we get our date via our file CreationTexte-BATTUT-CERIO-GUITTON.py and we have our data in our text file.
Once the data retrieved we will indeed use Kafka to put it in a topic and use Kafka connect with mongodb to perform queries on the data.

The main code (Kafka connection and Mongodb queries) is located in **Projet-DDS-BATTUT-CERIO-GUITTON.py**. It's the only file you'll need to run (manipulations to know how to run below).

Be aware that you might need to wait a bit for the response of the api key when launching CreationTexte-BATTUT-CERIO-GUITTON.py
# How to run

## Initialization (in your terminal)

Launch MongoDB

mongo --host 127.0.0.1:27017

Launch Zookeeper

zookeeper-server-start.sh config/zookeeper.properties

Launch Kafka

kafka-server-start.sh config/server.properties

And for the display of the data of the topic :

bin/kafka-console-consumer.sh --topic ProjetDDS --from-beginning --bootstrap-server localhost:9092


## Our Topic and Database 

For MongoDB :

Our database is called **"DDS"** and our collection is called **"myCollection"**.

For Kafka :

Our Topic is called **"ProjetDDS"**.

## Manipulation

You can read the code and import the librairies we are using on the IDE of your choice. The import of the librairies is already done on our file. 
You can also install the librairies if it's not already done (pip install name_of_your_library).


# Finally

You need to use three files, the jupyter notebook Projet-DDS-BATTUT-CERIO-GUITTON.py, fichier.txt (the file who contains the data of CreationTexte-BATTUT-CERIO-GUITTON.py) 
and CreationTexte-BATTUT-CERIO-GUITTON.py (the file who produces the text file), you need to put this three files in the same directory (directory of your choice).

Finally, when you see this line in Projet-DDS-BATTUT-CERIO-GUITTON.py:  

```py
%run '/home/alexis/DDS/CreationTexte-BATTUT-CERIO-GUITTON.py'
```

**Change it by your full path (the path of CreationTexte-BATTUT-CERIO-GUITTON.py).**


Work done by Alexis Cerio, Ines Guitton and Axel Battut.
