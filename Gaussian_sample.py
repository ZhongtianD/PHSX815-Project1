
import sys
import numpy as np


sys.path.append(".")
from Random import Gaussian

# main function for our coin toss Python code
if __name__ == "__main__":

    # default seed
    seed = 2048

    # default mean of the distribution
    mu = 0
    
    # default deviation of the distribution
    sigma = 1
    

    # default number of samples (per experiment)
    Nsample = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -seed [number] seed for random number generation")
        print ("   -mu [number] mean for the gaussian distribution")
        print ("   -sigma [number] standard deviation for the gaussian distribution")
        print ("   -Nsample [number] number of samples for each experiment")
        print ("   -Nexp [number] number of experiments")
        print ("   -output [.npy file] output file saved in the .npy format")
        print
        sys.exit(1)
    
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-mu' in sys.argv:
        p = sys.argv.index('-mu')
        mu = float(sys.argv[p+1])
    if '-sigma' in sys.argv:
        p = sys.argv.index('-sigma')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 :
            sigma = ptemp
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            Nsample = Ns
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # Initialze an object of the Gaussian class
    G = Gaussian(seed =seed, mu=mu, sigma =sigma)

    if doOutputFile:
        S = np.zeros((Nexp,Nsample))
        #Generate samples
        for e in range(Nexp):
            x = np.random.rand()
            #Generate samples with a random starting point
            S[e] = G.Gaussian_sample(mu+x*sigma,Nsample)
        np.save(OutputFileName, S)
   
