import paho.mqtt.client as m
import random
import time
broker = "localhost"
port = 1883
topic = "hyperloop/data"

client = m.Client()
client.connect(broker, port)

i = 0
while i in range(10):
    status = ["operational","docked","maintenance"]
    data = {
        "speed":random.randint(300,1200),
        "battery":random.randint(0,100),
        "status":random.choices(status)
    }
    client.publish(topic,str(data))
    i += 1
    time.sleep(4)
