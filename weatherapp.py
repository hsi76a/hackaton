from flask import Flask, jsonify, render_template, request
from custom_modules.api_functions import get_weer_op_locatie

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lattitude = request.form.get("inputLat")
        longitude = request.form.get("inputLng")
        # voer api request uit
        weer_op_locatie = get_weer_op_locatie(lattitude, longitude)
        if weer_op_locatie:
            return render_template('index.html', message=f"no Response for weather")
        else:
            # pass variabele naar rendertamplate
            return render_template('index.html', weer_lijst=weer_op_locatie)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
