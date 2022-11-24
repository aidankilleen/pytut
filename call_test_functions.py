# call_test_functions.py
# By: Aidan
# Date: 23/09/2022

# import a function from another file / module
from test_functions import greeting

# names = ["Alice", "Bob", "Carol", "Dan"]

# import a variable from another file / module
from test_functions import names

for name in names:
    greeting(name)

