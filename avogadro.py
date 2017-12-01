import math
import stdio

# Constants:
PXTOM = 0.175e-6    # m/px      -- Conversion Factor

DELTAT = 0.5        # s         -- deltat: Time elapsed between frames

TEMP = 297.0        # K         --      T: Room temperature
VISC = 9.135e-4     # Ns/m2     --    eta: Viscosity
RADIUS = 0.5e-6     # m         --    rho: Radius

GASC = 8.31457      # J/K mol   --      R: Gas constant


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    # Read displacements
    displacements = stdio.readAllFloats()

    # Calculate variance

    #      2   r1^2 + ... + rn^2
    # sigma  = -----------------
    #                 2n

    displacements = [(r * PXTOM)**2 for r in displacements]
    sigsq = sum(displacements)/(2 * len(displacements))

    # Calculate self-diffusion constant D

    # sigma^2 = 2 D deltat ==> D = sigma^2 / 2deltat
    D = sigsq / (2 * DELTAT)

    # Calculate Boltzmann constant k

    #         k T             6pi eta rho D
    # D = ----------- ==> k = -------------
    #     6pi eta rho               T

    boltzmann = (6.0 * math.pi * VISC * RADIUS * D) / TEMP

    # Print Boltzman (sic) constant
    stdio.writef('Boltzman = %e\n', boltzmann)

    # Calculate Avogadro's number Na

    #     R           R
    # k = -- ==> Na = -
    #     Na          k
    avogadro = GASC / boltzmann

    # Print Avogadro's number
    stdio.writef('Avogadro = %e\n', avogadro)

if __name__ == '__main__':
    main()
