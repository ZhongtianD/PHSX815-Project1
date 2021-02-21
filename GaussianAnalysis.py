#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Gaussian

# main function for our coin toss Python code
if __name__ == "__main__":
    
    #default sigma value
    sigma = 1
    # default mean value for hypothesis 0
    mu_0 = 0

    # default mean value for hypothesis 1
    mu_1 = 1

    haveH0 = False
    haveH1 = False

    if '-mu0' in sys.argv:
        p = sys.argv.index('-mu0')
        mu_0 = float(sys.argv[p+1])
    if '-mu1' in sys.argv:
        p = sys.argv.index('-mu1')
        mu_1 = float(sys.argv[p+1])
    if '-sigma' in sys.argv:
        p = sys.argv.index('-sigma')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 :
            sigma = ptemp
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    
    Nsample = 1
    LogLikeRatio0 = []
    LogLikeRatio1 = []
    G_0 = Gaussian(mu=mu_0,sigma=sigma)
    G_1 = Gaussian(mu=mu_1,sigma=sigma)

    LLR_min = 1e8
    LLR_max = -1e8
        
    file0 = np.load(InputFile0)
    Nsample = file0.shape[1]
        
    for i in range(file0.shape[0]):
        Nsum = 0
        LLR = 0
        for v in file0[i]:
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
                LLR += G_1.loglike(v)-G_0.loglike(v)

                
                    

            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR
            LogLikeRatio1.append(LLR)

    title = str(Nsample) +  " samples / experiment"
    LogLikeRatio0.sort()
    LogLikeRatio1.sort()
    alpha = LogLikeRatio0[95*len(LogLikeRatio0)//100]
    res = next(i for i,v in enumerate(LogLikeRatio1) if v > alpha)
    beta = res/len(LogLikeRatio1)
    

    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, Nsample+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    plt.hist(LogLikeRatio1, Nsample+1, density=True, facecolor='g', alpha=0.5, label="assuming $\\mathbb{H}_1$")
    plt.axvline(alpha, color='r', linewidth=1, label='$\\lambda_\\alpha$')
    plt.plot([], [], ' ', label="$\\alpha = 0.05$")
    plt.plot([], [], ' ', label="$\\beta = $"+str(beta) ) 
    plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)

    plt.grid(True)

    plt.show()
    plt.savefig('Gaussian.png')
    
