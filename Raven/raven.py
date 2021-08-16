# REQUIREMENTS

from flask import Flask
from flask.globals import request

from pyfade import Colors, Fade
from pycenter import center


from os import name, system
from base64 import b64decode

from src.database import Database



# FUNCTIONS AND VARIABLES

def clear():
    system("cls" if name == 'nt' else "clear")

Database.makedb()




# PORT AND APP INSTANCE CREATION

port = 8500

app = Flask("Raven")




# VARIABLES

raven = """
   █████████    ▄████████    ▄█    █▄     ▄████████   ██████▄   
  ███    ███   ███    ███   ███    ███   ███    ███   ███▀▀▀██▄ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███   ███ 
  ███▄▄▄▄███   ███    ███   ███    ███   ███▄▄▄       ███   ███ 
  ███▀▀▀▀▀     ██████████   ███    ███   ███▀▀▀       ███   ███ 
  ██████████   ███    ███   ███    ███   ███    █▄    ███   ███ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███   ███ 
  ███    ███   ███    █▀     ▀██████▀    ██████████   ███   ███ 
  ███    ███                                          ███   ███   
"""

author = "   - - - {} - - -".format(b64decode("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))


# MAIN FUNCTION

def main():
    clear()

    if name == 'nt':
        system("title Raven")
        system("mode 140, 40")

    print(Fade.Vertical(Colors.purple_to_red, center(raven)))
    print(Fade.Horizontal(Colors.red_to_black, center(author)))

    print("\n"*2)

    app.run(port=port)



# WEB PAGES CREATION

@app.route('/')
def index():
    return "Made with <3 by https://github.com/billythegoat356/Raven"


@app.route("/get/<int:id>", methods=['GET'])
def get_id(id):
    id = str(id)
    if Database.check(id):
        return "invalid id", 400
    
    return Database.get(id)

@app.route('/create', methods=['POST'])
def create():

    data = request.get_data()


    if data is None:
        return "invalid data", 400

    data = data.decode('utf-8')

    return Database.stock(data)



# START CODE

if __name__ == '__main__':
    main()