import requests


with open('/Users/michaelrudy/Desktop/Tokens/gh.txt', 'r') as in_file:
        token = in_file.readlines()
args = {
        'host': 'https://api.github.com/',
        'endpoint': 'users/michaelrudy/repos',
        'headers': {"Accept": "application/vnd.github.inertia-preview+json"},
        'username': 'michaelrudy',
        'token': token[0],
    }


def request(**args):
    response = requests.get(args.get('host')+args.get('endpoint'), headers=args.get('headers'), auth=(args.get('username'), args.get('token')))
    return response.json

