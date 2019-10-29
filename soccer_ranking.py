import sys


def parse_file(input_file):
    """Opens and parses a .txt file. Returns a list of lists representing the teams and final score a soccer match.
    e.g. [[home_team, home_score, away_team, away_score]]
    >>> test = parse_file('test-input.txt')
    >>> test[0]
    ['Tarantulas', 1, 'FC Awesome', 11]
    >>> type(test[0][2])
    <class 'str'>
    >>> type(test[0][3])
    <class 'int'>
    """
    games = []
    f = open(input_file, 'r')
    for line in f:
        game = line.strip('\n')
        game = game.split(', ')
        home_team = game[0][:-2].strip()
        home_score = int(game[0][-2:].strip())
        away_team = game[1][:-2].strip()
        away_score = int(game[1][-2:].strip())
        games.append([home_team, home_score, away_team, away_score])
    f.close()
    return games


def create_teams(games_played):
    """Accepts a list of 4-element lists and returns a dict with all unique team names initialized to zero.
    >>> test = create_teams([['Lions', 3, 'Snakes', 3], ['Snakes', 1, 'Lions', 0]])
    >>> len(test)
    2
    >>> sorted(test.items())
    [('Lions', 0), ('Snakes', 0)]
    """
    d = {}
    for game in games_played:
        if game[0] not in d:
            d[game[0]] = 0
        if game[2] not in d:
            d[game[2]] = 0
    return d


def calculate_team_standings(games_played, standings):
    """Accepts a list of games played and a dict of teams.
    Returns all teams standings according to the rules: a tie == 1, a win == 3 and a loss == 0.
    >>> test = calculate_team_standings([['L', 3, 'S', 3], ['S', 1, 'L', 0], ['S', 0, 'L', 0]], {'L': 0, 'S': 0})
    >>> sorted(test.items())
    [('L', 2), ('S', 5)]
    """
    for game in games_played:
        if game[1] == game[3]:
            standings[game[0]] += 1
            standings[game[2]] += 1
        elif game[1] > game[3]:
            standings[game[0]] += 3
            standings[game[2]] += 0
        else:
            standings[game[0]] += 0
            standings[game[2]] += 3
    return standings


def last(tup):
    """Returns the last element of a tuple.
    >>> test = last(('Lions', 5))
    >>> test
    5
    """
    return tup[-1]


def check_tense(num):
    """Return pts unless num == 1.
    >>> test = check_tense(1)
    >>> test
    'pt'
    >>> test = check_tense(-1)
    >>> test
    'pts'
    """
    if num == 1:
        return "pt"
    else:
        return "pts"


def rank_team_standings(standings):
    """Expects a dict of team standings.
    Returns a ranked list that is ordered from most to least points.
    If two or more teams have the same number of points, they will all have the same rank and be in alphabetical order.
    >>> rank_team_standings({'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0})
    [[1, 'Tarantulas', 6], [2, 'Lions', 5], [3, 'FC Awesome', 1], [3, 'Snakes', 1], [5, 'Grouches', 0]]
    >>> rank_team_standings({'Lions': 6, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0, 'Zebras': 1})
    [[1, 'Lions', 6], [1, 'Tarantulas', 6], [3, 'FC Awesome', 1], [3, 'Snakes', 1], [3, 'Zebras', 1], \
[6, 'Grouches', 0]]
    >>> rank_team_standings({'Lions': 6, 'Snakes': 6, 'Tarantulas': 6, 'FC Awesome': 6, 'Grouches': 6, 'Zebras': 1, \
'Ants': 6, 'Bees': 6, 'Cats': 6, 'Dogs': 6, 'Birds': 1, 'Rats': 2})
    [[1, 'Ants', 6], [1, 'Bees', 6], [1, 'Cats', 6], [1, 'Dogs', 6], [1, 'FC Awesome', 6], [1, 'Grouches', 6], \
[1, 'Lions', 6], [1, 'Snakes', 6], [1, 'Tarantulas', 6], [10, 'Rats', 2], [11, 'Birds', 1], [11, 'Zebras', 1]]
    >>> rank_team_standings({'Bees': 6, 'Ants': 6, 'FC Awesome': 6})
    [[1, 'Ants', 6], [1, 'Bees', 6], [1, 'FC Awesome', 6]]
    >>> rank_team_standings({'Grouches': 0})
    [[1, 'Grouches', 0]]
    """
    ranked = sorted(standings.items(), key=last, reverse=True)
    rank = 1
    prev_team = ranked[0][0]
    ranked_teams = [[rank, prev_team, standings[prev_team]]]
    dup_standing = 0

    for curr_team in ranked[1:]:
        if standings[curr_team[0]] == standings[prev_team]:
            ranked_teams.append([rank, curr_team[0], standings[curr_team[0]]])
            dup_standing += 1
        else:
            rank = rank + dup_standing + 1
            ranked_teams.append([rank, curr_team[0], standings[curr_team[0]]])
            dup_standing = 0
            prev_team = curr_team[0]

    ranked_teams_sorted = sorted(ranked_teams)
    return ranked_teams_sorted


def print_team_standings(teams_standing):
    """Expects a list of sorted ranked teams [[rank, team, score]] and prints the teams to stdout.
    >>> print_team_standings([[1, 'Tarantulas', 6], [2, 'Lions', 5], [3, 'FC Awesome', 1], [3, 'Snakes', 1], \
[5, 'Grouches', 0]])
    1. Tarantulas, 6 pts
    2. Lions, 5 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    5. Grouches, 0 pts
    >>> print_team_standings([[1, 'Lions', 6], [1, 'Tarantulas', 6], [3, 'FC Awesome', 1], [3, 'Snakes', 1], \
[3, 'Zebras', 1], [6, 'Grouches', 0]])
    1. Lions, 6 pts
    1. Tarantulas, 6 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    3. Zebras, 1 pt
    6. Grouches, 0 pts
    """
    for team in teams_standing:
        print("%s. %s, %s %s" % (team[0], team[1], team[2], check_tense(team[2])))


def main():
    if len(sys.argv) != 2:
        print("python3 soccer_ranking.py <sample-input.txt>")
        sys.exit(1)

    file_handle = sys.argv[1]
    total_games = parse_file(file_handle)
    stats = create_teams(total_games)
    stats = calculate_team_standings(total_games, stats)
    teams_ranked = rank_team_standings(stats)
    print_team_standings(teams_ranked)


if __name__ == '__main__':
    main()
