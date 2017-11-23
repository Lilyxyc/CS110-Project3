import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    files = sys.argv[4:]
    
    beads1 = BlobFinder(Picture(files[0]), tau).getBeads(P)
    for i in range(1, len(files)):
        beads0 = beads1
        beads1 = BlobFinder(Picture(files[i]), tau).getBeads(P)
        for bead in beads0:
            dist = min(bead.distanceTo(other) for other in beads1)
            if dist <= delta:
                stdio.writef('%.4f\n', dist)
        stdio.writeln()

if __name__ == '__main__':
    main()
