
# DoS Detection Dashboard

Welcome to the Live DoS Attack Dashboard! This interactive platform provides real-time insights into Denial of Service (DoS) attacks, making it easy to monitor malicious activity on your network. Using Flask, SocketIO, and Chart.js, the dashboard continuously reads data from a CSV file that tracks the number of SYN packets sent from each IP address.

With a dynamic line chart, you can visualize the frequency of SYN packets, allowing you to identify potential attacks as they happen. The live table displays the latest data, providing an easy-to-read overview of the attack details.

![dash](dash.png)

## Features
- **Live Chart:** Displays the number of SYN packets over time.
- **Top Offenders Table:** Shows the IPs that have sent the most SYN packets.
- **Live Update:** The data is updated every 5 seconds.

## Prerequisites
To run this project, you'll need the following Python packages:
- Python 3
- Flask
- Flask-SocketIO
- Eventlet
- Chart.js

### Install Dependencies
First, create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # For Unix/macOS systems
````

Then, install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **Running the Project**

1. **Start the firewall** (`fire.py`) to monitor and detect SYN packets:

   ```bash
   python fire.py
   ```

2. **Run the test script** (`test.py`) to simulate SYN flood packets and generate traffic for the dashboard to monitor:

   ```bash
   python test.py
   ```

3. Once the firewall and test script are running, **start the Flask server** to view the DoS attack data on the dashboard:

   ```bash
   python dashboard.py
   ```

This sequence ensures the firewall is actively monitoring, test traffic is being generated, and the Flask server is displaying live updates on the dashboard.

---


2. Open your browser and navigate to:

   ```
   http://localhost:5000
   ```

The dashboard will display the live SYN packet data and the top offenders table.

### Running with sudo

In case you need to run the script with elevated privileges, especially for network-related tasks, use the following command:

```bash
sudo /path/to/venv/bin/python3 dashboard.py
```

Make sure to replace `/path/to/venv/` with the actual path to your virtual environment. This will ensure that the required environment is used with elevated permissions.




