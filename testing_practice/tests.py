import unittest

from code import *

class Testing(unittest.TestCase):

	def test_common_elements_from_two_lists(self):
		
		a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

		expected_result = [1,2,3,4,5,6,7,8,9,10,11,12,13,21,34,55,89]

		actual_result = common_elements_from_two_lists(a, b)

		self.assertEqual(sorted(actual_result), sorted(expected_result))


	def test_02(self):
		'''
		Return the number of times that the letter “a” appears anywhere in the given string
		Given string is “I am a good developer. I am also a writer” and output should be 5.
		'''
		s = "I am a good developer. I am also a writer"
		expected_result = 5
		actual_result = coded_task_02(s)
		self.assertEqual(actual_result, expected_result)

	def test_03(self):
		'''
		Write a Python program to check if a given positive integer is a power of three

		Input : 9
		Output : True
		'''

		num = 9
		actual_result = coded_task_03(num)

		self.assertTrue(actual_result)


	def test_04(self):
		'''
		Write a Python program to add the digits of a positive integer repeatedly 
		until the result has a single digit.
 
		Input : 48
		Output : 3

		For example given number is 59, the result will be 5.
		Step 1: 5 + 9 = 14
		Step 1: 1 + 4 = 5
		'''

		num = 48
		expected_result = 3
		actual_result = coded_task_04(num)

		self.assertEqual(actual_result, expected_result)

	def test_05(self):
		'''
		Write a Python program to push all zeros to the end of a list.

		Input : [0,2,3,4,6,7,10]
		Output : [2, 3, 4, 6, 7, 10, 0]
		'''

		input_list = [0,2,3,4,6,7,10]
		expected_result = [2, 3, 4, 6, 7, 10, 0]
		actual_result = coded_task_05(input_list)

		self.assertEqual(actual_result, expected_result)


	def test_06(self):
		"""
		Write a Python program to check a sequence of numbers is an arithmetic progression or not.
		 
		Input : [5, 7, 9, 11]
		Output : True

		In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
		For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
		"""

		input_list = [5, 7, 9, 11]
		actual_result = coded_task_06(input_list)
		self.assertTrue(actual_result)


	def test_07(self):
		'''
		Write a Python program to find the number in a list that doesn't occur twice.

		Input : [5, 3, 4, 3, 4]
		Output : 5
		'''

		

if __name__ == '__main__':
	unittest.main()