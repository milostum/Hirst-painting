# import colorgram
# colors_object = colorgram.extract("image.jpg", 30)
# def import_colors(object_with_colors):
#     colors_rgb = []
#     for color in object_with_colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         rgb = (r, g, b)
#         colors_rgb.append(rgb)
#     return colors_rgb
# colors = import_colors(colors_object)
from turtle import Turtle, Screen, colormode
from random import choice
# #     []
milos = Turtle()
colormode(255)
color_list = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18),
              (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
              (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25),
              (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244),
              (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]

milos.penup()
milos.hideturtle()
milos.setposition(-200, -200)
x = -150
milos.speed("fastest")

for j in range(10):
    for i in range(10):
        milos.dot(20, choice(color_list))
        milos.penup()
        milos.forward(50)
    milos.goto(-200, x)
    x += 50
screen = Screen()
screen.exitonclick()
