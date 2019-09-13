import numpy as np
ry2ev = 13.6056980659

# oxygen vacancy on BVO (001) I2/b surface
# listed in Ry, reported in eV

qs = [0,+2,+4] # factor 1/2 built into code
#Edefects = np.multiply([-12927.12830943,-12927.36510268,-12927.18218],ry2ev)
#Edefects = np.multiply([-12927.12830943, -12927.43786935, -12927.45458],ry2ev)

# for demo purposes only
Edefects = np.multiply([-12927.02830943, -12927.43786935, -12927.55458],ry2ev)

Epristine = np.multiply([-12991.17022],ry2ev)
vbm = 0.6366 # from pristine 4x4x1 calculation
Eg = 3.5 # eV

# in DFT reference miu_O
#mius = np.multiply([[-31.95359378],[-31.90640068],[-31.80565576]],ry2ev)
#n_is= [[-1],[-1],[-1]]
mius = np.multiply([[-31.80565576]],ry2ev)
n_is = [[-2],[-2],[-2]]
#del_corr_qs = [0,0.8814,5.03] # unconverged q2+
del_corr_qs = [0,0.8814,2.36]

