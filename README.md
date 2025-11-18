Smart Agriculture IoT Monitoring System
A simulated IoT project that demonstrates real-time monitoring of agricultural conditions using temperature and moisture sensors. This system simulates IoT devices, processes sensor data with alert triggers, and provides a real-time dashboard for visualization.

Features:
IoT Device Simulation: Generates realistic sensor data for temperature and moisture
Real-time Alert System: Triggers alerts for high temperature (>35°C) and low moisture (<30%)
Live Dashboard: Interactive Streamlit dashboard with real-time charts
File-based Message Queue: Simulates message passing between components using JSON files
Modular Architecture: Separated components for data generation, processing, and visualization

📁 Project Structure
text
smart-agriculture-iot/
│
├── device_simulator.py    # Simulates IoT sensors
├── local_function.py      # Processes data and triggers alerts
├── dashboard.py           # Streamlit web dashboard
├── iot_messages.json      # Generated - message queue (raw data)
└── README.md              # This file
🛠️ Installation
Clone the repository

bash
git clone <your-repo-url>
cd smart-agriculture-iot
Install required dependencies

bash
pip install streamlit pandas
🎯 Usage
Method 1: Manual Execution (Recommended for development)
Start the IoT Device Simulator (Terminal 1)

bash
python device_simulator.py
This generates simulated sensor data every 3 seconds

Start the Data Processor (Terminal 2)

bash
python local_function.py
This processes data and triggers alerts for abnormal conditions

Launch the Dashboard (Terminal 3)

bash
streamlit run dashboard.py
Access the dashboard at http://localhost:8501

Method 2: Using the provided startup script
bash
# On Windows
start_agriculture_system.bat

# On Linux/Mac
chmod +x start_agriculture_system.sh
./start_agriculture_system.sh
📊 System Architecture
text
IoT Devices (Simulator)
        ↓
[Raw Data → iot_messages.json]
        ↓
Data Processor (local_function.py)
        ↓
[Processed Data → processed_data.json]
        ↓
Web Dashboard (Streamlit)
🔧 Components Description
1. Device Simulator (device_simulator.py)
Simulates IoT sensors with device ID "simDevice01"

Generates random temperature (25-40°C) and moisture (20-60%) readings

Writes data to iot_messages.json every 3 seconds

2. Data Processor (local_function.py)
Monitors iot_messages.json for new data

Triggers alerts for:

🔥 High Temperature: >35°C

💧 Low Moisture: <30%

Saves processed data to processed_data.json

3. Dashboard (dashboard.py)
Real-time Streamlit web application

Displays line chart of last 20 readings

Auto-refreshes every 3 seconds

📈 Sample Data Format
Raw Sensor Data:

json
{"device_id": "simDevice01", "temperature": 32.45, "moisture": 45.67}
Processed Data:

json
{"device_id": "simDevice01", "temperature": 32.45, "moisture": 45.67}
🚨 Alert Conditions
Temperature Alert: Values above 35°C

Moisture Alert: Values below 30%

🛠️ Customization
Modify Sensor Ranges
Edit in device_simulator.py:

python
"temperature": round(random.uniform(25, 40), 2),  # Change min/max
"moisture": round(random.uniform(20, 60), 2)      # Change min/max
Change Alert Thresholds
Edit in local_function.py:

python
if temp > 35:  # Change temperature threshold
if moist < 30: # Change moisture threshold
Adjust Update Intervals
Modify time.sleep(3) in all files to change refresh rates.

📋 Prerequisites
Python 3.7+
Required packages:
streamlit
pandas




bash
streamlit run dashboard.py --server.port 8502
