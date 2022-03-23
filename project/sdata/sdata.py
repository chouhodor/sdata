from flask import Blueprint, render_template , url_for, request, redirect, send_from_directory
from ..models import Snakes, Snake_location
from os import listdir
from os.path import isfile, join
import os


sdata = Blueprint('sdata', __name__, template_folder='templates', static_folder='static')

@sdata.route('/')
def index():

    snake_data = []
    snake_cache = Snakes.query.all()

    return render_template('snake_index.html',
    snake_cache=snake_cache
    )

@sdata.route('/get_snake_list', methods=['POST'])
def get_snake_list():

    region = request.form['region']

    data_list = []

    if request.method == 'POST':
        snake_list = Snake_location.query.filter_by(state=region).all()

        for s in snake_list:
            data_list.append(s.snake_id)

        snake_data = [Snakes.query.get(i) for i in data_list]

        snake_data = [a for a in snake_data]

        return render_template('snake_index.html',
        snake_data=snake_data,
        region=region
        )

@sdata.route('/get_snake_family', methods=['POST'])
def get_snake_family():

    family = request.form['family']

    if request.method == 'POST':
        snake_data = Snakes.query.filter_by(family=family).all()

        return render_template('snake_index.html',
        snake_data=snake_data,
        family=family
        )

@sdata.route('/snake_info/<int:id>')
def snake_info(id):

    snake_intel = Snakes.query.get(id)

    mypath = 'project/static/snake_img/' + str(id)

    img_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    def convert(string):
        li = list(string.split(","))
        return li

    return render_template('snake_info.html',
    snake_intel=snake_intel,
    img_files=img_files,
    convert=convert
    )


@sdata.route('/thumbnails/<int:id>')
def thumbnails(id):

    filename = str(id) + '.png'
    return send_from_directory('static/thumbnails', filename)
    

@sdata.route('/img_info/<int:id>/<filename>')
def img_info(id, filename):

    return send_from_directory('static/snake_img/' + str(id), filename)


@sdata.route('/img_info/<int:id>')
def geo(id):

    filename = str(id) + '.png'
    return send_from_directory('static/geo', filename)



@sdata.route('/test')
def test():

    snake_list = Snakes.query.get(3)

    print(snake_list)

    return render_template('snake_index.html')

    '''
    def convert(string):
        li = list(string.split(","))
        return li
    '''