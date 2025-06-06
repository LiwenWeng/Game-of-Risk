import random
from typing import Type

from game.events.attack import AttackEvent
from game.events.base_event import Event

class EventManager:
    def __init__(self, state, player):
        self.state = state
        self.player = player
        self.attacks: list[Type[AttackEvent]] = []
        self.company: list[Type[Event]] = []

    def register_attack(self, event_cls: Type[AttackEvent]):
        self.attacks.append(event_cls)

    def register_company(self, event_cls: Type[Event]):
        self.company.append(event_cls)

    def get_weighted_events(self, event_classes: list[Type[Event]]) -> list[Event]:
        instances = [cls(self.state, self.player) for cls in event_classes]
        for event in instances:
            if hasattr(event, "process_weight"):
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
        max_attacks = 0
        if risk >= 0.8:
            max_attacks = 3
        elif risk >= 0.5:
            max_attacks = 2
        elif risk >= 0.25:
            max_attacks = 1

        attack_events = self.get_weighted_events(self.attacks)
        company_events = self.get_weighted_events(self.company)

        company_event = self.select_random_event(company_events)
        if company_event:
            triggered_events.append(company_event)

        for _ in range(max_attacks):
            attack_event = self.select_random_event(attack_events)
            if attack_event:
                triggered_events.append(attack_event)
                attack_events.remove(attack_event)

        for event in triggered_events:
            self.state.log(f"{event.name}: {event.description}")
            event.apply()
