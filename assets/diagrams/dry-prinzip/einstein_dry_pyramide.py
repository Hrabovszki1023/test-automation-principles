import matplotlib.pyplot as plt
import numpy as np

# Geometrie des gleichseitigen Dreiecks
H = np.sqrt(3)        # Gesamthöhe für Seitenlänge 2
A = (-1.0, 0.0)
B = ( 1.0, 0.0)
C = ( 0.0, H)

# Hilfsfunktion: Schnittpunkte einer Horizontalen bei y0 mit den Dreiecksseiten
def x_bounds(y0):
    x_left  = -1.0 + y0 / H           # von A(-1,0) nach C(0,H)
    x_right =  1.0 - y0 / H           # von B(1,0)  nach C(0,H)
    return x_left, x_right

y1 = H/3.0
y2 = 2*H/3.0
xl1, xr1 = x_bounds(y1)
xl2, xr2 = x_bounds(y2)

# Polygone: unten (Trapez), Mitte (Trapez), oben (gleichseitiges Dreieck)
poly_bottom = np.array([A, B, (xr1, y1), (xl1, y1)])
poly_middle = np.array([(xl1, y1), (xr1, y1), (xr2, y2), (xl2, y2)])
poly_top    = np.array([(xl2, y2), (xr2, y2), C])

fig, ax = plt.subplots(figsize=(6, 7))

# Zeichnen
ax.fill(poly_bottom[:,0], poly_bottom[:,1], facecolor="#f8caca", edgecolor="black")  # rot/rosa
ax.fill(poly_middle[:,0], poly_middle[:,1], facecolor="#c7f2c8", edgecolor="black")  # grün
ax.fill(poly_top[:,0],    poly_top[:,1],    facecolor="#c7d2ff", edgecolor="black")  # blau

# Außenkontur betonen
outer = np.array([A, B, C, A])
ax.plot(outer[:,0], outer[:,1], color="black", linewidth=1.5)

# Labels mittig platzieren
ax.text(0, y1/2, "Konkret\n(z. B. XPath, Copy & Paste)", ha="center", va="center", fontsize=11, weight="bold")
ax.text(0, (y1+y2)/2, "Abstrakt\n(z. B. Keywords, Objektlisten)", ha="center", va="center", fontsize=11, weight="bold")
ax.text(0, (y2+H)/2 - 0.03, "Meta-Ebene\n(DRY-Prinzip, Architektur)", ha="center", va="center", fontsize=11, weight="bold")

ax.set_title("Einstein & DRY: Gleichseitige Pyramide in 3 Segmente", fontsize=13, weight="bold")
ax.set_aspect('equal', 'box')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, H+0.2)
ax.axis("off")

plt.tight_layout()

# Dateien speichern
png_path = "/mnt/data/einstein_dry_pyramide.png"
svg_path = "/mnt/data/einstein_dry_pyramide.svg"
plt.savefig(png_path, dpi=240, bbox_inches="tight")
plt.savefig(svg_path, bbox_inches="tight")
plt.show()

png_path, svg_path
