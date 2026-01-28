import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Simulator connected to MQTT broker with rc:", rc)

client = mqtt.Client(
    client_id="neurohome-simulator",
    clean_session=True
)

client.on_connect = on_connect
client.connect(BROKER, PORT, keepalive=60)

# 🔥 THIS IS THE MISSING LINE
client.loop_start()

print("NeuroHome Virtual Devices Started...")

while True:
    temp = random.randint(22, 35)
    motion = random.choice([0, 1])

    client.publish("neurohome/livingroom/temp", temp)
    client.publish("neurohome/livingroom/motion", motion)

    print(f"Temp: {temp}°C | Motion: {motion}")
    time.sleep(3)
