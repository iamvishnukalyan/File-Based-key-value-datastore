
#importing our library as lib
import library as lib

#creating a key-value pair using create()
lib.create("age",21)

#accessing the created key-value pair using read() function
#only key must be passed and respective value will be obtained
#if the time-to-live hasn't expired
lib.read("age")

#21 will be obtained as output

#deleting a key-value pair using delete() function
#only key must be passed and respective value will be deleted
#if the time-to-live hasn't expired
lib.delete("age")

#threading
#threads can be used to access by passing functions to targets and arguments
t.start()       #starts the thread
t.sleep() 

#many threads can be created in this way for accessing
