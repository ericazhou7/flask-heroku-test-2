from flask import render_template, Flask
import json # this lets us understand jsons that we get from websites!
import requests # this lets us talk to other servers!



## NOTE: some of these prints don't work properly on replit

# ex. 1: kanye quotes
api_url_kanye = "https://api.kanye.rest/" # for kanye quotes

response = requests.get(api_url_kanye)
# print(response) # prints what we get back from the API
json_string = response.content
# print(json_string) # prints the raw json as a string
data = json.loads(json_string)
# print(data) # prints the data as a dictionary
quote = data['quote']
# print(quote) # prints the kanye quote 


# ex. 2: ages
api_url_age = "https://api.agify.io/" # for getting ages

response = requests.get(api_url_age, params = {'name': 'chetan'})
# print(response) # won't do anything yet
json_string = response.content
# print(json_string) # prints the raw json as a string
data = json.loads(json_string)
# print(data) # prints the data as a dictionary
age = data['age']
# print(age)



## ex. 3: add to flask
app = Flask(__name__)

@app.route("/")
def index():

  # call the API and store the result to a variable
  response = requests.get(api_url_kanye)
  json_string = response.content
  # print(response) # gives us raw json
  data = json.loads(json_string)
  quote = data['quote']

  # use the variable to render HTML
  return render_template("index.html", q = quote)


app.run(host="0.0.0.0",
        port = 8080,
        debug = True)