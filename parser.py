import requests
from bs4 import BeautifulSoup


req = requests.get("http://www.zepetotime.com/booths/")

html = req.text

soup = BeautifulSoup(html, 'html.parser')

photos = soup.select(
	'body > table > tbody > tr'
)

# booth_ids = soup.select(
# 	'body > table > tbody > tr:nth-child(1) > td:nth-child(5)'
# )

# max_user_counts = soup.select(
# 	'body > table > tbody > tr:nth-child(1) > td:nth-child(3)'
# )

data = []

for photo in photos:
	tds = photo.find_all('td')
	if tds[2].text == "1":
		data.append(tds[4].text)

result_data = ",".join(data)
print(result_data)