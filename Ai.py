
import webbrowser
import subprocess
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from lxml import html
def searching(g):
 print(g)
 url="http://google.com/search?q="+g
 webbrowser.open_new_tab(url)
#h.get("www.anon3mou5.ga")
#h.get(command)
#g="Hey jerry rigs everything"
#print(g.encode('utf-8'))
def bing(command):
  command=command.split(' ')
  query='%20'.join(command)
  #print(query)
  req = requests.get('https://www.bing.com/search?q='+query)
  soup = BeautifulSoup(req.text,"html.parser")
  #print(soup)
  soup=soup.prettify(encoding = 'utf-8')
  #print(soup)
  results=[]
  end=0
  while True:
    links=soup.find('href="https://',end+4)
    if(links==-1):
        break
    end=soup.find(' ',links+5)
    link=soup[links+6:end-3]
    results.append(link)
  for i in results:
    print(i)
  webbrowser.open_new(results[0])
  #print(anker)

import time
subprocess.call('say Hello ',shell=True)
time.sleep(1)
from datetime import datetime as dt
tm=str(dt.now().time())
if(int(tm[:2])<13):
  status="It seems Morning now"
  subprocess.call('say ' + status ,shell=True)
elif(int(tm[:2])<16):
  status="It seems Afternoon now"
  subprocess.call('say ' + status,shell=True)
elif(int(tm[:2]<19)):
   status="It seems Evening now"
   subprocess.call('say ' + status,shell=True)
else:
   status="It seems Night now"
   subprocess.call('say '+ status,shell=True)
print(status)
time.sleep(1)

print("Presenting *FUTURA*")
subprocess.call('say Presenting FUTURAA',shell=True)
import time
time.sleep(1)
print("Booting Assistant........")
subprocess.call('say Booting your personal Assistant',shell=True)
time.sleep(1)


print("Rachana how may I help you..........")
subprocess.call('say Rachana how may i assist you',shell=True)
print("........Listening...........")
subprocess.call('say Listening to your precious words',shell=True)
r1=sr.Recognizer()
with sr.Microphone() as source:
try{ 
  audio=r1.listen(source,5000)
command=(r1.recognize_google(audio)).lower()
from googlesearch import search
print("You said:")
print(command.capitalize())
}
catch(Exception e)
{ 
  print("Couldn't catch you up!!!!")
}subprocess.call('say processing your request to'+command,shell=True)
if (command.find('youtube') > 0 and command.find('search') > 0):
   z=command.find('search')
   query=command[(z+6):]
   bing(command)
elif(command.find('search') >= 0):
    z=command.find('search')
    f=command[z+6:]
    searching(f)
elif(command.find('my website') >= 0):
    webbrowser.open_new_tab("http://www.anon3mous.tk")
elif(command.find("open")>=0):
    subprocess.call('open -a '+ command[5:],shell=True)
else:
    bing(command)
   #webbrowser.open_new(j[0])
#webbrowser.open_new_tab("http://youtube.com")
# def searching(g):
#  z=unicode(g,'utf-8')
#  url="http://google.com/search?q="+z
#  webbrowser.open_new_tab(url)
#h.get("www.anon3mou5.ga")
#h.get(command)
#g="Hey jerry rigs everything"
#print(g.encode('utf-8'))