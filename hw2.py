from audioop import reverse

import data
from data import Point, Rectangle, Duration, Song
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
# This function creates a rectangle based on two given points
# two point objects
# one rectangle object
def create_rectangle(point1: Point, point2: Point) -> Rectangle:
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_right_x = max(point1.x, point2.x)
    bottom_right_y = min(point1.y, point2.y)
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)
    return Rectangle(top_left, bottom_right)

# Part 2
# This function returns if the first duration is shorter than the second
# input: two time objects
# output: a boolean value
def shorter_duration_than(time1: Duration, time2: Duration) -> bool:
    total_time1 = time1.minutes * 60 + time1.seconds
    total_time2 = time2.minutes * 60 + time2.seconds
    return total_time1 < total_time2

# Part 3
# This function returns a list of all songs in a given list that are shorter than the given duration
def song_shorter_than(songs: list[Song], time1: Duration) -> list[Song]:
    short_songs = []
    for x in range(0, len(songs)):
        if (songs[x].duration.minutes*60 + songs[x].duration.seconds) < (time1.minutes*60 + time1.seconds):
            short_songs.append(songs[x])
    return short_songs

# Part 4
def running_time(songs: list[Song], numbers: list[int]) -> Duration:
    total_time = 0
    for i in numbers:
        total_time += songs[i].duration.minutes*60 + songs[i].duration.seconds
    return Duration(minutes = total_time // 60, seconds = total_time % 60)

# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(route) == 0:
        return True

    for i in range(len(route) - 1):
        pair = [route[i], route[i+1]]
        reversed_pair = [route[i+1], route[i]]

        if pair not in city_links and reversed_pair not in city_links:
            return False
    return True

# Part 6
def longest_repetition(numbers: list[int]) -> Optional[int]:
    if not numbers:
        return None

    longest_start_i = 0
    longest_length = 1
    current_start_i = 0
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                longest_start_i = current_start_i
            current_start_i = i
            current_length = 1
    if current_length > longest_length:
        longest_start_i = current_start_i
    return longest_start_i


