import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(topic, payload=None, qos=0, retain=False):
    print("Welcome to FloppyCHAT")

def on_disconnect(client,userdata, rc):
    if rc !=0:
        print("Gone Too Soon")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect

client.connect("82.165.16.151 -t UCC/pihealth", 1883, 60)

#To take in the Identity of the Client
user = str(input("Enter your Name: "))


while True:
    mgs =[{"topic": "paho/test/multiple", "payload":"multiple 1"}]
    publish.multiple(msgs, user)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()


#function for disconnect
        
mqtt.on_disconnect = on_disconnect
    
    