import re
import abc


class Action(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass


class Calculator(Action):
    operators = ['+', '-', '*', '/']

    def __init__(self, operator, a, b):
        self.operator = {
            'Multiplication of': '*',
            'times': '*',
            'Mul': '*',
            'x': '*',
            'Multiply': '*',
            'Add': '+',
            'Sub': '-',
            'subtract': '-',
        }[operator] if operator not in self.operators else operator
        self.numbers = [a, b]

    def execute(self):
        return str(eval(self.operator.join(self.numbers)))


patterns = [
    (
        re.compile(r'(?P<a>\d+)\s*(?P<operator>[-+/*x])\s*(?P<b>\d+)'),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Add)\s*(?P<a>\d+)\s*(with|by)\s*(?P<b>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Sub|subtract)\s*(?P<b>\d+)\s*(from)\s*'
            r'(?P<a>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Multiply|Mul)\s*(?P<a>\d+)\s*(with|by)\s*'
            r'(?P<b>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>(Multiplication(\s)of))\s*(?P<a>\d+)\s*'
            r'(and)\s*(?P<b>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(r'(?P<a>\d+)\s*(?P<operator>(times))\s*(?P<b>\d+)'),
        Calculator
    ),
]


class ParseError(Exception):
    def __init__(self, command):
        super().__init__(f'Cannot parse: {command}')


def find(command):
    for pattern, action in patterns:
        match = pattern.match(command)
        if match:
            return action, match.groupdict()

    raise ParseError(command)
