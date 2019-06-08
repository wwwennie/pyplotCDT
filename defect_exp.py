import numpy as np
# local modules

class Linear_Exp(object):
    """ Base class for linear expressions 
        y = mx + b
    """
    def __init__(self,m,b):
       self.m = m
       self.b = b
       self.lambda_exp = lambda x: m * x + b

    def __repr__(self):

        return ("y = %f x + %f".format(self.m, self.b))

    def __str__(self):
        return ("y = %f x + %f".format(self.m, self.b))

class Defect_Exp(Linear_Exp):
    """ 
        E_Vform = E[defect]-E[pristine] - \sum_i n_i * miu_i + q(Ef-vbm) + del_corr_q
        n_i > 0 for adding species
        n_i < 0 for removing species

        q: defect charge
        miu_i: list, chemical potentials
        n_i: list, integers; num species added or removed
        del_corr_q: charge correction term
    """ 
    def __init__(self,Edefect=0,Epristine=0,miu_i=[],n_i=[],q=[],vbm=0,del_corr_q=0):
       self.defect = Edefect
       self.pristine = Epristine
       self.miu_i = miu_i
       self.n_i = n_i
       self.q = q
       self.vbm = vbm 
       self.del_corr_q = del_corr_q
 
       super(Defect_Exp,self).__init__(self.q,self.find_b())
  
    def find_b(self):
       """ 
        E_Vform = E[defect]-E[pristine] - \sum_i n_i * miu_i + q*vbm + del_corr_q
       """
       return self.defect - self.pristine - np.dot(self.n_i,self.miu_i) + self.q*self.vbm + self.del_corr_q
        
