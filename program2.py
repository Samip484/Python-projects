'''This program greets the user as the local time
If it is morning ot greets the user Goodmorning .
'''
import time
a=input("Hello!!!Whats your name ?\n")
Hr = int(time.strftime('%H'))
min = int(time.strftime('%M'))
sec = int(time.strftime('%S'))
ap = time.strftime('%p')  

if ap == "AM":
    print("Good morning",a)
elif Hr >= 12 and Hr < 18:
    print("Good afternoon",a)
else:
    print("Good evening",a)
hr=int(time.strftime("%I"))    
print (f"/r{hr:02}:{min:02}:{sec:02} {ap}")   #use f-string to eliminate spaces and anuthing inside{} is treated as variable
                                        
                                                         
