from app.firewall import Firewall
from app.traffic import TrafficSimulator

# Set up firewall
firewall = Firewall()
firewall.add_rule("ALLOW ALL")

# Simulate traffic
traffic_simulator = TrafficSimulator(firewall)
packet = {"source": "192.168.1.1", "destination": "8.8.8.8", "port": 80}

if traffic_simulator.simulate(packet):
    print("Traffic allowed!")
else:
    print("Traffic blocked!")
