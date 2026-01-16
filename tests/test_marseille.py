import sys
sys.path.insert(0, 'src')
from topomap import TopomapGenerator

generator = TopomapGenerator(output_dir="output")

print("\n🏖️ Testing Marseille Map Generation\n")

marseille = generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    num_lines=60,
    exaggeration=5.0,
    output_filename="marseille_test.png",
    title="MARSEILLE",
    bg_color='#2B1B4D',
    line_color='white',
    line_width=1.5,
    smoothing=True
)

print(f"\n✅ Marseille map created: {marseille}")
