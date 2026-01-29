"""
Feature Engineering Module
This module contains functions to compute various features for diphoton events,
including  angular separations and transverse momentum characteristics.
"""
import numpy as np


def calculate_invariant_mass(pt1, eta1, phi1, pt2, eta2, phi2):
    """
    Calculate the invariant mass of a diphoton system. 
    """

    E1 = pt1 * np.cosh(eta1)
    E2 = pt2 * np.cosh(eta2)

    #Momentum components
    px1 = pt1 * np.cos(phi1)
    py1 = pt1 * np.sin(phi1)
    pz1 = pt1 * np.sinh(eta1)


    px2 = pt2 * np.cos(phi2)
    py2 = pt2 * np.sin(phi2)
    pz2 = pt2 * np.sinh(eta2)


    #Total 4 momentum
    E = E1 + E2
    px = px1 + px2
    py = py1 + py2
    pz = pz1 + pz2

    #invariant mass calculation
    m_squared = E**2 - (px**2 + py**2 + pz**2)
    m_squared = np.maximum(m_squared, 0)  # Numerical safety

    # Convert to GeV
    myy = np.sqrt(m_squared) / 1000.0 

    return myy

def calculate_delta_r(eta1, phi1, eta2, phi2):
    """
    Calculate the angular distance Delta R between two particles.
    """
    delta_eta = eta1 - eta2
    delta_phi = phi1 - phi2

    # Adjust delta_phi to be within the range [-pi, pi]
    delta_phi = np.arctan2(np.sin(delta_phi), np.cos(delta_phi))

    # Calculate Delta R
    delta_R = np.sqrt(delta_eta**2 + delta_phi**2)

    return delta_R


def calculate_delta_eta(eta1, eta2):
    """
    Calculate the absolute difference in pseudorapidity between two particles.
    """
    delta_eta = np.abs(eta1 - eta2)
    
    return delta_eta


def calculate_delta_phi(phi1, phi2):
    """
    Calculate the absolute difference in azimuthal angle between two particles.
    Adjusted to be within the range [0, pi]. 
    """
    delta_phi = phi1 - phi2
    
    # Adjust delta_phi to be within the range [-pi, pi]    
    delta_phi = np.arctan2(np.sin(delta_phi), np.cos(delta_phi))
    
    # Take absolute value to get [0, pi]
    delta_phi = np.abs(delta_phi)
    
    return delta_phi



def calculate_pt_ratio(pt_lead, pt_sublead):
    """
    Calculate the ratio of sublead pt to lead pt. 
    Range: (0, 1] - closer to 1 means more balanced. 
    """
    pt_ratio = pt_sublead / pt_lead
    
    return pt_ratio


def calculate_pt_asymmetry(pt_lead, pt_sublead):
    """
    Calculate the pt asymmetry between two photons.
    Range: [0, 1) - closer to 0 means more balanced.
    """
    pt_asymmetry = (pt_lead - pt_sublead) / (pt_lead + pt_sublead)
    
    return pt_asymmetry


def calculate_pt_sum(pt_lead, pt_sublead):
    """
    Calculate the total transverse momentum of the diphoton system. 
    """
    pt_sum = pt_lead + pt_sublead
    
    return pt_sum