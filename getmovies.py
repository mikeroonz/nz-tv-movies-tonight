from html.parser import HTMLParser
import urllib.request

url = urllib.request.urlopen("") #edit this - put in the NZCity TVNow guide webpage
html_as_string = url.read().decode()
url.close()

table_data = html_as_string.split("<t") #table_data is a list of separate lines that were split on the characters "<t"
for this_table_data in table_data: #go over every line doing the following
    if ">Movie:" in this_table_data: #if the line contains info about a movie, do the following (chop up the strings)
        line_split_on_movie = this_table_data.split(">Movie:")[1:]
        line_split_on_font = line_split_on_movie[0].split("font")
        movie_title = line_split_on_font[0][:-2]
        movie_time = line_split_on_font[3][9:-3]
        print(movie_time, movie_title)

