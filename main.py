import math, random
from attacker import Attacker
from player import Player

player = Player()

def pickEvent(x):
    riskGain = 0
    if x == 0:
        x = random.randint(1, 4)
    
    randInt = 0
    #events:
    if x == 1:
        cash = random.randint(1, 6500)
        print("You got SERVED! LAWSUIT TIME!!!!")
        print("You lost " + cash + " in the lawsuit.")
        player.money -= cash
        print("Your new balance is " + str(player.money))
    elif x == 2:
        print("Congratulations! The companies employees FINALLY DECIDED TO LISTEN TO YOU. You lose some risk :)")
        player.risk -= 1
    elif x == 3:
        randInt = random.randint(1, 6)
        if randInt == 1 or randInt == 2 or randInt == 3:
            victim = "Manager"
            riskGain = 1
        elif randInt == 4 or randInt == 5:
            victim = "Administrator"
            riskGain = 2
        else:
            victim = "CFO"
            riskGain = 4
        print("Someone in your company fell victim to phishing!!!")
        print("It was a " + victim + "!!!")
        print("You gained " + riskGain + " risk.")
        Player.risk += riskGain
    elif x == 4:
        print("INVESTIGATION!")
        print("Your company is being investigated for possible loss of PII and risk to users.")
        if Player.risk == 0:
            randInt = random.randint(1000, 5000)
            print("Your company has been found to be risk-free and has been promoted by the government! You earn " + randInt + " from the promotion.")
            Player.money += randInt


def newTurn():
    #PLEASE ADD A CLEAR HERE THNX XOXO
    turn += 1
    print("Turn " + str(turn) + ".")
    if turn == 3:
        Bobe = Attacker('Bobe', 1, 10)
        print("There has been news of cybersecurity attacks from the hacker known as \"Bobe\"!")
    if turn == 9:
        rando = Attacker('Anon', 2, 25)
        print("There has been news of cybersecurity attacks from the hacker known as \"Anon\"!")
    if turn == 15:
        terminator = Attacker('T3RM1NAT0R', 4, 50)
        print("There has been news of cybersecurity attacks from the hacker known as \"T3RM1NAT0R\"!")
    if turn == 20:
        jeff = Attacker('jeff', 5, 100)
        print("There has been news of cybersecurity attacks from the hacker known as \"jeff\"!!!")
    pickEvent()


turn = 0
playerName = input("Please input your name: ")
print("Welcome " + playerName + "!!!")
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