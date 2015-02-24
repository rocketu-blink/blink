import datetime
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests, re
from blink_app.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        print page_scrape(args)

def page_scrape(args):

    page_num = 1
    while page_num < 315536:

        url="http://www.imdb.com/search/title?sort=moviemeter,asc&start=" + str(page_num) + "&title_type=feature"
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        for link in soup.find_all('a'):
            url = str(link.get('href'))
            title = link.get('title')
            if url[0:7] == '/title/':
                try:
                    title = str(title)
                    if 'TV Series' in title or 'Mini-Series' in title or 'Short Film' in title or 'Documentary' in title or 'TV Movie' in title or 'Video' in title:
                        pass
                    elif '(' in title:
                        # Get soup
                        page_url = 'http://www.imdb.com' + url
                        page_r = requests.get(page_url)
                        page_soup = BeautifulSoup(page_r.content)
                        budget_url = page_url + 'business'
                        budget_r = requests.get(budget_url)
                        budget_soup = BeautifulSoup(budget_r.content)
                        keyword_url = page_url + 'keywords'
                        keyword_r = requests.get(keyword_url)
                        keyword_soup = BeautifulSoup(keyword_r.content)

                        #Grab Movie Data
                        title = page_soup.find(itemprop="name").text
                        try:
                            release_year = int(page_soup.find(itemprop="datePublished")['content'][:4])
                            release_month = int(page_soup.find(itemprop="datePublished")['content'][5:7])
                            release_day = int(page_soup.find(itemprop="datePublished")['content'][8:10])
                            release_date = datetime.date(release_year,release_month,release_day)
                        except:
                            release_year = 2000
                            release_date = datetime.date(2000,01,01)

                        try:
                            runtime_str = page_soup.find('time', itemprop="duration").text.strip()
                            runtime_list = [int(s) for s in runtime_str.split() if s.isdigit()]
                            runtime = int(runtime_list[0])
                        except:
                            runtime = 0

                        try:
                            mpaa_rating = page_soup.find(itemprop="contentRating")['content']
                        except:
                            mpaa_rating = 'Null'

                        try:
                            imdb_rating = page_soup.find('span',itemprop="ratingValue").text
                        except:
                            imdb_rating = 0.0

                        try:
                            synopsis = page_soup.find('p',itemprop="description").text.strip()
                        except:
                            synopsis = 'Data Missing'
                        # budget = int(re.sub("[^0-9]", "", budget_soup.find('div', id="tn15content").text.strip()[7:27]))
                        # try:
                        #     revenue_end = budget_soup.find('div', id="tn15content").text.strip().index('Worldwide')
                        #     revenue_str = budget_soup.find('div', id="tn15content").text.strip()[revenue_end - 15:revenue_end]
                        #     revenue_start = revenue_end - 15 + revenue_str.index("$")
                        # except ValueError:
                        #     try:
                        #         revenue_end = budget_soup.find('div', id="tn15content").text.strip().index('worldwide')
                        #         revenue_str = budget_soup.find('div', id="tn15content").text.strip()[revenue_end - 15:revenue_end]
                        #         revenue_start = revenue_end - 15 + revenue_str.index("$")
                        #     except ValueError:
                        #         pass
                        # revenue = int(re.sub("[^0-9]", "", budget_soup.find('div', id="tn15content").text.strip()[revenue_start:revenue_end]))
                        imdb_id = url[len(url)-10:len(url)-1]
                        imdb_url = page_url

                        #Create Movie Data
                        content_qs = Content.objects.get_or_create(title=title,
                                               release_date=release_date,
                                               release_year=release_year,
                                               runtime=runtime,
                                               mpaa_rating=mpaa_rating,
                                               # budget=budget,
                                               # revenue=revenue,
                                               synopsis=synopsis,
                                               imdb_rating=imdb_rating,
                                               imdb_id=imdb_id,
                                               imdb_url=imdb_url,
                                               )

                        #Create/Grab ContentType
                        name = 'movie'
                        content_type_qs = ContentType.objects.get_or_create(name=name)
                        content_qs[0].content_type = content_type_qs[0]

                        #Grab Genre Data
                        genres = []
                        for genre in page_soup.find_all('span', itemprop="genre"):
                            genre_temp = Genre.objects.get_or_create(name=genre.text)
                            genres.append(genre_temp[0])
                        #Connect Content to Genres
                        content_qs[0].genre.add(*genres)

                        #Grab Director Data
                        directors = []
                        for director in page_soup.find_all('div', itemprop="director"):
                            name = director.find('a').text
                            imdb_id = director.find('a')['href'][6:15]
                            imdb_url = 'http://www.imdb.com' + director.find('a')['href'][:16]

                            director_qs = Person.objects.get_or_create(name=name,
                                                                    imdb_id=imdb_id,
                                                                    imdb_url=imdb_url,
                                                                    )

                            directors.append(director_qs[0])

                            #Create/Grab PersonType
                            person_type = []
                            name = 'director'
                            person_type_qs = PersonType.objects.get_or_create(name=name)
                            person_type.append(person_type_qs[0])
                            director_qs[0].type.add(*person_type)

                        #Connect Content to Director
                        content_qs[0].director.add(*directors)

                        #Grab Writer Data
                        writers = []
                        for writer in page_soup.find_all('div', itemprop="creator"):
                            name = writer.find('a').text
                            imdb_id = writer.find('a')['href'][6:15]
                            imdb_url = 'http://www.imdb.com' + writer.find('a')['href'][:16]
                            type = PersonType.objects.get_or_create(name="writer")

                            writer_qs = Person.objects.get_or_create(name=name,
                                                                    imdb_id=imdb_id,
                                                                    imdb_url=imdb_url,
                                                                    )

                            writers.append(writer_qs[0])

                            #Create/Grab PersonType
                            person_type = []
                            name = 'writer'
                            person_type_qs = PersonType.objects.get_or_create(name=name)
                            person_type.append(person_type_qs[0])
                            writer_qs[0].type.add(*person_type)

                        #Connect Content to Director
                        content_qs[0].writer.add(*writers)

                        #Grab Actor/Character Data
                        for actor_even in page_soup.find_all('tr', 'even'):
                            if actor_even.find('td', itemprop="actor") != None:
                                #Create Actor
                                actor_name = actor_even.find('td', itemprop="actor").find('span').text
                                actor_imdb_id = actor_even.find('td', itemprop="actor").find('a')['href'][6:15]
                                actor_imdb_url = 'http://www.imdb.com' + actor_even.find('td', itemprop="actor").find('a')['href'][:16]

                                actor_qs = Person.objects.get_or_create(name=actor_name,
                                                                    imdb_id=actor_imdb_id,
                                                                    imdb_url=actor_imdb_url,
                                                                    )

                                #Create/Grab PersonType
                                person_type = []
                                name = 'actor'
                                person_type_qs = PersonType.objects.get_or_create(name=name)
                                person_type.append(person_type_qs[0])
                                actor_qs[0].type.add(*person_type)

                                #Create Character
                                try:
                                    character_type =[]
                                    character_name = actor_even.find('td', class_="character").find('a').text
                                    character_imdb_id = actor_even.find('td', class_="character").find('a')['href'][11:20]
                                    character_imdb_url = 'http://www.imdb.com' + actor_even.find('td', class_="character").find('a')['href'][:21]
                                    character_qs = Character.objects.get_or_create(name=character_name,
                                                                                imdb_id=character_imdb_id,
                                                                                imdb_url=character_imdb_url,
                                                                                )
                                    character_type.append(character_qs[0])
                                    #Connect to Actor
                                    actor_type = []
                                    actor_type.append(actor_qs[0])
                                    character_qs[0].actor.add(*actor_type)
                                    content_qs[0].characters.add(*character_type)



                                except AttributeError:
                                    pass
                            else:
                                pass
                        for actor_odd in page_soup.find_all('tr', 'odd'):
                            if actor_odd.find('td', itemprop="actor") != None:
                                #Creator Actor
                                actor_name = actor_odd.find('td', itemprop="actor").find('span').text
                                actor_imdb_id = actor_odd.find('td', itemprop="actor").find('a')['href'][6:15]
                                actor_imdb_url = 'http://www.imdb.com' + actor_odd.find('td', itemprop="actor").find('a')['href'][:16]

                                actor_qs = Person.objects.get_or_create(name=actor_name,
                                                                    imdb_id=actor_imdb_id,
                                                                    imdb_url=actor_imdb_url,
                                                                    )

                                #Create/Grab PersonType
                                person_type = []
                                name = 'actor'
                                person_type_qs = PersonType.objects.get_or_create(name=name)
                                person_type.append(person_type_qs[0])
                                actor_qs[0].type.add(*person_type)

                                #Create Character
                                try:
                                    character_type =[]
                                    character_name = actor_odd.find('td', class_="character").find('a').text
                                    character_imdb_id = actor_odd.find('td', class_="character").find('a')['href'][11:20]
                                    character_imdb_url = 'http://www.imdb.com' + actor_odd.find('td', class_="character").find('a')['href'][:21]
                                    character_qs = Character.objects.get_or_create(name=character_name,
                                                                                imdb_id=character_imdb_id,
                                                                                imdb_url=character_imdb_url,
                                                                                )

                                    character_type.append(character_qs[0])
                                    #Connect to Actor
                                    actor_type = []
                                    actor_type.append(actor_qs[0])
                                    character_qs[0].actor.add(*actor_type)
                                    content_qs[0].characters.add(*character_type)

                                except AttributeError:
                                    pass
                            else:
                                pass

                        # Grab Keyword Data
                        keywords = []
                        for keyword in keyword_soup.find_all('div', class_="sodatext"):
                            keyword_qs = Keyword.objects.get_or_create(name=keyword.find('a').text)
                            keywords.append(keyword_qs[0])
                        #Connect Content to Genres
                        content_qs[0].keywords.add(*keywords)

                        print content_qs[0].title + ' = Done!'
                        content_qs[0].save()

                except UnicodeEncodeError:
                    pass
        page_num += 50
