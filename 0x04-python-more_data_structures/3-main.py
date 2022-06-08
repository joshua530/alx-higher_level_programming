#!/usr/bin/python3
common_elements = __import__("3-common_elements").common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

set_1 = {}
set_2 = {}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {100, 2, 4, 9, 11}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
