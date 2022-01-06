import requests
import json
import csv
from tqdm import tqdm

#def movies_from_db():
#    with open("movies_yts.csv",'w') as file:
#        writer = csv.writer(file, delimiter=',')
#        writer.writerow(["Title","Plot","Genres"]) #header
#
#        for i in tqdm(range(35000)):
#            res = requests.get("https://yts.mx/api/v2/movie_details.json?movie_id={i}")
#            data = json.loads(res.content)
#            if data['status'] == 'ok':
#                movie = data['data']['movie']
#                plot = movie['description_intro']
#                title = movie['title_long']
#                genres = movie['genres']
#                writer.writerow([title,plot,genres])


def get_movies_by_list():
    with open("original_movie_plots_yts.csv",'w',newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Title","Plot","Genres"]) #header

        
        for i in tqdm(range(7500)):
            res = requests.get("https://yts.mx/api/v2/list_movies.json?limit=50&page={}".format(i))
            data = json.loads(res.content)
            status = data['status']
            if status == 'ok':
                movies = data['data']['movies']
                try:
                    for i in range(len(movies)):
                        if all(lab in movies[i].keys() for lab in ['title','genres','summary']):
                            title = movies[i]['title']
                            genres = movies[i]['genres']
                            plot = movies[i]['summary']
                            writer.writerow([title,plot,genres])
                except:
                    continue                    
    


get_movies_by_list()




