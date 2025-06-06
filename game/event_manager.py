import random
from typing import Type

from game.events.attack import AttackEvent
from game.events.attack import SupplyChainBreach, Phishing, DDOS, InsiderThreat, Ransomware, ZeroDayExploit
from game.events.company import (
    InvestorConfidence,
    IndustryPartnership,
    GrantAIDevelopment,
    BudgetCuts,
    DataMisconfiguration,
    EmployeeTraining
)
from game.events.base_event import Event

class EventManager:
    def __init__(self, state, player):
        self.state = state
        self.player = player

        self.attacks: list[Type[AttackEvent]] = [
            Phishing,
            DDOS,
            InsiderThreat,
            Ransomware,
            SupplyChainBreach,
            ZeroDayExploit,
        ]

        self.company: list[Type[Event]] = [
            InvestorConfidence,
            IndustryPartnership,
            GrantAIDevelopment,
            BudgetCuts,
            DataMisconfiguration,
            EmployeeTraining,
        ]

    def get_weighted_events(self, event_classes: list[Type[Event]]) -> list[Event]:
        instances = [cls(self.state, self.player) for cls in event_classes]
        for event in instances:
            event.process_weight()
        return instances

    def select_random_event(self, event_list: list[Event], chance_of_none: float = 0.1) -> Event | None:
        if not event_list:
            return None

        total_weight = sum(e.weight for e in event_list)
        none_weight = total_weight * (chance_of_none / (1 - chance_of_none))
        
        choices = event_list + [None]
        weights = [e.weight for e in event_list] + [none_weight]

        return random.choices(choices, weights=weights, k=1)[0]

    def trigger_events_for_day(self):
        triggered_events = []

        risk = self.state.risk_level
        max_attacks = 1
        if risk >= 0.67:
            max_attacks = 5
        elif risk >= 0.33:
            max_attacks = 3

        attack_events = self.get_weighted_events(self.attacks)
        company_events = self.get_weighted_events(self.company)

        random.shuffle(company_events)
        random.shuffle(attack_events)

        company_event = self.select_random_event(company_events)
        if company_event:
            triggered_events.append(company_event)
        else:
            self.state.log("No company events occurred today.")

        for _ in range(min(max_attacks, len(attack_events))):
            attack_event = self.select_random_event(attack_events)
            if attack_event:
                triggered_events.append(attack_event)
                attack_events.remove(attack_event)
            else:
                self.state.log("No attacks occurred today.")

        for event in triggered_events:
            self.state.log(f"{event.name}: {event.description}")
            event.apply()
