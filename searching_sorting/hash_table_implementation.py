#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HashTable():

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        position = startslot

        while self.slots[position] and not stop:
            if self.slots[position] == key:
                stop = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    h = HashTable(5)
    h[1] = 'One'
    h[2] = 'Two'
    h[3] = 'Three'
    h[6] = 'Six'
    h[11] = 'Eleven'
    print(h.slots)
    print(h[1])
    print(h[6])
    print(h[11])
