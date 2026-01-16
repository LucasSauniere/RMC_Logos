"""
Quick Test Script

Verify the reorganized project works correctly.
"""

import sys
sys.path.insert(0, 'src')

from topomap import TopomapGenerator, create_gradient_scaling

print("\n" + "="*60)
print("Testing Reorganized Project")
print("="*60 + "\n")

# Test 1: Basic import
print("✅ Test 1: Imports working")

# Test 2: Create generator
generator = TopomapGenerator(output_dir="output")
print("✅ Test 2: Generator created")

# Test 3: Test scaling function
scaling = create_gradient_scaling(10, start=0.5, end=1.5, style='linear')
print(f"✅ Test 3: Scaling factors: {scaling[:3]}... (length: {len(scaling)})")

# Test 4: Quick generation (small area for speed)
print("\n✅ Test 4: Generating test map...")
path = generator.generate(
    latitude=37.8651,
    longitude=-119.5383,
    size_km=10,
    resolution=50,
    num_lines=30,
    exaggeration=3.0,
    output_filename="quick_test.png",
    smoothing=True
)
print(f"   Map saved: {path}")

# Test 5: SVG generation
print("\n✅ Test 5: Generating SVG...")
svg_path = generator.generate(
    latitude=37.8651,
    longitude=-119.5383,
    size_km=10,
    resolution=40,
    num_lines=25,
    exaggeration=3.0,
    output_filename="quick_test.svg",
    format='svg',
    width=800,
    height=600,
    smoothing=True
)
print(f"   SVG saved: {svg_path}")

print("\n" + "="*60)
print("✅ All Tests Passed!")
print("="*60)
print("\nProject is working correctly!")
print("Next steps:")
print("  1. Open notebooks/01_getting_started.ipynb")
print("  2. Run examples from examples/ folder")
print("  3. Create your own maps!\n")
