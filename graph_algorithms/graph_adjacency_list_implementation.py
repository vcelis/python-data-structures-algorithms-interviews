#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Vertex():

    def __init__(self, key):
        self.id = key
        self.connections = {}

    def add_neighbor(self, nbr, weight=0):
        self.connections[nbr] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connections[nbr]

    def __str__(self):
        connections = str([x.id for x in self.connections])
        return f'{str(self.id)} connected to: {connections}'


class Graph():

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.num_vertices += 1
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def add_edge(self, origin, dest, weight=0):
        if origin not in self.vertices:
            self.add_vertex(origin)
        if dest not in self.vertices:
            self.add_vertex(dest)

        self.vertices[origin].add_neighbor(self.vertices[dest], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, n):
        return n in self.vertices


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vertices)
    g.add_edge(0, 1, 2)
    for vertex in g:
        print(vertex)
        print(vertex.get_connections)
        print('---------------------')
