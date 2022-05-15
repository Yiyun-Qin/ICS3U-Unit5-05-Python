#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, calculating the area of the triangle


def triangle(base, height):
    # This function calculates the area of the triangle
    area = 1 / 2 * base * height
    print("The area of the triangle is {} cm².".format(area))
    print("\nDone.")


def main():
    # This function does try and catch

    # input
    base_string = input("Enter the base length of the triangle (cm): ")
    height_string = input("Enter the height of the triangle (cm): ")

    # process & output
    print("")
    try:
        base_integer = int(base_string)
        height_integer = int(height_string)
        # call functions
        triangle(base_integer, height_integer)
    except Exception:
        print("Invalid number!")
        print("\nDone.")


if __name__ == "__main__":
    main()
