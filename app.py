from flask import Flask
from markupsafe import escape
import requests
app = Flask(__name__)

@app.route("/book/<int:isbn>")
def get_author(isbn):
    print(isbn)
    path = "https://openlibrary.org/isbn/" +str(isbn) + ".json"
    print(path, "path")
    res = requests.get(path)
    #print(res)
    #print(res.json)
    #print(res.status_code)
    if res.status_code == 200:
        return{"message" : res.json()}
    elif res.status_code == 404:
        return {"message" : "something went wrong"}
