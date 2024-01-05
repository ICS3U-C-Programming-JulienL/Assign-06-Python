#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: January 1, 2024
# This program either shows all the even numbers in a list or sorts two lists in numerical order


def sort_element_list(list_one, list_two):
    # combine list_one and list_two into sorted_list
    sorted_list = list_one + list_two

    # use a nested for loop to run through each combination of numbers in the list
    # source : https://www.geeksforgeeks.org/sort-a-list-in-python-without-sort-function/
    for counter_one in range(0, len(sorted_list)):
        for counter_two in range(counter_one + 1, len(sorted_list)):
            # if sorted_list[counter_one] >= sorted_list[counter_two] the make  sorted_list [counter_one] =  sorted_list [counter_two] and  sorted_list [counter_two] =  sorted_list [counter_one]
            if sorted_list[counter_one] >= sorted_list[counter_two]:
                sorted_list[counter_one], sorted_list[counter_two] = (
                    sorted_list[counter_two],
                    sorted_list[counter_one],
                )

    # return sorted_list
    return sorted_list


def sort_list_main():
    # declare the two int_lists
    int_list_one = []
    int_list_two = []

    # tell the user what the program does
    print(
        "This program displays the combined, sorted list of the user's two integer lists."
    )
    print("Make sure that both your lists are sorted in numerical order.")

    while True:
        # get user_int_str_one
        user_int_str_one = input(
            "First Int List : Enter your integer here (type stop to exit):"
        )
        try:
            # covert user_int_str_one to int
            user_int_one = int(user_int_str_one)

            # append user_int_one to the first int list
            int_list_one.append(user_int_one)
        except:
            # if user_int_str_one == "stop", then break out of the loop
            if user_int_str_one == "stop":
                break

            # if user_int_str_one cannot be converted, tell the user to enter a valid integer
            print(
                "{} is not valid, please enter a valid integer.".format(
                    user_int_str_one
                )
            )

    while True:
        # get user_int_str_two
        user_int_str_two = input(
            "Second Int List : Enter your integer here (type stop to exit):"
        )
        try:
            # covert user_int_str_two to int
            user_int_two = int(user_int_str_two)

            # append user_int_two to int to the second list of int
            int_list_two.append(user_int_two)
        except:
            # if user_int_str_two == "stop"
            if user_int_str_two == "stop":
                break

            # if user_int_str_two cannot be converted, tell the user to enter a valid integer
            print(
                "{} is not valid, please enter a valid integer.".format(
                    user_int_str_two
                )
            )

    # call the sort_element_list function
    sorted_list_main = sort_element_list(int_list_one, int_list_two)

    # display the sorted list
    print("Your combined, sorted list is {}".format(sorted_list_main))


def even_num_list(even_list_int):
    # use a for each loop when a_num is in even_list_int
    for a_num in even_list_int:
        # if a_num is not a multiple of 2, remove it from the list
        if a_num % 2 != 0:
            even_list_int.remove(a_num)

    # return even_list_int
    return even_list_int


def even_num_list_main():
    # declare int_list_even_num
    int_list_even_num = []

    # tell the user what the program does
    print("This program displays all the even numbers in a list of integers")

    while True:
        # get user_int_str
        user_int_str = input("Enter your integer here (type stop to exit):")
        try:
            # covert user_int_str to int
            user_int = int(user_int_str)

            # append user_int  to int_list_even_num
            int_list_even_num.append(user_int)
        except:
            # if user_int_str == "stop", then break
            if user_int_str == "stop":
                break

            # if user_int_str cannot be converted, tell the user to enter a valid integer
            print("{} is not valid, please enter a valid integer.".format(user_int_str))

    # call the even_num_list function
    even_list = even_num_list(int_list_even_num)

    # display the even list
    print("The even numbers in your list are {}".format(even_list))


def main():
    # get user_choice
    user_choice = input(
        "This program either shows all the even numbers in a list(Press 1 for this) or sorts two lists in numerical order(Press 2 for this)."
    )

    # if user_choice is 1, then call the even_num_list_main() function
    if user_choice == "1":
        even_num_list_main()
    elif user_choice == "2":
        # otherwise if user_choice is 2, then call the sort_list_main() function
        sort_list_main()
    else:
        # otherwise, tell the user to enter 1 or 2 as an option
        print("Please enter 1 or 2 as an option.")


if __name__ == "__main__":
    main()
