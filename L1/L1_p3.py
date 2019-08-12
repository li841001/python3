#https://static.pandateacher.com/Over%20The%20Rainbow.mp3
import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res.content

with open('Rainbow.mp3','wb') as m:
    m.write(music)