from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
total_turtles = []


def create_turtles(colour_list):
    """
    This function will create as many independent instances for Turtle() as colours are in the list
    and each instance will be assigned with a particular colour from the colour list.
    :param colour_list: It will bring a particular colour for each Turtle object.
    :return: It will return the final list with all the instances with a colour assigned.
    """
    count = 0
    while count < len(colour_list):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colour_list[count])
        total_turtles.append(new_turtle)
        count += 1
    return total_turtles


def initial_position(create_turtle):
    """
    This function will set an initial position for each instance created previously.
    :param create_turtle: This parameter will allow to loop through the list and assign the initial
    position.
    """
    count = 0
    y_cor = -130
    while count < len(create_turtle):
        turtle = create_turtle[count]
        y_cor += 30
        turtle.penup()
        turtle.setpos(x=-230, y=y_cor)
        count += 1


if __name__ == '__main__':
    print(user_bet)
    initial_position(create_turtles(colours))

    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in total_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    print(f"You've won! The {winning_turtle} is the winner!")
                else:
                    print(f"You've lost! The {winning_turtle} is the winner!")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()
