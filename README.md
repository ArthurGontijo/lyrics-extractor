# Lyrics Extractor
### Python Lyrics Webscrapper  

## About
This python script receives an artist name as input, search for this artist on the website [AZLyrics](https://www.azlyrics.com/) and then generates a txt file containing all the lyrics from this artists. This script can be usefull for data science projects that analizes music lyrics.

## Instalation and Usage
First of all, clone this repository using: <br>
```
git clone https://github.com/ArthurGontijo/lyrics-extractor
```
<br>

Then, install the requirements using: <br>
```
pip install -r requirements.txt
``` 
<br>
Now, execute the file called **webscrapper.py** it will ask you the name of the artist and then will start saving the lyrics in a txt file named **lyrics.txt**

## Warning
Unfortunately the extraction process is somehow slow because there is a five seconds delay between each request, otherwise the site's anti-bot system would trigger and block your ip adress from doing further requests.  
