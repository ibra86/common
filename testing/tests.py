import unittest

from homework import Rectangle


class RectangleTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Tests started')

    @classmethod
    def tearDownClass(cls):
        print('Tests completed')

    def test_rectangle_valid_values(self):
        a, b = 1, -1
        self.failUnlessRaises(ValueError, Rectangle, a, b)

    def test_get_rectangle_perimeter_valid_values(self):
        rect = Rectangle(10, 11)
        actual_result = rect.get_rectangle_perimeter()
        expected_result = 42
        self.assertEqual(actual_result, expected_result)

    def test_get_rectangle_square(self):
        rect = Rectangle(5, 6)
        actual_result = rect.get_rectangle_square()
        expected_result = 30
        self.assertEqual(actual_result, expected_result)

    def test_get_sum_of_corners(self):
        number_of_corners = 4
        rect = Rectangle(1, 1)
        actual_result = rect.get_sum_of_corners(number_of_corners)
        expected_result = 360
        self.assertEqual(actual_result, expected_result)

    def test_negative_get_sum_of_corners(self):
        rect = Rectangle(1, 1)
        number_of_corners_list = [-3, 0, 7, 'two']
        for n in number_of_corners_list:
            with self.subTest(n=n):
                if not isinstance(n, int):
                    self.failUnlessRaises(TypeError, rect.get_sum_of_corners, n)
                else:
                    self.failUnless((n <= 0) | (n > 4))

    def test_get_rectangle_diagonal(self):
        rect = Rectangle(3, 4)
        actual_result = rect.get_rectangle_diagonal()
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_circumscribed_circle(self):
        rect = Rectangle(6, 8)
        actual_result = rect.get_radius_of_circumscribed_circle()
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def test_get_radius_of_inscribed_circle(self):
        rect = Rectangle(2, 2)
        actual_result = rect.get_radius_of_inscribed_circle()
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test_negative_get_radius_of_inscribed_circle(self):
        rect = Rectangle(1, 2)
        self.failUnlessRaises(ValueError, rect.get_radius_of_inscribed_circle)


if __name__ == '__main__':
    unittest.main()
