from bs4 import BeautifulSoup
import requests
from blink_app.models import Content


count_skip = 0
count_update = 0

for x in range(1,325):
    link_data = requests.get("http://instantwatcher.com/titles/all/" + str(x) + "/")
    data = link_data.text

    soup = BeautifulSoup(data)

    for title in soup.find_all("a", class_="title-list-item-link title-detail-link"):
        name = title.text
        href = title["href"]
        movie_link = requests.get("http://instantwatcher.com" + href)
        movie_data = movie_link.text
        movie_soup = BeautifulSoup(movie_data)
        netflix =  movie_soup.find("a", href=True,text="Netflix page")['href']
        year1 = movie_soup.find("span", class_="infodata")
        year = year1.find("a").text
        try:
            movie_temp = Content.objects.get(
                    title=name,
                    release_year=year,
                )
            movie_temp.netflix_url = netflix
            movie_temp.save()
            print "Updated: " + name
            count_update += 1
        except:
            print "Skipped: " + name
            count_skip += 1

print "======================================"
print "===        Process Complete        ==="
print "======================================"
print str(count_update + count_skip) + " items viewed"
print str(count_update) + " items updated"
print str(count_skip) + " items skipped"