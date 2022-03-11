from flask import Blueprint, render_template , url_for, request, redirect
from ..models import Snakes, Snake_location


sdata = Blueprint('sdata', __name__, template_folder='templates', static_folder='static')

@sdata.route('/')
def index():

    snake_data = []

    return render_template('snake_index.html')

@sdata.route('/get_snake_list', methods=['POST'])
def get_snake_list():

    region = request.form['region']

    data_list = []

    if request.method == 'POST':
        snake_list = Snake_location.query.filter_by(state=region).all()

        for s in snake_list:
            data_list.append(s.snake_id)

        snake_data = [Snakes.query.get(i) for i in data_list]

        snake_data = [a.name_en for a in snake_data]

        return render_template('snake_index.html',
        snake_data=snake_data,
        region=region
        )

@sdata.route('/get_snake_family', methods=['POST'])
def get_snake_family():

    family = request.form['family']

    data_list = []

    if request.method == 'POST':
        snake_list = Snakes.query.filter_by(family=family).all()

        for s in snake_list:
            data_list.append(s.name_en)

        snake_data = data_list

        return render_template('snake_index.html',
        snake_data=snake_data,
        family=family
        )

@sdata.route('/snake_info/<int:id>')
def snake_info(id):
    def convert(string):
        li = list(string.split(","))
        return li

    snake_intel = Snakes.query.get(id)
    
    antivenom_list = convert(snake_intel.antivenom)

    return render_template('snake_info.html',
    snake_intel=snake_intel,
    antivenom_list=antivenom_list
    )


@sdata.route('/test')
def test():


    snake_list = Snakes.query.get(3)

    print(snake_list)

    return render_template('snake_index.html')