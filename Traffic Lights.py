from sense_hat import SenseHat
import time
sense = SenseHat()
state = 0
color = 0
stop = False
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)
red = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
red_yellow = [ n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
yellow = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
green = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, g, g, n, n, n,
 n, n, n, g, g, n, n, n
 ]
def chromia_state(duration,color):
   global stop
   #while stop == True :
     
   
 #localStop = stop
# while (stop==False): 
# while (localStop == stop) :
   if color == 0 :
     sense.set_pixels(red)
   elif color == 1 :
     sense.set_pixels(yellow)
   elif color == 2 :
     sense.set_pixels(green)
   elif color == 3 :
     sense.set_pixels(red_yellow)
   time.sleep(duration)
   sense.clear()

def out_of_order_state():
 sense.set_pixels(yellow)
 time.sleep(0.5)
 sense.clear()
 time.sleep(0.5)
def set_state():
 global state
# state variable has been defined outside
 if state < 3:
   state += 1
 elif state == 3:
   state = 0
 else:
   pass
def button_event(event):
 global state
 global color
 if event.action == 'released':
  if state != 4:
   state = 4
  else:
   state = 3
def button_event2(event):
 global stop
 if event.action == 'released':
   stop = True
def button_event3(event):
 global stop
 if event.action == 'released':
   stop = False
  
sense.stick.direction_middle = button_event
sense.stick.direction_up = button_event2
sense.stick.direction_down = button_event3
def main():
 global state
 global stop
 global color
 while True:
  
  
  if stop == False:
   if state == 0:
    chromia_state(3,0)
    
   elif state == 1:
    chromia_state(1,3)
   elif state == 2:
    chromia_state(2,2)
   elif state == 3:
    chromia_state(1,1)
   else:
    out_of_order_state()
   set_state()
  else :
    while (stop == True):
     if state == 0 :
      sense.set_pixels(red)
     elif state == 1 :
      sense.set_pixels(red_yellow)
     elif state == 2 :
      sense.set_pixels(green)
     elif state == 3 :
      sense.set_pixels(yellow)
    
     
     
     
   
    
if __name__ == '__main__':
  main()
  