import requests

# Make a GET request to a URL
url = 'http://192.168.0.1'
values = {'username': 'admin',
          'password': 'admin'}

response=requests.get(url)
if response.status_code == 200:
    print(f"Content from {url}:\n{response.text}")
else:
    print(f"Error: {response.status_code}")

response = requests.post(url, data=values)
print(response.content)

