# PHSX815-Project1

Gaussian_sample.py generates samples drawn from the gaussian distribution with slice sampling method.

GaussianAnalysis.py creates a Log-likelihood plot.

Use the -h flag to see instructions on input parameters.

For example, to generate samples of mu=1, use

python Gaussian_sample.py -mu 1 -sigma 1 -seed 5555 -Nsample 20 -Nexp 1000 -output gaussian1.npy

To analyze simulated samples from two different hypothesis of Gaussian, use

python GaussianAnalysis.py -mu0 0 -mu1 1 -sigma0 1 -sigma1 1 -alpha 0.05 -input0 gaussian0.npy -input1 gaussian1.npy

It will generate a picture of loglikelihood ratio plot comparing the two hypothesis

![alt text](https://github.com/ZhongtianD/PHSX815-Project1/blob/main/Gaussian.png?raw=true)
