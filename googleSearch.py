import webbrowser
from googlesearch import search
import re
import datetime
import database
import sys

query=[]
links=[]
errors=[]

''' function which opens most relevant web pages according configuration using googlesearch and webbrowser'''
def googleSearch(words,matches,min_value,max_value,sleep_time):

    try:
        if matches:
            words=words[21:]
            query.append(words)
        else:
            query.append("You didn't say, 'Hey bot search for me' :(")
            query.append(words)
            res="Tab opened with "+str(max_value)+" links, according settings Min : "+str(min_value)+", Max : "+str(max_value)+", Sleep time : "+str(sleep_time)
            links.append(res)
            links.append(" ")
        if words:
            for data in search(words,tld="co.in", num=min_value, stop=max_value, pause=sleep_time):
                links.append(data)
                webbrowser.open(data)
                date=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                db_res=database.add_data(date,words,data)
                if db_res == 1:
                    errors.append(" ")
                    errors.append("Voice search assistant could not connect with database.")                        

            links.append(" ")
            links.append("Your search results are successfully completed.")
            links.append(" ")
            words=""

    except:
        errors.append("Voice search assistant could not open web browser for search results, try again.")
        errors.append(" ")
        errors.append("Turn ON, to search your queries.")
        errors.append(" ")

    print('Done from googleSearch')



def getLinks():
    return links

def getQuery():
    return query

def getWebbrowserErrors():
    return errors

def closeSrch():
    sys.exit(0)
