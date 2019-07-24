import os
from instapy_cli import client
import schedule
import time, datetime   #importing necessary modules



username = 'elizabeth_olsen_4ever'  #provide Instagram username
password = 'adarsh12345@'           #password
directory = "C:\\Users\Cyril Tom Mathew\Desktop\instagram"   #specify the folder where your photos are saved
text = '''Cutiepie #fashion #style #love #actress #instagood #follow #photography #photooftheday #model #beautiful #art #beauty #fashionblogger #ootd #hollywood #cute #picoftheday
#moda #happy #gay #girl #fashionista #instafashion #fitness #makeup #followme #bhfyp #me #lifestyle #bhfyp'''  #Post description


def upload():
    
    dirfiles = os.listdir(directory)
    dirfiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) #sorting files
    
    with client(username, password) as ig:
        for i in range(0,2):                           #change the maximum value of range to the number of photos you need to upload daily
            pic = os.path.join(directory, dirfiles[i])
            ig.upload(pic, text)                       #uploading
            os.remove(pic)                             #deleting the uploaded image from the folder
    print("Successfully Uploaded On %s" %datetime.date.today())



schedule.every().day.at("08:00").do(upload) #specify the time to post the images

while True:                                 #Loop so that the program keeps on running all time. 
    schedule.run_pending()                  #check for pending tasks
    time.sleep(5) 
