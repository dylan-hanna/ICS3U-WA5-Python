#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program reverses the order of numbers or integers


def main():
    try:
        print(int(input("Enter word or set of integers:  ")[::-1]))

    except ValueError:
        print()
        print("Invalid Input")
        print()


if __name__ == "__main__":
    main()
