import pytest

class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def add(self,a,b):
        self._last_answer = a + b
        return self._last_answer

    def sub(self,a,b):
        self._last_answer = a - b
        return self._last_answer

    def mul(self,a,b):
        self._last_answer = a * b
        return self._last_answer

    def div(self, a, b):
        self._last_answer = a / b
        return self._last_answer

    def mod(self, a, b):
        self._last_answer = a % b 
        return self._last_answer 


NUMBER_1 = 3.0
NUMBER_2 = 2.0

@pytest.fixture
def calculator():
    return Calculator()


def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer

def testlast_answer_init(calculator):
    assert calculator.last_answer == 0.0

def test_add(calculator):
    answer = calculator.add(NUMBER_1, NUMBER_2)
    verify_answer(5.0, answer, calculator.last_answer )

def test_sub(calculator):
    answer = calculator.sub(NUMBER_1, NUMBER_2)
    verify_answer(1.0, answer, calculator.last_answer )

def test_mul(calculator):
    answer = calculator.mul(NUMBER_1, NUMBER_2)
    verify_answer(6.0, answer, calculator.last_answer ) 

def test_div(calculator):
    answer = calculator.div(NUMBER_1, NUMBER_2)
    verify_answer(1.5, answer, calculator.last_answer )

def test_mod(calculator):
    answer = calculator.mod(NUMBER_1, NUMBER_2)
    verify_answer(1.0, answer, calculator.last_answer )