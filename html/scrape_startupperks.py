import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.startupperks.xyz'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Save the HTML to a file
    with open('/var/www/seatospace.com/html/index.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    
    # Download CSS and JS files
    for link in soup.find_all('link'):
        if link.get('href'):
            asset_url = link['href'] if link['href'].startswith('http') else f'https://www.startupperks.xyz{link["href"]}'
            asset_response = requests.get(asset_url)
            asset_name = asset_url.split('/')[-1]
            with open(f'/var/www/seatospace.com/html/{asset_name}', 'wb') as asset_file:
                asset_file.write(asset_response.content)

    for script in soup.find_all('script'):
        if script.get('src'):
            script_url = script['src'] if script['src'].startswith('http') else f'https://www.startupperks.xyz{script["src"]}'
            script_response = requests.get(script_url)
            script_name = script_url.split('/')[-1]
            with open(f'/var/www/seatospace.com/html/{script_name}', 'wb') as script_file:
                script_file.write(script_response.content)
    
    print("Page scraped and assets saved successfully.")
else:
    print("Failed to retrieve the page.")