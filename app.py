import requests
from flask import Flask, abort, jsonify
from flask_cors import CORS
from config import X_Auth_Token, GCLOUD_CREDENTIAL_PATH


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
        headers = {'X-Auth-Token': X_Auth_Token}
        response = requests.get(uri, headers=headers)
        matches = response.json()['matches']
        return matches

    def get_leagues(matches: list):
        leagues = [
            tuple(match['competition'].items()) for match in matches if match
        ]

        return [dict(value) for value in set(leagues)]

    def get_pronos(home_team, away_team, date, referree):
        return {}

    @app.route('/')
    def hello_world():  # put application's code here
        return jsonify(
            {
                "message": "Hello Wordl"
            }
        )

    @app.route('/prono')
    def test():
        matches = get_matches()
        list_matches = [{'competition': {'name': match['competition']['name'],
                                         'logo': match['competition']['emblem']},
                         'homeTeam': {'name': match['homeTeam']['name'],
                                      'logo': match['homeTeam']['crest']},
                         'awayTeam': {'name': match['awayTeam']['name'],
                                      'logo': match['awayTeam']['crest']},
                         'date': match['utcDate']
                         } for match in matches if
                        match['status'] != 'FINISHED' and match['competition']['code'] in ['PL']
                        ]
        print(f'X_AUTH_TOKEN: {X_Auth_Token}')
        print(f'GCLOUD_CREDENTIAL_PATH: {GCLOUD_CREDENTIAL_PATH}')

        return jsonify({
            'success': True,
            'matches': list_matches,
            'league': get_leagues(list_matches),
            'token': f'X_AUTH_TOKEN: {X_Auth_Token}'
        })

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
