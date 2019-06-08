import numpy as np
ry2ev = 13.6056980659

# oxygen vacancy on BVO (001) I2/b surface
# listed in Ry, reported in eV

qs = [0,+1,+2]
Edefects = np.multiply([-12927.12830943,-12927.36510268,-12927.18218],ry2ev)
Epristine = np.multiply([-12991.17022],ry2ev)
vbm = 0.6366 # from pristine 4x4x1 calculation
Eg = 2.21 # eV

# in DFT reference miu_O
#mius = np.multiply([[-31.95359378],[-31.90640068],[-31.80565576]],ry2ev)
#n_is= [[-1],[-1],[-1]]
mius = np.multiply([[-31.80565576]],ry2ev)
n_is = [[-2]]
del_corr_qs = [0,-0.8814,-1.6]

