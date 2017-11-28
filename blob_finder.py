import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


class BlobFinder:
    """
    A data type for identifying blobs in a picture.
    """

    def __init__(self, pic, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same
        # dimensions as pic.
        x = pic.width()
        y = pic.height()
        marked = stdarray.create2D(x, y, False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        for i in range(x):
            for j in range(y):
                # 1. Create a Blob object called blob.
                blob = Blob()

                # 2. Call _findBlob() with the right arguments.
                self._findBlob(pic, tau, i, j, marked, blob)
                
                # 3. Add blob to _blobs if it has a non-zero mass.
                if blob.mass() > 0:
                    self._blobs.append(blob)

    def _findBlob(self, pic, tau, i, j, marked, blob):
        """
        Identifies a blob using depth-first search. The parameters are
        the picture (pic), luminance threshold (tau), pixel column (i),
        pixel row (j), 2D boolean matrix (marked), and the blob being
        identified (blob).
        """

        # Base case: return if pixel (i, j) is out of bounds, or if it
        # is marked, or if its luminance is less than tau.
        if i < 0 or i >= pic.width():
            return
        if j < 0 or j >= pic.height():
            return
        if marked[i][j]:
            return
        if luminance.luminance(pic.get(i, j)) < tau:
            return

        # Mark the pixel.
        marked[i][j] = True

        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call _findBlob() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i + 1, j, marked, blob)  # South
        self._findBlob(pic, tau, i, j + 1, marked, blob)  # East
        self._findBlob(pic, tau, i, j - 1, marked, blob)  # West
        self._findBlob(pic, tau, i - 1, j, marked, blob)  # North

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """

        return [blob for blob in self._blobs if blob.mass() >= P]


# Takes an integer P, a float tau, and the name of a JPEG file as
# command-line arguments; writes out all of the beads with at least P
# pixels; and then writes out all of the blobs (beads with at least 1 pixel).
def _main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])

    finder = BlobFinder(pic, tau)
    beads = finder.getBeads(P)
    stdio.writef('%d Beads:\n', len(beads))
    for bead in beads:
        stdio.writeln(bead)

    blobs = finder.getBeads(0)
    stdio.writef('%d Blobs:\n', len(blobs))
    for blob in blobs:
        stdio.writeln(blob)

if __name__ == '__main__':
    _main()
