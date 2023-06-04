# TODO for player stats
# Split win/loss and by how many points into two categories
# I need to know which team was away and home
# When player is inactive, fill it in with null values
# when a % is empty I need to put 0
# I need to convert all short hand team names into actual name

# TODO for overall project
# i need to move the labels into a another file
# i need to make database of short hand team names to actual names
# I need to make this function so it could be called for different players
# I think I will only do this for 2 teams to start with
# create a function that also extracts player data splits

# WARNING
# I am collecting from 2018
# I am only collecting from 10 players to start
# this data is from basketball reference
# it updates it once a day

# I did it like this because I added a few labels
table_labels = ['Game #',
                'Date',
                'Age',
                'His Team',
                'location',
                'Enemy Team',
                'Result',
                'Point Difference',
                'Starter',
                'Minutes Played',
                'Field Goals',
                'Field Goal Attempts',
                'Field Goal Percentage',
                '3 Point Field Goals',
                '3 Point Field Goal Attempts',
                '3 Point Field Goal Attempts',
                'Free Throws',
                'Free Throw Attempts',
                'Free Throw Percentage',
                'Offensive Rebounds',
                'Defensive Rebounds',
                'Total Rebounds',
                'Assists',
                'Steals',
                'Blocks',
                'Turnovers',
                'Personal Fouls',
                'Points',
                'Game Score',
                '+/-']

# converts acronyms
team_conversion = {
    'ATL'	: 'Atlanta Hawks',
    'BOS'	: 'Boston Celtics',
    'CHA'	: 'Charlotte Hornets',
    'CHO'   : 'Charlotte Hornets',
    'CHH'   : 'Charlotte Hornets',
    'CHI'	: 'Chicago Bulls',
    'CLE'	: 'Cleveland Cavaliers',
    'DAL'	: 'Dallas Mavericks',
    'DEN'	: 'Denver Nuggets',
    'DET'	: 'Detroit Pistons',
    'GSW'	: 'Golden State Warriors',
    'HOU'   : 'Houston Rockets',
    'IND'	: 'Indiana Pacers',
    'LAC'   : 'Los Angeles Clippers',
    'LAL'	: 'Los Angeles Lakers',
    'MEM'	: 'Memphis Grizzlies',
    'MIA'	: 'Miami Heat',
    'MIL'	: 'Milwaukee Bucks',
    'MIN'	: 'Minnesota Timberwolves',
    'NOP'	: 'New Orleans Pelicans',
    'NOH'   : 'New Orlean Hornets',
    'NYK'	: 'New York Knicks',
    'NJN'   : 'New Jersey Nets',
    'BKN'	: 'Brooklyn Nets',
    'BRK'   : 'Brooklyn Nets',
    'OKC'	: 'Oklahoma City Thunder',
    'ORL'	: 'Orlando Magic',
    'PHI'	: 'Philadelphia 76ers',
    'PHO'	: 'Phoenix Suns',
    'POR'	: 'Portland Trail Blazers',
    'SAC'	: 'Sacramento Kings',
    'SAS'   : 'San Antonio Spurs',
    'SEA'   : 'Seattle SuperSonics',
    'WSB'   : 'Washington Bullets',
    'TOR'	: 'Toronto Raptors',
    'UTA'	: 'Utah Jazz',
    'WAS'	: 'Washington Wizards'
}

