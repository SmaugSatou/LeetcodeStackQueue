"""
Solution
"""

from collections import deque

class MyStack:
    """
    My stack implementation using queue
    """

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """ Pushes element to stack.

        Args:
            x (int): Element to push.
        """

        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """ Pops an element from peek of stack

        Returns:
            int: Element on peek
        """

        return self.q.popleft()

    def top(self) -> int:
        """ Returns an element from peek of stack

        Returns:
            int: Element on peek
        """

        return self.q[0]

    def empty(self) -> bool:
        """ Returns True is stack is empty.

        Returns:
            bool: True if empty. False if not
        """

        return not self.q

# obj = MyStack()
# obj.push(1)
# obj.push(2)
# param_2 = obj.top()
# print(param_2)
# param_3 = obj.pop()
# print(param_3)
# param_4 = obj.empty()