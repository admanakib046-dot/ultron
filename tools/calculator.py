class calculator:

    def calculate(self, expression):
        try:
            result = eval(expression)
            return str(result)
        except Exception:
            return "Invalid calculation."
