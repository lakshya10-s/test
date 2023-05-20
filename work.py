import csv

movies = [[1,"The Shawshank Redemption",9.2,1994],
[2,"The Godfather",9.2,1972],
[3,"The Dark Knight",9.0,2008],
[4,"12 Angry Men",9.0,1957],
[5,"The Godfather Part II",9.0,1974],
[6,"Schindler List",8.9,1993]]

def write_movies_to_csv(movies):
	with open ('movies.csv', mode='w', newline="")as file:
		writer = csv.write(file)
		writer = csv.writer(file)
		writer.writerow(['id','name','rating','year'])
		for movies in movies:
			write.writerow(movies)



