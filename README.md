# 🏠 NeuroHome – IoT Smart Home Automation

*(UpskillCampus Internship Project)*

## Project Overview

NeuroHome is an IoT-based Smart Home Automation system developed as part of the UpskillCampus internship program.
The project simulates real-time sensor data and allows users to monitor and control home devices through a web-based dashboard.

It integrates **MQTT for communication**, **FastAPI for backend services**, and a **web interface for visualization and control**.


## Technologies Used

* Python
* FastAPI
* MQTT (Mosquitto / Paho MQTT)
* HTML, CSS, JavaScript
* Git & GitHub


## Project Features

* Real-time temperature and motion sensor simulation
* MQTT-based message communication
* FastAPI backend to process sensor data
* Web dashboard to visualize sensor values
* Device control simulation (fan/light)

## Folder Structure

backend/   -> FastAPI backend  
devices/   -> Sensor simulator  
web/       -> Web dashboard  
screenshots/ -> Project screenshots  
demodashboard.mp4 -> Demo video  
neurohomefinalreport.docx -> Final project report  

## How to Run the Project

### 1. Start MQTT Broker

mosquitto

### 2. Run Backend

cd backend 
python main.py


### 3. Run Sensor Simulator

cd devices
python device_simulator.py


### 4. Open Dashboard

web/index.html


## Demo Video

See **demodashboard.mp4** in this repository for full working demo.


## Screenshots

All screenshots are available inside the **/screenshots** folder.


## Internship Details

* Program: UpskillCampus Internship
* Domain: IoT 
* Duration: 6 Weeks
* Project Type: Academic + Practical Industry Project


## Author

**Name:** Abrar
**GitHub:** [https://github.com/Abraih/upskillCampus](https://github.com/Abraih/upskillCampus)


## Conclusion

This project helped me understand real-world IoT system design, backend API development, message-based communication using MQTT, and frontend dashboard integration.


