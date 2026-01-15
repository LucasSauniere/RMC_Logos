"""
Mayotte Relief Map Example

Recreates the "Les Reliefs de Mayotte" style topographic visualization.
"""

import sys
sys.path.insert(0, '../src')
from topomap import TopomapGenerator

# Create generator
generator = TopomapGenerator(output_dir="../output")

# Mayotte coordinates
LATITUDE = -12.8275
LONGITUDE = 45.1662

print("\n" + "="*60)
print("Generating: LES RELIEFS DE MAYOTTE")
print("(Joy Division style topographic visualization)")
print("="*60 + "\n")

# Generate the map
output_path = generator.generate(
    latitude=LATITUDE,
    longitude=LONGITUDE,
    size_km=25,
    resolution=150,
    num_lines=100,
    exaggeration=4.5,
    output_filename="mayotte_relief.png",
    title="LES RELIEFS DE MAYOTTE",
    bg_color='#2B1B4D',      # Deep purple
    line_color='white',
    line_width=1.2,
    fill_below=True,
    smoothing=True
)

print("\n" + "="*60)
print("✅ Map generated successfully!")
print("="*60)
print(f"\nSaved to: {output_path}")
print("\nThis map shows the volcanic topography of Mayotte,")
print("a beautiful island in the Mozambique Channel.\n")
