from turtle import Turtle


class ScoreBoard(Turtle):

    font = ("Arial", 15, "normal")
    align = "center"

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 280)
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.write_score()

    def save_high_score_to_file(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.score))

    def write_score(self):
        self.clear()
        self.write("Score: " + str(self.score) + ", High score: " + str(self.high_score), False, align=self.align, font=self.font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.save_high_score_to_file()
            self.high_score = self.score
        self.score = 0
        self.write_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, align=self.align, font=self.font)
