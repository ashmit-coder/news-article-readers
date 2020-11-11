import requests
from bs4 import BeautifulSoup
import webbrowser
from gtts import gTTS


# this will edit the link for getting the page you like
def edit( inp ):
    url = "https://inshorts.com/hi/read"
    if(inp.lower() == "0"):
        return url
    else:
        url += inp.lower()
        return url

ip = input("tell me what you want(0 if you wan it to be latest news) ") 
ur = edit(ip)
r =requests.get(ur)
soup = BeautifulSoup(r.text, "html.parser")

#  making and filteriing the soup
a = soup.find_all(itemprop = "articleBody")


gg = str(a)
h = gg.split("</div>")
t =[]
text = ''
for  x in h:
    try:
        y = x.split('<div itemprop="articleBody">')
        
        text = y[1]
        

        t.append(text)
    except Exception as e:
        pass


for x in t:
    text += str(x) + "    " 
 
# making and playing the mp3 
filename = "voice1.mp3"
tts = gTTS(text)
tts.save(filename)
webbrowser.open_new_tab(ur)
import playsound
playsound.playsound("voice1.mp3")