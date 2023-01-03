import requests
from flask import Flask, render_template, abort, jsonify


def create_app():
    app = Flask(__name__)

    def get_matches():
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

    def get_pronos(home_team, away_team, date, referree):
        return {}

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    @app.route('/pronos', methods=['GET', 'POST'])
    def compute_pronos():
        try:
            leagues, matches = get_matches()
            all_pronos = []
            for match in matches:
                pronos = get_pronos(match['homeTeam']['name'], match['awayTeam']['name']
                                    , match['utcDate'], match['referees']['name'])
                match['homeTeam']['pronos'] = pronos['homeTeam']
                match['awayTeam']['pronos'] = pronos['awayTeam']
                all_pronos.append(match)

            return jsonify({
                'success': True,
                'matches': all_pronos,
                'leagues': leagues
            })
        except Exception as e:
            abort(500, f'{type(e)}: {e}')
            # raise e

    @app.route('/test')
    def test():
        leagues, matches = get_matches()
        return render_template('test.html', leagues=leagues, matches=matches)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
