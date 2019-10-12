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


def print_team_standings(standings):
    """Prints to stdout the rank of teams, if the total points are equal teams get the same rank.
    >>> print_team_standings({'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0})
    1. Tarantulas, 6 pts
    2. Lions, 5 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    5. Grouches, 0 pts
    """
    ranked = sorted(standings.items(), key=last)
    team_rank = 1
    team_count = len(ranked)
    while team_count > 0:
        if team_count == 1:
            tense = check_tense(ranked[team_count - 1][1])
            print("%s. %s, %s %s" % (team_rank, ranked[team_count - 1][0], ranked[team_count - 1][1], tense))
            team_count -= 1
        elif ranked[team_count - 1][1] != ranked[team_count - 2][1]:
            tense = check_tense(ranked[team_count - 1][1])
            print("%s. %s, %s %s" % (team_rank, ranked[team_count - 1][0], ranked[team_count - 1][1], tense))
            team_rank += 1
            team_count -= 1
        elif ranked[team_count - 1][1] == ranked[team_count - 2][1]:
            tense = check_tense(ranked[team_count - 1][1])
            print("%s. %s, %s %s" % (team_rank, ranked[team_count - 1][0], ranked[team_count - 1][1], tense))
            print("%s. %s, %s %s" % (team_rank, ranked[team_count - 2][0], ranked[team_count - 1][1], tense))
            team_rank += 2
            team_count -= 2


def main():
    if len(sys.argv) != 2:
        print("python3 soccer_ranking.py <sample-input.txt>")
        sys.exit(1)

    file_handle = sys.argv[1]
    total_games = parse_file(file_handle)
    stats = create_teams(total_games)
    stats = calculate_team_standings(total_games, stats)
    print_team_standings(stats)


if __name__ == '__main__':
    main()
