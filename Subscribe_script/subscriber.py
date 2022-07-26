
import paho.mqtt.client as mqtt 
import time
import mysql.connector

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
        
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))
   client.subscribe("meter/data/#")

def on_message(client, userdata, msg):
   #print(msg.topic+" "+str(msg.payload))
   print(str(msg.payload))
   save_message(str(msg.payload))
   char = str(msg.payload)
   if char == 'x':
       client.disconnect()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("0.tcp.in.ngrok.io", 19072, 60)
client.loop_forever()


#################end for the function############################






















############################################################################
#broker_address, port=19072, keepalive=60, bind_address=""
# import paho.mqtt.client as mqttclient
# import time
# def on_connect(client,userdata,flags,rc):
#     if rc == 0:
#         print("client is connected")
#         global connected
#         connected=True
#     else:
#         print("client is not connected")
# def on_message(client,userdata,message):
#     print("Message recived" + str(message.payload.decode("utf-8")))
#     #print("Topic"+str(message.topic))

# connected=False
# Messagerecieved=False
# broker_address="0.tcp.in.ngrok.io"
# port=19072
# user="test_user"
# password="grampower"
# client = mqttclient.Client("MQTT")
# client.username_pw_set(user,password=password)
# client.on_connect=on_connect
# client.connect(broker_address,port=port)
# client.loop_start()
# client.subscribe("meter/data")
# while connected!=True:
#     time.sleep(0.2)
# while Messagerecieved!=True:
#     time.sleep(0.2)
# client.loop_stop()

##########################################################################
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    save_message(str(message.payload.decode("utf-8")))
    

broker_address="0.tcp.in.ngrok.io"

print("creating new instance")
client = mqtt.Client("P1") 
client.on_message=on_message 
print("connecting to broker")
client.connect(broker_address,port=19072) 
client.loop_start() 
print("Subscribing to topic","meter/data")
client.subscribe("meter/data")
print("Publishing message to topic","meter/data")
client.publish("meter/data","meter data")
time.sleep(4) # wait
client.loop_stop() 







# import paho.mqtt.client as mqtt

