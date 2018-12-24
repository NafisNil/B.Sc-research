import wikipedia
import wolframalpha
import webbrowser

while True:
    my_input = input("Question: ")
	
    if 'open reddit' in my_input:
        webbrowser.open("https://www.reddit.com/")
    if 'open youtube' in my_input:
        webbrowser.open("https://www.youtube.com/")
    if 'open facebook' in my_input:
        webbrowser.open("https://www.facebook.com/")
    if 'open twitter' in my_input:
        webbrowser.open("https://www.twitter.com/")
    if 'open quora' in my_input:
        webbrowser.open("https://www.quora.com/")
		
    try:
        #wolframalpha code here
        app_id = "Q2HXJ5-GYYYX6PYYP"

        #let's call our app id
        client = wolframalpha.Client(app_id)
        res = client.query(my_input)
        answer = next(res.results).text 

        print(answer)

    except:
        #wikipedia
        print(wikipedia.summary(my_input)) 
