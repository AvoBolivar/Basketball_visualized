import requests
from bs4 import BeautifulSoup
from .scraping_library import team_conversion, table_labels
import numpy as np
import pandas as pd


# gets the player stats that year
def get_player_stat(link):
    # getting the page
    web = requests.get(link)
    main_soup = BeautifulSoup(web.text, 'html.parser')

    # getting the table
    stat_table = main_soup.find(id='pgl_basic')
    stat_rows = stat_table.find_all('tr')

    # setting up vars
    year_stat = []
    game_stat = []

    # loop getting all the data
    for table_row in stat_rows:
        row = table_row.find_all('td')
        if len(row) > 8:
            for cell in row:
                try:
                    game_stat.append(int(cell.find('strong').contents[0]))
                except AttributeError:
                    try:
                        info = str(cell.find('a').contents[0])
                        if info[0].isalpha():
                            info = team_conversion[info]
                        game_stat.append(info)
                    except AttributeError:
                        try:
                            info = float(cell.contents[0])
                            game_stat.append(info)
                        except:
                            # splitting wins and losses
                            try:
                                info = str(cell.contents[0])
                                if info[2] == '(':
                                    letter = info[0]
                                    point_difference = info[3:len(info) - 1]
                                    game_stat.append(letter)
                                    game_stat.append(point_difference)
                                elif info[2] == '-':
                                    game_stat.append(info[:2])
                                else:
                                    game_stat.append(info)
                            except:
                                if len(cell.contents) > 0:
                                    game_stat.append('@')
                                else:
                                    game_stat.append('null')
            year_stat.append(game_stat)
            game_stat = []

    return year_stat


# returns list of links to access game data
def get_player_links(link, index):

    main_link = 'https://www.basketball-reference.com'
    new_link = main_link + link
    letter_page = requests.get(new_link)
    letter_soup = BeautifulSoup(letter_page.text, 'html.parser')
    table = letter_soup.find(id='players')
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')
    
    player_extension = table_rows[index].find('th').find('strong').find('a')['href']
    player_link = main_link + player_extension

    # links
    links = []

    web = requests.get(player_link)
    main_soup = BeautifulSoup(web.text, 'html.parser')

    table = main_soup.find(id='per_game')
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')
    if len(table_rows) > 3:
        table_rows = table_rows[len(table_rows)-3:]

    for r in table_rows:
        try:
            data = r.find('a')
            extension = data['href']
            links.append(main_link+extension)
        except TypeError:
            pass

    return links


# gets player home page link
def get_letter_link(letters):
    # converting the letter into number to find index
    # will make it more robust when applying to website

    # getting the page
    link = 'https://www.basketball-reference.com/players/'
    web = requests.get(link)
    main_soup = BeautifulSoup(web.text, 'html.parser')

    # getting the link to the letters
    outer_table = main_soup.find(class_='page_index')
    outer_row = outer_table.find_all('li')
    # gets extension for letters
    links = []
    for i in letters:
        index = ord(i) - 91
        links.append(outer_row[index].find('a')['href'])
    return links


def getting_players_from_letter(link):
    # prints all all players with that letter
    main_link = 'https://www.basketball-reference.com'
    new_link = main_link + link
    letter_page = requests.get(new_link)
    letter_soup = BeautifulSoup(letter_page.text, 'html.parser')
    table = letter_soup.find(id='players')
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')
    count = 0
    players = {}
    for i in table_rows:
        count += 1
        cell = i.find('th')
        try:
            players[count] = cell.find('strong').find('a').contents[0]
        except AttributeError:
            pass
    return players


def create_player_df(link, index):
    years_links = get_player_links(link, index)
    
    data = []

    for i in years_links:
        temp_data = get_player_stat(i)
        for j in temp_data:
            data.append(j)

    data = np.array(data)
    data = data.T

    temp_dict = {}
    for i in range(len(data)):
        temp_dict[table_labels[i]] = data[i]
    player_df = pd.DataFrame(temp_dict)
    player_df = clean_data(player_df)
    return player_df


def clean_data(dframe):
    file = dframe
    # converting win/loss to 1/0
    file['Result'] = file['Result'].map({'W': 1, 'L': 0})
    # converting date to datetime object
    file['Date'] = pd.to_datetime(file['Date'])
    # converting location 1: home / 0: away
    l = file.columns[4]
    file[l] = file[l].fillna('1')
    file[l] = file[l].map({'@': 0, '1': 1})
    # converting minutes played to a decimal
    # its still in base 60
    file['Minutes Played'] = file['Minutes Played'].map(lambda x: x.replace(':', '.'))
    file['Minutes Played'] = pd.to_numeric(file['Minutes Played'])
    # getting rid of last null values
    file['Free Throw Percentage'] = file['Free Throw Percentage'].fillna(0)
    return file

# create_player_csv()
# practice = getting_player_links('https://www.basketball-reference.com/players/w/willizi01.html')

