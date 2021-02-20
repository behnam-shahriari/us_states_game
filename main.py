import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game - Developed by Behnam Shahriari")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

total_states = 50
states = pandas.read_csv("50_states.csv")
guessed = []
all_states = states.state.to_list()
while len(guessed) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed)}/{total_states} Guess the State",
                                    prompt="What's another state's name?").lower()

    state = states["state"].str.lower()
    find = states[state == answer_state]
    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if len(find) > 0:
        guessed.append(answer_state.title())
        x = states.x[state == answer_state]
        y = states.y[state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(answer_state)
