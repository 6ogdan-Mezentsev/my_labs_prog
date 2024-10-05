class function:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def get_numbers_and_action(self):
        global a, b, act
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print("Операции: +, -, *, /")
        act = input("Выберите операцию: ")


    def calculate(self):
        function.get_numbers_and_action(self)
        if act == "+":
            print(function.add(self, a, b))
            return
        if act == "-":
            print(function.sub(self, a, b))
            return
        if act == "*":
            print(function.mult(self, a, b))
            return
        if act == "/":
            print(function.div(self, a, b))
            return

if __name__ == "__main__":
    calculator = function()
    calculator.calculate()
