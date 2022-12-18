'''https://exercism.org/tracks/python/exercises/difference-of-squares'''

def make_list(number):
    '''
    The task was for N natural numbers starts from 1. Default range generate from 0 to N-1:

    >>> list(range(7))
    [0, 1, 2, 3, 4, 5, 6]
    That's why limits or the range
    '''
    return list(range(1,number+1))

def square_of_sum(number):
    return sum(make_list(number)) ** 2


def sum_of_squares(number):
    # Create a new list with sqares o every element
    square_op = lambda a: a**2
    square_list = map(square_op, (make_list(number)))
    return (sum(square_list))

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
    pass

#Checks:
#print (square_of_sum(10))
#print (sum_of_squares(10))
#print (difference_of_squares(10))
