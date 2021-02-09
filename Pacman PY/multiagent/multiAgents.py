# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class RandomAgent(Agent):

    def getAction(selfself, gameState):
        legalMoves = gameState.getLegalActions()

        chosenAction = random.choice(legalMoves)

        return chosenAction


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """newFood = successorGameState.getFood().asList()
        minFood = 999999
        for food in newFood:
            minFood = min(minFood, dist(newPos, food))"""

        """ghost_pos = currentGameState.getGhostPositions()
        distToGhosts = [manhattanDistance(newPos, ghost_position) for ghost_position in ghost_pos]

        print("---------------------------------")
        print(currentGameState.getPacmanPosition(), action, newPos)
        print(ghost_pos)
        print(distToGhosts)
        print("---------------------------------")"""

        ghost_pos = currentGameState.getGhostPositions()
        distToGhosts = [manhattanDistance(newPos, ghost_position) for ghost_position in ghost_pos]
        distToFood = [manhattanDistance(newPos, foodPos) for foodPos in newFood.asList()]

        d1 = min(distToGhosts)
        if distToFood:
            d2 = min(distToFood) + 1
        else:
            d2 = 999999
        if d1 < 2:
            d1 = 0.00001
            return successorGameState.getScore() + 1 / d2 - 1 / d1
        else:
            return successorGameState.getScore() + 1 / d2


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """
    pacman = 0

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        max_value = -99999
        max_action = None

        for action in gameState.getLegalActions(0):
            action_value = self.Min_Value(gameState.generateSuccessor(0, action), 1, 0)
            if action_value > max_value:
                max_value = action_value
                max_action = action

        return max_action

    def Max_Value(self, gameState, depth):

        if (depth == self.depth) or (len(gameState.getLegalActions(0)) == 0):
            return self.evaluationFunction(gameState)

        listOfMin = list(self.Min_Value(gameState.generateSuccessor(0, action), 1, depth) for action in
                         gameState.getLegalActions(0))  # calculam minimul pentru fiecare fantoma

        return max(listOfMin)

    def Min_Value(self, gameState, agentIndex, depth):

        if len(gameState.getLegalActions(
                agentIndex)) == 0:  # daca nu mai sunt actiuni posibile sa calculeze scorul penntru agent
            return self.evaluationFunction(gameState)

        if agentIndex < gameState.getNumAgents() - 1:
            listOfMin = list(self.Min_Value(gameState.generateSuccessor(agentIndex, action), agentIndex + 1, depth)
                             for action in gameState.getLegalActions(agentIndex))
            return min(listOfMin)

        else:  # decat ultima fantoma trimite "semnal" catre pacman sa calculeze maxim din minimele obtinute
            decisionList = list(self.Max_Value(gameState.generateSuccessor(agentIndex, action), depth + 1)
                                for action in gameState.getLegalActions(agentIndex))
            return min(decisionList)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

        alpha = -99999
        beta = 99999

        max_action = None
        for action in gameState.getLegalActions(0):
            action_value = self.Min_Value(gameState.generateSuccessor(0, action), 1, 0, alpha, beta)
            if alpha < action_value:
                alpha = action_value
                max_action = action

        return max_action

    def Min_Value(self, gameState, agentIndex, depth, alpha, beta):

        if len(gameState.getLegalActions(agentIndex)) == 0:
            return self.evaluationFunction(gameState)

        action_value = 99999
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex < gameState.getNumAgents() - 1:
                siblingValue = self.Min_Value(gameState.generateSuccessor(agentIndex, action),
                                              agentIndex + 1, depth, alpha, beta)  # minimul dintre frati
                action_value = min(action_value, siblingValue)
            else:
                fatherValue = self.Max_Value(gameState.generateSuccessor(agentIndex, action),
                                             depth + 1, alpha, beta)  # maximul dintre copii
                action_value = min(action_value, fatherValue)

            if action_value < alpha:
                return action_value
            beta = min(beta, action_value)

        return action_value

    def Max_Value(self, gameState, depth, alpha, beta):

        if depth == self.depth or len(gameState.getLegalActions(0)) == 0:
            return self.evaluationFunction(gameState)

        action_value = -99999
        for action in gameState.getLegalActions(0):
            fatherValue = self.Min_Value(gameState.generateSuccessor(0, action), 1, depth, alpha, beta)
            # minimul dintre copii
            action_value = max(action_value, fatherValue)

            if action_value > beta:
                return action_value
            alpha = max(alpha, action_value)

        return action_value


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
