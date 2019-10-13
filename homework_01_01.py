# Unit 1 Lesson 1
# Author: Your name

# Each of these functions has a multi-line string (starts and ends with """) called a 
# docstring, which describes what it does and gives an example of how it should work.
# You should just leave the docstrings alone--your job is to replace the incorrect 
# return value with a correct return value

# Hints:
# - for `is_a_factor`, you are going to need moudlo, which we studied in Unit 0, Lesson 3.
# - for `is_prime`, you are going to need to use `is_a_factor`.  A number is prime if it has
#   no factors other than 1 and itself. 

def double(number):
    """
    Returns twice `number`

        >>> double(3)
        6
    """
    return 0

def triple(number):
    """
    Returns three times `number`

        >>> triple(123)
        369
    """
    return 0

def bigger(x, y):
    """
    Returns `x` or `y`, whichever is bigger.

        >>> bigger(100, 200)
        100
    """
    return 0

def has_an_eight(list_of_numbers):
    """
    Eight is lucky, so we often want to know whether a list contains at least one 8.
    Returns True or False, depending on whether `list_of_numbers` contains an 8.

        >>> has_an_eight([1,2,3,4])
        False
        >>> has_an_eight([9,8,7,6])
        True
    """
    return False

def is_a_factor(possible_factor, number):
    """
    Returns True or False, depending on whether `possible_factor` really is a 
    factor of `nuumber`.

        >>> is_a_factor(3, 9)
        True
        >>> is_a_factor(3, 7)
        False
        >>> is_a_factor(2, 2)
        True
    """
    return False

def is_prime(number):
    """
    Returns True or False, depending on whether `number` has any factors. 
    (Note: 1 and `number` don't count as factors.) This function should work
    for any integer bigger than 1. For now, let's assume the user 
    of this function is friendly and isn't going to try some nonsense like 
    is_prime(-2). 

        >>> for num in range(2, 7):
        ...     print(num, is_prime(num))

        2, True
        3, True
        4, False
        5, True
        6, False
    """
    return False


