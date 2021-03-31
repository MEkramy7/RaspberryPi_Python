from sense_hat import SenseHat
import time, random
sense = SenseHat()
o = (0,0,0) #no color
b = (0,0,255)
one_img = [o,o,o,o,o,o,o,o,
 o,o,o,o,o,o,o,o,
 o,o,o,o,o,o,o,o,
 o,o,o,b,b,o,o,o,
 o,o,o,b,b,o,o,o,
 o,o,o,o,o,o,o,o,
 o,o,o,o,o,o,o,o,
 o,o,o,o,o,o,o,o]
two_img = [b,b,b,b,b,o,o,o,
           o,o,o,o,b,o,o,o,
           o,o,o,o,b,o,o,o,
           o,o,o,o,b,o,o,o,
           b,b,b,b,b,o,o,o,
           b,o,o,o,o,o,o,o,
           b,b,b,b,b,o,o,o,
           b,b,b,b,b,o,o,o]
three_img = [b,b,b,b,b,b,b,b,
             o,o,o,o,o,o,o,b,
             o,o,o,o,o,o,o,b,
             b,b,b,b,b,b,b,b,
             o,o,o,o,o,o,o,b,
             o,o,o,o,o,o,o,b,
             o,o,o,o,o,o,o,b,
             b,b,b,b,b,b,b,b]
four_img = [b,o,o,o,b,o,o,o,
            b,o,o,o,b,o,o,o,
            b,o,o,o,b,o,o,o,
            b,b,b,b,b,o,o,o,
            o,o,o,o,b,o,o,o,
            o,o,o,o,b,o,o,o,
            o,o,o,o,b,o,o,o,
            o,o,o,o,b,o,o,o]
five_img = [o,o,o,b,b,b,b,b,
            o,o,o,b,o,o,o,o,
            o,o,o,b,o,o,o,o,
            o,o,o,b,b,b,b,b,
            o,o,o,o,o,o,o,b,
            o,o,o,o,o,o,o,b,
            o,o,o,o,o,o,o,b,
            o,o,o,b,b,b,b,b]

six_img =     [b,b,b,b,b,b,o,o,
               b,o,o,o,o,o,o,o,
               b,o,o,o,o,o,o,o,
               b,o,o,o,o,o,o,o,
               b,b,b,b,b,b,o,o,
               b,o,o,o,o,b,o,o,
               b,o,o,o,o,b,o,o,
               b,b,b,b,b,b,o,o]

 
def number_gen(event):
 if event.action == "pressed":
   van = random.randint(1,6)
   print(val)
   if val == 1:
     sense.set_pixels(one_img)
   elif val == 2:
      sense.set_pixels(two_img)
   elif val == 3:
      sense.set_pixels(three_img)
   elif val == 4:
      sense.set_pixels(four_img)
   elif val == 5:
      sense.set_pixels(five_img)
   elif val == 6:
      sense.set_pixels(six_img)
   time.sleep(2)
   sense.clear()
sense.stick.direction_up = number_gen
while True:
 # do nothing
 pass