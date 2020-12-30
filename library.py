s={} #dict to store data

#create
def create(key,value):
    if key in s:
        print("Key already exists")
    else:
        if(key.isalpha()): #enters only if key is alphabetic
                val=[value]
                if len(key)<=32: #length of key must be <= 32chars
                    s[key]=val
        else:
            print("Key name not correct")

            
#read
def read(key):
    if key in s: 
        val = s[key]
        return val #returns respective value of the key
    else:
        print("Doesn't exists")
    
        
    
#delete
def delete(key):
    if key in s:
        del s[key] #deletes the key
    else:
        print("key doesn't exists")
    
