class Firewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def delete_rule(self, index):
        if 0 <= index < len(self.rules):
            self.rules.pop(index)

    def get_rules(self):
        return self.rules
