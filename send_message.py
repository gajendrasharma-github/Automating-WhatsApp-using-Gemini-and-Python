import google.generativeai as genai

genai.configure(api_key="you can put your own api key here")


def generate_message(name, description, task):
    prompt = f'''
    You are an empathetic WhatsApp assistant. Craft a personalized message to {name} for the task "{task}". 
    Make it personalized using their trait and description which is: "{description}"

    Message should feel personal and align with their nature. Moreover, you should not sound like a robot. 
    You should sound like human. There should be an empathy even in a order or command.

    If content is lengthy, break sentences and give a line space to ensure maximum readability. Most of them will read on mobile.
    So make sure it is not a single paragraph but a well formatted one. 
        
    NOTE: 1. Just give the description. No other stuffs like "Here's your response"  or " Do you want me to do anything else" etc.
    2. Use simple english. The work should be communicated well not the jargon.
    3. Also, use a mix of English and Hindi. Eg: Socha Tumhe project ke bare me bata dun. So I am working on a project"
    4. Don't be too clingy.

    '''
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()



import gspread

gc = gspread.service_account(filename="whatsapp-messaging.json")
sheet = gc.open("Contacts").sheet1
data = sheet.get_all_records()


import pywhatkit as kit
import datetime
import time

task = "I am trying automating whatsapp using Python and Gemini and you are a part of my experiment XD. This message you're receving, that means my experiment is successful."

now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1

base_time = datetime.datetime.now() + datetime.timedelta(minutes=2)

for index, row in enumerate(data):
    name = row["Name"]
    number = "+91" + str(row["Number"])
    description = row["Description"]

    
    message = generate_message(name, description, task)
    print(f"\n📤 Sending to {name}: \n{message}\n")

    
    send_time = base_time + datetime.timedelta(minutes=index)
    hour = send_time.hour
    minute = send_time.minute

    try:
        kit.sendwhatmsg(number, message, hour, minute, wait_time=15, tab_close=True)
        print(f" Successfully scheduled for {name}")
    except Exception as e:
        print(f" Error sending to {name}: {e}")
