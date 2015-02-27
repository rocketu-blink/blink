from django.core.management import BaseCommand
from blink_app.models import Content
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        print get_content(args)


def get_content(args):
    count_skip = 0
    count_update = 0
    for x in range(1, 25):
        link_data = requests.get("http://amazon.instantwatcher.com/search?page=" +str(x) +"&prime=1#top-pagination")
        data = link_data.text
        soup = BeautifulSoup(data)
        link = soup.find_all("a", class_="title-in-list")

        for link in soup.find_all("a", class_="title-in-list"):
            try:
                title = link.text
                movie_page = link["href"]
                movie_page_data = requests.get("http://amazon.instantwatcher.com" + movie_page)
                movie_data = movie_page_data.text
                movie_soup = BeautifulSoup(movie_data)
                movie_temp = Content.objects.get(
                    title=link.text,
                    release_year=movie_soup.find("a", class_="detail-year").text,
                )
                prime_url = movie_soup.find("span", class_="license-kind").find("a")['href'][:44]
                movie_temp.prime_url = prime_url
                movie_temp.save()
                # try:
                #     link =
                #     print link
                # except:
                #     print "error in link@@@@@@@@@@@@@@@@@@@@@@"
                # try:
                #     imdb = movie_soup.find("a", "imdb-link")["href"][22:]
                #     print imdb
                # except:
                #     print "error in imdb@@@@@@@@@@@@@@@@@@@@"
                #
                # movie_temp[0].prime_url.add(link)
                print title + " = Updated!"
                count_update += 1
            except:
                title = link.text
                print title + " = Skipped..."
                count_skip += 1
    print "======================================"
    print "===        Process Complete        ==="
    print "======================================"
    print str(count_update + count_skip) + " items viewed"
    print str(count_update) + " items updated"
    print str(count_skip) + " items skipped"