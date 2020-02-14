"""
  Author : Alan Morris
  Date created : 2020-02-9
  Python-Version: 3.6
  About: unittests for Pluralsight interview project: Finding invalid fake ID numbers.
  Apologies for the camelCase
"""

import unittest
import solution

from io import StringIO
from contextlib import redirect_stdout


class TestIDValidationMethods(unittest.TestCase):
    valid_id_string = "63-688580-R63"
    valid_long_id_string = "63-9347183-P26"
    invalid_id_string = "63-688580-F63"
    valid_id_char = "R"
    invalid_id_char = "F"
    valid_id_int = 63688580

    # Execute the main function and retrieve stdout. We are going to run tests against this later to validate solution output.
    with redirect_stdout(StringIO()) as captured_stdout:
        solution.main()

    # Cast the string IO object to a string - stripping symbols.
    captured_text = captured_stdout.getvalue().strip()


    def test_task_1(self):
        self.assertNotRegex(self.captured_text,"Hello, world.", "\n\nDon't forget to delete the line: \nprint(\"Hello, world\")")
        self.assertNotEqual(self.captured_text,"", "\n\nOh no! nothing was printed. Check your syntax and indentations carefully!")
        self.assertRegex(self.captured_text,"59-772671-B59","\n\nBe sure that you're reading in the correct csv file: \ntruncated_mangled_voters_roll_hre.csv")

    def test_task_2(self):
        self.assertNotRegex(self.captured_text,"MUCHENGETE","\n\nRemember that you can select the n'th element of an array with: \narray[n]")

    def test_task_3(self):
        solution_result = solution.get_id_checkdigit(self.valid_id_string)
        self.assertEqual(len(solution_result),1,"\n\nEach ID has only one check digit. Be sure that you're only returning the third character from the end of the id_string")
        self.assertNotEqual(solution_result,"-","\n\nYou're off by one, be sure that you're selecting the third character from the end of the id_string")
        self.assertNotEqual(solution_result,"6","\n\nYou're off by one, be sure that you're selecting the third character from the end of the id_string")
        self.assertEqual(solution_result, self.valid_id_char, "\n\nBe sure that you're selecting the third character from the end of the ID: \nid_string[-3]")

    def test_task_4(self):
        solution_result = solution.get_id_digits(self.valid_id_string)
        self.assertIsInstance(solution_result, int, "\n\nRemember to cast your returned result into an integer")
        self.assertNotEqual(solution_result, 688643, "\n\nConcatenate your substrings before you cast to int")
        self.assertEqual(solution.get_id_digits(self.valid_long_id_string), 639347183, "\n\nAlthough it may be tempting to use string slicing here, some id_strings are 9 digits instead of 8. A better approach would be to split the string around the dashes with: \nid_string.split(\"-\") \nand then concatenate the first 2 items of the resulting array.")

        self.assertEqual(solution_result, self.valid_id_int, "")

    def test_task_5(self):
        solution_result = solution.calculate_id_checkdigit(self.valid_id_string)
        self.assertIsInstance(solution_result,str, "\n\nRemember the checkdigit is a character, not a number.")
        self.assertNotEqual(solution_result,"S","\n\nIt looks like you're off by 1, remember that python strings are indexed from 0 so subtract 1 from the result of your modulo 23 operation")
        self.assertEqual(solution_result, self.valid_id_char,"\n\nReread the instructions carefully.")

    def test_task_6(self):
        self.assertIsInstance(solution.check_id_valid(self.valid_id_string),bool,"\n\nThis function must return a boolean (True of False)")
        self.assertTrue(solution.check_id_valid(self.valid_id_string), "\n\nBe sure that your function returns True for valid id_string ")
        self.assertFalse(solution.check_id_valid(self.invalid_id_string), "\n\nBe sure that your function returns True for valid id_string ")

    def test_task_7(self):
        self.assertNotRegex(self.captured_text, "58-394313-D70", "\n\nBe sure that you are only printing invalid ID numbers.")

    def test_task_8(self):
        self.assertRegex(self.captured_text, "25-104900-T48", "\n\nRemember to change the input file from truncated_mangled_voters_roll_hre.csv to mangled_voters_roll_hre.csv")
   
if __name__ == '__main__':
    unittest.main()
