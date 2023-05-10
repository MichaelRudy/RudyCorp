import requests


def request(token):
    host = 'https://api.github.com/'
    endpoint = 'users/michaelrudy'
    headers = {"Accept": "application/vnd.github.inertia-preview+json"}
    username = "michaelrudy"
    token = token[0]
    response = requests.get(host+endpoint, headers=headers, auth=(username, token))
    print(response.json())


if __name__ == '__main__':
    with open('/Users/michaelrudy/Desktop/Tokens/gh.txt', 'r') as in_file:
        token = in_file.readlines()
    
    request(token)