import numpy as np


def cut_isEMTight(isEMTight):

    return isEMTight == 1


def cut_pt(pt_lead, pt_sublead, pt_lead_min = 40e3, pt_sublead_min = 30e3):


    return (pt_lead > pt_lead_min) & (pt_sublead > pt_sublead_min)


def cut_eta(eta_lead, eta_sublead):
    
    # |η| < 2.37 and avoid crack region 1.37 < |η| < 1.52
    eta_acceptance = (np.abs(eta_lead) < 2.37) & (np.abs(eta_sublead) < 2.37)

    not_in_crack_lead = ~((np.abs(eta_lead) > 1.37) & (np.abs(eta_lead) < 1.52))
    not_in_crack_sublead = ~((np.abs(eta_sublead) > 1.37) & (np.abs(eta_sublead) < 1.52))

    return eta_acceptance & not_in_crack_lead & not_in_crack_sublead

   