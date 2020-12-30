s={} #dict to store data

#create
def create(key,value):
    if key in s:
        print("Key already exists")
    else:
        if(key.isalpha()):          #enters only if key is alphabetic
            allowed_file_size = 1024*1024*1024          #Allowed file size os 1gb
            val_size = 16*1024          #Allowed value size is 16kb
            if len(s)<allowed_file_size and value<=val_size:
                val=[value]
                if len(key)<=32:     #length of key must be <= 32chars
                    s[key]=val
            else:
                print("Memory limit exceeded")
        else:
            print("Key name not correct")

            
#read
def read(key):
    if key in s: 
        val = str(key)+":"+ str(s[key])
        return val #returns respective value of the key
    else:
        print("Doesn't exists")
    
        
    
#delete
def delete(key):
    if key in s:
        del s[key] #deletes the key
        print(key,"<--- deleted successfully")
    else:
        print("key doesn't exists")
    
