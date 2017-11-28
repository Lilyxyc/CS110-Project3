import math
import stdio

# Constants:
PXTOM = 0.175e-6    # m/px      -- Conversion Factor

TEMP = 297.0        # K         -- Room temperature
VISC = 9.135e-4     # Ns/m2     -- Viscosity
RADIUS = 0.5e-6     # m         -- Radius

GASC = 8.31457      # J/K mol   -- Gas constant

# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    displacements = stdio.readAllFloats()
    displacements = [(r * PXTOM)**2 for r in displacements]
    diffusion = sum(displacements)/(2 * len(displacements))

    boltzman = (6.0 * math.pi * VISC * RADIUS * diffusion) / TEMP
    stdio.writef('Boltzman = %e\n', boltzman)

    avogadro = GASC / boltzman
    stdio.writef('Avogadro = %e\n', avogadro)

if __name__ == '__main__':
    main()
