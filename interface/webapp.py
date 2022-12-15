from flask import Flask, request, render_template
from markupsafe import escape
from flask import blueprints
from literki.literki import Literki


class WebApp:
    app: Flask = None

    def __init__(self, game: Literki):
        self.app = Flask(__name__)
        self.game = game
        self.app.add_url_rule('/', '', self.index, methods=['GET', 'POST'])

    def start(self):
        return self.app.run(debug=True)

    def index(self):
        name = request.args.get("name", "World")
        return render_template('index.html',
                               word_length=self.game.length,
                               max_tries=self.game.max_tries,
                               keyboard_layout=self.game.keyboard_layout,
                               keyboard_status=self.game.keyboard.status)
        # return f'Hello, {escape(name)}!'
