s={} #dict to store data
import time
import thread
from thread import*

#create
def create(key,value,timeout=0):
    if key in s:
        print("Key already exists")
    else:
        if(key.isalpha()):          #enters only if key is alphabetic

            allowed_file_size = 1024*1024*1024          #Allowed file size os 1gb
            val_size = 16*1024          #Allowed value size is 16kb
            
            if len(s)<allowed_file_size and value<=val_size:
                if timeout==0:
                    val=[value, timeout]
                else:
                    val = [value,time.time()+timeout]
                if len(key)<=32:     #length of key must be <= 32chars
                    s[key]=val
            else:
                print("Memory limit exceeded")
        else:
            print("Key name not correct")

            
#read
def read(key):
    if key in s:
        t=s[key]
        if t[1]!=0:
            if time.time()<t[1]:    #checking ttl of the key
                val = str(key)+":"+ str(t[0])
                return val      #returns respective value of the key
            else:
                print("time-to-live is expired")
    else:
        print("Doesn't exists")
    
        
    
#delete
def delete(key):
    if key in s:
        t=s[key]
        if t[1]!=0:
            if time.time()<t[1]:    #checking ttl of the key
                del s[key]      #deletes the key
                print(key,"<--- deleted successfully")
            else:
                print("time-to-live is expired")
        else:
            del s[key]      #deletes the key
            print(key,"<--- deleted successfully")
    else:
        print("key doesn't exists")
    
