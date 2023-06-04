# Basketball_visualized
Visualization web app


The back end is made in python using a couple of libraries. I think in order for you to work on it as well. You need to download python and the necessary libraries. This shouls not be to hard to be honest. I am going to make a list of steps below. Hopefully it all works out lol. 

### Setting up
1. First check if you have python installed. This could be done in the command line. type in "python --version"
2. If not download it and just get the latest version
3. Now you need to intall pip. Recommend watching a quick youtube video :)
4. After you have pip, getting the packages should be simple. Just type in the commands in you command prompt
5. pip install beautifulsoup4
6. pip install flask
7. pip install flask-login
8. pip install flask-sqlalchemy
9. pip install numpy
10. pip install pandas
11. pip install requests

Those should be all of them.

### How the directory is organized
- So the files are organized in a simple manner.
- Ignore the instance folder
- The website folder
  - ignore __pycache__ and static
  - templates
    - py_visuals: python script that will build the graphs that need to be displayed
    - base.html: This is like the parent class and all other html files are child classes of this parent file.
    - graph.html: supposed to display the graphs
    - home.html: nothing - will be deleted
    - login: where they choose letter of the player
    - names: they choose the actual player
    - sign_up: user chooses graph type (honestly might get rid of this, to make the project scope smaller)
    - variables.html: user chooses what variables they would like to see visualized
 - The only python file seriously important to front-end is auth.py. This file grabs the information from the user and stoores it. So that the computer knows what type of graph to build.
- main.py is just the script that starts it all

### Goal
Honestly I would like to make the different pages all into one page if possible. If not just make it more aesthetically pleasing.

### Where am I on development of backend
So all the data is collected, I just need to write the code the builds the actual visuals. I think I know how I could display the visuals, but it will not be interactive. Not sure if you know a method to make the visuals a little interactive? I am going to attempt plotly, but no promises. 


