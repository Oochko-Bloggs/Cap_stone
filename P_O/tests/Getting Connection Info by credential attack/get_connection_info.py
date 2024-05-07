import urllib.request

# Open a connection to a URL
web_url = urllib.request.urlopen('http://192.168.0.1')

# Get the result code and print it
print(f"Result code: {web_url.getcode()}")

# Read the data from the URL and print it
data = web_url.read()
print(data)

