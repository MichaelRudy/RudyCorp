import requests

def request(**args):
    response = requests.get(args.get('host')+args.get('endpoint'), headers=args.get('headers'), auth=(args.get('username'), args.get('token')))
    return response.json()

