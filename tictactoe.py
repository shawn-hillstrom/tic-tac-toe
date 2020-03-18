"""TicTacToe. A module for playing a simple game. """

import sys

def int_input(state, mover):
    print("%s's turn...(0..%i)" % (TicTacToe.Chrs[mover], len(state) - 1))
    return int(input())

class TicTacToe():
    """A Class representing the game of TicTacToe."""
    Column = 0
    Row = 1
    Diagonal = 2
    StaleMate = 3
    Chrs = {0: ' ', 1: 'X', -1: 'O'}

    def __init__(self, n=3):
        """Create a n-by-n tic-tac-toe game. n=3 by default"""

        self.n = n
        self.n2 = n**2
        self.reset()

    def reset(self, state=None):
        """Reset the game to the specified state, or to an empty board.
        A state is encoded as a list (or tuple) of elements in {-1, 0, 1}.
        -1 represents an 'O' (player 2), 0 represents an empty space and
        1 represents an 'X' (player 1).  The state is assumed to have an
        appropriate number of 'X's relative to the number of 'O's."""

        if state:
            ones = sum([i for i in state if i == 1])
            negs = sum([1 for i in state if i == -1])
            # ones (x's) go first

            assert ones == negs or ones == negs+1, "X's (1's) go first."

            # The game state is kept here as a list of values.
            # 0  indicates the space is unoccupied;
            # 1  indicates the space is occupied by Player 1 (X)
            # -1 indicates the space is occupied by Player 2 (O)
            self.board = list(state)
            s = sum(state)
            if s == 0:
                self.turn = 1
            else:
                self.turn = -1

        else:
            self.board = [0]*(self.n2)
            self.turn = 1

    def move(self, where):
        """Make the current player's move at the specified location/index and
        change turns to the next player; where is an index into the board in
        the range 0..(n**2-1)

        If the specified index is a valid move, modify the board,
        change turns and return True.

        Return False if the specified index is unopen, or does not exist"""
        if 0 <= where < self.n2 and self.board[where] == 0:
        	self.board[where] = self.turn
        	self.turn = -self.turn
        	return True
        else:
        	return False

    def show(self, stream=sys.stdout):
        """Displays the board on the specified stream."""
        for i in range(self.n):
        	for j in range(self.n):
        		print(' ' + TicTacToe.Chrs[self.board[j + (self.n * i)]] + ' ', end='', file=stream)
        		if j < (self.n - 1):
        			print('|', end='', file=stream)
        		else:
        			print('', file=stream)
        	if i < (self.n - 1):
        	    print('-' * (4 * self.n - 1), file=stream)

    def is_win(self):
        """Determines if the current board configuration is an end game.
        For a board of size n, a win requires one player to have n tokens
        in a line (vertical, horizontal or diagonal).

        Returns:
         (TicTacToe.Column, c, player): if player wins in column c
         (TicTacToe.Row, r, player): if player wins in row r
         (TicTacToe.Diagonal, 0, player): if player wins via
           a diagonal in the upper-left corner
         (TicTacToe.Diagonal, 1, player): if player wins via a
           diagonal in the upper-right corner
         (TicTacToe.StaleMate, 0, 0): if the game is a stalemate
         False: if the end state is not yet determined
        """
        column = [0]*self.n # Container for current column being checked.
        row = [0]*self.n # Container for current row being checked.
        diag = [0]*self.n # Container for current diagonal being checked.
        stalematePossible = True # Determines if a stalemate is possible.

        for i in range(self.n):
        	for j in range(self.n):
        		column[j] = self.board[i + (self.n * j)]
        		row[j] = self.board[j + (self.n * i)]
        		if i == 0 or i == (self.n - 1):
        			diag[j] = self.board[i + ((self.n + 1 - (2 * int(i != 0))) * j)]
        	if column[1:] == column[:-1] and column[0] != 0:
        	    return (TicTacToe.Column, i, column[0])
        	if row[1:] == row[:-1] and row[0] != 0:
        	    return (TicTacToe.Row, i, row[0])
        	if diag[1:] == diag[:-1] and diag[0] != 0:
        	    return (TicTacToe.Diagonal, i // (self.n - 1), diag[0])
        	if 0 in column or 0 in row or 0 in diag:
        		stalematePossible = False

        if stalematePossible:
        	return (TicTacToe.StaleMate, 0, 0)
       	else:
       		return False
    
    def describe_win(self, win):
        """Provides a text representation of an end-game state."""
        reason = {TicTacToe.Row: "Row", TicTacToe.Column: "Column",
                  TicTacToe.Diagonal: "Diagonal"}

        if win[0] == TicTacToe.StaleMate:
            return "StaleMate!"
        if win[0] == TicTacToe.Diagonal:
            if win[1] == 0:
                where = "Upper Left"
            else:
                where = "Upper Right"
        else:
            where = "%d" % win[1]
        return "%s (%d) wins @ %s %s" % (TicTacToe.Chrs[win[2]], win[2],
                                         reason[win[0]], where)

    def play(self, movefn=int_input, outstream=None, showwin=True):
        """Play the game of tictactoe!

        Arguments:
        movefn - a function that will provide possibly valid moves.
        outstream - a stream on which to show the game (if provided)
        showwin - if True, explicitly indicate the game is over
                  and describe the win

        Play should work (roughly) as follows:
         - verify the game is not in an end state
         - if outstream is provided, display the game state (using show())
         - acquire the next move from the movefn (see note below).
         - repeat steps above

         when an end state is reached:
         - print the state (if outstream is defined) and
         - print 'Game Over!' along with a description of the win
           if showwin is True.

        the movefn should take two arguments:
          (1) the game state; and (2) the current player
        """
        result = self.is_win()

        while (not result):
        	if outstream is not None:
        		self.show(stream=outstream)
        	self.move(movefn(self.get_state(), self.turn))
        	result = self.is_win()
        
        if outstream is not None:
        	self.show(stream=outstream)
        	if showwin:
        		print('Game Over!', self.describe_win(result), file=outstream)

        return result # For the purposes of Monte-Carlo.
    
    def get_state(self):
        """Get the state of the board as an immutable tuple"""
        return tuple(self.board)


def mc(state, n, debug=False):
    """Run a monte-carlo experiment in which we play the game using random
    moves.  Start each game at the specified state and run n
    simulations. Record the distribution of outcomes. Monte-carlo
    experiments such as this are used to evaluate states in complex
    games such as chess and go.

    Return a 4-tuple of:
    (games played, % won by player-1, % won by player-2, % stalemates)
    """
    def ran_input(state, mover):
        return random.randint(0, 8)

    gamesPlayed = 0
    winDist = {0: 0, 1: 0, -1: 0}

    for m in range(n):
    	t = TicTacToe()
    	t.reset(state)
    	result = t.play(movefn=ran_input, outstream=None, showwin=False)
    	winDist[result[2]] += 1
    	gamesPlayed += 1

    return (gamesPlayed, winDist[1] / gamesPlayed, winDist[-1] / gamesPlayed, winDist[0] / gamesPlayed)

if __name__ == "__main__":
    import argparse
    import random
    parser = argparse.ArgumentParser()
    parser.add_argument("--play", action='store_true')
    parser.add_argument("--state",
                        help="initial state comprised of values in {0,1,2}")
    parser.add_argument("--mc", type=int, default=1000,
                        help="monte carlo trials; default=%{default}")
    parser.add_argument("-n", type=int, default=3,
                        help="board length,width; default=%{default}")
    args = parser.parse_args()

    if args.state:
        # At the command line state will come in as a string drawn
        # from {0,1,2}.  -1 is not used here since it's awkwardly
        # two characters.
        assert len(args.state) == args.n**2, \
            "Expected string with %d elements" % (args.n**2)

        # state is input from set {0,1,2} but needs to be translated into
        # {0,1,-1} by changing '2' entries to -1.
        state = [int(z) for z in args.state]
        stateset = set(state)
        assert stateset.issubset(set([0, 1, 2])), \
            "Expected string with elements 0,1,2"
        state = [-1 if s == 2 else s for s in state]
        state = tuple(state)
        print("State is:", state)
    else:
        state = tuple([0]*(args.n**2))

    t = TicTacToe(args.n)
    if args.play:
        t.reset(state)
        t.play(outstream=sys.stdout)

    elif args.mc:
        (games, one, two, stale) = mc(state, args.mc)
        print("%d trials: 1 wins %.2f, "
              "-1 wins %.2f, stalemates %.2f" % (games, one, two, stale))
