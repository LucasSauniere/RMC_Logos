# 🗺️ Topographic Line Art Generator

Create stunning **Joy Division-style** topographic visualizations from real elevation data anywhere on Earth!

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## ✨ Features

- 🌍 **Worldwide Coverage** - SRTM elevation data for any location
- 🎨 **Multiple Styles** - Classic lines, SVG vectors, and halftone dots
- 🌊 **Smart Masking** - Automatically skips lines/dots over sea level
- 📊 **Scaling Factors** - Per-line elevation control for artistic effects
- 🎭 **Halftone Style** - Retro newspaper/pop art aesthetic with sea masking
- 🗺️ **GPX Track Overlay** - NEW: Superimpose GPS routes on your maps!
- ⚡ **Ultra-Fast Rendering** - NEW: 10-50x faster halftone rendering!
- 🚀 **High Performance** - Vectorized operations for high-resolution output
- 📓 **Interactive Tutorials** - Jupyter notebooks included
- 🎯 **Easy to Use** - Simple API and examples

## 🚀 Quick Start

### 1. Explore the Tutorials

```bash
# Start Jupyter
micromamba run -n topomap jupyter lab

# Open notebooks/01_getting_started.ipynb
```

### 2. Run an Example

```bash
# Basic example
micromamba run -n topomap python examples/basic_example.py

# Mayotte relief map
micromamba run -n topomap python examples/mayotte.py

# SVG logos
micromamba run -n topomap python examples/svg_logos.py
```

### 3. Use the API

```python
from topomap import TopomapGenerator, create_gradient_scaling

generator = TopomapGenerator(output_dir="output")

# Generate PNG
generator.generate(
    latitude=46.8523,
    longitude=-121.7603,
    size_km=20,
    num_lines=80,
    exaggeration=4.0,
    output_filename="rainier.png",
    title="MOUNT RAINIER"
)

# Generate SVG logo
generator.generate(
    latitude=35.3606,
    longitude=138.7278,
    size_km=15,
    num_lines=50,
    exaggeration=3.0,
    output_filename="fuji_logo.svg",
    format='svg',
    bg_color='#ffffff',
    line_color='#000000'
)

# Generate halftone style (with optimized fast rendering!)
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    output_filename="marseille_halftone.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#ffffff',
    dot_color='#000000',
    skip_zero_elevation=True,  # Mask dots over sea!
    fast_render=True           # 10-50x faster (default)!
)

# Use gradient scaling
scaling = create_gradient_scaling(60, start=0.5, end=1.5)
generator.generate(
    latitude=45.8326,
    longitude=6.8652,
    size_km=15,
    scaling_factors=scaling,
    output_filename="alps_scaled.png"
)

# Overlay GPX track on halftone map (NEW!)
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=150,
    output_filename="hiking_trail.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#ffffff',
    dot_color='#ff6900',
    # GPX overlay
    gpx_file="path/to/your/track.gpx",
    gpx_color='#000000',
    gpx_width=3.0
)
```

## 📁 Project Structure

```
Club_RMC/
├── notebooks/           # 📓 Interactive tutorials
│   ├── 01_getting_started.ipynb
│   ├── 02_marseille_example.ipynb
│   └── 03_halftone_style.ipynb
│
├── src/                 # 📦 Core library
│   └── topomap.py      # Main generator class
│
├── examples/            # 💡 Example scripts
│   ├── basic_example.py
│   ├── mayotte.py
│   ├── svg_logos.py
│   └── batch_generation.py
│
├── output/              # 🖼️  Generated files
│
├── docs/                # 📚 Documentation
│   ├── README.md
│   ├── QUICKSTART.md
│   └── API.md
│
└── requirements.txt
```

## 📦 Installation

The environment is already set up! Just activate it:

```bash
micromamba activate topomap
```

Or run commands directly:

```bash
micromamba run -n topomap python examples/basic_example.py
```

### Dependencies

- numpy - Numerical computations
- matplotlib - Visualization
- scipy - Data processing
- srtm.py - Elevation data
- svgwrite - SVG export
- rasterio - Geospatial data
- jupyter - Interactive notebooks

## 🎨 New Features

### 1. SVG Export

Perfect for logos and vector graphics:

```python
generator.generate(
    ...,
    format='svg',
    width=1200,
    height=1600
)
```

### 2. Scaling Factors

Control individual line elevations:

```python
from topomap import create_gradient_scaling

# Linear gradient
scaling = create_gradient_scaling(80, start=0.5, end=1.5, style='linear')

# Ease-in effect
scaling = create_gradient_scaling(80, start=0.3, end=1.2, style='ease_in')

# Custom factors
scaling = [1.0, 1.1, 1.2, ...] # One per line

generator.generate(..., scaling_factors=scaling)
```

### 3. Halftone Style with Sea Masking

Create retro newspaper/pop art style visualizations:

```python
generator.generate(
    ...,
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    skip_zero_elevation=True,  # Mask water bodies
    fast_render=True           # 10-50x faster!
)
```

**Features:**
- Dots of varying sizes represent elevation
- Automatic masking of seas/lakes (elevation ≤ 0)
- Customizable colors and patterns
- **NEW**: Ultra-fast vectorized rendering!

### 4. Performance Optimization 🚀

**NEW: Dramatically faster halftone rendering!**

The halftone generator now uses optimized vectorized operations:

```python
# High-resolution print (600 DPI)
generator.generate(
    ...,
    resolution=500,
    grid_spacing=5,
    fast_render=True,  # Default - renders in ~15 seconds!
    dpi=600
)
# Without optimization: Would take ~8 minutes!
```

**Performance improvements:**
- 🚀 **10-50x faster** rendering
- ⚡ **Vectorized operations** using NumPy
- 💾 **Memory efficient** for large images
- 🎨 **Identical visual output** to legacy method

**Speedup by resolution:**
- Resolution 100, spacing 10: ~10-15x faster
- Resolution 200, spacing 8: ~15-20x faster
- Resolution 500, spacing 5: ~30-40x faster
- Resolution 1000, spacing 3: ~50x+ faster

See `docs/PERFORMANCE_OPTIMIZATION.md` for detailed benchmarks and best practices.

### 5. Enhanced API

More flexible and powerful:

- Separate `create_png()` and `create_svg()` methods
- Better error handling
- Progress feedback
- Improved caching

## 📚 Documentation

- **[Getting Started Notebook](notebooks/01_getting_started.ipynb)** - Interactive tutorial
- **[Marseille Example](notebooks/02_marseille_example.ipynb)** - Detailed example
- **[Halftone Style Guide](notebooks/03_halftone_style.ipynb)** - Retro dot visualizations
- **[API Reference](docs/API.md)** - Complete API documentation
- **[Quick Start Guide](docs/QUICKSTART.md)** - Fast reference
- **[Halftone Style](docs/HALFTONE_STYLE.md)** - Halftone usage guide
- **[Sea/Lake Masking](docs/SEA_LAKE_MASKING_HALFTONE.md)** - Masking details
- **[Performance Optimization](docs/PERFORMANCE_OPTIMIZATION.md)** - 🚀 NEW: Speed guide
- **[Examples](examples/)** - Ready-to-run scripts

## 🌍 Interesting Locations

Try these coordinates for dramatic results:

### Mountains
- **Mount Everest**: 27.9881, 86.9250
- **Mount Rainier**: 46.8523, -121.7603
- **Mont Blanc**: 45.8326, 6.8652
- **Matterhorn**: 45.9763, 7.6586

### Canyons
- **Grand Canyon**: 36.1069, -112.1129
- **Death Valley**: 36.5323, -116.9325

### Volcanoes
- **Mount St. Helens**: 46.1914, -122.1956
- **Mount Fuji**: 35.3606, 138.7278

### Islands
- **Mayotte**: -12.8275, 45.1662
- **Hawaii**: 19.8207, -155.4680

## 🎯 Use Cases

- 🖼️ **Wall Art** - High-resolution prints
- 💼 **Logos** - Scalable SVG graphics
- 📱 **Wallpapers** - Custom backgrounds
- 🎓 **Education** - Geography visualization
- 🎨 **Art Projects** - Generative art
- 🎁 **Gifts** - Personalized maps

## 💡 Tips

1. **Mountainous terrain**: Use exaggeration 2.5-3.5
2. **Flat areas**: Use exaggeration 4.0-6.0
3. **Logos**: Use SVG format with 30-50 lines
4. **Prints**: Use resolution 150-200 and PNG
5. **Quick previews**: Use resolution 60-80
6. **Dramatic effects**: Use gradient scaling

## 🔧 Troubleshooting

**Slow generation?**
- Reduce `resolution` (try 80)
- Reduce `size_km` (try 10-15)
- Reduce `num_lines` (try 50)

**Lines too flat?**
- Increase `exaggeration` (try 5.0-6.0)
- Use gradient scaling

**Need vector output?**
- Use `format='svg'`
- Perfect for logos and printing

## 🎨 Inspiration

Inspired by:
- Joy Division's iconic "Unknown Pleasures" album cover
- Scientific topographic visualization
- Generative art and data visualization

## 📄 License

MIT License - See LICENSE file

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new features
- Improve documentation
- Report bugs
- Share your creations

---

**Made with ❤️ and Python**

**Start with [Getting Started Notebook](notebooks/01_getting_started.ipynb) →**
