from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import threading

# ---------------- BASIC SETUP ----------------
BROKER = "localhost"
PORT = 1883

app = FastAPI(title="NeuroHome Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- GLOBAL DATA ----------------
sensor_data = {
    "temp": 0,
    "motion": 0
}

device_states = {
    "light": "off",
    "fan": "off"
}

power_map = {
    "light": 60,   # watts
    "fan": 80
}

# ---------------- MQTT CALLBACKS ----------------
def on_connect(client, userdata, flags, rc):
    print("MQTT connected with rc =", rc)
    client.subscribe("neurohome/livingroom/#")

def on_message(client, userdata, msg):
    value = msg.payload.decode()
    print("MQTT:", msg.topic, value)

    if msg.topic.endswith("/temp"):
        sensor_data["temp"] = int(value)
    elif msg.topic.endswith("/motion"):
        sensor_data["motion"] = int(value)

# ---------------- MQTT THREAD ----------------
def mqtt_thread():
    print("MQTT THREAD STARTED")
    client = mqtt.Client(client_id="neurohome-backend", clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_forever()

threading.Thread(target=mqtt_thread, daemon=True).start()

# ---------------- API ROUTES ----------------
@app.get("/")
def home():
    return {"message": "NeuroHome Backend Running"}

@app.get("/sensors")
def get_sensors():
    return sensor_data

@app.get("/energy")
def energy():
    total = 0
    for device, state in device_states.items():
        if state == "on":
            total += power_map[device]

    return {
        "power_watts": total,
        "power_kw": round(total / 1000, 2)
    }

@app.post("/device/{room}/{device}/{state}")
def control_device(room: str, device: str, state: str):
    topic = f"neurohome/{room}/{device}"
    publish.single(topic, state, hostname=BROKER)
    device_states[device] = state
    return {
        "room": room,
        "device": device,
        "state": state,
        "status": "sent"
    }
