name = input("Enter your name : ")
age = input("Enter your age : ")
fav_movies = input("Enter your favorite movies seperated by comma : ").split(",")
fav_songs = input("Enter your fav_songs seperated by comma : ").split(",")
user = {}

user['name'] = name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs

for key,val in user.items():
    print(f"{key} : {val}")