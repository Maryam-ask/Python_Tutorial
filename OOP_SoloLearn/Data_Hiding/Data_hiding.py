class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):     # The __repr__ magic method is used for string representation of the instance.
        return "Queue({})".format(self._hiddenlist)
# In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
