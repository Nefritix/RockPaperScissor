import random


game_over = False


class Computer:

    def __init__(self, rock, paper, scissor):
        self.rock = rock
        self.paper = paper
        self.scissor = scissor

    def ai_choice1(self):
        return '{}'.format(self.rock)

    def ai_choice2(self):
        return '{}'.format(self.paper)

    def ai_choice3(self):
        return '{}'.format(self.scissor)


def win_condition(player_input, ai_input):
    # you win
    if player_input == "rock" and ai_input == "scissor":
        print("Ai chose " + ai_input)
        print("YOu win!")
    elif player_input == "paper" and ai_input == "rock":
        print("Ai chose " + ai_input)
        print("you win!")
    elif player_input == "scissor" and ai_input == "paper":
        print("Ai chose " + ai_input)
        print("you win!")
    # draw
    elif player_input == "rock" and ai_input == "rock":
        print("Ai chose " + ai_input)
        print("its a draw!")
    elif player_input == "paper" and ai_input == "paper":
        print("Ai chose " + ai_input)
        print("its a draw!")
    elif player_input == "scissor" and ai_input == "scissor":
        print("Ai chose " + ai_input)
        print("its a draw!")
    #ai wind
    elif ai_input == "rock" and player_input == "scissor":
        print("Ai chose " + ai_input)
        print("Ai wins!")
    elif ai_input == "paper" and player_input == "rock":
        print("Ai chose " + ai_input)
        print("Ai wins!")
    elif ai_input == "scissor" and player_input == "paper":
        print("Ai chose " + ai_input)
        print("AI wins!")

while not game_over:

    random_number = random.randint(1,3)
    ai_choices = Computer("rock", "paper", "scissor")
    if random_number == 1:
        player_input = input("Write rock, paper or scissor: ").lower()
        if player_input == "quit":
            game_over = True
        else:
            ai_input = (Computer.ai_choice1(ai_choices))
            win_condition(player_input, ai_input)
    elif random_number == 2:
        player_input = input("Write rock, paper or scissor: ").lower()
        if player_input == "quit":
            game_over = True
        else:
            ai_input = (Computer.ai_choice2(ai_choices))
            win_condition(player_input, ai_input)
    elif random_number == 3:
        player_input = input("Write rock, paper or scissor: ").lower()
        if player_input == "quit":
            game_over = True
        else:
            ai_input = (Computer.ai_choice3(ai_choices))
            win_condition(player_input, ai_input)







