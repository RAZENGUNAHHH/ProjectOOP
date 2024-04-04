import random

# Encapsulation (Encap)
class Player:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class HumanPlayer(Player):
    def choose_action(self):
        action = input("Choose your action (rock, paper, or scissors): ").lower()
        while action not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Please choose again.")
            action = input("Choose your action (rock, paper, or scissors): ").lower()
        return action

class ComputerPlayer(Player):
    def choose_action(self):
        return random.choice(['rock', 'paper', 'scissors'])

# Inheritance (Inherite)
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self, action1, action2):
        if action1 == action2:
            return "It's a tie!"
        elif (action1 == 'rock' and action2 == 'scissors') or \
             (action1 == 'paper' and action2 == 'rock') or \
             (action1 == 'scissors' and action2 == 'paper'):
            return f"{self.player1.get_name()} wins!"
        else:
            return f"{self.player2.get_name()} wins!"

# Polymorphism (Poly)
def play_game(player1, player2):
    game = Game(player1, player2)
    action1 = player1.choose_action()
    action2 = player2.choose_action()
    print(f"{player1.get_name()} chose {action1}.")
    print(f"{player2.get_name()} chose {action2}.")
    print(game.determine_winner(action1, action2))

# การใช้งาน
human_player = HumanPlayer("Player 1")
computer_player = ComputerPlayer("Computer")

play_game(human_player, computer_player)