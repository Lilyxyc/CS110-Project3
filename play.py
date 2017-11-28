import stddraw
from picture import Picture
import sys
from threshold import threshold

if len(sys.argv) < 3:
    print """
    Usage:
    python %s <run #> <frame delay> [<threshold>]
    """ % sys.argv[0]
    sys.exit()

stddraw.setCanvasSize(640, 480)
run = int(sys.argv[1])
delay = int(sys.argv[2])
tau = None
if len(sys.argv) > 3:
    tau = float(sys.argv[3])

for frame in range(200):
    pic = Picture('data/run_%d/frame%05d.jpg' % (run, frame))
    if tau:
        threshold(pic, tau)
    stddraw.picture(pic)
    stddraw.show(delay)
