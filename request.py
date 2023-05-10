# 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

import requests



def request():
    host = 'https://api.github.com/'
    endpoint = 'users/michaelrudy'
    headers = {"Accept": "application/vnd.github.inertia-preview+json"}
    username = "michaelrudy"
    token = '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'
    response = requests.get(host+endpoint, headers=headers, auth=(username, token))
    print(response.json())


if __name__ == '__main__':
    request()