"""Quick test to verify GPX overlay fix"""

import sys
sys.path.insert(0, '/Users/sauniere/Desktop/Perso/Club_RMC/src')

from topomap import TopomapGenerator

# Initialize generator
generator = TopomapGenerator(output_dir="/Users/sauniere/Desktop/Perso/Club_RMC/output")

print("Testing halftone generation with GPX overlay...")
print("=" * 60)

# Generate a small test map with GPX overlay
output = generator.generate(
    latitude=43.22,
    longitude=5.459,
    size_km=25,
    resolution=500,  # Lower resolution for quick test
    output_filename="test_gpx_overlay.png",
    format='halftone',
    
    # Halftone parameters
    dot_size_range=(0.7, 8.0),
    grid_spacing=10,
    bg_color='#ffffff',
    dot_color="#ff6900",
    invert=False,
    skip_zero_elevation=True,
    
    # GPX overlay parameters
    gpx_file="/Users/sauniere/Desktop/Perso/Club_RMC/examples/marseille-cassis.gpx",
    gpx_color='#000000',
    gpx_width=3.0,
    gpx_style='-',
    gpx_alpha=1.0,
    gpx_zorder=10,
    
    # Standard parameters
    smoothing=True,
    figsize=(12, 16),
    dpi=150  # Lower DPI for quick test
)

print("\n✅ Test successful!")
print(f"Output saved to: {output}")
