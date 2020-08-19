from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import playsound
from speechRecognition import speechRecognition,getRecognitionErrors,closeRec
from googleSearch import getLinks,getQuery,getWebbrowserErrors
import googleSearch
import threading
import time
import database
import csv
from tkinter import filedialog
from tkinter import font

class main:
    def __init__(self):
        display(380*'_')
        display("BVSA ~ Voice Search Assistant [ Version 0.1 ]")
        display(" ")
        display("Turn ON, to search your queries.")
        display(380*'_')
        

''' configuring main frame '''

master = Tk() 
master.title("BVSA ~ Voice Search Assistant")
master.iconbitmap('assets\\icon.ico')
master.geometry('570x710')
master.configure(bg='#314057')
check_on_mode=False
check_off_mode=False

def display(data):
 listbox.insert(END, data)
 lstbox_font= font.Font(family="Times",size=13)
 listbox.config(font=lstbox_font)
 

def on_button():
    global button_on,button_off,listbox,check_off_mode,check_on_mode,voice_image_label,start_thread_btn,start_thread_load
    if check_on_mode is False:
        check_off_mode=False
        check_on_mode=True
        button_on.configure(bg='green',font=("Impact", 20))
        button_off.configure(bg='#f0f3f7',font=("Impact", 20))
        try:
           th_img = threading.Thread(target=voice_image_on)
           th_img.start()
           th_off_ply = threading.Thread(target=playsound.playsound('assets\\audio\\start.mp3', True))
           th_off_ply.start() 
           start_thread_load = threading.Thread(target=loadRecognitionSearch)  
           time.sleep(0.01)
           #display(" ")
           display("Its ON.")
           display(" ")
           display("Waiting for your queries...")
           display(" ")
           start_thread_load.start()
        except:
           print ("Error: unable to start thread")
           display(" ")
           display("Error: unable to start thread.")
           display(" ")
    else:
        display("Its ON.")



'''loading other functions for speech recognition and google search '''

def loadRecognitionSearch(): 
        speechRecognition(get_lang(),get_minValue(),get_maxValue(),get_sleepTime())
        query=getQuery()
        if len(query) == 1:
            display(" ")
            display("You searched for : "+query[-1])
            display(" ")
        elif query:
            display(" ")
            display(query[0])
            display("You searched for : "+query[-1])
            display(" ")
                
        errors_rec=getRecognitionErrors()
        if errors_rec:
            display("")
            display(errors_rec[0])
            off_button()
            playsound.playsound('assets\\audio\\rec_error.mp3', True)
            return

        errors_web=getWebbrowserErrors()
        if errors_web:
            display("")
            display(errors_web[0])
            off_button()
            playsound.playsound('assets\\audio\\search_error.mp3', True)
            return

        links=getLinks()
        if links:
            for link in links:
               display(link)
            links.clear()   
            off_button()
            playsound.playsound('assets\\audio\\end.mp3', True)
            
        #closeRec()

''' functions used for speech recognition and google search modules end here'''  


def off_button():
    global button_on,button_off,listbox,check_off_mode,check_on_mode,voice_image_label
    voice_image_off()
    if check_off_mode is False and check_on_mode is not False:
        check_on_mode=False
        check_off_mode=True
        button_on.configure(bg='#f0f3f7',font=("Impact", 20))
        button_off.configure(bg='red',font=("Impact", 20))
        display(" ")
        display("Turned to OFF after completion.")
        display(" ")
        display("Turn ON, to search your queries.")
        display(display(380*'-'))
    else:
        display("Its OFF, turn ON first.")
        
def clearDisplay():
     print('Clearing display...')
     listbox.delete(0, END)
     googleSearch.query.clear()
     googleSearch.links.clear()
     googleSearch.errors.clear()   




'''configuring main frame start from here'''

def get_lang():
   global var
   return int(var.get())

var = IntVar() 
frame_0 = Frame(master)
frame_0.configure(bg='#314057')
label_spaceTop_0=Label(frame_0,text="\nspace_Top_0",bg='blue',width=970)

def voice_image_on():
    global voice_image_label
    voice_image_label.grid(row=0, column=0,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6) 
    
def voice_image_off():
    global voice_image_label
    voice_image_label.grid_forget()

voice_image = PhotoImage(file="assets\\voice_3.png")
voice_image_label = Label(frame_0, image = voice_image)
voice_image_label.grid(row=0, column=0,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6) 
voice_image_label.grid_forget()
button_on = Button(frame_0, text="ON",font=("Impact", 20),command=on_button)
button_on.grid(row=0, column=15,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)

button_off = Button(frame_0, text="OFF",font=("Impact", 20),bg='red',command=off_button)
button_off.grid(row=0, column=5,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)
frame_0.pack()


label_space_master=Label(master,text=" ",bg='#314057',width=970)
label_space_master.pack()
photo = PhotoImage(file ="assets\\robot_88.png")
label_image_2=Label(master,image=photo,width=300,height=300)
label_image_2.pack()
frame_1 = Frame(master)
frame_1.configure(bg='#314057')

label_settings=Label(frame_1,text="Settings:",width=10)
radio_btn_bangla = Radiobutton(frame_1, text="Bangla", variable=var, value=1,
                  command=get_lang)
radio_btn_all = Radiobutton(frame_1, text="All", variable=var, value=0,
                  command=get_lang)
label_min=Label(frame_1,text="Min:",width=4)

min_value = Entry(frame_1,width=3)
min_value.insert(END, '5')


def get_minValue():
    return int(min_value.get())


label_max=Label(frame_1,text="Max:",width=4)
max_value = Entry(frame_1,width=3)
max_value.insert(END, '5')

def get_maxValue():
    return int(max_value.get())

label_sleep_time=Label(frame_1,text="Sleep Time:",width=9)
ent_sleep_time = Entry(frame_1,width=3)
ent_sleep_time.insert(END, '1')
frame_1.pack()

def get_sleepTime():
    return int(ent_sleep_time.get())

label_settings.grid(row=0, column=0,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
radio_btn_bangla.grid(row=0, column=5,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
radio_btn_all.grid(row=0, column=10,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
label_min.grid(row=0, column=15,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
min_value.grid(row=0, column=20,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
label_max.grid(row=0, column=25,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
max_value.grid(row=0, column=30,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
label_sleep_time.grid(row=0, column=35,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
ent_sleep_time.grid(row=0, column=40,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)

frame_2 = Frame(master)
frame_2.configure(bg='#314057')

'''configuring main frame end here'''

   

''' fetching histories from database'''
def showHistory(listbox_history):

    histories=database.show_data()
    showBrowsingHistory(listbox_history)
    if histories:
        for history in histories:
             listbox_history.insert(END, "Date : "+history[0])
             listbox_history.insert(END, "Title : "+history[1])
             listbox_history.insert(END, "Link : "+history[2])
             listbox_history.insert(END, 280*'_')
    else:
        listbox_history.insert(END, "History is emptry.")

def showBrowsingHistory(listbox_history,res=""):

    if res:
        listbox_history.delete(0, END)
        listbox_history.insert(END," ")
        listbox_history.insert(END, "Showing Results")
        listbox_history.insert(END, 320*'-')
        lstbox_font= font.Font(family="Times",size=13)
        listbox_history.config(font=lstbox_font)
    else:
        listbox_history.delete(0, END)
        listbox_history.insert(END," ")
        listbox_history.insert(END, "Browsing History")
        listbox_history.insert(END, 320*'-')
        lstbox_font= font.Font(family="Times",size=13)
        listbox_history.config(font=lstbox_font)

''' deleting histories stored in database '''    
def deleteHistories(listbox_history):

    MsgBox =messagebox.askquestion ('Delete History','Are you sure you want to delete histories?',icon = 'warning')
    if MsgBox == 'yes':
        res=database.deleteAllHistory()
        showBrowsingHistory(listbox_history)
        listbox_history.insert(END, res)
    
def download_csv(listbox_history):

    file = filedialog.asksaveasfile(defaultextension="*.*", filetypes=[('history', '.csv'),])
    if file:
        try:
            with open(file.name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Title", "Link"])

                histories=database.show_data()
                for history in histories:
                    writer.writerow([history[0],history[1], history[2]])
                    
                showBrowsingHistory(listbox_history,"success")
                listbox_history.insert(END, "Successfully downloaded.")
        except:
             showBrowsingHistory(listbox_history,"failed")
             listbox_history.insert(END, "Failed To Download CSV file.")
        

''' searching histories using keyword from database '''        
def searchFromDB(listbox_history,data):
    
    histories=database.get_history_by_data(data)
    showBrowsingHistory(listbox_history,"search")
    if not histories:
         listbox_history.insert(END, "No data found.")
    else:
        for history in histories:
             listbox_history.insert(END, "Date : "+history[0])
             listbox_history.insert(END, "Title : "+history[1])
             listbox_history.insert(END, "Link : "+history[2])
             listbox_history.insert(END, 280*'_')

''' configuring second frame which shows browsing histories start from here.'''
def second_window():
    top=Toplevel()
    top.title("BVSA ~ Voice Search Assistant")
    top.iconbitmap('assets\\icon.ico')
    top.geometry('570x710')
    top.configure(bg='#314057')    
    label_spaceTop_1=Label(top,text=" ",bg='#314057',width=970)
    label_spaceTop_1.pack()
    top02 = Frame(top)
    top02.configure(bg='#314057')   
    label_image_2=Label(top02,image=photo,width=300,height=300)
    label_image_2.grid(row=0, column=0,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
    top02.pack()
    top2 = Frame(top)
    top2.configure(bg='#314057')
    search_bar_label=Label(top2,text="Search here:",width=9,font=("Helvetica", 11))
    search_bar_top2 = Entry(top2,width=33,font=("Helvetica", 15))
    search_bar_label.grid(row=0, column=0,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
    search_bar_top2.grid(row=0, column=5,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
    search_button = Button(top2, text="Search",font=("Helvetica", 11),command=lambda:searchFromDB(listbox_history,str(search_bar_top2.get())))
    search_button.grid(row=0, column=10,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
    top2.pack()
    top3 = Frame(top)
    top3.configure(bg='#314057')
    top3.pack()
    label_line_4=Label(top,text="",bg='#314057',width=970)
    label_line_4.pack()
    
    top4 = Frame(top)
    top4.configure(bg='#827857')
    top4.pack()
    scrollbar = Scrollbar(top4)
    scrollbar.pack( side = RIGHT, fill = Y )
    listbox_history = Listbox(top4,width=200,bg="black",foreground="white",height=100, font=("Helvetica", 12),yscrollcommand = scrollbar.set)
    listbox_history.pack()
    listbox_history.pack( side = LEFT, fill = BOTH)
    scrollbar.config( command = listbox_history.yview)
    delete_button = Button(top3, text="Delete history",font=("Helvetica", 11),command=lambda:deleteHistories(listbox_history))
    download_button = Button(top3, text="Download CSV",font=("Helvetica", 11),command=lambda:download_csv(listbox_history))
    delete_button.grid(row=0, column=0,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
    download_button.grid(row=0, column=15,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
    showHistory(listbox_history)
    
''' configuring second frame which shows browsing histories end here.'''   



'''configuring main frame start from here'''
clear_button = Button(frame_2, text="Clear",font=("Helvetica", 11),command=clearDisplay)
history_button = Button(frame_2, text="History",font=("Helvetica", 11),command=second_window)
clear_button.grid(row=0, column=10,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
history_button.grid(row=0, column=15,columnspan=4, rowspan=4,sticky=W+E+N+S, padx=6, pady=6)
frame_2.pack()


label_line_4=Label(master,text="",bg='#314057',width=970)
label_line_4.pack()

frame_3 = Frame(master)
frame_3.configure(bg='#827857')
frame_3.pack()
scrollbar = Scrollbar(frame_3)
scrollbar.pack( side = RIGHT, fill = Y )
listbox = Listbox(frame_3,width=200,bg="black",foreground="white",height=100, font=("Helvetica", 12),yscrollcommand = scrollbar.set)
listbox.pack()
listbox.pack( side = LEFT, fill = BOTH)
scrollbar.config( command = listbox.yview)

'''configuring main frame end here'''

if __name__ == '__main__':
 print("Starting...")
 init=main()
 master.mainloop()
 
