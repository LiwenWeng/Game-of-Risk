#all comments are just suggestions for further options in the game

class Attacker:
    def __init__(self, name, threat, willpower):
        self.name = name
        self.willpower = willpower
        self.threat = threat
        # attacking actions: DoS, DDoS, SQL injection, Trojan, Spoofing, Social Engineering attacks

john = Attacker('John', 34, 2)


class Player: 
    def __init__(self):
        self.health = 100
        self.vunerabilityLevel = 0
        self.vulnerabilities = 0

class Events:
    def __init__(self, timesCalled, threatAdjustment, vunlerabilityAdjustment):
        self.lastCalled = False
        self.timesCalled = timesCalled
        self.threatAdjustment = threatAdjustment
        self.vulnerabilityAdjustment = vunlerabilityAdjustment
# vulerability check actions: IDS Setup, SIEM detection, Blue/Red exercise
# defensive actions: honeypot (trap), firewall, patching, 
# attacking actions: Power Outage, SWAT, counterhack, (high levels) drone

#upgrades: Network Segmenting, VPN upgrade, Antivirus upgrades, Firewall upgrades, better traps, Threat Detection upgrades, Encryption software, outsourcing

#event example: (negative) an employee finds a USB and connects it to a device with their work information and documents on it.
#event example: (positive) 