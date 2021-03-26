import pygame
import random
import os

# Images
rock = pygame.transform.scale(pygame.image.load(os.path.join("images", "rock.png")), (100, 100))
paper = pygame.transform.scale(pygame.image.load(os.path.join("images", "paper.png")), (100, 100))
scissor = pygame.transform.scale(pygame.image.load(os.path.join("images", "scissor.png")), (100, 100))

# Intializing pygame module
pygame.init()


class Game:

    def __init__(self):
        self.width = 400
        self.height = 500
        self.display_surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("RPS Game")
        self.running = True
        self.mouse = pygame.mouse.get_pos()

        self.small_font = pygame.font.SysFont("Consolas", 25)
        self.extra_small_font = pygame.font.SysFont("consolas", 20)

        self.quit_b = self.small_font.render("Quit", True, (255, 255, 255))
        self.rock_b = self.small_font.render("rock", True, (255, 255, 255))
        self.paper_b = self.small_font.render("paper", True, (255, 255, 255))
        self.scissor_b = self.small_font.render("scissor", True, (255, 255, 255))
        self.restart_b = self.small_font.render("Restart Game", True, (255, 255, 255))

        self.ai_points = 0
        self.p_points = 0
        self.ai_options = ["rock", "paper", "scissor"]
        self.max_points = 5
        self.ai_ch = None
        self.p_ch = None
        self.round_val = None

    #     Selected images
        self.ai_img = None
        self.p_img = None

    def start_game(self):
        while self.running :
            self.mouse = pygame.mouse.get_pos()
            self.display_surface.fill((255, 255, 255))

            # display the points
            p_score_board = self.small_font.render("Player: " + str(self.p_points), True, (0, 0, 0))
            ai_score_board = self.small_font.render("AI: " + str(self.ai_points), True, (0, 0, 0))

            # draw the score board on to the screen
            self.display_surface.blit(p_score_board, (self.width * 0.05, self.height * 0.05))
            self.display_surface.blit(ai_score_board, (self.width * 0.05, self.height * 0.1))

            # Drawing different buttons for the user
            # ROCK
            pygame.draw.rect(self.display_surface, (0, 0, 0), [self.width * 0.25 - 85, self.height * 0.20, 90, 30])
            self.display_surface.blit(self.rock_b, (self.width * 0.25 - 75, self.height * 0.20))

            # PAPER
            pygame.draw.rect(self.display_surface, (0, 0, 0), [self.width * 0.50 - 85, self.height * 0.20, 90, 30])
            self.display_surface.blit(self.paper_b, (self.width * 0.50 - 75, self.height * 0.20))

            # SCISSOR
            pygame.draw.rect(self.display_surface, (0, 0, 0), [self.width * 0.75 - 85, self.height * 0.20, 130, 30])
            self.display_surface.blit(self.scissor_b, (self.width * 0.75 - 75, self.height * 0.20))

            # Different pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #     Checking for the mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Mouse click for quit button
                    if 129 <= self.mouse[0] <= 203 and 447 <= self.mouse[1] <= 482:
                        self.running = False

                    # mouse click for rock button
                    if 18 <= self.mouse[0] <= 104 and 102 <= self.mouse[1] <= 129:
                        self.p_img = rock
                        self.p_ch = "rock"
                        self.ai_selection()

                    # mouse click for paper button
                    if 116 <= self.mouse[0] <= 206 and 102 <= self.mouse[1] <= 129:
                        self.p_img = paper
                        self.p_ch = "paper"
                        self.ai_selection()

                    # mouse click for scissor button
                    if 219 <= self.mouse[0] <= 344 and 102 <= self.mouse[1] <= 129:
                        self.p_img = scissor
                        self.p_ch = "scissor"
                        self.ai_selection()

                    # mouse click for the restart button
                    if 84 <= self.mouse[0] <= 270 and 380 <= self.mouse[1] <= 420:
                        self.restart_game()

            # Displaying the images to the player
            if self.p_img is not None and self.ai_img is not None:
                player_tag = self.extra_small_font.render("Player: ",True, (0, 0, 0))
                ai_tag = self.extra_small_font.render("AI: ", True, (0, 0, 0))
                self.display_surface.blit(player_tag, (self.width * 0.10, self.height * 0.30))
                self.display_surface.blit(self.p_img, (self.width * 0.10, self.height * 0.35))
                self.display_surface.blit(ai_tag, (self.width * 0.50, self.height * 0.30))
                self.display_surface.blit(self.ai_img, (self.width * 0.50, self.height * 0.35))

            # Print the round val
            if self.round_val is not None:
                val = self.extra_small_font.render(self.round_val, True, (0, 0, 0))
                self.display_surface.blit(val, (self.width * 0.20, self.height * 0.60))

            # creating quit button
            pygame.draw.rect(self.display_surface, (0, 0, 0), [self.width / 2 - 75, self.height - 55, 80, 40])
            self.display_surface.blit(self.quit_b, (self.width / 2 - 65, self.height - 50))

            # Create restart button
            pygame.draw.rect(self.display_surface, (0, 0, 0), [self.width / 2 - 120, self.height - 125, 190, 40])
            self.display_surface.blit(self.restart_b, (self.width / 2 - 115, self.height - 120))

            pygame.display.flip()

    def ai_selection(self):
        self.ai_ch = random.choice(self.ai_options)
        if self.ai_ch == "rock":
            self.ai_img = rock
        elif self.ai_ch == 'paper':
            self.ai_img = paper
        else:
            self.ai_img = scissor
        self.round_winner()

    def round_winner(self):
        if self.ai_points < 5 and self.p_points < 5:
            if self.ai_ch == self.p_ch:
                self.round_val = "Its a tie!"
            elif self.ai_ch == 'rock':
                if self.p_ch == 'paper':
                    self.round_val = "Player won 1 point"
                    self.p_points += 1
                elif self.p_ch == 'scissor':
                    self.round_val = "Ai won 1 point"
                    self.ai_points += 1
            elif self.ai_ch == 'paper':
                if self.p_ch == 'rock':
                    self.round_val = "Ai won 1 point"
                    self.ai_points += 1
                elif self.p_ch == 'scissor':
                    self.round_val = "Player won 1 point"
                    self.p_points += 1
            elif self.ai_ch == 'scissor':
                if self.p_ch == 'rock':
                    self.round_val = "Player won 1 point"
                    self.p_points += 1
                elif self.p_ch == 'paper':
                    self.round_val = "Ai won 1 point"
                    self.ai_points += 1
        if self.p_points == 5:
            self.round_val = "Player won the match"
        elif self.ai_points == 5:
            self.round_val = "AI won the match"

    def restart_game(self):
        self.ai_points = 0
        self.p_points = 0
        self.ai_ch = None
        self.p_ch = None
        self.p_img = None
        self.ai_img = None
        self.round_val = None

game = Game()
game.start_game()