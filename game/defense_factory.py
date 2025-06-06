from game.defenses import (
    Firewall, 
    Antivirus, 
    IntrusionDetectionSystem, 
    MultiFactorAuthentication, 
    AIAnomalyDetection, 
    IncidentResponsePlan, 
    SIEM,
    NetworkSegmentation,
    DeceptionTechnology
)

class DefenseFactory:
    ALL_DEFENSES = [
        Firewall,
        Antivirus,
        IntrusionDetectionSystem,
        MultiFactorAuthentication,
        AIAnomalyDetection,
        IncidentResponsePlan,
        SIEM,
        NetworkSegmentation,
        DeceptionTechnology,
    ]

    def create_all(cls, state):
        return [defense_class(state) for defense_class in cls.ALL_DEFENSES]

    def list_all_defenses(cls):
        return [defense_class.name for defense_class in cls.ALL_DEFENSES]