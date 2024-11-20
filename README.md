# Firewall-Configuration-Simulator
![Screenshot 2024-11-20 225022](https://github.com/user-attachments/assets/7b71169a-6350-458f-8f21-1c7fc642588c)




Description
The Firewall Configuration Simulator is a Python-based application that allows users to simulate and test firewall rules and network traffic behavior. This project features a graphical user interface (GUI) for ease of interaction and backend functionality to configure and test custom firewall rules.

Features
Add, remove, and view firewall rules.
Simulate network traffic and observe whether traffic is allowed or blocked.
Customizable interface with a background wallpaper.
Modular design to separate GUI, firewall logic, and traffic simulation.
Project Structure
bash
Copy code
firewall_simulator/
│
├── assets/
│   └── wallpaper.png  # Background image for the GUI
│
├── app/
│   ├── __init__.py    # Marks the folder as a Python package
│   ├── gui.py         # GUI logic (Tkinter-based)
│   ├── firewall.py    # Firewall logic
│   └── traffic.py     # Traffic simulation logic
│
├── tests/
│   └── test_firewall.py  # Unit tests for the firewall and traffic simulator
│
├── main.py           # Main script to launch the GUI application
├── test_simulation.py # Standalone traffic simulation script
├── README.md         # Project documentation (this file)
└── requirements.txt  # Python dependencies
Requirements
Python 3.8 or newer
Libraries:
tkinter (comes pre-installed with Python on most platforms)
Pillow for image handling (must be installed manually)
Setup Instructions
Clone or download the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/firewall_simulator.git
cd firewall_simulator
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure the assets folder contains wallpaper.png. If missing, add a background image with this name.

Usage
Run the GUI Application
Start the app by running:
bash
Copy code
python main.py
Use the GUI to:
Add firewall rules.
Simulate traffic.
View results in real-time.
Run Traffic Simulation Standalone
For testing without the GUI:

bash
Copy code
python test_simulation.py
Testing
Unit tests are located in the tests/ folder.
Run all tests using:
bash
Copy code
python -m unittest discover -s tests
Code Details
Firewall (firewall.py)
This module defines the Firewall class:

add_rule(rule: str): Adds a firewall rule.
remove_rule(rule: str): Removes a firewall rule.
evaluate(packet: dict): Checks if a packet passes the rules.
Traffic Simulator (traffic.py)
This module defines the TrafficSimulator class:

simulate(packet: dict): Simulates a network packet against the firewall rules.
GUI (gui.py)
The GUI uses Tkinter:

Displays firewall rules in a list.
Allows users to add/remove rules and simulate traffic.
Example
Traffic Simulation Code
Here’s an example of how the firewall and traffic simulation can be used programmatically:

python
Copy code
from app.firewall import Firewall
from app.traffic import TrafficSimulator

# Set up the firewall
firewall = Firewall()
firewall.add_rule("ALLOW ALL")

# Simulate traffic
traffic_simulator = TrafficSimulator(firewall)
packet = {"source": "192.168.1.1", "destination": "8.8.8.8", "port": 80}

if traffic_simulator.simulate(packet):
    print("Traffic allowed!")
else:
    print("Traffic blocked!")
Expected Output
If the firewall rule ALLOW ALL is active:

Copy code
Traffic allowed!
License
This project is licensed under the MIT License.

