# Nothing is yet used from re CLASS
# import re

# importing a sys-class to operate with passed arguments in the command line
import sys

# a definition of an object of a CLASS "sys"
sys_argv = sys.argv

# To manipulate the arguments, converting arguments into a string and storing into a variable - sys_argv_str
sys_argv_str = ''

for arguments in range(len(sys_argv) - 1):
    sys_argv_str = sys_argv_str + str(sys_argv[arguments + 1])
    sys_argv_str = sys_argv_str + " "

# last character is removed from the string.
sys_argv_str = sys_argv_str[:-1]

# list form of the string- Each characters are separated into an individual list elements as a string
sys_argv_string_list = list(sys_argv_str)


# This function solves all the parenthesis that is expressed.
def parenthesis(sys_argv_str_list):
    # after each iteration in the while loop the list - sys_argv_str_list will diminish in its length.
    while len(sys_argv_str_list) > 1:

        open_braces_list = []  # Will record the index position of the open round brackets from sys_argv_str_list
        close_braces_list = []  # Will record the index position of the close round brackets from sys_argv_str_list

        # This loop actually generates both lists on the matching of the element in the condition follow:
        for count, element in enumerate(sys_argv_str_list):
            if element == "(":
                open_braces_list.append(count)
            elif element == ")":
                close_braces_list.append(count)

        # A new function will measure the length of the smallest possible bracket from the main list - sys_argv_str_list
        def measure(list1, list2):
            # list1 and list2 are the parameters passed in as open_braces_list and close_braces_list respectively

            # Empty list is created to find the length of the brackets lies inside the main list - sys_argv_str_list
            brackets = []

            # A nested loop will find all the bracket's length. - First, it will find the smallest bracket,
            for j in range(len(list1) - 1):

                # This empty list will yield the result of all the length of the brackets from last-open bracket to
                # all the closed brackets. Therefore, it will have the smallest bracket's length after sorting.
                distance = []

                # A loop to iterate for all the elements from last open bracket's index position to all the closed
                # bracket's position that occur after it. The condition inside loop constitutes only to find those
                # elements occur after the last open parenthesis to all the closed parenthesis
                for i in range(len(list2)):

                    if list2[i] > list1[-1 - j]:
                        distance.append(list2[i] - list1[-1 - j])

                distance.sort()

                # Only the zeroth element of the list - distance contains the smallest distance
                brackets.append(distance[0])

                # pop out that element which has already been counted so conflict does not arise in the next iteration.
                list2.pop(0)

            # After the end of the loop list - brackets will have all the complete length from their index positions
            return brackets

        # Calling of the function with lists of index positions of open and close parenthesis respectively
        inner_brackets = measure(open_braces_list, close_braces_list)

        # This is appending a distance of the final parenthesis. This was not generated in the function-measure. so
        # appended manually.
        inner_brackets.append(len(sys_argv_str_list) - 1)

        # Function will solve smallest parenthesis in the main  list. Arguments are original list and the brackets- list
        # that has all the distances of the parenthesis
        def bracket_solution(ori_list, list1, list2):

            bracket_str = ''

            #  print(f'{list1[-1] + 1} and {list1[-1] + list2[0]}')

            # To conjoin all the string elements and making a string that has an expression(
            # ADD or MULTIPLY and other integer expressions )
            for i in range(list1[-1] + 1, list1[-1] + list2[0]):
                bracket_str = bracket_str + ori_list[i]

            #  print(bracket_str)

            #  print(list1[-1])
            #  print(list1[-1] + list2[0])

            # removing all the elements of the original list after bracket_str was created. This will only remove the
            # elements of the smallest brackets. The start and stop values of the range function is chosen as such to
            # yield the desired output.
            for i in range(list1[-1], list1[-1] + list2[0]):
                ori_list.pop(list1[-1])

            # A split method to seperate out among the expressions
            bracket_str_split_list = bracket_str.split()

            value = 0
            # A condition will find out which expression the list element has and the rest will be their integers.
            if 'multiply' in bracket_str_split_list:

                # A function will convert the string elements into integer and do the operation.
                def multiply(fun):
                    # This to index position of the list will always have the final integers
                    return int(fun[1]) * int(fun[2])

                value = multiply(bracket_str_split_list)

            elif 'add' in bracket_str_split_list:

                # A function will convert the string elements into integer and do the operation.
                def add(fun):
                    # This to index position of the list will always have the final integers.
                    return int(fun[1]) + int(fun[2])

                value = add(bracket_str_split_list)

            #  print(f'{ori_list} and everything')
            #  print(f'{ori_list[list1[-1]]} and_all')

            # To append the output of the expression in the main list in the form of a string.
            ori_list[list1[-1]] = str(value)

            # This Print function will enable QA how the brackets are being striped down the line.
            # print(f'{ori_list} and lastly')

            return ori_list

        # A function is now called to solve the inner most and last bracket first.
        new_list = bracket_solution(sys_argv_str_list, open_braces_list, inner_brackets)

        # A new assignment is done because the list is modified with inner and last most parenthesis solved. This
        # will be again passed in the while -loop as a renewed list.
        sys_argv_str_list = new_list

        # final output will only contain the resolution of the last bracket
        # print(sys_argv_str_list)

    # Final Out-put after looping through all the parenthesis with solution and replacement of the elements happens
    # inside created functions.
    print(sys_argv_str_list[0])


try:
    # MAin program execution, If there is only an integer added in the program then it will take the argument
    # as the answer itself.
    if type(int(sys_argv_str)) == int:
        print(int(sys_argv_str))

except ValueError:
    parenthesis(sys_argv_string_list)
