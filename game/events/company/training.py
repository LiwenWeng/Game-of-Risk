from game.events.base_event import Event

class EmployeeTraining(Event):
    name = "Employee Training Initiative"
    description = "Company-wide security training reduces the risk of human error."

    def apply(self):
        self.state.risk_level = max(0, self.state.risk_level - 0.1)
        self.state.log("Training completed. Risk level slightly reduced.")

    def process_weight(self):
        if self.state.risk_level >= 0.5:
            self.weight += 1
