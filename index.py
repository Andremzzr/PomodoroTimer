from playsound import playsound
import time



def countdown(t, hmt):
    interval = 600
    t *= 60
    first_value_of_t = t
    key = True
    while hmt > 0:
        while key:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            if t == 0:
                key = False
            
        hmt -= 1
        print("Waiting... Go have some rest, you deserve it")
        playsound("audio.mp3")
        time.sleep(interval)
        key = True  
        t = first_value_of_t   
    print('You did a good job today :D')
  
  

t = int(input("Enter the time in minutes: "))

hmt = int(input("Enter how many times will you do the Pomodoro: "))
  

countdown(t,hmt)
