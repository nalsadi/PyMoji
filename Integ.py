from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import io
from google.cloud import vision
var = vision.Client()

Builder.load_string('''
<CameraClick>:
  orientation:'vertical'
  Camera:
    id: camera
    resolution:(700,700)
    play: False
  ToggleButton:
    text:'On/Off'
    on_press: camera.play = not camera.play
    size_hint_y: None
    height: '48dp'
  Button:
    text: 'Capture'
    size_hint_y: None
    height: '48dp'
    on_press: root.capture() ''')

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("PNG.png")
        facial_values()

        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()

def facial_values():
    with io.open("PNG.png",'rb') as imageFile:
        imagePassing = imageFile.read()
    image = var.image(imagePassing)

    faces = image.detect_faces()
    for face in faces:
        print "Amount of Joy",face.emotions.joy

TestCamera().run()
