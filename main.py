from flask import Flask, render_template, request
import requests



def get_weather_results(zip_code):
    api_key = "bd04540de70a58837a4af62931553235"
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()




app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template("tem.html")

@app.route('/results', methods ={'POST'})
def render_results():
    zip_code = request.form['zipCode']
    
    data = get_weather_results(zip_code)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    return render_template('tem2.html', 
                            location=location, 
                            temp=temp, 
                            feels_like=feels_like, 
                            weather=weather)
  

if __name__ == "__main__":
    app.run()    

    
    
            
