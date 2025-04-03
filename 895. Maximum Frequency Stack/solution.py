"""
Solution
"""

class FreqStack:
    """
    Frequency stack implementation
    """

    def __init__(self):
        self.freq_to_nums = {}
        self.num_to_freq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """ Pushes value to stack.

        Args:
            val (int): Value to push.
        """

        freq = self.num_to_freq.get(val, 0)

        freq += 1
        self.num_to_freq[val] = freq

        self.max_freq = max(self.max_freq, freq)

        if freq not in self.freq_to_nums:
            self.freq_to_nums[freq] = []

        self.freq_to_nums[freq].append(val)

    def pop(self) -> int:
        """ Pops value with the most frequency (closer to peek).

        Returns:
            int: Valu ewith the most frequency and closest to the peek of stack.
        """

        num_to_pop = self.freq_to_nums[self.max_freq].pop()

        self.num_to_freq[num_to_pop] -= 1

        if not self.freq_to_nums[self.max_freq]:
            self.max_freq -= 1

        return num_to_pop
