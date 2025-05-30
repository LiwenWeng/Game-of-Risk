#all comments are just suggestions for further options in the game

class Attacker:
    def __init__(self, name, threat, willpower):
        self.name = name
        self.willpower = willpower
        self.threat = threat
        # attacking actions: DoS, DDoS, SQL injection, Trojan, Spoofing, Social Engineering attacks


class Player: 
    def __init__(self):
        self.health = 100
        self.vunerabilityLevel = 0
        self.vulnerabilities = 0
        self.money = 10000

class Events:
    def __init__(self, threatAdjustment, vunlerabilityAdjustment, damage):
        self.lastCalled = False
        self.timesCalled = 0
        self.threatAdjustment = threatAdjustment
        self.vulnerabilityAdjustment = vunlerabilityAdjustment
        self.damage = damage

turn = 0
playerName = input("Please input your name: ")
print("Welcome " + playerName + "!!!")
player = Player()
print("The objective of this game is to survive and not let your company go under for as long as possible.")
print("You start with 100 life, and $10,000")
print("You also start with no vulnerabilities to exploit, but events and attackers can open them up!")
print("Good luck!")


#turn three, nine, fifteen, and twenty attackers are 'added'. 

# vulerability check actions: IDS Setup, SIEM detection, Blue/Red exercise
# defensive actions: honeypot (trap), firewall, patching, 
# attacking actions: Power Outage, SWAT, counterhack, (high levels) drone

#upgrades: Network Segmenting, VPN upgrade, Antivirus upgrades, Firewall upgrades, better traps, Threat Detection upgrades, Encryption software, outsourcing

#event example: (negative) an employee finds a USB and connects it to a device with their work information and documents on it.
#event example: (positive) 