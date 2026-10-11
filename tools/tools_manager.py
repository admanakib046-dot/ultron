from tools.calculator import calculator

class ToolsManager:
    def __init__(self):
        self.calculator = calculator()
    def use(self,tool,data):
        if tool =="calculator":
            return self.calculator.calculate(data)
        return "Tool not found"