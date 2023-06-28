1
import sqlite3
import mechanicalsoup
import pandas as pd

web = mechanicalsoup.StatefulBrowser()
web.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

th = web.page.find_all("th", attrs={"class": "table-rh"})
info = [value.text.replace("\n", "") for value in th]

td = web.page.find_all("td")
columns = [value.text.replace("\n", "") for value in td]

column_names = [
    "Founder",
    "Maintainer",
    "Initial_Release_Year",
    "Current_Stable_Version",
    "Security_Updates",
    "Release_Date",
    "System_Distribution_Commitment",
    "Forked_From",
    "Target_Audience",
    "Cost",
    "Status"
]

# Ensure all arrays have the same length
max_length = min(len(info), len(columns) // len(column_names))
info = info[:max_length]
columns = columns[:max_length * len(column_names)]

dictionary = {"Distribution": info}

for index, key in enumerate(column_names):
    dictionary[key] = [columns[i] for i in range(index, len(columns), len(column_names))]

df = pd.DataFrame(data=dictionary)

connection = sqlite3.connect('Linux.db')
cursor = connection.cursor()

# cursor.execute("CREATE TABLE Linux (Distro, " + ", ".join(column_names) + ")")

for i in range(len(df)):
    cursor.execute("INSERT INTO Linux VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(df.iloc[i]))

connection.commit()
connection.close()

=============

2
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen("https://docs.python.org/3/library/random.html")
soup = bs(page, 'html.parser')
names = soup.body.findAll('dt')
function_names = re.findall(r'id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]
description = soup.body.findAll('dd')
function_usage = []

for item in description:
    item = item.text
    item = item.replace('\n', ' ')
    function_usage.append(item)

print(function_names)
print(function_usage)
print(len(function_names))

data = pd.DataFrame({'function name': function_names, 'function usage': function_usage})
print(data)============

3
import sqlite3
conn = sqlite3.connect('gta_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS gta
                  (year INTEGER, title TEXT, location TEXT)''')
gta_data = [
    (1997, "GTA", 'New Guernsey'),
    (1999, "GTA", "USA"),
    (2001, "GTA III", "Liberty City"),
    (2002, "GTA: Vice City", "Vice City"),
    (2004, "GTA: San Andreas", "San Andreas"),
    (2008, "GTA IV", "Liberty City")
]
cursor.executemany('INSERT INTO gta VALUES (?,?,?)', gta_data)
cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                  (city_name TEXT, country TEXT)''')
cities_data = [("Liberty City", "New York")]
cursor.executemany('INSERT INTO cities VALUES (?,?)', cities_data)
conn.commit()
cursor.execute("SELECT * FROM gta")
gta_rows = cursor.fetchall()
print("Data in 'gta' table:")
for row in gta_rows:
    print(row)
cursor.execute("SELECT * FROM cities")
cities_rows = cursor.fetchall()
print("\nData in 'cities' table:")
for row in cities_rows:
    print(row)
cursor.execute("UPDATE gta SET location = 'New York' WHERE location = 'Liberty City'")
cursor.execute("UPDATE cities SET city_name = 'New York' WHERE city_name = 'Liberty City'")
conn.commit()
cursor.execute("SELECT * FROM gta")
updated_gta_rows = cursor.fetchall()
print("\nUpdated data in 'gta' table:")
for row in updated_gta_rows:
    print(row)
cursor.execute("SELECT * FROM cities")
updated_cities_rows = cursor.fetchall()
print("\nUpdated data in 'cities' table:")
for row in updated_cities_rows:
    print(row)
conn.close()

================



4
from flask import Flask

app = Flask(__name__)

books = [
    {"title": "Harry Potter", "price": 9.99, "isbn": "9781234567890"},
    {"title": "Lord Of The Rings", "price": 14.99, "isbn": "9780987654321"},
    {"title": "Godfather", "price": 19.99, "isbn": "9785432167890"}
]

@app.route('/')
def home():
   return "Welcome to the Bookstore!"
@app.route('/books')
def all_books():
      return books

@app.route('/book/<isbn>')
def get_book(isbn):
    for book in books:
        if book["isbn"] == isbn:
            return f"Title: {book['title']}, Price: ${book['price']}"
    return "Book not found"

if __name__ == '__main__':
    app.run(debug=True)


======


5
import dataset
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

db = dataset.connect('sqlite:///api.db')

book_list = {
    '1': {
        "id": "1",
        "name": "Elon Musk",
        "author": "Ashlee Vance"
    },
    '2': {
        "id": "2",
        "name": "Steve Jobs",
        "author": "Walter Isaacson"
    }
}

table = db['book_list']

table.insert(
    {
        "book_id": "1",
        "name": "Elon Musk",
        "author": "Ashlee Vance"
    }
)

table.insert(
    {
        "book_id": "2",
        "name": "Steve Jobs",
        "author": "Walter Isaacson"
    }
)


@app.route('/api/books', methods=['GET', 'PUT'])
def api_books():
    if request.method == 'GET':
        return make_response(jsonify(book_list), 200)


if __name__ == '__main__':
    app.run()
=======

6

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://coreyms.com/')
articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline)
    summary = article.find('.entry-content p', first=True).text
    print(summary)
    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)
    print()



=========================

7
from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "Description": "Python in AI",
        "course_id": "0",
        "name": "Python AI Certificate",
        "site": "btu.edu.ge"
    },
    {
        "Description": "CCNA",
        "course_id": "1",
        "name": "CCNA Certificate",
        "site": "netacad.com"
    },
    {
        "Description": "Linux",
        "course_id": "2",
        "name": "Linux Certificate",
        "site": "netdevgroup.com"
    }
]


@app.route('/')
def index():
    return "Python, CCNA, Linux, OpenAI"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route("/courses", methods=['POST'])
def create():
    course = {
        "Description": "SQLserver",
        "course_id": "3",
        "name": "SQLserver Certificate",
        "site": "mygreatlearning.com"
    }
    courses.append(course)
    return jsonify({'Created': course})


if __name__ == "__main__":
    app.run(debug=True)

# CMD: curl -i -H *Application-Type: Application/json* -X POST http://127.0.0.1:5000/courses
===========================




8
import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
html = requests.get(url)
tesla = BeautifulSoup(html.content, 'html.parser')
results = tesla.find(id='ResultsContainer')
job_title = results.find_all('h2', class_='title is-5')
for job in job_title:
    print(job.text)



========


9

def outer_function(text):
    def inner_function():
        print(text)

    return inner_function


a = outer_function('Tesla')
a()
 ============

10
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


print_h1 = html_tag('h1')
print_h1('TeslaLine')
print_h1('netTesla')
print_p = html_tag('p')
print_p('Python')
======



11)
from flask import Flask, jsonify
app=Flask(__name__)
courses=[{
      "Description":"Python in AI",
      "course_id":"0",
      "name":"Python AI Certificate",
      "site":"btu.edu.ge"
      },
     {
      "Description":"CCNA",
      "course_id":"1",
      "name":"CCNA Certificate",
      "site":"netacad.com"
      },
     {
      "Description":"Linux",
      "course_id":"2",
      "name":"Linux Certificate",
      "site":"netdevgroup.com"
 }]
@app.route('/')
def index():
    return "Python, CCNA, Linux, OpenAI"
@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':courses})
@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})
@app.route("/courses", methods=['POST'])
def create():
    course={"Description":"SQLserver",
    "course_id":"3",
    "name":"SQLserver Certificate",
    "site":"mygreatlearning.com"}
    courses.append(course)
    return jsonify({'Created':course})
@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description']="TESLA OS"
    return jsonify({'course':courses[course_id]})
@app.route("/courses/<int:course_id>", methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result':True})
if __name__=="__main__":
    app.run(debug=True)
    #cmd curl -i -H *Content-Type: Application/json* -X DELETE http://127.0.0.1:5000/courses/2
========
12)
import mechanicalsoup
soup=mechanicalsoup.StatefulBrowser()
soup.open('http://coreyms.com')
for article in soup.page.find_all('article'):
    headline=article.h1.a.text
    print(headline)
    summary=article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src=article.find('iframe', class_='youtube-player')['src']
        vid_id=vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]
        yt_link=f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link=None
    print(yt_link)
    print()
=======================
13
from flask import Flask, jsonify
app=Flask(__name__)
courses=[{
      "Description":"Python in AI",
      "course_id":"0",
      "name":"Python AI Certificate",
      "site":"btu.edu.ge"
      },
     {
      "Description":"CCNA",
      "course_id":"1",
      "name":"CCNA Certificate",
      "site":"netacad.com"
      },
     {
      "Description":"Linux",
      "course_id":"2",
      "name":"Linux Certificate",
      "site":"netdevgroup.com"
 }]
@app.route('/')
def index():
    return "Python, CCNA, Linux"
@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':courses})
if __name__=="__main__":
    app.run(debug=True)
==========

14

import requests
from bs4 import BeautifulSoup
url = "https://coreyms.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
post_titles = soup.find_all(["h1", "a"], class_="entry-title")
post_contents = soup.find_all("div", class_="entry-content")
youtube_videos = soup.find_all("iframe", class_="youtube-player")
for title in post_titles:
    print("Post Title:", title.text)
for content in post_contents:
    print("Post Content:", content.text)
for video in youtube_videos:
    video_id = video["src"].split("/embed/")[1].split("?")[0]
    print("YouTube Video ID:", video_id)

========

15
from flask import Flask, jsonify
app=Flask(__name__)
courses=[{
      "Description":"Python in AI",
      "course_id":"0",
      "name":"Python AI Certificate",
      "site":"btu.edu.ge"
      },
     {
      "Description":"CCNA",
      "course_id":"1",
      "name":"CCNA Certificate",
      "site":"netacad.com"
      },
     {
      "Description":"Linux",
      "course_id":"2",
      "name":"Linux Certificate",
      "site":"netdevgroup.com"
 }]
@app.route('/')
def index():
    return "Python, CCNA, Linux, OpenAI"
@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':courses})
@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})
@app.route("/courses", methods=['POST'])
def create():
    course={"Description":"SQLserver",
    "course_id":"3",
    "name":"SQLserver Certificate",
    "site":"mygreatlearning.com"}
    courses.append(course)
    return jsonify({'Created':course})
@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description']="TESLA OS"
    return jsonify({'course':courses[course_id]})
if __name__=="__main__":
    app.run(debug=True)

