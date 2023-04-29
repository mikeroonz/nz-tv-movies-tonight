from html.parser import HTMLParser
import urllib.request

url = urllib.request.urlopen("https://") #edit this - put the nzcity tvnow guide webpage
html = url.read().decode()
url.close()

class Parse(HTMLParser):
    data_is_movie = False
    movie_info = []

    def __init(self):
        super().__init__()
        self.reset()

    def handle_data(self, data):
        if "Movie" in data:
            self.data_is_movie = True
        if self.data_is_movie:
            self.movie_info.append(data)

    def handle_endtag(self, tag):
        if tag == "td":
            if self.data_is_movie:
                print(self.movie_info)
                self.data_is_movie = False
                self.movie_info.clear()

testParser = Parse()
testParser.feed(html)
