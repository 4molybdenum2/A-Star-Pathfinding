# Program to demonstrate the A-Star Pathfinding algorithm
# Open list is the list of nodes to be evaluated whose f_cost is already evaluated
# Closed List is the list of node already evaluated

# g_cost is the cost of path from start to the current node
# h_cost is the cost of path from current node to the end node (heuristic cost, calculated by Pythagoras Theorem)
# Priority must be given to node with lowest h_cost if f_cost are equal
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
MAUVE = (224, 176, 255)
RED = (255,0,0)  # colour tuples to be used later in the program
clock = pygame.time.Clock()

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

dim = len(maze)
width = 32 * dim
display = pygame.display.set_mode((width, width+32))
display.fill(WHITE)  # fill the display with WHITE color


class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g_cost = start_node.h_cost = start_node.f_cost = 0
    end_node = Node(None, end)
    end_node.g_cost = end_node.h_cost = end_node.f_cost = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f_cost < current_node.f_cost:
                current_node = item
                current_index = index
                
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g_cost = current_node.g_cost + 1
            child.h_cost = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f_cost = child.g_cost + child.h_cost

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g_cost > open_node.g_cost:
                    continue

            # Add the child to the open list
            open_list.append(child)

def windowLoop(maze,start,end):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit(0)
            for i in range(0, width, 32):
                pygame.draw.line(display, BLACK, (i, 0), (i, width))  # drawing row lines 32px apart
            for j in range(0, width, 32):
                # drawing column lines 32px apart
                pygame.draw.line(display, BLACK, (0, j), (width, j))
            pygame.display.update()

            for i in range(0, width, 32):
                # to deal with internal PyGame events in the event queue which cause the
                # system to freeze
                pygame.event.pump()
                for j in range(0, width, 32):
                    if maze[int(i/32)][int(j/32)] == 1:
                        pygame.draw.rect(display, BLACK, (j, i, 32, 32))
            pygame.display.update()

            path = astar(start,end)

            for index, coordinates in enumerate(path):
                if index!=0 or index!=len(path)-1:
                    pygame.event.pump()
                    pygame.draw.rect(display , RED , (coordinates[1]*32, coordinates[0]*32 , 32 , 32))
                    pygame.display.update()
                else:
                    pygame.event.pump()
                    pygame.draw.rect(display , GREEN , (coordinates[1]*32, coordinates[0]*32 , 32 , 32))
                    pygame.display.update()


def main():

    start = (0, 0)
    end = (7, 6)

    windowLoop(maze,start,end)


if __name__ == '__main__':
    main()