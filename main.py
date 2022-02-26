import pandas
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

df = pandas.read_csv("50_states.csv")
states_data = df.state.to_list()
guessed_states = []
missing_states = []


def get_missing_states():
    for state in states_data:
        if state not in guessed_states:
            missing_states.append(state)
    # print(missing_states)
    missing_states_data = pandas.DataFrame(missing_states)
    missing_states_data.to_csv("missed_states.csv")


while len(guessed_states) < 50:
    t = Turtle()
    t.hideturtle()
    player_answer = screen.textinput(title=f"You got {len(guessed_states)}/50 states",
                                     prompt="Name a U.S. state, type quit to exit").title()
    # print(player_answer)
    if player_answer == "Quit":
        screen.bye()
        break
    elif player_answer in states_data:
        missing_states = []
        if player_answer in guessed_states:
            pass
            # t.goto(-45, 0)
            # t.color("red")
            # t.write("You already got this one, name a different state", align=ALIGNMENT, font=FONT)
        else:
            guessed_states.append(player_answer)
            answered_state = df[df.state == player_answer]
            t.penup()
            t.goto(int(answered_state.x), int(answered_state.y))
            # we can also use this instead of player answer...series.item() returns the first item in data
            # t.write(guessed_state.state.item())
            t.write(player_answer)

    get_missing_states()
screen.exitonclick()


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()
