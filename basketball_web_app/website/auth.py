from flask import Blueprint, render_template, request, flash, redirect, url_for
from .scraping import get_letter_link, getting_players_from_letter, create_player_df
from .scraping_library import table_labels

auth = Blueprint('auth', __name__)
letters = []
data = []
chck_boxes = []
players_chosen = []
ext = []
dataframes = []
vars = []

# choosing letters
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        letters.clear()
        data.clear()

        for i in range(25):
            temp = request.form.get(str(i))
            if temp != None:
                letters.append(temp)
        if len(letters) > 2:
            print("error")
            flash('You can only choose up to 2 letters', category='error')
            return render_template("login.html")
        else:
            print(letters)
            # getting letter extensions
            extensions = get_letter_link(letters)
            ext.append(extensions)
            # will hold dictionaries of the player data
            for i in extensions:
                players = getting_players_from_letter(i)
                data.append(players)
                
            flash('Great', category='success')
            return redirect(url_for('auth.names'))

    return render_template("login.html")


# choosing graphtype
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        graphType = request.form.get('graphType')
        if isinstance(graphType, str):
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))
        else:
            flash('first field must be less than 3', category='error')

    return render_template("sign_up.html")

# choosing variables
@auth.route('/names', methods=['GET', 'POST'])
def names():
    if request.method == 'POST':
        player_values = []
        for i in data:
            player_values += list(i.keys())
        for i in player_values:
            player = request.form.get(str(i))
            if player != None:
                chck_boxes.append(int(player[0]))
        print(chck_boxes)
        
        # once player has been chosen
        # if 2 letters chosen the dictionaries will be merged
        dict_players = {}
        for dictionary in data:
            for p in dictionary:
                dict_players[p] = dictionary[p]
        
        # players_chosen.append(dict_players[chck_boxes[0]])
        # ext = ext[0]
        
        # for index in range(len(ext[0])):
        #     dataframes.append(create_player_df(ext[index], players_chosen[index]))
            

        return redirect(url_for('auth.variables'))
    
    return render_template("names.html", p=data, l=letters, amnt=len(letters))

@auth.route('/variables', methods=['GET', 'POST'])
def variables():
    label_index = list(range(len(table_labels)))
    if request.method == 'POST':
        for i in label_index:
            picked = request.form.get(str(i))
            if picked != None:
                vars.append(int(picked[0]))
        print(vars)
        return redirect(url_for('auth.graph'))

    return render_template("variables.html", labels=table_labels, index=label_index)

@auth.route('/graph', methods=['GET', 'POST'])
def graph():
    # this is where the dataframe will be created and all I will pass in is the dataframe. All other things would be sorted in html file

    print('in graph page')
    print()
    return render_template("graph.html", df=dataframes, vars=vars)
