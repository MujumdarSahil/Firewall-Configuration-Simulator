class TrafficSimulator:
    def __init__(self, firewall):
        self.firewall = firewall

    def simulate(self, packet):
        rules = self.firewall.get_rules()
        # Logic to check if the packet is allowed
        for rule in rules:
            if rule == "ALLOW ALL":  # Example rule
                return True
        return False
