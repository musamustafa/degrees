import numpy as np
from util import Node, StackFrontier, QueueFrontier

class Node:

    def __init__(self, state=None, parent=None, movie=None):
        self.state = state
        self.parent = parent
        self.movie = movie

        self.g = 0 
        self.h = 0 
        self.f = 0 

    def __eq__(self, other):
        return self.state == other.state


    # This function return the path of the search
    def return_path(current_node):
        path = []

        current = current_node
        while current is not None:
            path.append(current.state)
            current = current.parent

        # Return reversed path as we need to show from start to end path
        path.reverse()
        # we update the path of start to end found by A-star search with every step incremeted by 1
        return path

    def astar(self, cost, start, end):

        # Create start and end node with initialized values for g, h, and f
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        frontier = QueueFrontier()
        frontier.add(start_node)
        max_iterations = 40 

        yet_to_visit_list = []
        visited_list = []
        yet_to_visit_list.append(start_node)

        while len(yet_to_visit_list) > 0:
            current_node = yet_to_visit_list[0]
            current_index = 0
            for index, item in enumerate(yet_to_visit_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            yet_to_visit_list.pop(current_index)
            visited_list.append(current_node)
            if current_node == end_node:
                return self.return_path(current_node)

            children = []

            for movie, new_neighbor in neighbors_for_person(current_node.state):
                if new_neighbor == end_node.state:
                    child = Node(state=new_neighbor, parent=current_node, movie=movie)
                    frontier.add(new_neighbor)



def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors
