import unittest
import group


class MyTestCase(unittest.TestCase):

    def test_groups_of_three_1(self):
        arr = [1,2,3,2,2,3,3,2,3,5,2]
        actual = group.groups_of_3(arr)
        expected = [[1,2,3],[2,2,3],[3,2,3],[5,2]]
        self.assertEqual(expected,actual)

    def test_groups_of_three_2(self):
        arr = [5,2,3,1,2,3,57,40,20]
        actual = group.groups_of_3(arr)
        expected = [[5,2,3],[1,2,3],[57,40,20]]
        self.assertEqual(expected,actual)

    def test_groups_of_three_2(self):
        arr = []
        actual = group.groups_of_3(arr)
        expected = [[]]
        self.assertEqual(expected,actual)


if __name__ == '__main__':
    unittest.main()
