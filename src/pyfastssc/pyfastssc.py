from juliacall import Main as jl

jl.seval("using FastSSC")
__compute_SSC_integral = jl.seval('FastSSC.SSC_integral')

def compute_Sijkl(volume_element, WA, WB, WC, WD, responseAB, responseCD, σ2, nz, nl, ntomo, dz):
    Sijkl = __compute_SSC_integral(volume_element, WA, WB, WC, WD, responseAB, responseCD, σ2, nz, nl, ntomo, dz)
    return np.array(Sijkl)
