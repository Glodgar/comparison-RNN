from config.config import *

def getSpecifications():
    if T:
        name = "T"
    if Tpot:
        name += "_Tpot"
    if p:
        name += "_p"
    if Tdew:
        name += "_Tdew"
    if rh:
        name += "_rh"
    if VPmax:
        name += "_VPmax"
    if VPact:
        name += "_VPact"
    if VPdef:
        name += "_VPdef"
    if sh:
        name += "_sh"
    if H2OC:
        name += "_H2OC"
    if rho:
        name += "_rho"
    if wv:
        name += "_wv"
    if max_wv:
        name += "_maxWv"
    if wd:
        name += "_wd"
    return name