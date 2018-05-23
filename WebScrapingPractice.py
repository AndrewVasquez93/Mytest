from bs4 import BeautifulSoup
import requests
# Gets basic html file.
htmlFile = open("webPage.html")
soup = BeautifulSoup(htmlFile, "lxml")

#print(soup.prettify())
#print(list(soup.children))
print([type(item) for item in list(soup.children)])

html = list(soup.children)[1]
body = list(html.children)[3]
print(list(body.children))
print(list(body.children))

# Get p from list of children.
p = list(body.children)[1]
print(p.get_text())

# Get p by searching through BeautifulSoup object.
x = soup.find_all('p')[0].get_text()
print(x)

# Gets html file for class and ID practice.
page2 = open("class_id_webPage.html")
soup2 = BeautifulSoup(page2, "lxml")

# You can search files for tags by class and id.
print(soup2.find_all('p', class_='outer-text'))
print(soup2.find_all('p', id='first'))

print(soup2.select("html body"))

# Practice searching for specific information.
# This example gets today's weather in San Francisco from a weather forecast page.
weatherPage = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
weatherSoup = BeautifulSoup(weatherPage.content, "lxml")
seven_day = weatherSoup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

# You can treat the Beautiful Soup object like a dict to find the image title name.
img = tonight.find("img")
desc = img['title']
print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

tomorrow = forecast_items[2]
img2 = tomorrow.find("img")
desc2 = img2['title']
print(desc2)
