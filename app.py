import requests
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
            if request.method == 'POST':
                    city = request.form.get('city').capitalize()
                    # add data to the database.
                    try:
                        con = sqlite3.connect('weather.db')
                        cur = con.cursor()
                        cur.execute("INSERT into cities (name) values (?)", (city,))
                        con.commit()
                        print("City Is Successfully Added")
                    except:
                        con.rollback()
                        print("Something Goes To Wrong")
                    finally:
                        con.close()

            # fetch data from database.

            city_list = []
            weather_data = []

            con = sqlite3.connect('weather.db')
            cur = con.cursor()
            cur.execute("select DISTINCT name from cities ORDER BY id DESC LIMIT 3")
            rows = cur.fetchall()
            for row in rows:
                for name in row:
                    city_list.append(name)    
            con.close()

            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9dbf888430bc49504f1509e5e826002a'

            for city in city_list:
                receive_data = requests.get(url.format(city)).json()
                weather={
                    'city': city.capitalize(),
                    'temperature': receive_data['main']['temp'],
                    'description': receive_data['weather'][0]['description'],
                    'icon': receive_data['weather'][0]['icon']
                }
                weather_data.append(weather)
            # print(weather_data)
    except:
        return render_template('pageNotFound.html')
    return render_template('weather.html', weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=False)
