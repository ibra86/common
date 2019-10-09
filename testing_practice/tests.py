import unittest

from testing_practice.code import coded_task_01, coded_task_02, coded_task_03, coded_task_04, coded_task_05, \
    coded_task_06, coded_task_07, coded_task_08, coded_task_09, coded_task_10, coded_task_11, coded_task_12, \
    coded_task_13, coded_task_14, coded_task_15, coded_task_16, coded_task_17, coded_task_18, coded_task_19, \
    coded_task_20


class Testing(unittest.TestCase):

    def test_01(self):
        '''
        Task 1:
        Take two lists, say for example these two:
          a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
          b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        and write a program that returns a list that contains only the elements that are common between the lists
        (without duplicates).
        '''

        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 34, 55, 89]
        actual_result = coded_task_01(a, b)
        self.assertEqual(sorted(actual_result), sorted(expected_result))

    def test_02(self):
        '''
        Task 2:
        Return the number of times that the letter “a” appears anywhere in the given string
        Given string is “I am a good developer. I am also a writer” and output should be 5.
        '''
        s = "I am a good developer. I am also a writer"
        expected_result = 5
        actual_result = coded_task_02(s)
        self.assertEqual(expected_result, actual_result)

    def test_03(self):
        '''
        Task 3:
        Write a Python program to check if a given positive integer is a power of three

        Input : 9
        Output : True
        '''
        num = 9
        actual_result = coded_task_03(num)
        self.assertTrue(actual_result)

    def test_04(self):
        '''
        Task 4:
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

        self.assertEqual(expected_result, actual_result)

    def test_05(self):
        '''
        Task 5:
        Write a Python program to push all zeros to the end of a list.

        Input : [0,2,3,4,6,7,10]
        Output : [2, 3, 4, 6, 7, 10, 0]
        '''

        input_list = [0, 2, 3, 4, 6, 7, 10]
        expected_result = [2, 3, 4, 6, 7, 10, 0]
        actual_result = coded_task_05(input_list)

        self.assertEqual(expected_result, actual_result)

    def test_06(self):
        """
        Task 6:
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
        Task 7:
        Write a Python program to find the number in a list that doesn't occur twice.

        Input : [5, 3, 4, 3, 4]
        Output : 5
        '''
        input_list = [5, 3, 4, 3, 4]
        actual_result = coded_task_07(input_list)
        expected_result = 5
        self.assertEqual(expected_result, actual_result)

    def test_08(self):
        '''
        Task 8:
        Write a Python program to find a missing number from a list.

        Input : [1,2,3,4,6,7,8]
        Output : 5
        '''
        input_list = [1, 2, 3, 4, 6, 7, 8]
        actual_result = coded_task_08(input_list)
        expected_result = 5
        self.assertEqual(expected_result, actual_result)

    def test_09(self):
        '''
        Task 9:
        Write a Python program to count the elements in a list until an element is a tuple.

        Sample Test Cases:
        Input: [1,2,3,(1,2),3]
        Output: 3
        '''
        input_list = [1, 2, 3, (1, 2), 3]
        actual_result = coded_task_09(input_list)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)

    def test_10(self):
        '''
        Task 10:
        Write a program that will take the str parameter being passed and return the string in reversed order.
        For example: if the input string is "Hello World and Coders" then your program should return the string
        "sredoC dna dlroW olleH".
        '''
        input_string = "Hello World and Coders"
        actual_result = coded_task_10(input_string)
        expected_result = "sredoC dna dlroW olleH"
        self.assertEqual(expected_result, actual_result)

    def test_11(self):
        '''
        Task 11:
        Write a program that will take the num parameter being passed and return the number of hours and minutes
        the parameter converts to (ie. if num = 63 then the output should be 1:3).
        Separate the number of hours and minutes with a colon.
        '''
        num = 63
        actual_result = coded_task_11(num)
        expected_result = '1:3'
        self.assertEqual(expected_result, actual_result)

    def test_12(self):
        '''
        Task 12:
        Write a program that will take the parameter being passed and return the largest word in the string.
        If there are two or more words that are the same length, return the first word from the string with that length.
        Ignore punctuation.

        Sample Test Cases:
        Input:"fun&!! time"
        Output:time

        Input:"I love dogs"
        Output:love
        '''
        input_string = "fun&!! time"
        actual_result = coded_task_12(input_string)
        expected_result = "time"
        self.assertEqual(expected_result, actual_result)

    def test_13(self):
        '''
        Task 13:
        Write a program (using functions!) that asks the user for a long string containing multiple words.
        Print back to the user the same string, except with the words in backwards order.

        For example:
        Input: My name is Michele
        Outout: Michele is name My
        '''
        input_string = "My name is Michele"
        actual_result = coded_task_13(input_string)
        expected_result = "Michele is name My"
        self.assertEqual(expected_result, actual_result)

    def test_14(self):
        '''
        Task 14:
        Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
        Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number
        of numbers in the sequence to generate.
        (Hint: The Fibonnaci seqence is a sequence of numbers where the next
        number in the sequence is the sum of the previous two numbers in the sequence.
        The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
        '''
        num_fib = 7
        actual_result = coded_task_14(num_fib)
        expected_result = [1, 1, 2, 3, 5, 8, 13]
        self.assertEqual(expected_result, actual_result)

    def test_15(self):
        '''
        Task 15:
        Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
        Write one line of Python that takes this list a and makes a new list that has only the even elements of
        this list in it.
        '''
        input_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        actual_result = coded_task_15(input_list)
        expected_result = [1, 9, 25, 49, 81]
        self.assertEqual(expected_result, actual_result)

    def test_16(self):
        '''
        Task 16:
        Write a program that will add up all the numbers from 1 to input number.
        For example: if the input is 4 then
        your program should return 10 because 1 + 2 + 3 + 4 = 10.
        '''
        input_num = 4
        actual_result = coded_task_16(input_num)
        expected_result = 10
        self.assertEqual(expected_result, actual_result)

    def test_17(self):
        '''
        Task 17:
        Write a program that will take the parameter being passed and return the factorial of it.
        For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
        '''
        input_num = 4
        actual_result = coded_task_17(input_num)
        expected_result = 24
        self.assertEqual(expected_result, actual_result)

    def test_18(self):
        '''
        Task 18:
        Write a program that will take the str parameter being passed and modify it using the following algorithm.
        Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
        Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

        Input: abcd
        Output: bcdE
        '''
        input_str = 'abcdz'
        actual_result = coded_task_18(input_str)
        expected_result = 'bcdEA'
        self.assertEqual(expected_result, actual_result)

    def test_19(self):
        '''
        Task 19:
        Write a program that will take the str string parameter being passed and return the string with the letters in
        alphabetical order
        (ie. hello becomes ehllo).
        Assume numbers and punctuation symbols will not be included in the string.

        Input: edcba
        Output: abcde
        '''
        input_str = 'edcba'
        actual_result = coded_task_19(input_str)
        expected_result = 'abcde'
        self.assertEqual(expected_result, actual_result)

    def test_20(self):
        '''
        Task 20:
        Write a program that will take both parameters being passed and return the true if num2 is greater than num1,
        otherwise return the false. If the parameter values are equal to each other then return the string -1
        '''
        num1, num2 = 1, 2
        actual_result = coded_task_20(num1, num2)
        expected_result = True
        self.assertEqual(expected_result, actual_result)

        num1, num2 = 1, -2
        actual_result = coded_task_20(num1, num2)
        expected_result = False
        self.assertEqual(expected_result, actual_result)

        num1, num2 = 1, 1
        actual_result = coded_task_20(num1, num2)
        expected_result = '-1'
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
