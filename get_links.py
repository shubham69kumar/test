import requests
import re

# Prompt for URL
url = input('Enter the URL: ')

# Fetch webpage content
response = requests.get(url)
html = response.text

# Extract social links
social_links = re.findall(r'https?://(www\.)?(facebook|linkedin|twitter)\.[a-zA-Z]{2,6}/[^\s"]+', html)

# Extract email
email_matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
email = email_matches[0] if email_matches else 'Email not found'

# Extract contact number
contact_matches = re.findall(r'\+?\(?\d{0,3}\)?[\s\-.]?\d{3}[\s\-.]?\d{3}[\s\-.]?\d{4}', html)
contact = contact_matches[0] if contact_matches else 'Contact not found'

# Display results
print('Social links -')
if social_links:
    for i, link in enumerate(social_links, start=1):
        print(f'{i}. {link}')
else:
    print('No social links found')

print('Email:', email)
print('Contact:', contact)
