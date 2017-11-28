import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture
import stddraw


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    lines = []

    stddraw.setCanvasSize(640, 480)
    stddraw.setXscale(0, 640)
    stddraw.setYscale(0, 480)
    stddraw.setPenColor(stddraw.RED)
    stddraw.setPenRadius()

    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    files = sys.argv[4:]

    stddraw.picture(Picture(files[0]))
    stddraw.show(0)

    beads1 = BlobFinder(Picture(files[0]), tau).getBeads(P)

    for i in range(1, len(files)):
        stddraw.picture(Picture(files[i]))

        beads0 = beads1
        beads1 = BlobFinder(Picture(files[i]), tau).getBeads(P)
        for bead in beads0:
            closest = sorted(beads1, key=bead.distanceTo)[0]

            dist = bead.distanceTo(closest)
            if dist <= delta:
                lines.append(
                    ((bead.x(), bead.y()), (closest.x(), closest.y())))
                stdio.writef('%.4f\n', dist)
        stdio.writeln()

        for ((x0, y0), (x1, y1)) in lines:
            stddraw.line(x0, 480-y0, x1, 480-y1)
        stddraw.show(0)
    # stddraw.show()

if __name__ == '__main__':
    main()
