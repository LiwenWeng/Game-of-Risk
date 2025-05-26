#all comments are just suggestions for further options in the game

class Attacker:
    def __init__(self, name, strength, threat):
        self.name = name
        self.willpower = 100
        self.strength = strength
        self.threat = threat
        # attacking actions: DoS, DDoS, SQL injection, Trojan, Spoofing, Social Engineering attacks

john = Attacker('John', 34, 2)


class Player: 
    def __init__(self, health, vulerabilityLevel, vulnerabilities, ):
        pass
# vulerability check actions: IDS Setup, SIEM detection, Blue/Red exercise
# defensive actions: honeypot (trap), firewall, patching, 
# attacking actions: Power Outage, SWAT, counterhack, (high levels) drone

#upgrades: Network Segmenting, VPN upgrade, Antivirus upgrades, Firewall upgrades, better traps, Threat Detection upgrades, Encryption software, outsourcing