import random


class RPSGame:
    def __init__(self):
        self.ai_points = 0
        self.p_points = 0
        self.ai_options = ["rock", "paper", "scissor"]
        self.max_points = 5
        self.ai_ch = None
        self.p_ch = None

    def start_game(self):
        while self.ai_points < self.max_points and self.p_points < self.max_points:
            print("1.rock 2.paper 3.scissor 4.check score 5.quit")
            self.p_ch = int(input("Please enter any one option number\n"))
            self.p_ch = self.player_section()
            if self.p_ch is not None:
                self.ai_ch = random.choice(self.ai_options)
                print(f"Player choose: {self.p_ch}")
                print(f"AI choose: {self.ai_ch}")

                self.round_winner()

        self.end_game()

    def player_section(self):
        ch = self.p_ch
        if ch == 1:
            return "rock"
        elif ch == 2:
            return "paper"
        elif ch == 3:
            return "scissor"
        elif ch == 4:
            self.check_points()
            return None
        elif ch == 5:
            self.end_game()
        else:
            print("Please enter a proper value")
            return None

    def round_winner(self):
        if self.ai_ch == self.p_ch:
            print("Its a tie")
        elif self.ai_ch == 'rock':
            if self.p_ch == 'paper':
                print("Player won 1 point")
                self.p_points += 1
            elif self.p_ch == 'scissor':
                print("AI won 1 point")
                self.ai_points += 1
        elif self.ai_ch == 'paper':
            if self.p_ch == 'rock':
                print("Ai won 1 point")
                self.ai_points += 1
            elif self.p_ch == 'scissor':
                print("Player won 1 point")
                self.p_points += 1
        elif self.ai_ch == 'scissor':
            if self.p_ch == 'rock':
                print("Player won 1 point")
                self.p_points += 1
            elif self.p_ch == 'paper':
                print("AI won 1 point")
                self.ai_points += 1

    def end_game(self):
        print("\nGame Results")
        self.check_points()

        if self.ai_points == self.p_points:
            print("It's a tie!")
        elif self.p_points > self.ai_points:
            print("Player won the match")
        else:
            print("AI won the match")
        quit(0)

    def check_points(self):
        print(f"Player points: {self.p_points}")
        print(f"AI points: {self.ai_points}")


game = RPSGame()
game.start_game()
