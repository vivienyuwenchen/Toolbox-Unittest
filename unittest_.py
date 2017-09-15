""" A program that uses unittest to test a function that sorts a list of numbers
and removes negative numbers"""

import unittest


def sort_(list_):
    """ Sorts a list of numbers
        returns: a sorted list of numbers
    """
    list_.sort()

    return list_


def remove_(list_):
    """ Removes negative numbers from a list
        returns: a list with negative numbers removed
    """
    for number in list_:
        if number < 0:
            list_.remove(number)

    return list_


def sort_and_remove(list_):
    """ Sorts a list of numbers and removes negative numbers
        returns: a sorted list with negative numbers removed
    """
    list_ = sort_(remove_(list_))

    return list_


class test_sort_and_remove(unittest.TestCase):
    """ Performs unit tests on sort_, remove_, and sort_and_remove
    """
    def test_sort_(self):
        input_ = [9, 4, -1, 429, -62, 3, 0, 9, -1000, 17]
        output_ = [-1000, -62, -1, 0, 3, 4, 9, 9, 17, 429]
        self.assertEqual(sort_(input_), output_)

    def test_remove_(self):
        input_ = [9, 4, -1, 429, -62, 3, 0, 9, -1000, 17]
        output_ = [9, 4, 429, 3, 0, 9, 17]
        self.assertEqual(remove_(input_), output_)

    def test_sort_and_remove(self):
        input_ = [9, 4, -1, 429, -62, 3, 0, 9, -1000, 17]
        output_ = [0, 3, 4, 9, 9, 17, 429]
        self.assertEqual(sort_and_remove(input_), output_)


if __name__ == '__main__':
    unittest.main()
