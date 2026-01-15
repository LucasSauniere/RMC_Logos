"""
Batch Generation Example

Generate multiple maps at once for different locations.
"""

import sys
sys.path.insert(0, '../src')
from topomap import TopomapGenerator

# Create generator
generator = TopomapGenerator(output_dir="../output")

# Define locations
locations = [
    {
        "name": "Mount Rainier",
        "lat": 46.8523,
        "lon": -121.7603,
        "size_km": 20,
        "exaggeration": 4.0
    },
    {
        "name": "Grand Canyon",
        "lat": 36.1069,
        "lon": -112.1129,
        "size_km": 25,
        "exaggeration": 5.0
    },
    {
        "name": "Mont Blanc",
        "lat": 45.8326,
        "lon": 6.8652,
        "size_km": 15,
        "exaggeration": 3.5
    },
    {
        "name": "Mount Fuji",
        "lat": 35.3606,
        "lon": 138.7278,
        "size_km": 18,
        "exaggeration": 3.5
    },
    {
        "name": "Matterhorn",
        "lat": 45.9763,
        "lon": 7.6586,
        "size_km": 12,
        "exaggeration": 3.0
    }
]

print("\n" + "="*60)
print("Batch Generation: Creating multiple topographic maps")
print("="*60 + "\n")

# Generate all maps
results = []
for i, loc in enumerate(locations, 1):
    print(f"[{i}/{len(locations)}] Generating: {loc['name']}...")
    
    filename = f"{loc['name'].lower().replace(' ', '_')}.png"
    
    path = generator.generate(
        latitude=loc['lat'],
        longitude=loc['lon'],
        size_km=loc['size_km'],
        resolution=120,
        num_lines=80,
        exaggeration=loc['exaggeration'],
        output_filename=filename,
        title=loc['name'].upper(),
        bg_color='#2B1B4D',
        line_color='white',
        line_width=1.5,
        smoothing=True
    )
    
    results.append((loc['name'], path))
    print(f"    ✅ Saved to: {path}\n")

print("="*60)
print(f"✅ Batch generation complete! Created {len(results)} maps")
print("="*60)
print("\nGenerated maps:")
for name, path in results:
    print(f"  - {name}: {path}")
print()
