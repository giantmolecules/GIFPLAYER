import pyglet

import sys, getopt

arglist = sys.argv[1:]

file = ''
try:
  opts, args = getopt.getopt(arglist,"hf:",["file="])
except getopt.GetoptError:
  print( 'test.py -f <file>')
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     print ('No help for you!')
     sys.exit()
  elif opt in ("-f", "--file"):
     file = arg
print( 'Input file is ', file)

display = pyglet.canvas.Display()
monitor = display.get_default_screen()


sprite = pyglet.sprite.Sprite(pyglet.resource.animation(file))

H_ratio = max(sprite.height, monitor.height) / min(sprite.height, monitor.height)
W_ratio = max(sprite.width, monitor.width) / min(sprite.width, monitor.width)

sprite.scale = min(H_ratio, W_ratio) # sprite.scale = 2 would double the size.
                                     # We'll upscale to the lowest of width/height
                                     # to not go out of bounds. Whichever
                                     # value hits the screen edges first essentially.

window = pyglet.window.Window(width=monitor.width, height=monitor.height, fullscreen=True)

pyglet.gl.glClearColor(0, 0, 0, 0)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()
