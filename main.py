# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle.Turtle()
tim.speed('fastest')

color_list = [(218, 150, 96), (39, 105, 161), (119, 164, 208), (193, 69, 28), (152, 60, 85), (239, 77, 40), (237, 209, 89), (217, 126, 154), (28, 130, 61), (221, 69, 95), (117, 193, 155), (190, 160, 40), (43, 48, 127), (140, 30, 48), (152, 30, 18), (29, 32, 64), (68, 36, 29), (102, 113, 184), (245, 163, 151), (10, 105, 38), (149, 212, 196), (245, 205, 2), (53, 29, 38), (236, 167, 180), (49, 169, 138), (31, 50, 40)]

number_of_dots = 101

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()