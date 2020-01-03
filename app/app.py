import argparse
import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
Bootstrap(app)

def load_gif_list():
    gif_list = [l.strip() for l in open('synth_proposals_v1.lst').readlines()]

    display_list = list()
    for i in range(0, 100, 4):
        display_list.append(gif_list[i:i+4])

    print(display_list)

    return display_list

@app.route('/view', methods=['GET', 'POST'])
def view():
    gif_list = load_gif_list()
    return render_template('view.html', gif_list=gif_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='0.0.0.0', help='Server IP')
    parser.add_argument('--port', type=int, default=5000, help='Server port')
    args = parser.parse_args()

    app.run(debug=True, host=args.ip, port=args.port)