import paho.mqtt.client as m
import pandas as pd
import time
broker = "localhost"
port = 1883
topic = "hyperloop/data"
file_path = "data.csv"

def on_message(client,userdata,msg):
    data = msg.payload.decode()
    print(data)
    with open(file_path,"a") as f:
        f.write(data + "\n")

client = m.Client()
client.on_message = on_message
client.connect(broker,port)
client.subscribe(topic)
client.loop_forever()
'''
the subscriber should be running forever so that the data send by the publisher is received continuosly by the subscriber.
 
 but how do i implement this in code

the main question is how the data gets stored and how the streamlit application is going to be using that data to visualize it using graphs


'''
