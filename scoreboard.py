from turtle import Turtle
AL = "center"
FONT = ("Courier", 20, "normal")

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")

    def draw_borders(self):
        self.goto(-280, -280)
        self.pendown()
        for _ in range(4):
            self.forward(555)
            self.left(90)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 272)
        self.score = 0

    def writesocre(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", False, align=AL, font=FONT)

    def increase_score(self):
        self.score += 1

    def reset1(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.writesocre()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align=AL, font=FONT)
