from flask import Flask, render_template
import requests

app = Flask(__name__)

headers = {
    "X-RapidAPI-Key": "0c39ae03ddmsh54c68ca89567e04p1870f1jsn5ac9b871b287",
    "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}
seattle = {"city": "Seattle"}
shangai = {"city": "Shangai"}
toronto = {"city": "Toronto"}
mumbai = {"city": "Mumbai"}
new_york = {"city": "New York"}
boston = {"city": "Boston"}
london = {"city": "London"}


@app.route("/")
def home():
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    response = requests.request("GET", url, headers=headers, params=seattle)
    shaingai_temp = requests.request(
        "GET", url, headers=headers, params=shangai)
    toronto_temp = requests.request(
        "GET", url, headers=headers, params=toronto)
    mumbai_temp = requests.request("GET", url, headers=headers, params=mumbai)
    newyork_temp = requests.request(
        "GET", url, headers=headers, params=new_york)
    london_temp = requests.request("GET", url, headers=headers, params=london)
    boston_temp = requests.request("GET", url, headers=headers, params=boston)
    print(shaingai_temp.json())
    return render_template("index.html", shangai=shaingai_temp.json(), toronto=toronto_temp.json(), mumbai=mumbai_temp.json(), new_york=newyork_temp.json(), london=london_temp.json(),boston=boston_temp.json())


if __name__ == "__main__":
    app.run()
