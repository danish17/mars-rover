from flask import Flask, render_template, request, jsonify
import lib.calculate

app = Flask(__name__)


@app.route('/')
def _app():
    return render_template('index.html')


@app.route('/calculate', methods=["POST"])
def calculate():
    rover_upper_right_corner_x = str(request.form.get('rover_upper_right_corner_x'))
    rover_upper_right_corner_y = str(request.form.get('rover_upper_right_corner_x'))
    rover_current_pos_x = str(request.form.get('rover_current_pos_x'))
    rover_current_pos_y = str(request.form.get('rover_current_pos_y'))
    rover_current_dir = request.form.get('rover_current_direction')
    rover_instructions = request.form.get('rover_instructions')

    rover_to_be = lib.calculate.calc(
        upper_right_corner=[rover_upper_right_corner_x, rover_upper_right_corner_y],
        current_position=[rover_current_pos_x, rover_current_pos_y, rover_current_dir],
        instructions=rover_instructions
    )

    if request.method == "POST":
        return render_template('index.html', result=rover_to_be)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
