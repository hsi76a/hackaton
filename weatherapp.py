from flask import Flask, jsonify, render_template, request
from custom_modules.api_functions import get_weer_op_locatie, get_verkeers_info

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lattitude = request.form.get("lattitude")
        longitude = request.form.get("longitude")
        plaatsnaam = request.form.get("plaatsnaam")
        # voer api request uit
        weer_op_locatie = get_weer_op_locatie(lattitude, longitude)
        verkeerinfo = get_verkeers_info(plaatsnaam)
        # if weer_op_locatie = False:
        #     return render_template('index.html', message=f"no Response for weather")
        # else:
        # pass variabele naar rendertamplate

        wind_deg = weer_op_locatie['current']['wind_deg']
        windrichting = ""

        if wind_deg > 45:
            if wind_deg > 135:
                if wind_deg > 225:
                    if wind_deg > 315:
                        windrichting = 'Noord'
                    else:
                        windrichting = 'West'
                else:
                    windrichting = 'Zuid'
            else:
                windrichting = 'Oost'

            return render_template('index.html', wind_richting=windrichting, weer_lijst=weer_op_locatie, verkeerinfo=verkeerinfo)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
