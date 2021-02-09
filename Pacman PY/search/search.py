# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
"""
    """print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    x = problem.getSuccessors(problem.getStartState())

    for y in x:
        print("Possible position:" + str(y[0]) + "\nDirection:" + str(y[1]) + "\nCost:" + str(y[2]))
        print()"""

    "*** YOUR CODE HERE ***"
    start_node = problem.getStartState()
    if problem.isGoalState(start_node):
        return []
    visited = []
    processing = Stack()
    processing.push((start_node, []))
    while not processing.isEmpty():
        curr = processing.pop()

        if problem.isGoalState(curr[0]):
            return curr[1]
        if curr[0] not in visited:
            visited.append(curr[0])
            for n in problem.getSuccessors(curr[0]):
                if n[0] not in visited:
                    processing.push((n[0], curr[1] + [n[1]]))
    util.raiseNotDefined()
    "w = Directions.WEST"
    "return [w, w]"

    """intial_state = problem.getStartState()
    (next_state, action, _) = problem.getSuccessors(intial_state)[0]
    (next_next_state, next_action, _) = problem.getSuccessors(next_state)[0]
    print("A possible sequence of actions is: ", action, " followed by", next_action)
    return [action, next_action]"""

    """x = problem.getSuccessors(problem.getStartState())
    while x is not None:
        for y in x:
            return [y[1], y[1]]"""

    # node1 = CustomNode("first", 5)
    # node2 = CustomNode("second", 1)

    # my_stack = Stack()
    # my_stack.push(node1)
    # my_stack.push(node2)
    # popped_elem = my_stack.pop()
    # print("Popped elem is: ", popped_elem.getName(), " with cost ", popped_elem.getCost())


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    processing = util.Queue()
    processing.push((problem.getStartState(), [], []))
    visited = []
    while not processing.isEmpty():
        node, actions, cost = processing.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for child, direction, cost_child in problem.getSuccessors(node):
                processing.push((child, actions + [direction], cost + [cost_child]))
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    processing = util.PriorityQueue()
    processing.push((problem.getStartState(), [], 0), 0)
    visited = []
    while not processing.isEmpty():
        node, actions, cost = processing.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for child, direction, cost_child in problem.getSuccessors(node):
                processing.push((child, actions + [direction], cost_child + cost), cost + cost_child)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    processing = util.PriorityQueue()
    processing.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    visited = []
    while not processing.isEmpty():
        node, actions, cost = processing.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for child, direction, cost_child in problem.getSuccessors(node):
                g = cost + cost_child
                processing.push((child, actions + [direction], cost + cost_child), g + heuristic(child, problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
