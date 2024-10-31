import data
import hw2
import unittest
from data import Point, Rectangle, Duration, Song
from hw2 import create_rectangle, shorter_duration_than, song_shorter_than, running_time, validate_route, \
    longest_repetition


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        result = create_rectangle(Point(2,2), Point(10,10))
        expected = Rectangle(Point(2,10), Point(10,2))
        self.assertEqual(expected, result)
    def test_create_rectangle2(self):
        result = create_rectangle(Point(-6,-5), Point(4,3))
        expected = Rectangle(Point(-6, 3), Point(4,-5))
        self.assertEqual(expected, result)
    # Part 2
    def test_shorter_duration_than(self):
        result = shorter_duration_than(Duration(45,30), Duration(44,58))
        expected = False
        self.assertEqual(expected, result)
    def test_shorter_duration_than2(self):
        result = shorter_duration_than(Duration(1,12), Duration(1,36))
        expected = True
        self.assertEqual(expected, result)

    # Part 3
    def test_song_shorter_than(self):
        result = song_shorter_than([Song("Happy", "Pharrel Williams", Duration(3, 53)),
                                    Song("Whenever, Wherever", "Shakira", Duration(3,17)),
                                    Song("Cruel Summer", "Taylor Swift", Duration(2, 59))],
                                   Duration(3,0))
        expected = [Song("Cruel Summer", "Taylor Swift", Duration(2, 59))]
        self.assertEqual(expected, result)
    def test_song_shorter_than2(self):
        result = song_shorter_than([Song("Apple", "Charlie xcx", Duration(2, 32)),
                                    Song("Why", "Sabrina Carpenter", Duration(2, 52)),
                                    Song("Wildest Dreams", "Taylor Swift", Duration(3, 41))],
                                   Duration(3, 0))
        expected = [Song("Apple", "Charlie xcx", Duration(2, 32)),
                    Song("Why", "Sabrina Carpenter", Duration(2, 52))]
        self.assertEqual(expected, result)
    # Part 4
    def test_running_time(self):
        result = running_time([Song("Happy", "Pharrel Williams", Duration(3, 53)),
                                    Song("Whenever, Wherever", "Shakira", Duration(3, 17)),
                                    Song("Cruel Summer", "Taylor Swift", Duration(2, 59))],
                                   [0,2,1])
        expected = Duration(10,9)
        self.assertEqual(expected, result)
    def test_running_time2(self):
        result = running_time([Song("Apple", "Charlie xcx", Duration(2, 32)),
                               Song("Why", "Sabrina Carpenter", Duration(2, 52)),
                               Song("Wildest Dreams", "Taylor Swift", Duration(3, 41))],
                              [1, 0, 2])
        expected = Duration(9, 5)
        self.assertEqual(expected, result)
    # Part 5
    def test_validate_route(self):
        result = validate_route([ ['san luis obispo', 'santa margarita'],
                                            ['san luis obispo', 'pismo beach'],
                                            ['atascadero', 'santa margarita'],
                                            ['atascadero', 'creston']],
                                ['san luis obispo', 'santa margarita', 'atascadero'])
        expected = True
        self.assertEqual(expected, result)
    def test_validate_route2(self):
        result = validate_route([ ['san luis obispo', 'santa margarita'],
                                            ['san luis obispo', 'pismo beach'],
                                            ['atascadero', 'santa margarita'],
                                            ['atascadero', 'creston']],
                                ['san luis obispo', 'atascadero'])
        expected = False
        self.assertEqual(expected, result)
    # Part 6
    def test_longest_repetition(self):
        result = longest_repetition([1,1,2,2,1,1,1,3])
        expected = 4
        self.assertEqual(expected, result)
    def test_longest_repetition2(self):
        result = longest_repetition([2,4,2,2,5,4,5,5,5,6,7])
        expected = 6
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
