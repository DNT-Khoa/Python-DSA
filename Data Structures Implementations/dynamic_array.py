"""
    List of operations we need for a dynamic array
    - access value as specific index: A[k]
    - set value as specific index: A[k] = value
    - get length 
    - append a new element at the end of array (with automatic resizing)
    - insert value as a specific index
    - delete value from the end of array
    - remove value at specific index
"""
import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1  # by default, the array capacity will be 1
        self._A = self._make_array(self._capacity)

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError("Index out of bound!")

        return self._A[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self._n:
            raise IndexError("")

        self._A[index] = value

    def __len__(self):
        return self._n

    def append(self, value):
        # Firstly, check if the capacity is already full
        if self._n == self._capacity:
            self._resize_array(self._capacity * 2)

        # Add value at the end of array
        self._A[self._n] = value
        # Increment the length of array
        self._n += 1

    def insert(self, index, value):
        if not 0 <= index < self._n:
            raise IndexError("Index out of bound!")

        # Firstly, check if the capacity is already full
        if self._n == self._capacity:
            self._resize_array(self._capacity * 2)

        # Shift element after specified index one step to the right
        for i in range(self._n, index, -1):
            self._A[i] = self._A[i - 1]

        # Assign value at specified index
        self._A[index] = value
        # Increment the length of array
        self._n += 1

    def delete(self):
        if self._n == 0:
            return

        # Set value of last element to 0
        self._A[self._n - 1] = 0
        # Decrement the length of array
        self._n -= 1

    def removeAt(self, index):
        if self._n == 0:
            return

        if not 0 <= index < self._n:
            raise IndexError("Index out of bound!")

        # Shift all values after specified index 1 step to the left
        for i in range(index, self._n - 1):
            self._A[i] = self._A[i + 1]

        # Assign the last element with value 0
        self._A[self._n - 1] = 0
        # Decrement the length of array
        self._n -= 1

    def _resize_array(self, capacity):
        B = self._make_array(capacity)
        self._capacity = capacity

        # Assign elements from old array to new one
        for i in range(self._n):
            B[i] = self._A[i]

        # Replace the old array with new one
        self._A = B

    def _make_array(self, capacity):
        return (ctypes.py_object * capacity)()


# Instantiate
arr = DynamicArray()
# Append new element
arr.append(1)
arr.append(2)
arr.insert(1, 3)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[2])
