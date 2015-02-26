from bs4 import BeautifulSoup
import requests


count_skip = 0
count_update = 0
link_data = requests.get("http://www.hulu.com/movies/all")
data = link_data.text

soup = BeautifulSoup(data)

for links in soup.find("a", text="Ghostbusters"):
        title = links.text
        hulu_url = links["href"]
        print hulu_url

        try:
            movie_temp = Content.objects.get(
                    title=title,
                )
            print movie_temp
            # movie_temp.hulu_url = hulu_url
            # movie_temp.save()
            print title + " = Updated!"
            count_update += 1
            pass
        except:
            print title + " = Skipped..."
            count_skip += 1
        break

print "======================================"
print "===        Process Complete        ==="
print "======================================"
print str(count_update + count_skip) + " items viewed"
print str(count_update) + " items updated"
print str(count_skip) + " items skipped"