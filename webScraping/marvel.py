import requests
from bs4 import BeautifulSoup
import pprint
import os
import json

main_url = "https://www.imdb.com/superheroes/all-marvel-movies-in-order/ls020525837/"
main_page = requests.get(main_url)
main_soup = BeautifulSoup(main_page.text, "html.parser")

def get_movies_list():
    
    movie_names = []
    released_on = []
    ratings = []
    movie_urls = []
    movie_runtime = []
    movie_genre = []
    lister_list = main_soup.find("div", class_ = "lister-list")
    all_content_list = lister_list.find_all("div", class_ = "lister-item mode-detail")
    # appending movie names in movie_names list
    for div in all_content_list:
        movie = div.find("div", class_ = "lister-item-content").h3.a.get_text()
        movie_names.append(movie)

    # appending movie release year in realsed_on list
        h3 = div.find("h3", class_ = "lister-item-header")
        span = h3.find("span", class_ = "lister-item-year text-muted unbold").get_text().strip()
        year = span[1:5]
        released_on.append(year)

    # extracting rating from each movie
        rating = div.find("div", class_ = "ratings-bar").strong.get_text()
        ratings.append(rating)
    
    # extracting links of each movie 
        url = div.find("div", class_ = "lister-item-content").h3.a['href']
        link = "https://www.imdb.com"+str(url)
        movie_urls.append(link)

    # time duration of the movie
        item = div.find("p", class_ = "text-muted text-small")
        runtime = item.find("span", class_ = "runtime").get_text().strip()
        minutes = runtime[:3]
        movie_runtime.append(minutes)
    # finding genres of the movies
        genre_span = item.find("span", class_ = "genre").get_text().strip()
        genre_string = genre_span.replace(" ", "")
        genre_list = genre_string.split(",")
        movie_genre.append(genre_list)

    # creating a dictionary to collect the above information
    list_of_Marvel_details = []
    for movie_index in range(len(all_content_list)):
        all_details = {"Name":"", "Year of Release":"", "Rating":"", "URL":"", "Runtime":"", "Genre":[]}
        all_details["Name"] = movie_names[movie_index]
        all_details["Year of Release"] = released_on[movie_index]
        all_details["Rating"] = ratings[movie_index]
        all_details["URL"] = movie_urls[movie_index]
        all_details["Runtime"] = movie_runtime[movie_index]
        all_details["Genre"] = movie_genre[movie_index]
        list_of_Marvel_details.append(all_details)

    return list_of_Marvel_details

def selectMovie(url):
    movie_page = requests.get(url)
    movie_soup = BeautifulSoup(movie_page.text, "html.parser")

    summary = movie_soup.find("div", class_ = "ipc-html-content ipc-html-content--base")



def backup(data, file_name):
    raw_data = json.dumps(data)
    with open("marvel/data/jsons/"+file_name, 'w') as f:
        f.write(raw_data)
    print("done")
    # json_name=''
    # for cache in url[27:]:
    #     if '/' not in cache:
    #         json_name +=cache
    #     else:
    #         file = json_name+'json'
    #         break
    
    # data = None
    # if os.path.exists('marvel/data/jsons'+json_name):
    #     file = open("marvel/data/jsons"+json_name)
    #     data = file.read()
    #     file.close()
    #     return data
    # if data == None:
    #     return get_movies()


details = get_movies_list()
pprint.pprint(selectMovie(details[0]["URL"]))