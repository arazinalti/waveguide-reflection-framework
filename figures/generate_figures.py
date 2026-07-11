"""
Generate all 7 figures from the paper.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Create figures directory if it doesn't exist
os.makedirs('figures', exist_ok=True)

# ============================================================
# Figure 1: Planar Waveguide Geometry
# ============================================================
def plot_figure1():
    fig, ax = plt.subplots(figsize=(8, 3))
    
    ax.axhline(y=1, color='k', linewidth=2)
    ax.axhline(y=-1, color='k', linewidth=2)
    
    x = np.linspace(0, 6, 100)
    y = 1 - (x/3) * 2
    ax.plot(x, y, 'r-', linewidth=2, label='Ray path')
    
    ax.annotate('', xy=(2, 1), xytext=(2, -1), 
                arrowprops=dict(arrowstyle='<->', color='b', lw=2))
    ax.text(2.1, 0, '2h', fontsize=12, color='b', fontweight='bold')
    
    ax.annotate('', xy=(3, 1), xytext=(0, 1), 
                arrowprops=dict(arrowstyle='<->', color='g', lw=2))
    ax.text(1.5, 1.2, 'Δx', fontsize=12, color='g', fontweight='bold')
    
    ax.text(4.5, 0.3, 'θ', fontsize=14, color='r', fontweight='bold')
    
    ax.text(-0.3, 1.2, 'Cladding (n₂)', fontsize=10)
    ax.text(-0.3, -1.2, 'Cladding (n₂)', fontsize=10)
    ax.text(2.5, 0.5, 'Core (n₁)', fontsize=10, ha='center')
    
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Fig. 1: Geometry of a Planar Optical Waveguide', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('figures/figure1.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 1 saved as 'figures/figure1.png'")

# ============================================================
# Figure 2: Skew Ray Trajectory
# ============================================================
def plot_figure2():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    r = 1.0
    z_cyl = np.linspace(0, 10, 50)
    theta_cyl = np.linspace(0, 2*np.pi, 50)
    THETA, Z = np.meshgrid(theta_cyl, z_cyl)
    X_cyl = r * np.cos(THETA)
    Y_cyl = r * np.sin(THETA)
    
    ax.plot_surface(X_cyl, Y_cyl, Z, alpha=0.15, color='gray')
    
    for z in np.linspace(0, 10, 6):
        theta_circ = np.linspace(0, 2*np.pi, 50)
        ax.plot(r * np.cos(theta_circ), r * np.sin(theta_circ), z, 
                color='gray', linewidth=0.5, alpha=0.3)
    
    z_helix = np.linspace(0, 10, 500)
    theta_helix = 2 * np.pi * z_helix / 2.5
    x_helix = r * np.cos(theta_helix)
    y_helix = r * np.sin(theta_helix)
    ax.plot(x_helix, y_helix, z_helix, 'r-', linewidth=3, label='Skew ray')
    
    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('Fig. 2: Skew Ray Trajectory in Cylindrical Fiber', fontsize=12)
    ax.legend(fontsize=10)
    ax.view_init(elev=25, azim=45)
    
    plt.tight_layout()
    plt.savefig('figures/figure2.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 2 saved as 'figures/figure2.png'")

# ============================================================
# Figure 3: Reflection Count vs. Distance
# ============================================================
def plot_figure3():
    h = 50e-6
    L = np.linspace(0, 100, 11)
    angles_deg = [5, 10, 15, 20]
    colors = ['b', 'r', 'g', 'm']
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for i, th_deg in enumerate(angles_deg):
        th = np.radians(th_deg)
        N = L * np.tan(th) / (2 * h) / 1e5
        ax.plot(L, N, 'o-', color=colors[i], linewidth=2, markersize=8, 
                label=f'θ = {th_deg}°')
    
    ax.set_xlabel('Propagation Distance L (m)', fontsize=12)
    ax.set_ylabel('Number of Reflections N (×10⁵)', fontsize=12)
    ax.set_title('Fig. 3: Reflection Count vs. Propagation Distance', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 8)
    
    plt.tight_layout()
    plt.savefig('figures/figure3.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 3 saved as 'figures/figure3.png'")

# ============================================================
# Figure 4: Comparison with Classical Model
# ============================================================
def plot_figure4():
    h = 50e-6
    alpha_abs = 0.2
    alpha_sc = 5e-5
    L = np.linspace(0, 100, 500)
    angles_deg = [2, 5, 10, 15]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    
    for idx, th_deg in enumerate(angles_deg):
        th = np.radians(th_deg)
        ax = axes[idx // 2, idx % 2]
        
        P_prop = np.exp(-L * (alpha_abs / np.cos(th) + alpha_sc * np.tan(th) / (2 * h)))
        P_class = np.exp(-alpha_abs * L)
        
        ax.plot(L, P_prop, 'b-', linewidth=2.5, label='Proposed Model')
        ax.plot(L, P_class, 'r--', linewidth=2.5, label='Classical Model')
        ax.set_xlabel('Propagation Distance L (m)', fontsize=10)
        ax.set_ylabel('Transmitted Power P/P₀', fontsize=10)
        ax.set_title(f'θ = {th_deg}°', fontsize=12)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.05)
    
    plt.suptitle('Fig. 4: Comparison between Proposed and Classical Models', fontsize=14)
    plt.tight_layout()
    plt.savefig('figures/figure4.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 4 saved as 'figures/figure4.png'")

# ============================================================
# Figure 5: Effect of Azimuthal Angle
# ============================================================
def plot_figure5():
    a = 50e-6
    L = 50
    theta = np.radians(10)
    phi = np.linspace(0, np.radians(60), 100)
    
    N = L * np.tan(theta) / (2 * a * np.cos(phi))
    P = np.exp(-0.2 * L / np.cos(theta) - 5e-5 * N)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    
    ax1.plot(np.degrees(phi), N, 'b-', linewidth=2.5)
    ax1.set_xlabel('Azimuthal Angle φ (degrees)', fontsize=11)
    ax1.set_ylabel('Number of Reflections N', fontsize=11)
    ax1.set_title('(a) Reflection Count vs. φ', fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(np.degrees(phi), P, 'g-', linewidth=2.5)
    ax2.set_xlabel('Azimuthal Angle φ (degrees)', fontsize=11)
    ax2.set_ylabel('Transmitted Power P/P₀', fontsize=11)
    ax2.set_title('(b) Power Transmission vs. φ', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle('Fig. 5: Effect of Azimuthal Angle φ', fontsize=14)
    plt.tight_layout()
    plt.savefig('figures/figure5.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 5 saved as 'figures/figure5.png'")

# ============================================================
# Figure 6: Wavelength Dependence
# ============================================================
def plot_figure6():
    lam_nm = np.linspace(800, 1700, 500)
    angles_deg = [2, 5, 10, 15]
    colors = ['b', 'r', 'g', 'm']
    
    fig, ax = plt.subplots(figsize=(9, 5.5))
    
    for i, th_deg in enumerate(angles_deg):
        th = np.radians(th_deg)
        alpha_abs = 0.8 * np.exp(-800 / lam_nm) + 0.01 * (lam_nm / 1000)**(-4)
        alpha_sc = 5e-5 * (1550 / lam_nm)**4
        loss = (alpha_abs / np.cos(th) + alpha_sc * np.tan(th) / (2 * 50e-6)) * 100
        ax.plot(lam_nm, loss, color=colors[i], linewidth=2.5, label=f'θ = {th_deg}°')
    
    ax.axvline(x=850, color='gray', linestyle=':', alpha=0.7, linewidth=2, label='850 nm')
    ax.axvline(x=1310, color='gray', linestyle=':', alpha=0.7, linewidth=2, label='1310 nm')
    ax.axvline(x=1550, color='gray', linestyle=':', alpha=0.7, linewidth=2, label='1550 nm')
    
    ax.set_xlabel('Wavelength λ (nm)', fontsize=12)
    ax.set_ylabel('Total Loss (dB)', fontsize=12)
    ax.set_title('Fig. 6: Wavelength Dependence of Total Attenuation', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(800, 1700)
    ax.set_ylim(0, 25)
    
    plt.tight_layout()
    plt.savefig('figures/figure6.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 6 saved as 'figures/figure6.png'")

# ============================================================
# Figure 7: Design Nomograms
# ============================================================
def plot_figure7():
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    
    # ===== (a) P/P₀ vs (h, θ) =====
    h = np.linspace(10, 100, 50) * 1e-6          
    theta = np.radians(np.linspace(1, 20, 50))   
    H, TH = np.meshgrid(h, theta)              
    
    P1 = np.exp(-100 * (0.2 / np.cos(TH) + 5e-5 * np.tan(TH) / (2 * H)))
    

    contour1 = axes[0].contourf(h * 1e6, np.degrees(theta), P1, 20, cmap='viridis')
    axes[0].set_xlabel('Core Half-Thickness h (μm)', fontsize=10)
    axes[0].set_ylabel('Launch Angle θ (degrees)', fontsize=10)
    axes[0].set_title('(a) P/P₀ vs. (h, θ)', fontsize=11)
    fig.colorbar(contour1, ax=axes[0], label='P/P₀')
    
    # ===== (b) P/P₀ vs (a, φ) =====
    a = np.linspace(10, 100, 50) * 1e-6
    phi = np.radians(np.linspace(0, 60, 50))
    A, PH = np.meshgrid(a, phi)
    
    P2 = np.exp(-100 * (0.2 / np.cos(np.radians(10)) + 
                5e-5 * np.tan(np.radians(10)) / (2 * A * np.cos(PH))))
    
   
    contour2 = axes[1].contourf(a * 1e6, np.degrees(phi), P2, 20, cmap='plasma')
    axes[1].set_xlabel('Core Radius a (μm)', fontsize=10)
    axes[1].set_ylabel('Azimuthal Angle φ (degrees)', fontsize=10)
    axes[1].set_title('(b) P/P₀ vs. (a, φ)', fontsize=11)
    fig.colorbar(contour2, ax=axes[1], label='P/P₀')
    
    # ===== (c) θ_opt vs (α_abs, α_sc) =====
    alpha_abs = np.linspace(0.1, 1.0, 50)
    alpha_sc = np.linspace(1e-5, 2e-4, 50)
    AA, AS = np.meshgrid(alpha_abs, alpha_sc)
    
    theta_opt = np.zeros_like(AA)
    condition = AS / (2 * 50e-6 * AA) <= 1
    theta_opt[condition] = np.degrees(np.arcsin(AS[condition] / (2 * 50e-6 * AA[condition])))
    
  
    contour3 = axes[2].contourf(alpha_abs, alpha_sc * 1e5, theta_opt, 20, cmap='coolwarm')
    axes[2].set_xlabel('Absorption Coefficient α_abs (m⁻¹)', fontsize=10)
    axes[2].set_ylabel('Scattering Coefficient α_sc (×10⁻⁵)', fontsize=10)
    axes[2].set_title('(c) θ_opt vs. (α_abs, α_sc)', fontsize=11)
    fig.colorbar(contour3, ax=axes[2], label='θ_opt (degrees)')
    
    plt.suptitle('Fig. 7: Design Nomograms for Waveguide Optimization', fontsize=14)
    plt.tight_layout()
    plt.savefig('figures/figure7.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ Figure 7 saved as 'figures/figure7.png'")

# ============================================================
# Main Execution
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Generating all 7 figures...")
    print("=" * 50)
    print()
    
    plot_figure1()
    plot_figure2()
    plot_figure3()
    plot_figure4()
    plot_figure5()
    plot_figure6()
    plot_figure7()
    
    print()
    print("=" * 50)
    print("✅ All figures generated successfully!")
    print("📁 Files saved in 'figures/' directory:")
    print("   ✅ figure1.png")
    print("   ✅ figure2.png")
    print("   ✅ figure3.png")
    print("   ✅ figure4.png")
    print("   ✅ figure5.png")
    print("   ✅ figure6.png")
    print("   ✅ figure7.png")
    print("=" * 50)
