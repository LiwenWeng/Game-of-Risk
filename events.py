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