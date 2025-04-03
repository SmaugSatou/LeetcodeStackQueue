"""
Solution
"""

class MyQueue:
    """
    My queue implementation using stacks.
    """

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        """ Pushes an element to queue

        Args:
            x (int): Elememt to push.
        """

        while self.st1:
            self.st2.append(self.st1.pop())

        self.st1.append(x)

        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:
        """ Pops an element from queue.

        Returns:
            int: First element in queue.
        """

        return self.st1.pop()

    def peek(self) -> int:
        """ Returns an element from peek of queue.

        Returns:
            int: First element in queue.
        """

        return self.st1[-1]

    def empty(self) -> bool:
        """ Returns True if queue is empty.

        Returns:
            bool: True if empty. False if not
        """

        return not self.st1

# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
