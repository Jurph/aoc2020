# Advent of Code 2020, Day 1

Problem statement [https://adventofcode.com/2020/day/1](here), if you want to follow along. 

**Part 1:** Given a list of numbers, find two numbers that sum to 2020. I created a `Problem` class for ingesting the input and giving me access to `p.integers` to play with. We just work through the whole list, comparing each number to each other number and seeing if they sum to the target.

**Part 2:** We could just add a third nested loop, the way we did last time, so why all of the `frontways` and `backways`? The numbers we've been given are *mostly* four-digit numbers that are close to 2,000 -- we know that we won't find three numbers greater than 700 that sum to 2020. The `while()` loop prunes entries in the list that are larger than (2020 - 2 * smallest number), since those won't be usable in a solution that sums to 2020. Then we go through the outer loops forward (looking for small numbers first) and the inner loop backward (looking for big numbers first). 

