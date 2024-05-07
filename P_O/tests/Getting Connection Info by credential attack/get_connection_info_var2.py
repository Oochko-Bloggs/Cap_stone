from selenium import webdriver
from selenium .webdriver.chrome.service import Service

# Initialize a Chrome browser
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('http://192.168.0.1/login')

# Find the username and password fields by their HTML attributes (e.g., name, id)
username_field = driver.find_element_by_name('username')
password_field = driver.find_element_by_name('passwd')

# Enter your credentials
username_field.send_keys('admin')
password_field.send_keys('admin')

# Submit the form (e.g., click the login button)
login_button = driver.find_element_by_id('login-button')
login_button.click()

# Now you're logged in!
response = driver.get('http://192.168.0.1')
print(response)
