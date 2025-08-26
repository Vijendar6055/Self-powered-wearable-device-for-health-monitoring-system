🌐 IoT & Machine Learning Based Respiratory Disorder Detection

This project is about developing a smart health monitoring system that can detect possible respiratory disorders using IoT sensors and Machine Learning (Random Forest). It is designed to be energy-efficient by harvesting power from renewable sources like Thermoelectric Generators and PV cells.

🚀 Project Overview

Microcontroller: ESP32 (ESP-WROOM-32)

Sensors Used:

MPU6050 (Acceleration & Movement Monitoring)

MQ-135 (Air Quality / Gas Sensor)

Power Supply:

Thermoelectric Generator + PV Cells → MPPT Controller → Battery & Supercapacitor → DC-DC Converter → ESP32 & Sensors

Machine Learning: Random Forest model trained on sensor data to predict possible respiratory disorders.

Output: Results are shown on a real-time Web Dashboard via ESP32.

✨ Features

✅ Real-time data collection from MPU6050 & MQ-135

✅ Respiratory disorder prediction using Random Forest

✅ Self-sustainable power supply using renewable energy

✅ Web-based live monitoring interface

✅ Low-cost and portable IoT healthcare solution

🏥 Applications

Early detection of respiratory problems like Asthma, Bronchitis, COPD

Remote healthcare monitoring

Smart medical IoT devices

📊 Workflow (Block Diagram)

Power Generation: Thermoelectric Generator & PV Cells

Energy Storage: Battery + Supercapacitor

Regulation: DC-DC Converter

Microcontroller (ESP32): Reads sensors

Data Processing: Machine Learning (Random Forest)

Output: Possible respiratory disorder shown on Webpage
