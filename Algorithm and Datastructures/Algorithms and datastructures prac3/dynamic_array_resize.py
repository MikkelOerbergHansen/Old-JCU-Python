
from dynamic_array import DynamicArray


class DynamicArrayResize(DynamicArray):
    def __init__(self, resizeValue):
        """Create an empty array."""
        super().__init__()
        self._resizeValue = resizeValue

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(int(self._resizeValue * self._capacity)+1)  # so double capacity
        self._A[self._n] = obj
        self._n += 1
