import requests

def get_all_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'

    res = requests.get(url)

    data = res.json()
    
    if data['success'] and "data" in data:
        
        print(data["message"])


get_all_user()