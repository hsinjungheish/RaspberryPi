import sys
import time
import RPi.GPIO as GPIO
import music as music

def main():
  GPIO.setmode(GPIO.BCM)
  
  STEPS_PER_REVOLUTION = 32 * 64
  SEQUENCE = [[1, 0, 0, 0], 
              [1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 1]]


  STEPPER_PINS = [17,18,27,22]
  for pin in STEPPER_PINS:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
  
  SEQUENCE_COUNT = len(SEQUENCE)
  PINS_COUNT = len(STEPPER_PINS)
  
  sequence_index = 0
  direction = 1
  steps = 0


    
  if len(sys.argv)>1:
    wait_time = int(sys.argv[1])/float(1000)
  else:
    wait_time = 10/float(1000)

  try:
      print('按下 Ctrl-C 可停止程式')
      start = time.monotonic()
      while True:
          duration = time.monotonic()-start
          for pin in range(0, PINS_COUNT):
              GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])

          steps += direction
          if steps >= STEPS_PER_REVOLUTION:
              direction = -1
          elif steps < 0:
              direction = 1

          sequence_index += direction
          sequence_index %= SEQUENCE_COUNT

          #print('index={}, direction={}'.format(sequence_index, direction))
          time.sleep(wait_time)
          if duration >= 5.0:
              music.playmusic()
              break
  except KeyboardInterrupt:
      print('關閉程式')
  finally:
      GPIO.cleanup()
