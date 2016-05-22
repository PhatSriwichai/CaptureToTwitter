import sys
import datetime
import time
from twython import Twython
import pygame
import pygame.camera
from pygame.locals import *
from time import sleep
import RPi.GPIO as GPIO
 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()



CONSUMER_KEY = '2N5qiLKpdGLVUsiG4DMNYAFa7'
CONSUMER_SECRET = 'aFoRm89KpFYgW6Bcs5WqdN0AFie6FZM06WluZS9SwjFTN1by4g'
ACCESS_KEY = '3075993602-c3BGnjjWSrI1PU9vnlHl8AY26ZcgWUuckStLzK0'
ACCESS_SECRET = 'ZEqG0yJ0GtCvBbggUmTbRoeDFKc9eSTHcL6F1QVCbnTFg'
 
# define image size
imageWidth = 320
imageHeight = 240

screen = pygame.display.set_mode((imageWidth, imageHeight))
 
while True:
 
  
    timeStampString = datetime.datetime.now().strftime("%A %Y-%m-%d %I:%M:%S %p")
    pygame.display.set_caption(timeStampString)
    image = cam.get_image()
    screen.blit(image, (0,0))
    pygame.display.flip()
    
    
    
    if GPIO.input(11) == GPIO.LOW:
        print "Saving image"
        timeStampString = datetime.datetime.now().strftime("%A %Y-%m-%d %I:%M:%S %p")
	image = cam.get_image()
	pygame.image.save(image,timeStampString+'.jpg')
	photo = open(timeStampString+'.jpg','rb')
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
	api.update_status_with_media(media=photo, status='My RPi be tweeting images now => ')
        sleep(1)
    
    if GPIO.input(13) == GPIO.LOW:
        print "Exit"
        break


