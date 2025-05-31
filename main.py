import math, random

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
    def __init__(self, threatAdjustment, vulnerabilityAdjustment, damage, cost):
        self.lastCalled = False
        self.timesCalled = 0
        self.threatAdjustment = threatAdjustment
        self.vulnerabilityAdjustment = vulnerabilityAdjustment
        self.damage = damage
        self.cost = cost

powerOutage = Events(2, 1, 15, 0)
lawsuit = Events(0, 0, 0, 5000)



def pickEvent():
    x = random.randint(1, 2)
    if x == 1:
        cash = random.randint(1, 6500)
        print("You got SERVED! LAWSUIT TIME!!!!")
        print("You lost " + cash + " in the lawsuit.")
        player.money -= cash
        print("Your new balance is " + str(player.money))
    elif x == 2:
        print("Congratulations! The companies employees FINALLY DECIDED TO LISTEN TO YOU. Your company is slightly less vulnerable :)")
        player.vunerabilityLevel -= 1

def newTurn():
    turn += 1
    print("Turn " + str(turn) + ".")
    if turn == 3:
        Bobe = Attacker('Bobe', 1, 10)
    if turn == 9:
        rando = Attacker('Rando', 2, 25)
    if turn == 15:
        terminator = Attacker('T3RM1NAT0R', 4, 50)
    if turn == 20:
        jeff = Attacker('jeff', 5, 100)
    pickEvent()

turn = 0
playerName = input("Please input your name: ")
print("Welcome " + playerName + "!!!")
player = Player()
print("The objective of this game is to survive and not let your company go under for as long as possible.")
print("You start with 100 life, and $10,000")
print("You also start with no vulnerabilities to exploit, but events and attackers can open them up!")
print("Good luck!")
newTurn()


#turn three, nine, fifteen, and twenty attackers are 'added'. 

# vulerability check actions: IDS Setup, SIEM detection, Blue/Red exercise
# defensive actions: honeypot (trap), firewall, patching, 
# attacking actions: Power Outage, SWAT, counterhack, (high levels) drone

#upgrades: Network Segmenting, VPN upgrade, Antivirus upgrades, Firewall upgrades, better traps, Threat Detection upgrades, Encryption software, outsourcing

#event example: (negative) an employee finds a USB and connects it to a device with their work information and documents on it.
#event example: (positive) 