import requests
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    def get_match():
        uri = 'https://api.football-data.org/v4/matches'
        headers = {'X-Auth-Token': '3d6e6f89c3e244e4813c0c44a32fd80b'}

        leagues = []
        response = requests.get(uri, headers=headers)
        matches = response.json()['matches']
        for match in matches:
            leagues.append(match['competition'])
        unique_leagues = []
        [unique_leagues.append(x) for x in leagues if x not in unique_leagues]
        return unique_leagues, matches

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    @app.route('/test')
    def test():
        leagues, matches = get_match()
        return render_template('test.html', leagues=leagues, matches=matches)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
