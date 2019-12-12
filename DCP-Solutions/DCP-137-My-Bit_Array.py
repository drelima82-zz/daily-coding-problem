# This problem was asked by Amazon.
# Implement a bit array.
# A bit array is a space efficient array that holds a value of 1 or 0 at each index.
#     •	init(size): initialize the array with size
#     •	set(i, val): updates index at i with val where val is either 1 or 0.
#     •	get(i): gets the value at index i.


class Bit_Array:
    def __init__(self, size):
        self.indices = set()
        self.size = size

    #used to scan the indices on self.indices
    #if find the index on indices list, set this position to 1, otherwise 0 (so, if there is no indices, array will be entirelly 0)
    def toArray(self):
        arr = list()
        for index in range(self.size):
            if index in self.indices:
                arr.append(1)
            else:
                arr.append(0)
        return arr

    def getIndicesSet(self):
        print("Indices: ", self.indices)

    def get(self, i):
        if i >= self.size:
            raise Exception("Invalid Index for getting value")

        return int(i in self.indices)

    def set(self, i, val):
        if i >= self.size:
            raise Exception("Invalid Index for setting value")
        if val < 0 or val > 1:
            raise Exception("Invalid value for indice - Valid values are 0 and 1")
        
        #self.indices.add(i)
        if val and i not in self.indices:
            self.indices.add(i)
        elif not val and i in self.indices:
            self.indices.remove(i)

class BitArray_Andre:
    def __init__(self, size):
        self._size = size
        self._set = set()
 
    def toArray(self):
        return [self.get(i) for i in range(self._size)]
 
    def get(self, i):
        return 1 if i in self._set else 0
   
    def set(self, i, val):
        if val:
            self._set.add(i)
       
        else:
            self._set.remove(i)
 
 
class BitArray_Dorian:
    def __init__(self, size):
        self._size = size
        self.n = 0   # equal to SET  --> Set encoded in bits
   
    def toArray(self):
        return [self.get(i) for i in range(self._size)]
 
    def get(self, i):
        return (self.n >> i) & 1
 
    def set(self, i, val):
        if val:
            self.n |= 1 << i
       
        else:
            self.n &= ~(1 << i)
 
    def _set(self, i, val):
        bit = self.get(i)
        if bit == bool(val):
            return
       
        self.n ^= 1 << i
 


class BitArray_Dorian_V2:
    def __init__(self, size, int_size=8):
        self._int_size = int_size
        self._size = size
        size_factor = ((size + int_size - 1) // int_size)
        self.ns = [0] * size_factor

    def toArray(self):
        return [self.get(i) for i in range(self._size)]

    def get(self, i):
        box_position = i // self._int_size
        box_internal_pos = i % self._int_size
        n = self.ns[box_position]
        
        return (n >> box_internal_pos) & 1

    def set(self, i, val):
        box_position = i // self._int_size
        box_internal_pos = i % self._int_size
        n = self.ns[box_position]

        if val:
            n |= 1 << box_internal_pos
       
        else:
            n &= ~(1 << box_internal_pos)
        
        self.ns[box_position] = n

size = 10 
bArray = BitArray_Dorian_V2(size, int_size=3)
print(bArray.ns)
#bArray = BitArray_Andre(size)
#bArray = Bit_Array(size)

print("Array: ", [bArray.get(i) for i in range(size)])
bArray.set(3, 1)
print(bArray.toArray())
bArray.set(6, 1)
bArray.set(4, 1)
print(bArray.toArray())
bArray.set(3, 0)
bArray.set(6, 0)
bArray.set(8, 1)
print(bArray.toArray())

print("Array: ", [bArray.get(i) for i in range(size)])

print(bArray.ns)
