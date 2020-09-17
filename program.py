import requests
def speak(str):
    from win32com.client import Dispatch

    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    print("enter 1 for business news")
    print("enter 2 for entertainment news")   
    print("enter 3 for health news")
    print("enter 4 for science news")
    print("enter 5 for sports news")
    print("enter 6 for technology news")
    choice=int(input)
    if(choice==1):
        response = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxx')
    if(choice==2):
        response = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=xxxxxxxxxxxxxxxxxxxxxxx')
    if(choice==3):
        response = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    if(choice==4):
        response = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    if(choice==5):
        response = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    if(choice==6):
        response = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    

    res=response.text
    res2=res
    title=[]
    description=[]
    i=1
    for a in res2:
        x = res.split('"title"')[i]
        sentence=f"news number {i} "
        c=0
        for ch in x:
            if ch=='"':
                c=c+1
                continue
            if c==1:
                sentence=sentence+ch
            if c==2:
                break
        title.append(sentence)
        i=i+1
        if(i==21):
            break
    i=1
    for a in res2:
        x = res.split('"description"')[i]
        sentence=""
        c=0
        for ch in x:
            if ch=='"':
                c=c+1
                continue
            if c==1:
                sentence=sentence+ch
            if c==2:
                break
        description.append(sentence)
        i=i+1
        if(i==21):
            break
    
    for i,char in enumerate(title):

        speak(title[i])
        if(description[i]!="url"):
            speak(description[i])
