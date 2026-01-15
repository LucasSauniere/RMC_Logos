"""
SVG Logo Creation Example

Generate SVG files perfect for logos and vector graphics.
"""

import sys
sys.path.insert(0, '../src')
from topomap import TopomapGenerator, create_gradient_scaling

# Create generator
generator = TopomapGenerator(output_dir="../output")

print("\n🎨 SVG Logo Generator\n")
print("Creating vector graphics perfect for logos...\n")

# Example 1: Simple SVG logo
print("1. Generating Mount Fuji logo (SVG)...")
generator.generate(
    latitude=35.3606,
    longitude=138.7278,
    size_km=20,
    resolution=80,
    num_lines=40,
    exaggeration=3.0,
    output_filename="fuji_logo.svg",
    format='svg',
    bg_color='#ffffff',
    line_color='#000000',
    line_width=2.0,
    width=1200,
    height=800,
    smoothing=True
)

# Example 2: SVG with gradient scaling
print("\n2. Generating Alps logo with gradient scaling (SVG)...")
scaling = create_gradient_scaling(50, start=0.3, end=1.2, style='ease_out')
generator.generate(
    latitude=46.5197,
    longitude=7.9531,
    size_km=15,
    resolution=60,
    num_lines=50,
    exaggeration=3.5,
    scaling_factors=scaling,
    output_filename="alps_logo_scaled.svg",
    format='svg',
    bg_color='#ffffff',
    line_color='#1a1a2e',
    line_width=1.8,
    width=1000,
    height=1000,
    smoothing=True
)

print("\n✅ SVG logos generated!")
print("\nThese files are:")
print("  - Scalable to any size")
print("  - Editable in Illustrator/Inkscape")
print("  - Perfect for print and web")
print("  - Ready for logo use\n")
