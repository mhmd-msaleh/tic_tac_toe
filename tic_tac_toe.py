import random

def display_board(board): 
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    pass
    

def player_input():
    """
    This function will take in a player input and assign their marker as 'X' or 'O'. 

    Args: 
        None
    
    Returns: 
        (Player x marker, Player y marker) => X: first player to choose
    """
    marker = ''
    while not (marker == 'X' or marker == 'O'): 
        marker = input("Player: 1 Do you want to be X or O?").upper()
        if marker == 'X': 
            return ('X', 'O')
        else: 
            return ('O', 'X') 
    pass

def place_marker(board, marker, position):
    """
    This function takes in the board list object, a marker ('X' or 'O'), 
    and a desired position (number 1-9) and assigns it to the board.

    Args: 
        board: List representing tic tac toe board
        marker: Player's marker (X/O)
        position: Player's chosen position to place the marker
    
    Returns: 
        None
    """
    board[position] = marker
    pass

def win_check(board, mark):
    """
    This function takes in a board and a mark (X or O) and then checks to see if that mark has won

    Args: 
        board: List representing tic tac toe board
        marker: Player's marker (X/O)

    Returns: 
        True if there is a win, false otherwise
    """
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    
    for combination in winning_combinations: 
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == mark: 
            return True
    return False

def choose_first():
    """
    randomly decide which player goes first.

    Returns: 
     string of which player plays first
    """

    if random.randint(0, 1) == 0: 
        return 'Player 1'
    else: 
        return 'Player 2'
    pass

def flip_turn(turn):
    """flip players turn
    
    Args: 
        turn: current player (Player 1 / Player 2)
        
    Returns: 
        The next player
    """
    return 'Player 2' if turn == 'Player 1' else 'Player 1' 


def space_check(board, position):
    """checks whether a position on the board is freely available.
    
    Args: 
        board: List representing the Tic Tac Toe board.
        position: Position in the board getting checked
    
    Returns: 
        True if position is free, False otherwise
    """
    
    return board[position] == ' '
    pass

def full_board_check(board):
    """check whether all positions in board are filled
    
    Args: 
        board: List representing the Tic Tac Toe board
        
    Returns: 
        True if board is full, False otherwise
    """
    
    for i in range(9): 
        if space_check(board, i): 
            return False
    return True
    pass

def player_choice(board):
    """asks for a player's next position (1-9)
    then gives the associated list position (0-8)
    
    Args: 
        board: List representing the Tic tac toe board
        
    Returns: 
        position indicating player's choice
    """
    
    while(True): 
        position = int(input("Please Select next position (1-9)\n")) - 1
        if space_check(board, position): 
            return position
        else: 
            print('This position is already filled\n')
    pass

def replay():
    """Asks the player if they want to play again
    
    Args: 
        None

    Returns: 
        True if the player input is 'Yes', False if 'No' 
    """

    replay_answer = input("Do you want to play agian ?\n Type (Yes/No)\n").lower()
    if replay_answer == 'yes':
        return True 
    elif replay_answer == 'no': 
        return False
    pass

def play_round(board, turn, marker, game_on): 
    """ Single round play: 
            - starting from showing the board
            - choosing position
            - placing marker
            - checking if there is a Win or a Tie
            - Flipping Player's turn
    
    Args: 
        board: List representing tic tac toe board
        turn: Currnt player
        marker: current player's marker
        game_on: boolean variable indicating the current state of the game

    Returns: 
        turn: Next player 
        game_on: True if there is no Win or Tie, False otherwise
    """
    # show the board
    print('\n Now' + turn + ' turn')
    display_board(board)

    # choose position
    position = player_choice(board)

    # place marker
    place_marker(board, marker, position)

    # check win
    if win_check(board, marker): 
        display_board(board)
        print(turn + ' Has WON !!')
        game_on = False

    # There is no win
    else: 
        # check tie
        if full_board_check(board): 
            display_board(board)
            print('Tie Game')
            game_on = False
        
        # no tie ? Then Let the next player play
        else: 
            turn=flip_turn(turn)
    return (turn, game_on)
    pass

def main(): 
    print('Welcome to Tic Tac Toe!')
    display_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    while True:
        """ Setting up the game """
        # Reset board
        board = [' '] * 9
        # Let palyer 1 choose marker 
        player1_marker, player2_marker = player_input()
        
        # Set who will play first
        turn = choose_first()
        print(turn + ' will go first') 

        play_game = input('Ready to play? (yes/no)')
        game_on = True if play_game == 'yes' else False

        ## Game Play 
        while game_on:
            # Player 1 Turn
            if turn == 'Player 1': 
                turn, game_on = play_round(board, turn, player1_marker, game_on)
            # Player2's turn.
            else: 
                turn, game_on = play_round(board, turn, player2_marker, game_on)
        if not replay():
            break
    pass

if __name__ == '__main__': 
    main()

