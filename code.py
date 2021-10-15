import csv
import time
import datetime

def strftime(timestamp, format_string='%Y'):
    return datetime.datetime.fromtimestamp(timestamp).year

userId = []
movieId = []
genres = []
nolink_movie = []
rating_pnum = []

with open('./ml-25m/tags.csv',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for line in reader:       
        user = line['userId']
        movie = line['movieId']
        userId.append(user)
        movieId.append(movie)
print("tags表处理完成...")

with open('./ml-25m/ratings.csv',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for line in reader:       
        user = line['userId']
        movie = line['movieId']
        userId.append(user)
        movieId.append(movie)
        if strftime(int(line['timestamp'])) == 2018:
            rate_user = line['userId']
            rating_pnum.append(rate_user)
print("ratings表处理完成...")      

with open('./ml-25m/movies.csv',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for line in reader:       
        movie = line['movieId']
        gen = line['genres']
        movieId.append(movie)
        genres= genres+line['genres'].split('|')
print("movies表处理完成...")   

with open('./ml-25m/links.csv',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for line in reader:       
        movie = line['movieId']
        movieId.append(movie)
        if line['imdbId']=='' and line['tmdbId']==2018:
            nolink = line['movieId']
            nolink_movie.append(nolink)
print("links表处理完成...")    

with open('./ml-25m/genome-scores.csv',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for line in reader:       
        movie = line['movieId']
        movieId.append(movie)
print("genome-scores表处理完成...")  

print('=================================结果如下=====================================')
print("一共有{}个不同的用户".format(len(set(userId))))
print("一共有{}个不同的电影".format(len(set(movieId))))
print("一共有{}个不同的电影种类".format(len(set(genres))))
print("一共有{}个电影没有外部链接".format(len(set(nolink_movie))))
print("2018年一共有{}人进行过电影评分".format(len(set(rating_pnum))))
