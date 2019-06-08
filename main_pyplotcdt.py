# compatible with Python 3.7+

import numpy as np

# local modules
from defect_exp import *
from defect_plot import *

if __name__ == "__main__":

#  line1 = Linear_Exp(2,-4) 
#  line2 = Linear_Exp(0.5,2) 
#  list_lambda  = [line1.lambda_exp, line2.lambda_exp]
#
#  plotter = defect_plot(list_lambda)
#  plt.show()

  from data_bvo_ovac import *

  list_lambdas = []
  # for each chemical potential condition
  print("q    miu    n_i   del_corr   sum")
  print("--------------------------------")
  for i in np.arange(len(mius)):
     miu = mius[i]
     n_i = n_is[i]
     # make list_lambas for each charge state
     for i in np.arange(len(Edefects)):
         func = (Defect_Exp(Edefect=Edefects[i], \
                                      Epristine=Epristine, \
                                      miu_i = miu, \
                                      n_i = n_i,   \
                                      q = qs[i],   \
                                      vbm = vbm,   \
                                      del_corr_q = del_corr_qs[i])) 
         print(func.m,miu,n_i,del_corr_qs[i],func.b)
         list_lambdas.append(func.lambda_exp)
     plotter = defect_plot(list_lambdas, \
                            title=r"$\miu_{O}$",
                            axes_labels=(r"$E_f -E_{vbm}$ (eV)",r"$E^{q}_{form}$ (eV)"), \
                            xaxis = (0,Eg+0.01), \
                            yaxis = (-5,5),
                            show_min=False)
     plt.draw()
     plt.pause(0.001)
     input("Press [enter] to continue") 
