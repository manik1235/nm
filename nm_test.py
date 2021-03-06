""" Tests for Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""

import unittest
import nm
from collections import namedtuple

class Test_nmpy_pension_est(unittest.TestCase):
    """ Tests for the pension estimator function
    """
    def test_known_answers(self):
        # Ballpark = Top Earnings Years * # of years of service * 0.011
        # creating some manually calculated results.
        # Probably need to watch for floating point issues.
        known_answers = {(35000, 10): 3850,
                         (100000, 35): 38500,
                         (63000, 9): 6237,
                         }
        for k in known_answers:
            self.assertEqual(nm.pension_est(*k), known_answers[k])

class Test_nm_objectives(unittest.TestCase):
    """ Collection of Tests for the objectives module
    """
    def test_known_answers(self):
        # Set up a dictionary of the keyword inputs, and what
        # the results should be, for various combinations of input
        # Structure:
        # List of tuples. [(input_dictionary{param_name: value},
        #                   output_list_of_tuples), ...]
        known_input_output = [({'input_str': '1 2 3 4 5 6 7'},
                               [(7, 'Evaluating your investment portfolio.'),
                                (6, 'Properly addressing your estate settlement needs.'),
                                (5, 'Providing for long-term care needs.'),
                                (4, 'Providing for you and your family in the event of a disability.'),
                                (3, 'Providing for your family in the event of death.'),
                                (2, 'Funding a comfortable retirement.'),
                                (1, "Funding your children's education.")]
                               ),
                              ({'input_str': '1 2 3 4 5 6 7', 'r': 65},
                               [(7, 'Evaluating your investment portfolio.'),
                                (6, 'Properly addressing your estate settlement needs.'),
                                (5, 'Providing for long-term care needs.'),
                                (4, 'Providing for you and your family in the event of a disability.'),
                                (3, 'Providing for your family in the event of death.'),
                                (2, 'Funding a comfortable retirement by age 65.'),
                                (1, "Funding your children's education.")]
                               ),
                              ({'input_str': '1 2 3 4 5 6 7', 'r': 52, 'b': 500},
                               [(7, 'Evaluating your investment portfolio.'),
                                (6, 'Properly addressing your estate settlement needs.'),
                                (5, 'Providing for long-term care needs.'),
                                (4, 'Providing for you and your family in the event of a disability.'),
                                (3, 'Providing for your family in the event of death.'),
                                (2, 'Funding a comfortable retirement by age 52.'),
                                (1, "Funding your children's education."),
                                (999, 'Allocate $500 per month toward attaining these objectives.')]
                               ),
                              ]

        for kwinput, output in known_input_output:
            self.assertListEqual(nm.objectives(**kwinput), output)
    

class Test_nmpy(unittest.TestCase):
    """ Collection of tests for the nm.py functions
    """
    def test_weeks_in_year(self):
        known_answers = {2018: 52,
                         2019: 52,
                         2020: 53,
                         }


if __name__ == '__main__':
    unittest.main()
