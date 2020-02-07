import requests

def send_request_to_google(url=''):
    response = requests.get(f'http://www.google.com/{url}')
    print(f'Response Code: {response.status_code}')
    print(f'Headers: {response.headers["Content-Type"]}')
    # print(f'Content: {response.text}')

send_request_to_google()



def send_fx_request(url=''):
    response = requests.get(f'https://api.exchangeratesapi.io/latest{url}')
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f'Something went wrong: {response.status_code}')

send_fx_request('?base=AUD')

