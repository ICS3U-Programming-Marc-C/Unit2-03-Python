#!/usr/bin/env python3
# Created by Marc Coffi
# Created on February 2022
# This is a program that calculates the circumference of a circle using tau

import constants


def main():
    print("This program calculates the circumference of a circle using tau.")
    radius = float(input("Enter a radius in centimeters: "))
    circumference = (constants.TAU*radius)
    print("The Circumference is {}cm.".format(circumference))


if __name__ == "__main__":
    main()
