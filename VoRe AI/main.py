""" 
    Developed By      : Carlos T.
    Contributed By    : Zharfan D.S., Rhenal Z.M.W., Kevin C.
    A L.T.A.I. Project 2020 modified prototype for university AI project. This project is protected with Apache License.
    Version 1.7
    -------------------------------------------------------- Imports --------------------------------------------------------------"""
import os                                       # For auto-install, auto-update, auto-uninstall, debugging and logging.

# Automatic Install, upgrade or downgrade libraries to the specified stable versions.
# When all libraries are installed and met the requirements, the os commands below will be skipped!
os.system("pip install -r requirements.txt")
os.system("cls")

import time                                     # To get system time.
import json                                     # Allowing JSON dictionary functionality.
import requests                                 # gTTS is an online API and requires requesting.
import random                                   # Allow unique outputs.
import playsound                                # Plays audio files within the script.
import threading                                # Keeps responsiveness of the program.
from tkinter import *                           # Tkinter stuffs.
from tkinter import font
from tkinter import ttk
import speech_recognition as sr                 # Speech recognition library.
from gtts import gTTS                           # Text to speech library by Google.
""" -------------------------------------------------------- Globals ----------------------------------------------------------------"""
# Strings
message_time = "[" + time.strftime("%d/%m/%Y %H:%M") + "]"
left = LEFT
normal = NORMAL
active = ACTIVE
garis = "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"
voreico = 'VoReAIicon.ico'

# Integers
chicken_price = 30000
beef_price = 25000
coffee_price = 5000
x = 7000

# Booleans
voice = False

# Dictionaries
with open("brain.json", "r") as b:
    brain = json.load(b)
    
""" --------------------------------------- Voice Recognition and Text To Speech Constructors ---------------------------------------"""
def speak(text):
    tts = gTTS(text=text, lang="en")
    date_string = time.strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    tts.save(filename)
    sound_thread = threading.Thread(target=lambda:playsound.playsound(filename))
    sound_thread.start()
    
def get_audio():
    global voice 
    voice = True
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        said = r.recognize_google(audio)
            
    return said
    
""" -------------------------------------------------------- GUI Constructors -------------------------------------------------------"""
# Constructing the GUI skeletons
root = Tk()
root.title("VoRe AI")
root.configure(bg='#212121')
root.geometry("1200x600")
root.iconbitmap(voreico)

segoeNormal = font.Font(family="Orbitron")
segoeNormal.config(size=10)
segoeBold = font.Font(family="Orbitron", weight="bold")
segoeBold.config(size=25)

# Construct and configure tabs
tabParent = ttk.Notebook(root)
tab0 = Frame(tabParent)     # Tab for Homepage
tabMenu = Frame(tabParent)  # Tab for Food Menu
tab1 = Frame(tabParent)     # Tab for Ordering Food
tab2 = Frame(tabParent)     # Tab for Removing Orders
tab3 = Frame(tabParent)     # Tab for Listing Orders
tab4 = Frame(tabParent)     # Tab for User Profile
tabParent.add(tab0, text="Interactive Chat")
tabParent.add(tabMenu, text="Food Menu")
tabParent.add(tab1, text="Order Food")
tabParent.add(tab2, text="Remove Orders")
tabParent.add(tab3, text="List Orders")
tabParent.add(tab4, text="Payment")

tabParent.pack(expand=1, fill="both")

tab0.configure(bg="#212121")
tabMenu.configure(bg="#212121")
tab1.configure(bg="#212121")
tab2.configure(bg="#212121")
tab3.configure(bg="#212121")
tab4.configure(bg="#212121")
""" --------------------------------------------------- Tab 0 Contents Constructor ---------------------------------------------------"""
# Tab for ordering food.
tab0.pack_propagate(0) # Prevent Overflowing

# Constructing Frames
tab0_frame1 = Frame(tab0, bg="#212121")
tab0_frame2 = Frame(tab0, bg="#212121")
tab0_frame3 = Frame(tab0, bg="#212121")
tab0_frame1.pack()
tab0_frame2.pack()
tab0_frame3.pack()

def main(que, tab0_label1): # User Interactions
    global voice
    if que.lower() in ['hello', 'hi', 'howdy', 'greetings', 'yo']:
        a = "Hey there!", "Hello there!", "Greetings!", "Howdy partner!", "Yo!", "Hi!", "Hello!", "Hi there!"
        b = random.choice(a)
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['bye-bye', 'bye', 'goodbye', 'good bye', 'bye bye']:
        a = "See you!", "Good bye!", "Bye bye!", "I'll see you next time!", "Alright, good bye!"
        b = random.choice(a)
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['thanks', 'thank you', 'thank you very much', 'I appreciate that', 'that is much appreciated', "that's much appreciated"]:
        a = "You're welcome!", "No problem!", "My pleasure to be of a help!", "Not a problem!", "Glad to help anytime!", "I won't let you down!"
        b = random.choice(a)
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['ok', 'okay', 'allright', 'all right', 'alright', 'yes', 'no']:
        a = "Hmm?", que + " what?", "Okay"
        b = random.choice(a)
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['are you sad?', 'are you sad', 'are you sad ?', 'are you happy?', 'are you happy', 'are you happy ?', 'are you angry?', 'are you angry', 'are you angry ?']:
        a = "I don't have emotions.", "What is sadness?", "I am just an AI.", "I have no capabilities of expressing feelings."
        b = random.choice(a)
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['how are you?', 'how are you today?', 'how are you', 'how are you ?', 'how are you today', 'how are you today ?']:
        a = "I'm always great, thank you!", "I am well.", "I always am ready to serve my users."
        b = random.choice(a)
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)        
    # ---------------------------------------------------------------------------------------------------------------------
    elif que.lower() in ['/?', '/help', 'what are the commands?', 'what are the commands', 'what are the commands ?']:
        b = "You can execute these commands here :"
        c = "\n\n/help ( /? ) \n /order \n /menu \n /intro"
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b + c, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['/order', 'i want to order', 'can i order?', 'can i order', 'can i order ?'] or que == "can I order?" or que == "can I order" or que == "can I order ?" or que == "I want to order":
        b = "To order food, go to the Order Food tab and fill in all of the fields.\nTo remove orders, go to the remove orders tab."
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['/menu', 'show me the menu', 'can i see the menu?', 'can i see the menu ?', 'can i see the menu'] or que == "can I see the menu?" or que == "can I see the menu ?" or que == "can I see the menu":
        b = "You can see the menu in the Food Menu tab!"
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['/intro', '/introduce', 'introduce yourself', 'who are you?', 'who are you ?', 'who are you']:
        b = "My name is VoRe AI created based on Carlos' Rena prototype. My purpose is to serve users as a digitalized waiter for a restaurant or cafe."
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['how much is chicken?', 'how much is chicken', 'how much is chicken ?', 'what is the price of chicken?', 'what is the price of chicken', 'what is the price of chicken ?']:
        b = "The chicken costs IDR. " + chicken_price
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['how much is Beef?', 'how much is Beef', 'how much is Beef ?', 'what is the price of Beef?', 'what is the price of Beef', 'what is the price of Beef ?']:
        b = "The Beef costs IDR. " + beef_price
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    elif que.lower() in ['how much is coffee?', 'how much is coffee', 'how much is coffee ?', 'what is the price of coffee?', 'what is the price of coffee', 'what is the price of coffee ?']:
        b = "The coffee costs IDR. " + coffee_price
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
        speak(b)
    # ---------------------------------------------------------------------------------------------------------------------
    elif que.lower() in ['test']: # For testing only!
        tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : Testing...", font=segoeNormal, bg="#212121", fg="cyan")
        tab0_label2.pack()
    else:
        if voice == False:
            a = "Sorry, I don't understand what you're saying!", "My apologies, but I don't understand your statement!", "I don't get it!", "I can't respond to that at the moment!", "I can't respond to that yet!", "If you are using slangs, I don't speak slangs!"
            b = random.choice(a)
            tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="red")
            tab0_label2.pack()
            speak(b)
        elif voice == True:
            a = "You'll need to speak clearly so that I can hear you better!", "I can't hear you!", "Pardon me, can you please repeat?"
            b = random.choice(a)
            tab0_label2 = Label(tab0_frame3, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="red")
            tab0_label2.pack()
            speak(b)
            voice = False
    
    tab0_label1.after(x, tab0_label1.destroy)    
    tab0_label2.after(x, tab0_label2.destroy)

# Button Events
def btn_submit():
    que = user_input.get()
    tab0_label1 = Label(tab0_frame3, text=message_time + " " + brain["data1"] + " : " + que, font=segoeNormal, bg="#212121", fg="lime")
    tab0_label1.pack()
    
    main(que, tab0_label1)

def btn_voice():
    print("[DEBUG] : Interactive Chat Listening...")
    que = get_audio()
    tab0_label1 = Label(tab0_frame3, text=message_time + " " + brain["data1"] + " : " + que, font=segoeNormal, bg="#212121", fg="lime")
    tab0_label1.pack()
    
    main(que, tab0_label1)
    
Label(tab0_frame1, text=" ", bg="#212121").pack()
Label(tab0_frame1, text="Interactive Chat", font=segoeBold, bg="#212121", fg="cyan").pack()
Label(tab0_frame1, text="Your Message :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left)
user_input = Entry(tab0_frame1, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
user_input.pack(side=left)

Button(tab0_frame1, text="Submit", command=btn_submit, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left, padx=5)
Button(tab0_frame1, text="Voice", command=btn_voice, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left)

Label(tab0_frame2, text=garis, fg="cyan", bg="#212121").pack()
b = "Hello there! How can I help you?"
Label(tab0_frame2, text=message_time + " VoRe : " + b, font=segoeNormal, bg="#212121", fg="cyan").pack()
speak(b)
""" --------------------------------------------------- Tab Menu Contents Constructor ---------------------------------------------------"""
# Tab for food menu.
tabMenu_frame1 = Frame(tabMenu, bg="#212121")
tabMenu_frame1.pack()
Label(tabMenu_frame1, text=" ", bg="#212121").pack()
Label(tabMenu_frame1, text=" ", bg="#212121").pack()
Label(tabMenu_frame1, text="Food Menu", font=segoeBold, bg="#212121", fg="cyan").pack()
Label(tabMenu_frame1, text="This is where you see the menu and price.", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tabMenu_frame1, text=garis, fg="cyan", bg="#212121").pack()
Label(tabMenu_frame1, text="1. chicken (IDR." + str(chicken_price) + ")", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tabMenu_frame1, text="2. Beef (IDR." + str(beef_price) + ")", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tabMenu_frame1, text="3. Coffee (IDR." + str(coffee_price) + ")", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tabMenu_frame1, text=garis, fg="cyan", bg="#212121").pack()
""" --------------------------------------------------- Tab 1 Contents Constructor ---------------------------------------------------"""
# Tab for ordering food.
tab1_frame1 = Frame(tab1, bg="#212121")
tab1_frame2 = Frame(tab1, bg="#212121")
tab1_frame3 = Frame(tab1, bg="#212121")
tab1_frame4 = Frame(tab1, bg="#212121")
tab1_frame5 = Frame(tab1, bg="#212121")
tab1_frame6 = Frame(tab1, bg="#212121")
tab1_frame7 = Frame(tab1, bg="#212121")
tab1_frame1.pack()
tab1_frame2.pack()
tab1_frame3.pack()
tab1_frame4.pack()
tab1_frame5.pack()
tab1_frame6.pack()
tab1_frame7.pack()

def tab1_btn_submit():
    tn = table_number.get()
    fn = food_name.get()
    fq = food_quantity.get()
    
    tab1_label1 = Label(tab1_frame7, text=garis, fg="cyan", bg="#212121")
    tab1_label1.pack()
    if len(tn) != 0 and len(fn) != 0 and len(fq) != 0:
        if fn == "chicken":
            food_name_tn = "chicken" + tn
            food_qty_tn = "chicken" + "_quantity" + tn
            brain[food_name_tn] = "Chicken"
            brain[food_qty_tn] = fq

            tab1_label2 = Label(tab1_frame7, text="✅ Your order is successfully submitted, you can now check your \norders in the List Orders tab.", font=segoeNormal, bg="#212121", fg="cyan")
            tab1_label2.pack()
            speak("Your order is successfully submitted, you can now check your \norders in the List Orders tab.")
        elif fn == "beef":
            food_name_tn = "beef" + tn
            food_qty_tn = "beef" + "_quantity" + tn
            brain[food_name_tn] = "Beef"
            brain[food_qty_tn] = fq

            tab1_label2 = Label(tab1_frame7, text="✅ Your order is successfully submitted, you can now check your \norders in the List Orders tab.", font=segoeNormal, bg="#212121", fg="cyan")
            tab1_label2.pack()
            speak("Your order is successfully submitted, you can now check your \norders in the List Orders tab.")
        elif fn == "coffee":
            food_name_tn = "coffee" + tn
            food_qty_tn = "coffee" + "_quantity" + tn
            brain[food_name_tn] = "Coffee"
            brain[food_qty_tn] = fq

            tab1_label2 = Label(tab1_frame7, text="✅ Your order is successfully submitted, you can now check your \norders in the List Orders tab.", font=segoeNormal, bg="#212121", fg="cyan")
            tab1_label2.pack()
            speak("Your order is successfully submitted, you can now check your \norders in the List Orders tab.")
        else:
            tab1_label2 = Label(tab1_frame7, text="⚠ You can only order chicken, Beef or coffee!", font=segoeNormal, bg="#212121", fg="cyan")
            tab1_label2.pack()
            speak("You can only order Chicken, Beef or Coffee!")
    else:
        tab1_label2 = Label(tab1_frame7, text="⚠️ All fields must be filled! You cannot leave a field or more empty!", font=segoeNormal, bg="#212121", fg="cyan")
        tab1_label2.pack()
        speak("All fields must be filled! You cannot leave a field or more empty!")

    tab1_label3 = Label(tab1_frame7, text=garis, fg="cyan", bg="#212121")
    tab1_label3.pack()
    # Remove the labels after x second(s).
    tab1_label1.after(x, tab1_label1.destroy)
    tab1_label2.after(x, tab1_label2.destroy)
    tab1_label3.after(x, tab1_label3.destroy)

    with open("brain.json", "w") as b:
        json.dump(brain, b, indent=4)

def tab1_btn_voice():
    print("[DEBUG] : Tab1 - Field1 Listening...") 
    speak("What do you want to order?")
    field1 = get_audio()
    food_name.insert(0, field1)
    i = 1
    if i == 1:
        print("[DEBUG] : Tab1 - Field2 Listening...")
        speak("How many do you want to order?")
        field2 = get_audio()
        food_quantity.insert(0, field2)
        i = 2
        if i == 2:
            print("[DEBUG] : Tab1 - Field3 Listening...")
            speak("What is your table number?")
            field3 = get_audio()
            table_number.insert(0, field3)

Label(tab1_frame1, text=" ", bg="#212121").pack()
Label(tab1_frame1, text=" ", bg="#212121").pack()
Label(tab1_frame1, text="Order Food", font=segoeBold, bg="#212121", fg="cyan").pack()
Label(tab1_frame1, text="Fill in the form below and submit to add new order or edit order. Make sure you did not input the \nwrong table number, otherwise other's data will be overridden!", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tab1_frame1, text=garis, fg="cyan", bg="#212121").pack()

Label(tab1_frame2, text="Food Name :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left, padx=9)
food_name = Entry(tab1_frame2, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
food_name.pack(side=left)

Label(tab1_frame3, text="Food Quantity :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left)
food_quantity = Entry(tab1_frame3, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
food_quantity.pack(side=left)

Label(tab1_frame4, text="Table Number :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left)
table_number = Entry(tab1_frame4, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
table_number.pack(side=left)

Label(tab1_frame5, text=garis, fg="cyan", bg="#212121").pack()

Button(tab1_frame6, text="Submit", command=tab1_btn_submit, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left)
Button(tab1_frame6, text="Voice", command=tab1_btn_voice, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left, padx=5)

""" --------------------------------------------------- Tab 2 Contents Constructor ---------------------------------------------------"""
# Tab for removing orders.
tab2_frame1 = Frame(tab2, bg="#212121")
tab2_frame2 = Frame(tab2, bg="#212121")
tab2_frame3 = Frame(tab2, bg="#212121")
tab2_frame4 = Frame(tab2, bg="#212121")
tab2_frame5 = Frame(tab2, bg="#212121")
tab2_frame6 = Frame(tab2, bg="#212121")
tab2_frame1.pack()
tab2_frame2.pack()
tab2_frame3.pack()
tab2_frame4.pack()
tab2_frame5.pack()
tab2_frame6.pack()

def tab2_btn_submit():
    tn = table_number2.get()
    food_name_tn1 = "chicken" + tn
    food_qty_tn1 = "chicken" + "_quantity" + tn
    food_name_tn2 = "beef" + tn
    food_qty_tn2 = "beef" + "_quantity" + tn
    food_name_tn3 = "coffee" + tn
    food_qty_tn3 = "coffee" + "_quantity" + tn
    fn = food_name2.get()

    tab2_label1 = Label(tab2_frame6, text=garis, fg="cyan", bg="#212121")
    tab2_label1.pack()
    try:
        if len(tn) != 0:
            if fn == "chicken":
                brain.pop(food_name_tn1)
                brain.pop(food_qty_tn1)
        
                tab2_label2 = Label(tab2_frame6, text="✅ Your order is successfully removed, you can reorder again at the order food tab.", font=segoeNormal, bg="#212121", fg="cyan")
                tab2_label2.pack() 
            elif fn == "beef":
                brain.pop(food_name_tn2)
                brain.pop(food_qty_tn2)

                tab2_label2 = Label(tab2_frame6, text="✅ Your order is successfully removed, you can reorder again at the order food tab.", font=segoeNormal, bg="#212121", fg="cyan")
                tab2_label2.pack()  
            elif fn == "coffee":
                brain.pop(food_name_tn3)
                brain.pop(food_qty_tn3)
                 
                tab2_label2 = Label(tab2_frame6, text="✅ Your order is successfully removed, you can reorder again at the order food tab.", font=segoeNormal, bg="#212121", fg="cyan")
                tab2_label2.pack()              
            else: 
                tab2_label2 = Label(tab2_frame6, text="⚠ You can only remove orders for chicken, Beef or coffee!", font=segoeNormal, bg="#212121", fg="cyan")
                tab2_label2.pack()
        else:    
            tab2_label2 = Label(tab2_frame6, text="⚠️ All fields must be filled! You cannot leave a field or more empty!", font=segoeNormal, bg="#212121", fg="cyan")
            tab2_label2.pack()
    except KeyError:
        tab2_label2 = Label(tab2_frame6, text="⚠ That data is either deleted or never existed!", font=segoeNormal , fg="cyan", bg="#212121")
        tab2_label2.pack()
        
    tab2_label3 = Label(tab2_frame6, text=garis, fg="cyan", bg="#212121")
    tab2_label3.pack()
    # Remove the labels after x second(s).
    tab2_label1.after(x, tab2_label1.destroy)
    tab2_label2.after(x, tab2_label2.destroy)
    tab2_label3.after(x, tab2_label3.destroy)
    
    with open("brain.json", "w") as b:
        json.dump(brain, b, indent=4)    

Label(tab2_frame1, text=" ", bg="#212121").pack()
Label(tab2_frame1, text=" ", bg="#212121").pack()
Label(tab2_frame1, text="Remove Orders", font=segoeBold, bg="#212121", fg="cyan").pack()
Label(tab2_frame1, text="Fill in the form below and submit to remove orders. Make sure you did not input the wrong table \nnumber, otherwise data of another user will be deleted!", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tab2_frame1, text=garis, fg="cyan", bg="#212121").pack()

Label(tab2_frame2, text="Food Name :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left, padx=9)
food_name2 = Entry(tab2_frame2, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
food_name2.pack(side=left)

Label(tab2_frame3, text="Table Number :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left)
table_number2 = Entry(tab2_frame3, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
table_number2.pack(side=left)

Label(tab2_frame4, text=garis, fg="cyan", bg="#212121").pack()

Button(tab2_frame5, text="Submit", command=tab2_btn_submit, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left)

""" --------------------------------------------------- Tab 3 Contents Constructor ---------------------------------------------------"""
# Tab for listing orders.
tab3.pack_propagate(0) # Prevent Overflowing

tab3_frame1 = Frame(tab3, bg="#212121")
tab3_frame2 = Frame(tab3, bg="#212121")
tab3_frame3 = Frame(tab3, bg="#212121")
tab3_frame4 = Frame(tab3, bg="#212121")
tab3_frame5 = Frame(tab3, bg="#212121")
tab3_frame1.pack()
tab3_frame2.pack()
tab3_frame3.pack()
tab3_frame4.pack()
tab3_frame5.pack()

def tab3_btn_submit():
    tn = table_number3.get()
    food_name_tn1 = "chicken" + tn
    food_qty_tn1 = "chicken" + "_quantity" + tn
    food_name_tn2 = "beef" + tn
    food_qty_tn2 = "beef" + "_quantity" + tn
    food_name_tn3 = "coffee" + tn
    food_qty_tn3 = "coffee" + "_quantity" + tn
    
    # Destroy all labels after 3 seconds to prevent spamming.
    tab3_label1 = Label(tab3_frame5, text=" ", bg="#212121")
    tab3_label1.pack()
    
    tab3_label2 = Label(tab3_frame5, text=garis, fg="cyan", bg="#212121")
    tab3_label2.pack()
    
    if len(tn) != 0:
        tab3_label3 = Label(tab3_frame5, text="Order list for table " + tn + " :", font=segoeBold, bg="#212121", fg="cyan")
        tab3_label3.pack()
        speak("Order list for table " + tn)
    elif len(tn) == 0:
        tab3_label3 = Label(tab3_frame5, text="Error :", font=segoeBold, bg="#212121", fg="cyan")
        tab3_label3.pack()
        if food_name_tn1 not in brain and food_name_tn2 not in brain and food_name_tn3 not in brain:
            tab3_label8 = Label(tab3_frame5, text="⚠ You left a field empty, please complete the form!", font=segoeNormal, bg="#212121", fg="cyan")
            tab3_label8.pack()
            speak("You left a field empty, please complete the form!")
    else:
        tab3_label3 = Label(tab3_frame5, text="Error :", font=segoeBold, bg="#212121", fg="cyan")
        tab3_label3.pack()
        
    # Check orders one by one. If order is not in dictionary, the program will not send the element.
    if food_name_tn1 in brain:
        tab3_label4 = Label(tab3_frame5, text="Chicken : " + brain[food_qty_tn1], font=segoeNormal, bg="#212121", fg="cyan")
        tab3_label4.pack()
        speak(brain[food_qty_tn1] + "Chicken")
        
    if food_name_tn2 in brain:
        tab3_label5 = Label(tab3_frame5, text="Beef : " + brain[food_qty_tn2], font=segoeNormal, bg="#212121", fg="cyan")
        tab3_label5.pack()
        speak(brain[food_qty_tn2] + "Beef")
        
    if food_name_tn3 in brain:
        tab3_label6 = Label(tab3_frame5, text="Coffee : " + brain[food_qty_tn3], font=segoeNormal, bg="#212121", fg="cyan")
        tab3_label6.pack()
        speak(brain[food_qty_tn3] + "Coffee")
        
    if food_name_tn1 not in brain and food_name_tn2 not in brain and food_name_tn3 not in brain and len(tn) != 0:
        tab3_label8 = Label(tab3_frame5, text="⚠ That data does not exist! Did you forget your table number?", font=segoeNormal, bg="#212121", fg="cyan")
        tab3_label8.pack()
        speak("That data does not exist! Did you forget your table number?")
    
    tab3_label7 = Label(tab3_frame5, text=garis, fg="cyan", bg="#212121")
    tab3_label7.pack()
    
    tab3_label1.after(x, tab3_label1.destroy)
    tab3_label2.after(x, tab3_label2.destroy)
    tab3_label3.after(x, tab3_label3.destroy)
    
    try:
        tab3_label4.after(x, tab3_label4.destroy)
        tab3_label5.after(x, tab3_label5.destroy)
        tab3_label6.after(x, tab3_label6.destroy)
    except:
        print("[DEBUG] : Skipped 3 unused labels to prevent error bug!")
        
    tab3_label7.after(x, tab3_label7.destroy)
    
    try:
        tab3_label8.after(x, tab3_label8.destroy)
    except:
        print("[DEBUG] : Skipped 1 unused labels to prevent error bug!")
        
def tab3_btn_voice():
    print("[DEBUG] : Tab3 - Field1 Listening...") 
    speak("What is your table number?")
    field1 = get_audio()
    table_number3.insert(0, field1)

Label(tab3_frame1, text=" ", bg="#212121").pack()
Label(tab3_frame1, text=" ", bg="#212121").pack()
Label(tab3_frame1, text="List Orders", font=segoeBold, bg="#212121", fg="cyan").pack()
Label(tab3_frame1, text="Fill in a table number and submit to list orders.", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tab3_frame1, text=garis, fg="cyan", bg="#212121").pack()

Label(tab3_frame2, text="Table Number :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left)
table_number3 = Entry(tab3_frame2, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
table_number3.pack(side=left)

Label(tab3_frame3, text=garis, fg="cyan", bg="#212121").pack()

Button(tab3_frame4, text="Submit", command=tab3_btn_submit, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left)
Button(tab3_frame4, text="Voice", command=tab3_btn_submit, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left, padx=5)

""" --------------------------------------------------- Tab 4 Contents Constructor ---------------------------------------------------"""
# Tab for payment.
tab4.pack_propagate(0) # Prevent Overflowing
paymentMethod = IntVar()
paymentMethod.set(1)

tab4_frame1 = Frame(tab4, bg="#212121")
tab4_frame2 = Frame(tab4, bg="#212121")
tab4_frame3 = Frame(tab4, bg="#212121")
tab4_frame4 = Frame(tab4, bg="#212121")
tab4_frame5 = Frame(tab4, bg="#212121")
tab4_frame6 = Frame(tab4, bg="#212121")
tab4_frame7 = Frame(tab4, bg="#212121")
tab4_frame1.pack()
tab4_frame2.pack()
tab4_frame3.pack()
tab4_frame4.pack()
tab4_frame5.pack()
tab4_frame6.pack()
tab4_frame7.pack()

def sel():
    if paymentMethod.get() == 1:
        selection = "✅ You chose to pay with digital cash."
        speak("You chose to pay with digital cash.")
    elif paymentMethod.get() == 2:
        selection = "✅ You chose to pay with physical cash."
        speak("You chose to pay with physical cash.")
    elif paymentMethod.get() == 3:
        selection = "✅ You chose to pay with both methods."
        speak("You chose to pay with both methods.")
    
    tab4_label1 = Label(tab4_frame7, text=garis, fg="cyan", bg="#212121")
    tab4_label1.pack()
    tab4_label2 = Label(tab4_frame7, text=selection, fg="cyan", bg="#212121", font=segoeNormal)
    tab4_label2.pack()
    tab4_label3 = Label(tab4_frame7, text=garis, fg="cyan", bg="#212121")
    tab4_label3.pack()
    
    tab4_label1.after(x, tab4_label1.destroy)
    tab4_label2.after(x, tab4_label2.destroy)
    tab4_label3.after(x, tab4_label3.destroy)
   
def tab4_btn_list():
    tn = table_number4.get()
    food_name_tn1 = "chicken" + tn
    food_qty_tn1 = "chicken" + "_quantity" + tn
    food_name_tn2 = "beef" + tn
    food_qty_tn2 = "beef" + "_quantity" + tn
    food_name_tn3 = "coffee" + tn
    food_qty_tn3 = "coffee" + "_quantity" + tn
    
    tab4_label1 = Label(tab4_frame7, text=" ", bg="#212121")
    tab4_label1.pack()
    
    tab4_label2 = Label(tab4_frame7, text=garis, fg="cyan", bg="#212121")
    tab4_label2.pack()
    
    if len(tn) != 0:
        tab4_label3 = Label(tab4_frame7, text="Order list for table " + tn + " :", font=segoeBold, bg="#212121", fg="cyan")
        tab4_label3.pack()
        speak("Order list for table " + tn)
    elif len(tn) == 0:
        tab4_label3 = Label(tab4_frame7, text="Error :", font=segoeBold, bg="#212121", fg="cyan")
        tab4_label3.pack()
        if food_name_tn1 not in brain and food_name_tn2 not in brain and food_name_tn3 not in brain:
            tab4_label8 = Label(tab4_frame7, text="⚠ You left a field empty, please complete the form!", font=segoeNormal, bg="#212121", fg="cyan")
            tab4_label8.pack()
            speak("You left a field empty, please complete the form!")
    else:
        tab4_label3 = Label(tab4_frame7, text="Error :", font=segoeBold, bg="#212121", fg="cyan")
        tab4_label3.pack()
        
    # Check orders one by one. If order is not in dictionary, the program will not send the element.
    if food_name_tn1 in brain:
        sigma_food1 = chicken_price * int(brain[food_qty_tn1])
        tab4_label4 = Label(tab4_frame7, text="Chicken : " + brain[food_qty_tn1] + " (IDR." + str(sigma_food1) + ")", font=segoeNormal, bg="#212121", fg="cyan")
        tab4_label4.pack()
        speak(brain[food_qty_tn1] + "Chicken. Price," + str(sigma_food1) + "rupiah")
    else:
        sigma_food1 = 0
        
    if food_name_tn2 in brain:
        sigma_food2 = beef_price * int(brain[food_qty_tn2])
        tab4_label5 = Label(tab4_frame7, text="Beef : " + brain[food_qty_tn2] + " (IDR." + str(sigma_food2) + ")", font=segoeNormal, bg="#212121", fg="cyan")
        tab4_label5.pack()
        speak(brain[food_qty_tn2] + "Beef. Price," + str(sigma_food2) + "rupiah")
    else:
        sigma_food2 = 0
        
    if food_name_tn3 in brain:
        sigma_food3 = coffee_price * int(brain[food_qty_tn3])
        tab4_label6 = Label(tab4_frame7, text="Coffee : " + brain[food_qty_tn3] + " (IDR." + str(sigma_food3) + ")", font=segoeNormal, bg="#212121", fg="cyan")
        tab4_label6.pack()
        speak(brain[food_qty_tn3] + "Coffee. Price," + str(sigma_food3) + "rupiah")
    else:
        sigma_food3 = 0
    
    sigma_overall = sigma_food1 + sigma_food2 + sigma_food3
    tab4_label9 = Label(tab4_frame7, text="Total : IDR." + str(sigma_overall), font=segoeNormal, bg="#212121", fg="cyan")
    tab4_label9.pack()
    speak("Total " + str(sigma_overall) + " rupiah") 
    
    if food_name_tn1 not in brain and food_name_tn2 not in brain and food_name_tn3 not in brain and len(tn) != 0:
        tab4_label8 = Label(tab4_frame7, text="⚠ That data does not exist! Did you forget your table number?", font=segoeNormal, bg="#212121", fg="cyan")
        tab4_label8.pack()
        speak("That data does not exist! Did you forget your table number?")
    
    tab4_label7 = Label(tab4_frame7, text=garis, fg="cyan", bg="#212121")
    tab4_label7.pack()
    
    tab4_label1.after(x, tab4_label1.destroy)
    tab4_label2.after(x, tab4_label2.destroy)
    tab4_label3.after(x, tab4_label3.destroy)
    
    try:
        tab4_label4.after(x, tab4_label4.destroy)
        tab4_label5.after(x, tab4_label5.destroy)
        tab4_label6.after(x, tab4_label6.destroy)
    except:
        print("[DEBUG] : Skipped 3 unused labels to prevent error bug!")
        
    tab4_label7.after(x, tab4_label7.destroy)
    
    try :
        tab4_label8.after(x, tab4_label8.destroy)
    except:
        print("[DEBUG] : Skipped 1 unused labels to prevent error bug!")
        
    tab4_label9.after(x, tab4_label9.destroy)
   
def tab4_btn_confirm():
    tn = table_number4.get()
    food_name_tn1 = "chicken" + tn
    food_qty_tn1 = "chicken" + "_quantity" + tn
    food_name_tn2 = "beef" + tn
    food_qty_tn2 = "beef" + "_quantity" + tn
    food_name_tn3 = "coffee" + tn
    food_qty_tn3 = "coffee" + "_quantity" + tn

    if len(tn) != 0 and paymentMethod.get() == 1:
        if food_name_tn1 in brain or food_name_tn2 in brain or food_name_tn3 in brain:
            try:
                brain.pop(food_name_tn1)
                brain.pop(food_qty_tn1)
        
                brain.pop(food_name_tn2)
                brain.pop(food_qty_tn2)

                brain.pop(food_name_tn3)
                brain.pop(food_qty_tn3)
            except KeyError:
                if food_name_tn1 in brain:
                    brain.pop(food_name_tn1)
                    brain.pop(food_qty_tn1)
            
                if food_name_tn2 in brain:
                    brain.pop(food_name_tn2)
                    brain.pop(food_qty_tn2)
                
                if food_name_tn3 in brain:
                    brain.pop(food_name_tn3)
                    brain.pop(food_qty_tn3)

            selection = "✅ Payment successful! Thank you for using our service!"
            speak("Payment successful! Thank you for using our service!")
        else:
            selection = "⚠ Payment failed! That data does not or no longer exist!"
            speak("Payment failed! That data does not or no longer exist!")
    elif len(tn) != 0 and paymentMethod.get() >= 2 and paymentMethod.get() <= 3:
        if food_name_tn1 in brain or food_name_tn2 in brain or food_name_tn3 in brain:
            try:
                brain.pop(food_name_tn1)
                brain.pop(food_qty_tn1)
        
                brain.pop(food_name_tn2)
                brain.pop(food_qty_tn2)

                brain.pop(food_name_tn3)
                brain.pop(food_qty_tn3)
            except KeyError:
                if food_name_tn1 in brain:
                    brain.pop(food_name_tn1)
                    brain.pop(food_qty_tn1)
            
                if food_name_tn2 in brain:
                    brain.pop(food_name_tn2)
                    brain.pop(food_qty_tn2)
                
                if food_name_tn3 in brain:
                    brain.pop(food_name_tn3)
                    brain.pop(food_qty_tn3)
                    
            selection = "✅ Please go to the cashier to finalize payment with physical cash! \nThank you for using our service!"
            speak("Please go to the cashier to finalize payment with physical cash! \nThank you for using our service!")
        else:
            selection = "⚠ Payment failed! That data does not or no longer exist!"
            speak("Payment failed! That data does not or no longer exist!") 
    else:
        selection = "⚠ You need fill in the table number, choose a payment method and check your orders. \nAfter that, confirm if everything is correct!"
        speak("You need fill in the table number, choose a payment method and check your orders. After that, confirm if everything is correct!")
    
    with open("brain.json", "w") as b:
        json.dump(brain, b, indent=4) 
    
    tab4_label1 = Label(tab4_frame7, text=garis, fg="cyan", bg="#212121")
    tab4_label1.pack()
    tab4_label2 = Label(tab4_frame7, text=selection, fg="cyan", bg="#212121", font=segoeNormal)
    tab4_label2.pack()
    tab4_label3 = Label(tab4_frame7, text=garis, fg="cyan", bg="#212121")
    tab4_label3.pack()
    
    tab4_label1.after(x, tab4_label1.destroy)
    tab4_label2.after(x, tab4_label2.destroy)
    tab4_label3.after(x, tab4_label3.destroy)

Label(tab4_frame1, text=" ", bg="#212121").pack()
Label(tab4_frame1, text=" ", bg="#212121").pack()   
Label(tab4_frame1, text="Payment", font=segoeBold, bg="#212121", fg="cyan").pack()
Label(tab4_frame1, text="Fill in the table number and choose your payment method!", font=segoeNormal, bg="#212121", fg="cyan").pack()
Label(tab4_frame1, text=garis, fg="cyan", bg="#212121").pack()

Label(tab4_frame2, text="Table Number :", font=segoeNormal, bg="#212121", fg="cyan").pack(side=left)
table_number4 = Entry(tab4_frame2, borderwidth=0, fg="cyan", bg="gray", font=segoeNormal)
table_number4.pack(side=left)

Label(tab4_frame3, text=" ", bg="#212121").pack()

paymentMethod = IntVar()
Radiobutton(tab4_frame4, text="Digital Cash", variable=paymentMethod, font=segoeNormal, fg="cyan", bg="#333333", activebackground="cyan", activeforeground="#333333", value=1, command=sel).pack(side=left)
Radiobutton(tab4_frame4, text="Physical Cash", variable=paymentMethod, font=segoeNormal, fg="cyan", bg="#333333", activebackground="cyan", activeforeground="#333333", value=2, command=sel).pack(side=left, padx=5)
Radiobutton(tab4_frame4, text="Both", variable=paymentMethod, font=segoeNormal, fg="cyan", bg="#333333", activebackground="cyan", activeforeground="#333333", value=3, command=sel).pack(side=left)

Label(tab4_frame5, text=garis, fg="cyan", bg="#212121").pack()

Button(tab4_frame6, text="Check Orders", command=tab4_btn_list, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left)
Button(tab4_frame6, text="Confirm", command=tab4_btn_confirm, font=segoeNormal, bg="#333333", fg="cyan", activebackground="cyan", activeforeground="#333333", borderwidth=0).pack(side=left, padx=5)

root.mainloop()