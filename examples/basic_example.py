"""
Basic Example: Generate a topographic map

This is the simplest way to create a map.
Edit the coordinates and parameters below!
"""

import sys
sys.path.insert(0, '../src')
from topomap import TopomapGenerator

# Create generator
generator = TopomapGenerator(output_dir="../output")

# YOUR SETTINGS - Edit these!
LATITUDE = 37.8651      # Yosemite Valley
LONGITUDE = -119.5383
SIZE_KM = 15
NUM_LINES = 60
EXAGGERATION = 4.0

# Generate the map
output_path = generator.generate(
    latitude=LATITUDE,
    longitude=LONGITUDE,
    size_km=SIZE_KM,
    resolution=100,
    num_lines=NUM_LINES,
    exaggeration=EXAGGERATION,
    output_filename="my_map.png",
    title="MY TOPOGRAPHIC MAP",
    bg_color='#2B1B4D',
    line_color='white',
    line_width=1.5,
    smoothing=True
)

print(f"\n✅ Map saved to: {output_path}")
print(f"\nOpen the file to see your creation! 🗺️")
