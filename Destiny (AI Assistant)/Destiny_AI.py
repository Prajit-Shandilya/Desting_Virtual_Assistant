from asyncio import tasks
import sys
from sys import maxsize
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import pyautogui
import psutil
from pywikihow import  search_wikihow
import tkinter as tk
import time
import PyPDF2



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir !")

    elif hour>=12 and hour<18:
        speak("good afternoon sir !")  

    else:
        speak("good evening sir !") 

    speak("I am Destiny, Please tell me how may I help you") 
        


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again plz...")
        return "None"
    query = query.lower()
    return query

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f017b6354a9b4f8bae18cba6ba71b95b'

    main_page = requests.get(main_url).json()
    article = main_page['articles']
    head = []
    day = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in article:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is {head[i]}")

def issTracker():
    import urllib.request
    import json
    
    api_url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(api_url)
    object = json.loads(response.read())
    lat = object['iss_position']['latitude']
    lon = object['iss_position']['longitude']

    url = 'https://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(lon) + '#map=3/' + str(lat) + '/' + str(lon)



    webbrowser.open_new(url)

def twilioSender():
    from twilio.rest import Client 
 
    account_sid = 'AC6ec00e5a2c2b4efed794a71b9b79d777' 
    auth_token = '07909a59bf166301151c6e3511d7fa9a' 
    client = Client(account_sid, auth_token) 
    speak('Please type the message sir')
    message = input('Please enter the message:')
    
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body= message,      
                                to='whatsapp:+919508876731' 
                            ) 
    
  
def ReadPdf():
   # Read the PDF file binary mode
    pdf_path= input('Enter the path of the pdf:')
    pdf_file = open(pdf_path, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
    #Find the number of pages in the PDF document
    number_of_pages = read_pdf.getNumPages()
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
    for i in range(0, number_of_pages ):
    # Read the PDF page 
        page = read_pdf.getPage(i)
        
        # Extract the text of the PDF page 
        page_content = page.extractText()
        
        # set the audio speed and volume
        newrate=200
        engine.setProperty('rate', newrate)
        newvolume=200
        engine.setProperty('volume', newvolume)
            
        # say method on the engine that passing input text to be spoken 
        engine.say(page_content) 
        
        # run and wait method to processes the voice commands.  
        engine.runAndWait()

def QrCode():
    import qrcode
    qr = qrcode.QRCode(version= 40, box_size=18,border=6)
    data = input('Please enter the text:')
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill = "black", back_color="aqua")
    img.save("testQR.png")

def pencilArt():
    import numpy as np
    import cv2
    import scipy.ndimage
    import image
    import imageio as ig

    img = input('Enter the url of the image:')


    def rgb2gray(rgb):
        return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

    def dodge(front,back):
        final_sketch = front*255/(255-back)
        final_sketch[final_sketch>255] = 255
        final_sketch[back==255] = 255
        return final_sketch.astype('uint8')


    ss= ig.imread(img)
    gray = rgb2gray(ss)

    i = 255-gray

    blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)
    r = dodge(blur,gray)

    cv2.imwrite('Sketch.png',r)


    

def numTracker():
    import phonenumbers
    from phonenumbers import geocoder
    from phonenumbers import carrier

    speak('Please enter the number to get details')

    number = input('Enter the number to get details:')
    ch_number = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_number, "en"))
    country = geocoder.description_for_number(ch_number, "en")

    service_pro = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_pro,"en"))
    service = carrier.name_for_number(service_pro,"en")

    speak(f"The number is from {country}")
    speak(f"It is provided by {service}")


    

def weather():
    import tkinter as tk
    import requests
    import time
 

    def getWeather(canvas):
        city = textField.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        label1.config(text = final_info)
        label2.config(text = final_data)


    canvas = tk.Tk()
    canvas.geometry("600x500")
    canvas.title("Weather App")
    f = ("poppins", 15, "bold")
    t = ("poppins", 35, "bold")

    textField = tk.Entry(canvas, justify='center', width = 20, font = t)
    textField.pack(pady = 20)
    textField.focus()
    textField.bind('<Return>', getWeather)

    label1 = tk.Label(canvas, font=t)
    label1.pack()
    label2 = tk.Label(canvas, font=f)
    label2.pack()
    canvas.mainloop()  

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand()
        if 'wikipedia' in query:
            speak("Searching wikipedia sir")
            query= query.replace('wikipedia', "")
            results= wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            speak('Opening youtube,please wait sir')
            webbrowser.open_new('youtube.com')

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open_new('google.com')
        
        elif 'my website' in query:
            speak('opening your whtehat website')
            webbrowser.open_new('https://prajitshandilya.whjr.site')

        elif 'expo' in query:
            speak('opening snack dot expo dot IO')
            webbrowser.open_new('https://snack.expo.dev/')
        
        elif 'internet speed' in query:
            speak('checking the internet speed on fast.com')
            webbrowser.open_new('fast.com')

        elif 'github' in query:
            speak('opening your github')
            webbrowser.open_new('github.com')

        elif 'white hat' in query:
            speak('opening whitehat junior')
            webbrowser.open_new('https://code.whitehatjr.com/s/dashboard')

        elif 'amazon' in query:
            speak('opening amazon')
            webbrowser.open_new('amazon.in')

        elif 'play music' in query:
            speak('playing from your music')
            music_dir = 'D:\\MusicForPrajit'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is{time}")

        elif 'visual code studio' in query:
            speak('opening visual studio code')
            Cpath= "C:\\Users\\Girish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Cpath)
        
        elif 'firefox' in query:
            speak('opening firefox browser')
            Fpath= "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(Fpath)

        elif 'telegram' in query:
            speak('opening telegram')
            Tpath= "C:\\Users\\Girish\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(Tpath)

        elif 'thank you' in query or 'thanks' in query:
            speak("Your welcome sir")

        elif 'sorry' in query:
            speak("No problem sir !")

        elif 'good' in query:
            speak("thank you sir")

        elif 'okay' in query or 'ok' in query:
            speak('okay sir')

        elif 'hello' in query:
            speak("Hello sir, nice to meet you")

        elif 'hi' in query:
            speak("Hi sir, nice to meet you")

        elif 'designed' in query:
            speak("I was designed by Prajit Shandilya")
            
        elif 'your name' in query:
            speak("My name is Destiny")

        elif 'nice' in query:
            speak("thank you sir")

        elif 'temperature' in query:
            speak("getting the temperature")
            
            search = "temperature in sasaram"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            print(f"Current {search} is {temp}")
            speak(f"Current {search} is {temp}")

        elif 'how are you' in query:
            speak("I am fine sir")
            print("😊😊")

        elif 'who are you' in query or 'about yourself' in query:
            speak("My name is Destiny and I am your personal assistant. I am the little sister of google assistant. I was designed by Prajit Shandilya in th year 2022. I am designed in python language, as I am designed for Master Hasan Neshat Alam. I can do certain functions in your system, if you want more you have to update me. That's all about me, Thank You!")

        
        elif 'where i am' in query or 'where we are' in query:
            speak('wait, let me check')
            try:
                ipAdd = requests.get('https://api64.ipify.org/').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                region = geo_data['region']
                country = geo_data['country']
                print(f"Sir I am not sure but i think we are in {city} of region {region} of {country}")
                speak(f"Sir I am not sure but i think we are in {city} of region {region} of {country}")
                
            
            except Exception as e:
                speak("Sorry sir, network issue detected, not able to check the location")
                pass

        elif 'screenshot' in query or  'take a screenshot' in query:
            speak('Please tell me the name of screenshot file')
            name = takeCommand().lower()
            speak('Sir, please hold on for few seconds')
            img = pyautogui.screenshot()
            img.save((name)+'.png')
            speak('I am done sir, screenshot is taken and saved to our main folder')

        elif 'how much power left' in query or 'power we have' in query or 'battery' in query:
           
            battery = psutil.sensors_battery()
            percent = battery.percent
            print(f'System have {percent} percent battery')
            speak(f'sir our system have {percent} percent battery')
            
            if percent>=75:
                speak('we have enough power to work sir')
            elif percent>=40 and percent<=75:
                speak('we have the power but you might connect the charger')
            
            elif percent<=39:
                speak('battery is low , connect the charger')

            elif percent <=20:
                speak('Battery is too low , connect the charger fast as the system is going to shutdown')


        elif 'how to do mod' in query or 'how to do mode' in query:
            speak('How to do mode is activated')
            while True:
                speak('please tell me what you want to know')
                how = takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak('How to do mode is deactivated')
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak('sorry sir, not able to find this')


        elif 'mobile camera' in query:
            import urllib.request
            import cv2
            import numpy as np
            import time
            speak('accessing your mobile camera')
            URL = "http://192.168.1.9:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break

            cv2.destroyAllWindows()

        elif 'news' in query:
            speak('Please wait sir, fetching the latest news')
            news()

        elif 'weather' in query:
            speak('Please wait sir, fetching weather details. Weather app is activated, search for the place')
           
            weather()

        elif 'read a PDF' in query or 'read PDF' in query or 'read pdf' in query:
            speak('Enter the path of the pdf file')
            ReadPdf()
        
        elif 'pdf to text' in query or 'PDF to text' in query:
           speak('This feature will be available soon')

        elif 'send a message' in query or 'whatsapp' in query or 'message' in query:
            twilioSender()
            speak('Message sent succesfully sir')

        elif 'Space Station' in query or 'space station' in query:
            speak('Tracking the live position of the ISS')
            issTracker()

        elif 'phone number' in query or 'mobile number' in query:
            numTracker()

        elif 'qr code' in query or 'QR code' in query or 'QR' in query:
            speak('Please enter the text for generating qr code')
            QrCode()
            speak('QR Code generated in our main folder')

        elif 'sketch' in query:
            speak('please enter the url of the image')
            speak('Designing the sketch with artificial pencil')
            pencilArt()
            speak('Done')

            
    
    
if __name__ == "__main__":
    speak("establishing databases")
    speak("connecting to satellite number 92")
    
    while True:
        TaskExecution()
    
      