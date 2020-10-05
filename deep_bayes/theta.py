import numpy as np

def encode(theta, plow, phigh):
    plow = np.array(plow)
    phigh = np.array(phigh)
    if len(theta.shape)==2:
        plow=plow[None,:]
        phigh=phigh[None,:]
        
    etheta = np.arctanh((theta-plow)/(phigh-plow)*2-1)
    return etheta

def decode(etheta, plow, phigh):
    plow = np.array(plow)
    phigh = np.array(phigh)
    if len(etheta.shape)==2:
        plow=plow[None,:]
        phigh=phigh[None,:]

    theta = (np.tanh(etheta)+1)/2*(phigh-plow)+plow
    return theta