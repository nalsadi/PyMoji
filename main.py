import kivy
import sys
import io
from google.cloud import vision

var = vision.Client()

print "Arguemnets Passed In: ",str(sys.argv)

def action_type(args):
    if(args[1] == "Exp?"):
        facial_values(args[2])

def facial_values(path):
    with io.open(path,'rb') as imageFile:
        imagePassing = imageFile.read()
    image = var.image(imagePassing)

    faces = image.detect_faces()
    for face in faces:
        print "Amount of Joy",face.emotions.joy
        print




action_type(sys.argv)
