"""
Test script to verify that lines are not drawn over zero elevation (sea).
This will generate images with and without the skip_zero_elevation feature.
"""

import sys
sys.path.insert(0, 'src')

from topomap import TopomapGenerator

# Create generator
generator = TopomapGenerator(output_dir="output")

# Test with Marseille (coastal city with lots of sea)
print("\n" + "="*70)
print("Testing zero elevation masking with Marseille (coastal area)")
print("="*70)

# Marseille coordinates
marseille_lat = 43.2965
marseille_lon = 5.3698

# Generate with zero elevation masking (new default behavior)
print("\n1. Generating WITH zero elevation masking (lines skip over sea)...")
generator.generate(
    latitude=marseille_lat,
    longitude=marseille_lon,
    size_km=15,
    resolution=150,
    num_lines=60,
    exaggeration=4.0,
    output_filename="marseille_with_masking.png",
    format='png',
    skip_zero_elevation=True,  # NEW PARAMETER
    figsize=(12, 16),
    dpi=300
)

# Generate without zero elevation masking (old behavior)
print("\n2. Generating WITHOUT zero elevation masking (lines drawn everywhere)...")
generator.generate(
    latitude=marseille_lat,
    longitude=marseille_lon,
    size_km=15,
    resolution=150,
    num_lines=60,
    exaggeration=4.0,
    output_filename="marseille_without_masking.png",
    format='png',
    skip_zero_elevation=False,  # Disable masking to see old behavior
    figsize=(12, 16),
    dpi=300
)

# Generate SVG with masking
print("\n3. Generating SVG WITH zero elevation masking...")
generator.generate(
    latitude=marseille_lat,
    longitude=marseille_lon,
    size_km=15,
    resolution=150,
    num_lines=60,
    exaggeration=4.0,
    output_filename="marseille_with_masking.svg",
    format='svg',
    skip_zero_elevation=True,
    width=1200,
    height=1600
)

print("\n" + "="*70)
print("✅ Test complete! Check the output folder:")
print("   - marseille_with_masking.png (lines skip sea)")
print("   - marseille_without_masking.png (lines over sea)")
print("   - marseille_with_masking.svg (vector format with masking)")
print("="*70 + "\n")
