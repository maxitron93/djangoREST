import requests

def client():
    credentials = {
        'username': 'maxitron',
        'password': 'dummypass'
    }

    response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    print(f'Status Code: {response.status_code}')
    response_data = response.json()
    print(response_data)

client()
