"""
sim/coupled_oscillators.py

Stuart-Landau coupled-oscillator model for three rails: Light (L), Our (O), Dark (D).
Provides an RK4 integrator and simple plotting helpers.

Usage:
    import coupled_oscillators as co
    zs, t = co.integrate_example(...)
"""

import numpy as np

def stuart_landau_rhs(z, lambdas, omegas, C):
    """
    Right-hand side of Stuart-Landau network.
    z: array_like complex shape (N,)
    lambdas, omegas: arrays shape (N,)
    C: coupling matrix shape (N,N) where C[i,j] contributes to node i from node j
    returns dz/dt (complex array)
    """
    # ensure numpy arrays
    z = np.asarray(z, dtype=complex)
    lambdas = np.asarray(lambdas)
    omegas = np.asarray(omegas)
    # autonomous nonlinear term
    nonlinear = (lambdas + 1j * omegas - np.abs(z)**2) * z
    coupling = C.dot(z)
    return nonlinear + coupling

def rk4_step(z, dt, rhs, *rhs_args):
    k1 = rhs(z, *rhs_args)
    k2 = rhs(z + 0.5*dt*k1, *rhs_args)
    k3 = rhs(z + 0.5*dt*k2, *rhs_args)
    k4 = rhs(z + dt*k3, *rhs_args)
    return z + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

def integrate(z0, lambdas, omegas, C, dt=0.01, t_max=200.0):
    """
    Integrate Stuart-Landau network using RK4.
    z0: initial complex vector (N,)
    returns: zs (N, steps) complex array, times t (steps,)
    """
    steps = int(np.ceil(t_max / dt))
    zs = np.zeros((len(z0), steps), dtype=complex)
    t = np.linspace(0.0, t_max, steps)
    z = z0.copy().astype(complex)
    for idx in range(steps):
        zs[:, idx] = z
        z = rk4_step(z, dt, stuart_landau_rhs, lambdas, omegas, C)
    return zs, t

def global_coherence(zs, weights=None):
    """
    Compute global coherence R(t) from complex time series zs (N, steps).
    """
    if weights is None:
        weights = np.ones(zs.shape[0])
    weights = np.asarray(weights)[:, None]
    numerator = np.abs(np.sum(weights * zs, axis=0))
    denominator = np.sum(weights * np.abs(zs), axis=0)
    # avoid div-by-zero
    denom_safe = np.where(denominator == 0, 1e-12, denominator)
    R = numerator / denom_safe
    return R
