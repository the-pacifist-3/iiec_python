import pyttsx3
import os
import time
import re
from urlextract import URLExtract

def listToString(s):  #function to convert a list to string
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


#voice configuration
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id) 

pyttsx3.speak("hello....,how can i help you ?")
localtime = time.asctime( time.localtime(time.time()) )
while True:
	print("chat with me with your requirements : "  , end='')
	p = input()
	if (("run" in p) or ("execute" in p) or ("launch" in p))  and (("firefox" in p) or ("browser" in p)):
	  pyttsx3.speak("the firefox browser ,  has  been  opened for you.")
	  os.system("firefox")
	elif((("time" in p) and ("what" in p)) or (("tell" in p ) and ("time" in p))):
		pyttsx3.speak("the local time and date is ")
		print("the local time and date is " , localtime)
	elif (("run" in p) or ("launch" in p) or ("execute" in p )) and  (("kate" in p) or (("text" in p) and ("editor" in p))) :
	  pyttsx3.speak("kate text editor ,has been opened for you.")
	  os.system("kate")
	elif ((("open" in p) or ("run" in p) or ("execute" in p))  and (( ("file" in p) and ("manager" in p) ))) :
	  pyttsx3.speak("dolphin file manager , has been launched for you. ")
	  os.system("dolphin")
	elif((('open' in p) or (("go" in p)and ("to" in p)))and (('www.' in p) and (".com" in p))):
		extractor = URLExtract()
		urls = extractor.find_urls(p)
		x = listToString(urls)
		pyttsx3.speak(x + " ,  has been opened in firefox.")
		os.system("firefox " + x)
	elif  ("exit" in p)  or ("quit" in p):
	  pyttsx3.speak("goodbye?!!!!!")
	  break
	else:
	  pyttsx3.speak("i do not understand you..?")
	  print("dont support")

