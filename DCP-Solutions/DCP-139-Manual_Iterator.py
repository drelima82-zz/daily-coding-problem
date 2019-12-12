# Problem 139
# This problem was asked by Google.
# Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek().
# peek shows the next element that would be returned on next().
# Here is the interface:
# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass

#     def peek(self):
#         pass

#     def next(self):
#         pass

#     def hasNext(self):
#         pass


class Iterator:
    def __init__(self, list : list):
        self._list = list
        self._pos = 0

    def next(self):
        value = self._list[self._pos]
        self._pos += 1
        return value

    def hasNext(self):
        return self._pos < len(self._list)



class PeekableInterface(object):
    def __init__(self, iterator : Iterator):
        self.iterator = iterator

        self.has_next_val = iterator.hasNext()
        if self.has_next_val:
            self.next_val = iterator.next()
        
    def peek(self):
        return self.next_val

    def next(self):
        next_val = self.next_val
        iterator = self.iterator

        has_next_val = iterator.hasNext()
        self.next_val = iterator.next() if has_next_val else None

        self.has_next_val = has_next_val
        return next_val

    def hasNext(self):
        return self.has_next_val

list = [1, 2, 3, 4, 5]
iterator = Iterator(list)
iterator = PeekableInterface(iterator)
while iterator.hasNext():
    peek = iterator.peek()
    print(iterator.next())
    print(iterator.peek(), iterator.peek())
    print()

exit()

peekable = PeekableInterface(iterator)

assert peekable.peek() == 1
assert peekable.hasNext()

assert peekable.next() == 1
assert peekable.next() == 2
assert peekable.next() == 3

assert peekable.peek() == 4
assert peekable.hasNext()

assert peekable.next() == 4
assert peekable.hasNext()
assert peekable.peek() == 5

assert peekable.next() == 5
assert peekable.hasNext() == False
assert peekable.peek() == None
assert peekable.next() == None