import collections
from typing import Dict, List


class Stack:
    def __init__(self, id):
        self.id = id
        self.items = collections.deque([])

    def push(self, item: float):
        self.items.append(item)

    def pop(self) -> float:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def apply_operand(self, operand):
        if len(self.items) < 2:
            raise ValueError(
                "Stack does not have enough operands for operation"
            )

        # Pop the top two operands from the stack
        operand2 = self.pop()
        operand1 = self.pop()

        # Apply the operand and push the result back onto the stack
        if operand == "+":
            result = operand2 + operand1
        elif operand == "-":
            result = operand2 - operand1
        elif operand == "*":
            result = operand2 * operand1
        elif operand == "/":
            if operand1 == 0:
                self.push(operand1)
                self.push(operand2)
                raise ZeroDivisionError("Division by zero")
            result = operand2 / operand1
        else:
            raise ValueError("Invalid operand")

        self.push(result)


class RPNCalculator:
    def __init__(self):
        self.stacks = {}
        self.operands = ["+", "*", "-", "/"]
        self.counter_id = 0

    def create(self):
        stack_id = self.counter_id
        if stack_id not in self.stacks:
            self.stacks[stack_id] = Stack(stack_id)
            self.counter_id += 1
            return stack_id
        else:
            raise ValueError("Stack with that name already exists")

    def get_stacks(self) -> Dict:
        return self.stacks

    def get_operands(self) -> List:
        return self.operands

    def get(self, stack_id):
        if stack_id in self.stacks:
            return self.stacks[stack_id].items
        else:
            return None

    def push(self, stack_id, value):
        if stack_id in self.stacks:
            self.stacks[stack_id].push(value)
            return self.stacks[stack_id].items
        else:
            return None

    def delete(self, stack_id):
        if stack_id in self.stacks:
            del self.stacks[stack_id]
            return self.stacks
        else:
            return None

    def apply_operand(self, stack_id, operand):
        if stack_id not in self.stacks:
            return None
        if operand not in self.operands:
            raise ValueError("Operand not supported")

        stack = self.stacks[stack_id]

        stack.apply_operand(operand)

        return stack.items
