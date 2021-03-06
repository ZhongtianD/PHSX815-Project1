# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Gaussian class from Random.py file
sys.path.append(".")
from Random import Gaussian

# main function for our coin toss Python code
if __name__ == "__main__":
    
    #default sigma 0 value
    sigma_0 = 1
    #default sigma 1 value
    sigma_1 = 1
    # default mean value for hypothesis 0
    mu_0 = 0

    # default mean value for hypothesis 1
    mu_1 = 1
    
    # default alpha value
    alpha = 0.05

    haveH0 = False
    haveH1 = False

    if '-mu0' in sys.argv:
        p = sys.argv.index('-mu0')
        mu_0 = float(sys.argv[p+1])
    if '-mu1' in sys.argv:
        p = sys.argv.index('-mu1')
        mu_1 = float(sys.argv[p+1])
    if '-sigma0' in sys.argv:
        p = sys.argv.index('-sigma0')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 :
            sigma_0 = ptemp
            sigma_1 = ptemp
    if '-sigma1' in sys.argv:
        p = sys.argv.index('-sigma1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 :
            sigma_1 = ptemp
    if '-alpha' in sys.argv:
        p = sys.argv.index('-alpha')
        ptemp = float(sys.argv[p+1])
        if (ptemp > 0 and ptemp<1) :
            alpha = ptemp
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-h' in sys.argv or '--help' in sys.argv or not haveH1:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -mu0 [number]     mean for H0")
        print ("   -mu1 [number]     mean for H1")
        print ("   -sigma0 [number]   sigma for H0 ( and H1 if there is no sigma1 input)")
        print ("   -sigma1 [number]   sigma for H1")
        print ("   -alpha [number]   alpha value for H0")
        print
        sys.exit(1)
    
    Nsample = 1
    LogLikeRatio0 = []
    LogLikeRatio1 = []
    #initialise Gaussian models
    G_0 = Gaussian(mu=mu_0,sigma=sigma_0)
    G_1 = Gaussian(mu=mu_1,sigma=sigma_1)

    LLR_min = 1e8
    LLR_max = -1e8
    
    #loading files    
    file0 = np.load(InputFile0)
    Nsample = file0.shape[1]
        
    for i in range(file0.shape[0]):
        Nsum = 0
        LLR = 0
        for v in file0[i]:
            #loglikelihood ratio
            LLR += G_1.loglike(v)-G_0.loglike(v)

                
                    

        if LLR < LLR_min:
              LLR_min = LLR
        if LLR > LLR_max:
              LLR_max = LLR
        LogLikeRatio0.append(LLR)

    if haveH1:
        file1 = np.load(InputFile1)
            
        for i in range(file1.shape[0]):
            LLR = 0
            for v in file1[i]:
                #loglikelihood ratio
                LLR += G_1.loglike(v)-G_0.loglike(v)

                
                    

            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR
            LogLikeRatio1.append(LLR)

    title = str(Nsample) +  " samples / experiment"
    #sort sequence to find $\\lambda_\\alpha$ and beta
    LogLikeRatio0.sort()
    LogLikeRatio1.sort()
    L_alpha = LogLikeRatio0[int(len(LogLikeRatio0)*(1-alpha))]
    res = next(i for i,v in enumerate(LogLikeRatio1) if v > L_alpha)
    beta = res/len(LogLikeRatio1)
    

    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, 50, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    plt.hist(LogLikeRatio1, 50, density=True, facecolor='g', alpha=0.5, label="assuming $\\mathbb{H}_1$")
    plt.axvline(L_alpha, color='r', linewidth=1, label='$\\lambda_\\alpha$')
    plt.plot([], [], ' ', label="$\\alpha = $"+str(alpha))
    plt.plot([], [], ' ', label="$\\beta = $"+str(beta) ) 
    plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)

    plt.grid(True)

    plt.savefig('Gaussian.png')
    plt.show()
    
    
