#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020

# This program finds the average of a list of marks

import random


def average_of_numbers(passed_in_list_of_marks):
    # this function finds the average of a list of marks

    total = 0
    length = len(passed_in_list_of_marks)

    for list_item in passed_in_list_of_marks:
        total += list_item

    average = round(total / length)

    return average


def main():
    # this function uses a list
    list_of_marks = []
    temp_mark = None

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")

    while True:
        try:
            mark_as_string = input("Enter a mark : ")
            temp_mark = int(mark_as_string)
            if temp_mark <= 100 and temp_mark >= 0:
                list_of_marks.append(temp_mark)
            elif temp_mark == -1:
                average = average_of_numbers(list_of_marks)
                print("\nThe average of the marks is : {0}%".format(average))
                break
            else:
                print("\nInvalid input entered, please try again.")
                break
        except Exception:
            print("\nInvalid input entered, please try again.")
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
