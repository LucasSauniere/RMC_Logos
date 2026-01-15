# Project Summary

## Topographic Line Art Generator
A Python project for generating "Joy Division" style topographic visualizations from real elevation data.

---

## 📁 Project Files

### Main Scripts (Ready to Use)
- **`simple_example.py`** - The easiest way to create custom maps. Edit parameters and run.
- **`test_v2.py`** - Test script to verify installation. Run this first!
- **`generate_mayotte.py`** - Example inspired by the attached image (Mayotte island)

### Core Library
- **`topomap_generator_v2.py`** - Main generator class (recommended version)
- **`topomap_generator.py`** - Original version (requires GDAL, more complex setup)

### Documentation
- **`README.md`** - Complete documentation with all details
- **`QUICKSTART.md`** - Quick reference guide for common tasks
- **`requirements.txt`** - Python package dependencies

### Output
- **`output/`** - Directory where generated images are saved
  - `test_yosemite.png` - Test image already generated

---

## 🎯 What You Can Do Now

### 1. Generate More Test Maps
```bash
# Test with Mayotte (from your image)
micromamba run -n topomap python generate_mayotte.py

# Or run the multi-example script
micromamba run -n topomap python topomap_generator_v2.py
```

### 2. Create Your Own Map
Edit `simple_example.py`:
```python
LATITUDE = 45.8326      # Mont Blanc, for example
LONGITUDE = 6.8652
SIZE_KM = 20
TITLE = "MONT BLANC"
```

Then run:
```bash
micromamba run -n topomap python simple_example.py
```

### 3. Use the API in Your Own Scripts
```python
from topomap_generator_v2 import TopomapGenerator

generator = TopomapGenerator(output_dir="my_maps")
generator.generate(
    latitude=YOUR_LAT,
    longitude=YOUR_LON,
    size_km=15,
    num_lines=80,
    exaggeration=4.0,
    output_filename="my_map.png",
    title="MY MAP"
)
```

---

## 🛠️ Environment

### Created Environment
- **Name**: `topomap`
- **Python**: 3.11
- **Location**: `/Users/sauniere/micromamba/envs/topomap`

### Installed Packages
- numpy 2.4.1
- matplotlib 3.10.8
- scipy 1.17.0
- rasterio 1.4.4
- srtm.py 0.3.7
- pillow 12.1.0
- gdal 3.12.1 (with dependencies)

### Activate Environment
```bash
# Method 1: Activate
micromamba activate topomap

# Method 2: Run directly
micromamba run -n topomap python your_script.py
```

---

## 🎨 Key Features

✅ **Working Features:**
- Worldwide elevation data access via SRTM
- High-resolution image generation (300 DPI)
- Customizable colors, lines, and exaggeration
- Gaussian smoothing for cleaner output
- Fast elevation data fetching
- Automatic caching of downloaded data

✅ **Tested Locations:**
- Yosemite Valley ✓ (test image generated)
- Ready to test: Mount Rainier, Grand Canyon, Mont Blanc, Mayotte

---

## 📊 Technical Details

### Data Source
- **SRTM (Shuttle Radar Topography Mission)**
- 90m resolution worldwide
- Downloaded via srtm.py library
- Cached locally after first download

### Processing Pipeline
1. Fetch elevation data for bounding box
2. Resample to specified resolution (e.g., 100x100 points)
3. Apply optional Gaussian smoothing
4. Normalize elevation values
5. Generate horizontal line slices
6. Apply vertical displacement based on elevation
7. Render with matplotlib and save as PNG

### Output Format
- PNG format
- 300 DPI resolution
- Default size: 12" × 16"
- Transparency support
- High-quality anti-aliasing

---

## 🔧 Customization Options

### Visual Parameters
- `num_lines` (50-100): Number of horizontal slices
- `exaggeration` (2.0-6.0): Vertical scale factor
- `line_width` (1.0-2.0): Line thickness
- `bg_color`: Background color (hex or name)
- `line_color`: Line color (hex or name)
- `smoothing` (True/False): Apply Gaussian smoothing

### Data Parameters
- `resolution` (80-200): Elevation sample points
- `size_km` (10-30): Square area size
- `latitude`, `longitude`: Center coordinates

---

## 🚀 Next Steps

1. **Run More Examples**: Try different locations
2. **Experiment**: Adjust exaggeration and colors
3. **Share**: Create maps of your favorite places
4. **Customize**: Modify the code for your needs
5. **Print**: Generate high-res images for physical prints

---

## 📚 Learn More

- See `README.md` for complete documentation
- Check `QUICKSTART.md` for quick tips
- Examine `topomap_generator_v2.py` to understand the code
- Explore different locations and settings!

---

## ✨ Inspiration

This project creates visualizations similar to:
- **Joy Division's "Unknown Pleasures" album cover** (1979)
- **Scientific topographic representations**
- **Data-driven generative art**

The technique of showing terrain through horizontal lines with vertical displacement is a classic visualization method that gained iconic status through Peter Saville's album design for Joy Division.

---

**Environment Status: ✅ Ready to use!**
**Test Status: ✅ Verified working!**
**Output: ✅ Successfully generated test image!**

**You're all set to create amazing topographic art! 🗺️**
