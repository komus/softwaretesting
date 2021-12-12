"""
Create a project
Create a virtual environment
Create a class Calculator that should perform the following actions:
Addition / Subtraction
Multiplication / Division
Take (n) root of number
Reset memory (Calculator must have its own memory, meaning it should manipulate its starting number 0 until it is reset.). This means that for example calculator should perform actions with a value inside its memory (for this example value inside the calculator's memory is 0): calculator.add(2) results in 2.

"""

from typing import Union


class Calculator:
    def __init__(self, number: Union[int, float] = 0):
        """
         Constructor of Calculator
         .__value: the number passed by the user.
         :param number: the initial value of the calculator. If not specified, value is 0
        """
        self.__value = number

    @staticmethod
    def __validate_user_input(number: Union[int, float]):
        if not isinstance(number, (int, float)):
            raise TypeError("Calculator only accepts int and float")

    def reset(self) -> None:
        """
        Resets the value to zero
        :return: None
        """
        self.__value = 0

    def add(self, number: Union[int, float]) -> float:
        self.__validate_user_input(number)
        self.__value += number
        return self.__value

    def sub(self, number):
        self.__validate_user_input(number)
        self.__value -= number
        return self.__value

    def multi(self):
        pass

    def div(self, number: Union[int, float]) -> float:
        self.__validate_user_input(number)
        try:
            self.__value /= number
            return self.__value
        except ZeroDivisionError as err:
            "Not raising error but displaying it"
            print(f"{err.args[0]}")

    @property
    def get_calculator_value(self):
        return self.__value

    def root(self,  number: Union[int, float]):
        self.__validate_user_input(number)
        # zero cannot be a root number
