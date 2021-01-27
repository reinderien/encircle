# encircle
<<<<<<< Updated upstream
 test
=======
# Nothing is yet used from re CLASS
import re

# importing a sys-class to operate with passed arguments in the command line
import sys

# a definition of an object of a CLASS "sys"
sys_argv = sys.argv

# To manipulate the arguments, converting arguments into a string and storing into a variable
sys_argv_str = '' #

for arguments in range(len(sys_argv) - 1):
    sys_argv_str = sys_argv_str + str(sys_argv[arguments + 1])
    sys_argv_str = sys_argv_str + " "

# list form of the string
sys_argv_str_list = list(sys_argv_str)

sys_argv_str_list.pop()  # To pop the last element of the list which is a space (a redundant element)

#  print(f" original parameter converted into list - sys_argv_str_list = {sys_argv_str_list}")

while len(sys_argv_str_list) > 1:

    open_braces_list = []  # Will record the index position of the open round brackets from sys_argv_str_list
    close_braces_list = []  # Will record the index position of the close round brackets from sys_argv_str_list

    for count, element in enumerate(sys_argv_str_list):
        if element == "(":
            open_braces_list.append(count)
        elif element == ")":
            close_braces_list.append(count)


    def measure(list1, list2):
        brackets = []

        for j in range(len(list1) - 1):

            distance = []

            for i in range(len(list2)):

                if list2[i] > list1[-1 - j]:
                    distance.append(list2[i] - list1[-1 - j])

            distance.sort()

            brackets.append(distance[0])
            list2.pop(0)

        return brackets


    inner_brackets = measure(open_braces_list, close_braces_list)
    inner_brackets.append(len(sys_argv_str_list) - 1)


    def bracket_solution(ori_list, list1, list2):

        bracket_str = ''

        #  print(f'{list1[-1] + 1} and {list1[-1] + list2[0]}')

        for i in range(list1[-1] + 1, list1[-1] + list2[0]):
            bracket_str = bracket_str + ori_list[i]

        #  print(bracket_str)

        #  print(list1[-1])
        #  print(list1[-1] + list2[0])

        # removing all the elements of the original list after bracket_str was created.
        for i in range(list1[-1], list1[-1] + list2[0]):
            ori_list.pop(list1[-1])

        bracket_str_split_list = bracket_str.split()

        value = 0

        if 'multiply' in bracket_str_split_list:

            def multiply(fun):
                return int(fun[1]) * int(fun[2])

            value = multiply(bracket_str_split_list)

        elif 'add' in bracket_str_split_list:

            def add(fun):
                return int(fun[1]) + int(fun[2])

            value = add(bracket_str_split_list)

        #  print(f'{ori_list} and everything')
        #  print(f'{ori_list[list1[-1]]} and_all')

        ori_list[list1[-1]] = str(value)

        #  print(f'{ori_list} and lastly')

        return ori_list


    #  for i in range(len(inner_brackets)):
    #  print(f'{open_braces_list} and {inner_brackets}')

    # for loop for a function to work
    new_list = bracket_solution(sys_argv_str_list, open_braces_list, inner_brackets)
    sys_argv_str_list = new_list

    # final output will only contain the resolution of the last bracket
    # print(sys_argv_str_list)

# Final Out-put
print(sys_argv_str_list[0])

