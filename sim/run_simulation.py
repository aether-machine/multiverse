#!/usr/bin/env python3
# run_simulation.py
import os
import numpy as np
import matplotlib.pyplot as plt
from coupled_oscillators import integrate, global_coherence

def default_parameters():
    # indices: 0=Light, 1=Our, 2=Dark
    lambdas = np.array([-0.10,  0.05, -0.20])   # drive/damp per rail
    omegas  = np.array([1.00, 1.10, 0.90])      # natural frequencies
    # coupling matrix C (rows=target, cols=source)
    C = np.array([
        [0.0, 0.20, 0.01],
        [0.05, 0.0,  0.05],
        [0.01, 0.30, 0.0 ]
    ], dtype=float)
    return lambdas, omegas, C

def main(out_dir="results", dt=0.02, t_max=400.0):
    os.makedirs(out_dir, exist_ok=True)
    lambdas, omegas, C = default_parameters()
    rng = np.random.default_rng(1)
    z0 = 1e-3 * (rng.standard_normal(3) + 1j * rng.standard_normal(3))

    zs, t = integrate(z0, lambdas, omegas, C, dt=dt, t_max=t_max)
    R = global_coherence(zs)

    # plotting
    fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True,
                             gridspec_kw={'height_ratios':[2,1]})
    axes[0].plot(t, np.abs(zs[0,:]), label='Light A', lw=1.2)
    axes[0].plot(t, np.abs(zs[1,:]), label='Our A', lw=1.2)
    axes[0].plot(t, np.abs(zs[2,:]), label='Dark A', lw=1.2)
    axes[0].set_ylabel('Amplitude |z|')
    axes[0].legend(loc='upper left')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(t, R, color='k', lw=1.0)
    axes[1].set_ylabel('Global coherence R')
    axes[1].set_xlabel('t (s)')
    axes[1].set_ylim(-0.05, 1.05)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    out_path = os.path.join(out_dir, "coherence_locking.png")
    plt.savefig(out_path, dpi=300)
    print(f"Saved figure: {out_path}")

if __name__ == "__main__":
    main()
