## Description

This web crawler is designed to scrape the top ranked 250 movies on imdb. It's a simple crawler that demonstates how you can use scrapy to quickly pull data into an organized manner. This contains all of the files that are needed to activate the spider as well as the outputed csv file that was created from running it. Becasue of the nature of the code, the movies in the csv are not listed exactly as they are on imdb, but the data is still all there. The output of the data file contains the following field for each movie: title, director, mpa rating, length, genre, release date, imdb_rating, vote count, and synopsis.

## Dependencies

This web crawler was created using *scrapy* and uses version 1.6. with python 3.8. For easy use of scrapy use the anaconda distribution. [For windows you can download it at] (https://docs.anaconda.com/anaconda/install/windows/) Once you install the anaconda distribution, you can open an *Anaconda prompt* and then type `conda install scrapy` This will provide you with all the dependencies you should need.

## Instructions

Open a terminal and navigate to the folder with the files. Make sure you have activated the virtual environment that has scrapy and its dependencies. Then type `scrapy crawl best_movies -o top_250_movies.csv` and hit enter. This will scrape the data as well as store it into a csv file for later analysis. Alternatively, you can use the exension `.json` to create a json file instead. This code works as of April 2, 2020.
