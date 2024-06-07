import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game ;)')
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


point = turtle.Turtle()
states = pandas.read_csv('./50_states.csv')


correct_answers = []

while True:

    try:
        answer_state = screen.textinput(
                title=f'Correct: {len(correct_answers)}/50', 
                prompt="'Guess the State:\n What's another state name? "
            ).title()
    except ValueError as e:
        print(f'{e}: Incorrect input!')


    # get correct state data
    state_data = states.loc[states['state'] == answer_state]


    try:
        # unpacking data from data list
        state_name, x, y = state_data.values[0]
        correct_answers.append(state_name)
    except IndexError as e:
        print(f'{e}: There no item with that index!')


    # text point
    point.penup()
    point.goto((x, y))
    point.write(state_name, align="center", font=("Arial", 16, "normal"))
    point.hideturtle()
 

    continue





