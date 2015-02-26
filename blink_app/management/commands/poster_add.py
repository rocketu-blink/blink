from django.core.management import BaseCommand
from blink_app.models import Content
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        print page_scrape(args)

def page_scrape(args):

    data = json.loads(open('blink_app/management/commands/posters2000-2014.json').read())
    for i in range(len(data)):
        try:
            title = data[i]['title']
            link = data[i]['link']
            year = int(data[i]['year'])
            movie_temp = Content.objects.get(
                        title=title,
                        release_year=year,
                    )
            movie_temp.poster = link
            print title + " Success"
        except:
            title = data[i]['title']
            print title + " Fail"