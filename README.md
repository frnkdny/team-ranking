**Requirements**

Requires Python 3

Tested on:
```
$ python3 --version 
Python 3.7.4
```

**Usage**

soccer_ranking.py expects file.txt on the command line
```
$ python3 soccer_ranking.py
python3 soccer_ranking.py <sample-input.txt>
```

*Usage Examples*

Calculates the team ranking of sample-input.txt and prints expected-output to stdout. 
Rank goes from most to least points. If the total points are equal then the teams get the same rank.

```
$ python3 soccer_ranking.py sample-input.txt
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

**Testing**
 
Tests use [doctest](https://docs.python.org/3/library/doctest.html) and are defined in the docstring of a function. 
Tests for soccer_ranking.py are located inside the file. 
Some tests require the file test-input.txt which is located in the same directory as soccer_ranking.py

*Running tests*

soccer_ranking.py doctests can be run from the command line. 
Without the verbose flag, no output is listed unless a test fails. 

```
$ python3 -m doctest soccer_ranking.py
$ 
```

Add the -v flag to print verbose output for all tests.
 
 ```
$ python3 -m doctest -v soccer_ranking.py
Trying:
    test = calculate_team_standings([['L', 3, 'S', 3], ['S', 1, 'L', 0], ['S', 0, 'L', 0]], {'L': 0, 'S': 0})
Expecting nothing
ok
Trying:
    sorted(test.items())
Expecting:
    [('L', 2), ('S', 5)]
ok
Trying:
    test = check_tense(1)
Expecting nothing
ok
Trying:
    test
Expecting:
    'pt'
ok
Trying:
    test = check_tense(-1)
Expecting nothing
ok
Trying:
    test
Expecting:
    'pts'
ok
Trying:
    test = create_teams([['Lions', 3, 'Snakes', 3], ['Snakes', 1, 'Lions', 0]])
Expecting nothing
ok
Trying:
    len(test)
Expecting:
    2
ok
Trying:
    sorted(test.items())
Expecting:
    [('Lions', 0), ('Snakes', 0)]
ok
Trying:
    test = last(('Lions', 5))
Expecting nothing
ok
Trying:
    test
Expecting:
    5
ok
Trying:
    test = parse_file('test-input.txt')
Expecting nothing
ok
Trying:
    test[0]
Expecting:
    ['Tarantulas', 1, 'FC Awesome', 11]
ok
Trying:
    type(test[0][2])
Expecting:
    <class 'str'>
ok
Trying:
    type(test[0][3])
Expecting:
    <class 'int'>
ok
Trying:
    print_team_standings([[1, 'Tarantulas', 6], [2, 'Lions', 5], [3, 'FC Awesome', 1], [3, 'Snakes', 1], [5, 'Grouches', 0]])
Expecting:
    1. Tarantulas, 6 pts
    2. Lions, 5 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    5. Grouches, 0 pts
ok
Trying:
    print_team_standings([[1, 'Lions', 6], [1, 'Tarantulas', 6], [3, 'FC Awesome', 1], [3, 'Snakes', 1], [3, 'Zebras', 1], [6, 'Grouches', 0]])
Expecting:
    1. Lions, 6 pts
    1. Tarantulas, 6 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    3. Zebras, 1 pt
    6. Grouches, 0 pts
ok
Trying:
    rank_team_standings({'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0})
Expecting:
    [[1, 'Tarantulas', 6], [2, 'Lions', 5], [3, 'FC Awesome', 1], [3, 'Snakes', 1], [5, 'Grouches', 0]]
ok
Trying:
    rank_team_standings({'Lions': 6, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0, 'Zebras': 1})
Expecting:
    [[1, 'Lions', 6], [1, 'Tarantulas', 6], [3, 'FC Awesome', 1], [3, 'Snakes', 1], [3, 'Zebras', 1], [6, 'Grouches', 0]]
ok
Trying:
    rank_team_standings({'Lions': 6, 'Snakes': 6, 'Tarantulas': 6, 'FC Awesome': 6, 'Grouches': 6, 'Zebras': 1, 'Ants': 6, 'Bees': 6, 'Cats': 6, 'Dogs': 6, 'Birds': 1, 'Rats': 2})
Expecting:
    [[1, 'Ants', 6], [1, 'Bees', 6], [1, 'Cats', 6], [1, 'Dogs', 6], [1, 'FC Awesome', 6], [1, 'Grouches', 6], [1, 'Lions', 6], [1, 'Snakes', 6], [1, 'Tarantulas', 6], [10, 'Rats', 2], [11, 'Birds', 1], [11, 'Zebras', 1]]
ok
Trying:
    rank_team_standings({'Bees': 6, 'Ants': 6, 'FC Awesome': 6})
Expecting:
    [[1, 'Ants', 6], [1, 'Bees', 6], [1, 'FC Awesome', 6]]
ok
Trying:
    rank_team_standings({'Grouches': 0})
Expecting:
    [[1, 'Grouches', 0]]
ok
2 items had no tests:
    soccer_ranking
    soccer_ranking.main
7 items passed all tests:
   2 tests in soccer_ranking.calculate_team_standings
   4 tests in soccer_ranking.check_tense
   3 tests in soccer_ranking.create_teams
   2 tests in soccer_ranking.last
   4 tests in soccer_ranking.parse_file
   2 tests in soccer_ranking.print_team_standings
   5 tests in soccer_ranking.rank_team_standings
22 tests in 9 items.
22 passed and 0 failed.
Test passed.
```

