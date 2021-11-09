import subprocess
import os
from facebook_scraper import get_posts
import threading 
import time
from numpy import *
from os import system
from twilio.rest import Client
import random
import datetime


#u2Gt#9%2gDyg_kX
#vE68<CN<AZSCEPv

#+14842659707


account_sid = 'AC085fec8621e6a9b5730fe75446402be9'
auth_token = '8e50264d25bf5cb3e982f232ae8770bd'
client = Client(account_sid, auth_token)


def update():

    count = 0
    temp_arr1 = []
    hold_arr =[]
    num_post =0
    post_text_arr = []
    
    

    start_time = datetime.datetime.now().time().strftime('%H:%M:%S')

    while True:

        

        #arr_posts = get_posts('nintendo', pages=1)
        i =0

        #print(arr_posts['post_id]'][:50])
        #print(arr_posts[1])

        for post in get_posts('sportsmanskelso',pages =2):
            

            #print("\n",post['post_id'][:50])

            

            convert_num = int(post['post_id'][:50])
            
            j = convert_num


            temp_arr1.insert(i, j)

            post_text_arr.insert(i,(post['text'][:50]))
            

            #print("this is the num : ", temp_arr1[i])

            i=+1
            

        

        if count == 0:
            #temp_arr1 = get_posts.copy()
            count +=1
            print("This is temp at 1: ",temp_arr1[0])
            print("This is temp at 2: ",temp_arr1[1])
            print("====================================\n")


            hold_arr.insert(0,temp_arr1[0])
            hold_arr.insert(1,temp_arr1[1])


        if(temp_arr1[1] != hold_arr[1]):


            print("NOTIFY!!!!!!!!!!!!!!!\n")
            num_post+=1;
            print("NEW POST:: COUNT: " , num_post)
            print("================================\n")


            message = client.messages \
                .create(
                     body="New Post for sportsmanskelso",
                     from_='+14842659707',
                     to='+13605621236'
                 )
            print(message.sid)

            hold_arr.insert(1,temp_arr1[1])


        if(temp_arr1[1] == hold_arr[1]):
            system('clear')

            count +=1
            print("Pinned post id: ",temp_arr1[0])
            print("Newest post id: ",temp_arr1[1])
            print("=================================\n\n")
            print("Top post, 2nd post (NOTICE: Top could be pinned) \n")

            print("post ID: \n",temp_arr1[0])
            print(post_text_arr[0])
            print("post ID: \n",temp_arr1[1])

            print(post_text_arr[1])
            print("post ID: \n",temp_arr1[2])
            print(post_text_arr[2])



            
           

            
            end_time = datetime.datetime.now().time().strftime('%H:%M:%S')

            total_time=(datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))

            
            print("\n")
            print("========================\n")
            print("Current run time", total_time )
            print("Number of times ran:  " , count)
            print("NEW POST::    COUNT:  " , num_post)

            print("========================\n")

        num = random.randint(60,180)
        time.sleep(num)






update()







