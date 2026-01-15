# Topographic Line Art Generator

Generate beautiful "Joy Division" style topographic visualizations from real elevation data anywhere on Earth! This project creates horizontal line maps with vertical displacement based on terrain height, similar to the iconic *Unknown Pleasures* album cover.

![Example](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- 🌍 **Worldwide Coverage**: Works for any location on Earth using SRTM elevation data
- 🎨 **Customizable**: Adjust colors, line count, exaggeration, and more
- 🏔️ **High Quality**: Generates high-resolution images (300 DPI)
- 🚀 **Easy to Use**: Simple API and example scripts included
- ⚡ **Fast**: Efficient elevation data fetching and processing

## Installation

This project uses micromamba for environment management. The environment has already been created with all necessary dependencies.

### Running Scripts

```bash
# Activate the environment
micromamba activate topomap

# Or run commands directly without activating
micromamba run -n topomap python simple_example.py
```

### Dependencies
- numpy - Numerical computations
- matplotlib - Visualization
- scipy - Data smoothing
- srtm.py - Elevation data fetching
- rasterio - Geospatial data processing
- pillow - Image processing

## Quick Start

### 1. Run the Test

First, verify everything is working:

```bash
micromamba run -n topomap python test_v2.py
```

This will generate a test map of Yosemite Valley and verify your installation.

### 2. Create Your Custom Map

The easiest way to create your own map is with `simple_example.py`:

```bash
micromamba run -n topomap python simple_example.py
```

Edit the parameters in `simple_example.py` to customize your map:

```python
LATITUDE = 48.8566      # Your location's latitude
LONGITUDE = 2.3522      # Your location's longitude
SIZE_KM = 20            # Size of area in kilometers
RESOLUTION = 120        # Elevation sample points (80-150)
NUM_LINES = 80          # Number of horizontal lines
EXAGGERATION = 3.0      # Vertical exaggeration factor
TITLE = "PARIS REGION"  # Map title
```

### 3. Using the Python API

For more control, use the API directly:

```python
from topomap_generator_v2 import TopomapGenerator

# Create generator
generator = TopomapGenerator(output_dir="output")

# Generate a map
generator.generate(
    latitude=46.8523,           # Mount Rainier
    longitude=-121.7603,
    size_km=20,                 # 20km x 20km area
    resolution=120,             # 120x120 elevation points
    num_lines=80,               # 80 horizontal lines
    exaggeration=4.0,           # 4x vertical exaggeration
    output_filename="rainier.png",
    title="MOUNT RAINIER",
    smoothing=True
)
```

### 4. Run Multiple Examples

The main script includes several pre-configured examples:

```bash
micromamba run -n topomap python topomap_generator_v2.py
```

This will generate maps for:
- Mount Rainier, Washington
- Grand Canyon, Arizona  
- Mont Blanc, Alps

## Parameters Guide

### Location Parameters
- **latitude**: Center latitude in decimal degrees (-90 to 90)
- **longitude**: Center longitude in decimal degrees (-180 to 180)
- **size_km**: Size of the square area in kilometers (recommended: 10-30km)

### Data Parameters
- **resolution**: Number of elevation sample points per dimension (recommended: 80-150)
  - Higher resolution = more detail but slower
  - For testing: use 80-100
  - For final output: use 120-150

### Visual Parameters
- **num_lines**: Number of horizontal lines (recommended: 50-100)
  - More lines = more detail
- **exaggeration**: Vertical exaggeration multiplier (recommended: 2.0-6.0)
  - Higher values make terrain more dramatic
  - Flat areas: use 4-6
  - Mountainous areas: use 2-4
- **line_width**: Width of the lines in points (recommended: 1.0-2.0)
- **bg_color**: Background color (hex code or color name)
- **line_color**: Line color (hex code or color name)
- **fill_below**: Fill area below lines (True/False)
- **smoothing**: Apply Gaussian smoothing to data (True/False)

## Interesting Locations to Try

Here are some locations with interesting topography:

### Mountains
- **Mount Everest**: 27.9881, 86.9250
- **Matterhorn**: 45.9763, 7.6586
- **Mount Fuji**: 35.3606, 138.7278
- **Denali**: 63.0695, -151.0074

### Canyons & Valleys
- **Grand Canyon**: 36.1069, -112.1129
- **Death Valley**: 36.5323, -116.9325
- **Yosemite Valley**: 37.8651, -119.5383

### Volcanoes
- **Mount St. Helens**: 46.1914, -122.1956
- **Krakatoa**: -6.1024, 105.4230
- **Mauna Kea**: 19.8207, -155.4680

### Coastal Features
- **Big Sur Coast**: 36.2704, -121.8081
- **Amalfi Coast**: 40.6333, 14.6029

## Tips for Best Results

1. **Choose Areas with Relief**: Flat areas won't look as interesting
2. **Start with Lower Resolution**: Use resolution=80-100 for testing, increase for final output
3. **Experiment with Exaggeration**: Different terrain types need different exaggeration values
4. **Adjust Line Count**: More lines for detailed areas, fewer for broader views
5. **Size Matters**: 15-25km usually provides a good balance
6. **First Download Takes Time**: Elevation data is fetched from NASA servers
7. **Use Smoothing**: Enable smoothing for cleaner, more aesthetic results

## How It Works

1. **Data Download**: Uses `srtm.py` to fetch SRTM (Shuttle Radar Topography Mission) data
   - 90m resolution worldwide coverage
   - Data is cached locally after first download

2. **Data Processing**: 
   - Samples elevation data at specified resolution
   - Applies optional Gaussian smoothing
   - Normalizes elevation values

3. **Visualization**: Creates horizontal "slices" through the terrain
   - Each line represents elevation at that latitude
   - Lines are displaced vertically based on elevation
   - Lines are drawn back-to-front with z-ordering for proper occlusion

## Output

Images are saved to the `output/` directory with:
- High resolution (300 DPI)
- PNG format with transparency support
- Customizable size (default: 12" x 16")

## Project Structure

```
Club_RMC/
├── topomap_generator_v2.py    # Main generator class (recommended)
├── topomap_generator.py       # Original version (requires GDAL setup)
├── simple_example.py          # Easy-to-edit example script
├── test_v2.py                 # Installation test script
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── output/                    # Generated images go here
```

## Troubleshooting

### Connection Errors
- Check your internet connection
- SRTM data is downloaded from NASA servers
- Try again if the server is temporarily unavailable

### "No elevation data available"
- Verify coordinates are valid (latitude: -90 to 90, longitude: -180 to 180)
- Some oceanic areas don't have elevation data
- Try a different location

### Slow Performance
- Reduce `resolution` (try 80 instead of 150)
- Reduce `size_km` (smaller area)
- Reduce `num_lines` (fewer lines to render)

### Lines Look Too Flat/Too Exaggerated
- Adjust the `exaggeration` parameter
- Flat areas: increase to 4-6
- Mountainous areas: decrease to 2-3

### Memory Issues
- Reduce `resolution` 
- Reduce `size_km`
- Close other applications

## Inspiration and References

This project was inspired by:
- **Joy Division's *Unknown Pleasures* album cover** - The iconic visualization that popularized this style
- **Scientific Visualization** - Traditional methods of representing topographic data
- **Generative Art Community** - Artists exploring data-driven visualizations

The code is original but draws on common techniques used in topographic visualization and inspired by the broader community of developers working with geospatial data visualization.

## Credits

- **SRTM Data**: NASA's Shuttle Radar Topography Mission
- **Python Libraries**: NumPy, Matplotlib, SciPy, SRTM.py
- **Concept**: Inspired by Joy Division's album art and topographic data visualization techniques

## License

MIT License - feel free to use and modify!

## Contributing

Suggestions and improvements are welcome! Feel free to:
- Add new visualization styles
- Improve performance
- Add new features
- Report bugs
- Share your creations!

---

**Happy Mapping! 🗺️**

## Example Gallery

Once you've generated some maps, here are some interesting locations to try:
