"""
Test script for halftone style topographic visualization.
This will generate a few halftone examples to verify the feature works.
"""

import sys
sys.path.insert(0, 'src')

from topomap import TopomapGenerator

# Create generator
generator = TopomapGenerator(output_dir="output")

print("\n" + "="*70)
print("Testing Halftone Style Visualization")
print("="*70)

# Test 1: Basic halftone
print("\n1. Generating basic halftone (Marseille)...")
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=12,
    resolution=80,
    output_filename="test_halftone_basic.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#ffffff',
    dot_color='#000000',
    figsize=(10, 12),
    dpi=200
)

# Test 2: Inverted pattern
print("\n2. Generating inverted pattern...")
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=12,
    resolution=80,
    output_filename="test_halftone_inverted.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#ffffff',
    dot_color='#000000',
    invert=True,  # Inverted!
    figsize=(10, 12),
    dpi=200
)

# Test 3: Pop art style
print("\n3. Generating pop art style...")
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=12,
    resolution=80,
    output_filename="test_halftone_popart.png",
    format='halftone',
    dot_size_range=(0.5, 10.0),
    grid_spacing=10,
    bg_color='#fff5f5',
    dot_color='#dc143c',  # Red
    figsize=(10, 12),
    dpi=200
)

# Test 4: Dense grid
print("\n4. Generating dense grid (more detail)...")
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=12,
    resolution=80,
    output_filename="test_halftone_dense.png",
    format='halftone',
    dot_size_range=(0.3, 6.0),
    grid_spacing=6,  # Smaller spacing = more dots
    bg_color='#ffffff',
    dot_color='#000000',
    figsize=(10, 12),
    dpi=200
)

print("\n" + "="*70)
print("✅ All tests complete! Check the output folder:")
print("   - test_halftone_basic.png")
print("   - test_halftone_inverted.png")
print("   - test_halftone_popart.png")
print("   - test_halftone_dense.png")
print("="*70 + "\n")
