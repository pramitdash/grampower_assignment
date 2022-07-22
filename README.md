# grampower_assignment
This Project can used to collecting the data from MQTT source and store in the database, and available the device data information to the client flawlessly as per request.

# Prerequisite:
 I am assuming you have cloned and completed the setup of the project. 

# Lets start:
## This script is used to collect the device collected data via MQTT and store in the database, here we using mysql as the database
### Importing library and modules
 ```
import paho.mqtt.client as mqtt 
import time
import mysql.connector
 ```
# Run the project:
Open any favorite IDE, open the terminal
install the virtual enviornment package in the computer by following command:
```
pip install virtualenv
```
after that create the virtual env by below command:
```
virtualenv venv
```
Here "venv" is our current enviornment name.<br>
After that need to activate our virtual enviornment by the command:
```
> .\venv\Scripts\activate 
```
#### Good to go our virtual enviornment is now activated.<br>
install the required dependencies like django, paho-mqtt etc.<br>
## Dependencies:
### The main function:

# this method we use to save our recived data from diffrent device to the database
```
def save_message(s):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db1"
    )
    #print(mydb)
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO graph_device (id, device_desc) VALUES (%s, %s)"
        val = (0,s)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        print(e)

#this on_connect method initiated when we get connected to the MQTT server       
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))
   client.subscribe("meter/data/#")

#this on_message method helps to collect the data what we recived from the devices
def on_message(client, userdata, msg):
   #print(msg.topic+" "+str(msg.payload))
   print(str(msg.payload))
   save_message(str(msg.payload))
   char = str(msg.payload)
   if char == 'x':
       client.disconnect()

#connecting to the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("0.tcp.in.ngrok.io", 19072, 60)
client.loop_forever()


```
# Description of the function:
In the Script we are using the paho_mqtt library to connect with the MQTT server and collect the data then calling the "save_message" method which is basically storing the data as a string in the Database.

# The Main Project 
## This is the main project where i used Django as the framework.
Like we setup our virtual enviornment for the above script we did the same here also before that we are going to create our django project folder by following command 
```
> django-admin startproject realtime_graph
> python manage.py runserver # this command to run the server to test
```
Then with in the project folder we have to create our application by following command.
```
> python manage.py startapp graph

```
# Dependencies
we can install all our required packages in a single go by this command:
apart from that we need to install redis in our system.
```
pip3 install -r requirements.txt
```
It will install all the project's dependencies to the virtual enviornment.<br>
Next need to activate our flask enviornment variable.<br>
## Then we are ready to run the project with this below command
```
> python manage.py runserver
```
## For checkout the login process we need to go for the given url:
```
http://127.0.0.1:8000/accounts/login/
username: grampower
password: Password@123
```
# Description of the Project :
In this project i used the ASGI (Asynchronous Service Getway Interface) to make the data transfer flowless in between the server and client dashboard.
This project is mainly focused on socket programming architecture using Django.
I used the 'Channel' library which is a FIFO data structure based solution to communicate the server and client data transfer in bound.
Next i used the 'Redis' which is  wark as a message cache storing procedure here to store the frequently transfering data without latancy.
Then as per the ASGI data channeling architecture i follow all the configuration and procedure.
Also i interduce the Rest api concept to fetch the device information from database and send back to the client as per the request.
However this project is not complete yet its need some more implementation to run as per the assignment.

## Thank You So Much for giving the time to evaluate the project


