from sense_hat import SenseHat
import time
sense = SenseHat()
p = [2,3]
light_len = 3
space_size = 8
speed = 1/7
r = (255,0,0)
n = (0,0,0)
space = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 r, r, r, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
def shift_right() :
  global p
  
   
  space[p[1]*space_size+p[0]+1] = r
  space[p[1]*space_size+p[0]-2] = n
  print(p[1]*space_size+p[0]-1)
  sense.set_pixels(space)
  #print(p)
  p[0] = p[0]+ 1
  #print(p,"\n")

def shift_left():
  space[((p[1])*space_size)+p[0]+1] = n
  space[((p[1])*space_size)+p[0]-2] = r
  
  sense.set_pixels(space)
  p[0] = p[0]- 1
  

def main():
 global p
 while True:
   
  
  while True:
   shift_right()
   print('hi')
   time.sleep(speed)
   if p[0] == space_size-1: break
  while True:
   shift_left()
   time.sleep(speed)
   if p[0] == light_len-2: break

if __name__ == '__main__':
  main()
  