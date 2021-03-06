# REQUIREMENTS

from flask import Flask, redirect, request


from os import name, system

from src.database import Database



# FUNCTIONS AND VARIABLES

def clear():
    system("cls" if name == 'nt' else "clear")

Database.makedb()




# PORT AND APP INSTANCE CREATION

port = 8500

app = Flask("Astebin")




# MAIN FUNCTION

def main():
    clear()
    app.run(port=port)



# WEB PAGES CREATION

@app.route('/')
def index():
    return redirect("https://github.com/billythegoat356/Astebin")


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
