import requests
from flask_cors import CORS
from flask import Flask, render_template, abort, jsonify


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

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
        list_matches = []
        for match in matches:
            if not match['status'] == 'FINISHED':
                match_reduced = {}
                match_reduced.update({'competition': {'name': match['competition']['name'],
                                                      'logo': match['competition']['emblem']},
                                      'homeTeam': {'name': match['homeTeam']['name'],
                                                      'logo': match['homeTeam']['crest']},
                                      'awayTeam': {'name': match['awayTeam']['name'],
                                                   'logo': match['awayTeam']['crest']},
                                      'date': match['utcDate']
                                      })

                list_matches.append(match_reduced)
        return jsonify({
            'success': True,
            'matches': list_matches,
            'league': leagues
        })
        # return render_template('test.html', leagues=leagues, matches=matches)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
