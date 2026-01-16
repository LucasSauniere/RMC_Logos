# Ridge Map Usage Guide

## Creating Joy Division Style Topographic Art

This document explains how to use the `ridge_map` library to create iconic "Unknown Pleasures" style visualizations in notebook `05_joydivision_style.ipynb`.

## What is ridge_map?

`ridge_map` is a Python library specifically designed to create ridgeline plots (Joy Division plots) from elevation data. It automatically fetches SRTM elevation data and creates beautiful visualizations with proper line occlusion.

## Installation

```bash
pip install ridge_map
```

## Basic Usage

### 1. Import the Library

```python
from ridge_map import RidgeMap
import matplotlib.pyplot as plt
```

### 2. Define a Bounding Box

Use [bboxfinder.com](http://bboxfinder.com) to find coordinates:

```python
# Format: (lon_min, lat_min, lon_max, lat_max)
bbox = (5.29, 43.22, 5.45, 43.37)  # Marseille, ~15km x 15km
```

### 3. Create a RidgeMap

```python
rm = RidgeMap(bbox=bbox)
```

### 4. Get Elevation Data

```python
values = rm.get_elevation_data(
    num_lines=80,       # Number of horizontal lines
    elevation_pts=300   # Points per line
)
```

### 5. Plot the Map

```python
fig, ax = plt.subplots(figsize=(12, 16))

rm.plot_map(
    values=values,
    label='MARSEILLE',
    label_x=0.55,
    label_y=0.12,
    label_size=70,
    line_color='white',
    background_color='black',
    kind='elevation',
    linewidth=1.5,
    ax=ax
)

plt.savefig('output.png', dpi=300, facecolor='black')
plt.show()
```

## Key Parameters

### RidgeMap.__init__()

- **bbox**: `(lon_min, lat_min, lon_max, lat_max)` - Geographic bounding box
- **font**: Optional custom font (defaults to Cinzel Regular)

### get_elevation_data()

- **num_lines**: Number of horizontal ridgelines (40-120 typical)
- **elevation_pts**: Points per line (200-500 typical)
- **viewpoint_angle**: Rotation angle in degrees (0-360)
- **crop**: Whether to crop corners when rotating
- **interpolation**: Smoothing level (0-5, use 0 or 1)

### plot_map()

- **values**: Elevation array from `get_elevation_data()`
- **label**: Title text
- **label_x**, **label_y**: Label position (0-1)
- **label_size**: Font size for title
- **label_color**: Label color (defaults to line_color)
- **line_color**: Line color (hex, name, or RGB tuple)
- **background_color**: Background (hex, name, or RGB 0-1)
- **kind**: `'elevation'` (uniform) or `'gradient'` (fading)
- **linewidth**: Line thickness (1-3 typical)
- **size_scale**: Overall size scaling

### plot_annotation()

- **label**: Annotation text
- **coordinates**: `(longitude, latitude)` of point
- **x_offset**, **y_offset**: Label offset from point
- **label_size**: Annotation text size
- **annotation_size**: Marker size
- **color**: Color of annotation
- **background**: Whether to add background to label

## Examples from Notebook 05

### Classic Joy Division (White on Black)

```python
marseille_bbox = (5.29, 43.22, 5.45, 43.37)
rm = RidgeMap(bbox=marseille_bbox)
values = rm.get_elevation_data(num_lines=80, elevation_pts=300)

fig, ax = plt.subplots(figsize=(12, 16))
rm.plot_map(
    values=values,
    label='MARSEILLE',
    line_color='white',
    background_color='black',
    kind='elevation',
    linewidth=1.5,
    ax=ax
)
plt.savefig('marseille_classic.png', dpi=300, facecolor='black')
```

### Inverted Style (Black on White)

```python
rm.plot_map(
    values=values,
    label='MARSEILLE',
    line_color='black',
    background_color='white',
    kind='elevation',
    linewidth=1.5,
    ax=ax
)
plt.savefig('marseille_inverted.png', dpi=300, facecolor='white')
```

### Colorful Variations

```python
# Neon Green
rm.plot_map(
    values=values,
    line_color='#00ff00',
    background_color='black',
    kind='elevation',
    linewidth=1.5,
    ax=ax
)

# Hot Magenta on Dark Purple
rm.plot_map(
    values=values,
    line_color='#ff1493',
    background_color=(0.05, 0.01, 0.13),  # RGB tuple
    kind='elevation',
    linewidth=1.5,
    ax=ax
)
```

### Gradient Style

```python
rm.plot_map(
    values=values,
    label='MARSEILLE',
    line_color='#ffd700',  # Gold
    background_color=(0.1, 0.1, 0.18),
    kind='gradient',  # Fading lines!
    linewidth=2.0,
    ax=ax
)
```

### With Annotations

```python
rm.plot_map(values=values, line_color='white', background_color='black', ax=ax)

# Add landmark
rm.plot_annotation(
    label='Notre-Dame\nde la Garde',
    coordinates=(5.3709, 43.2842),
    x_offset=0.05,
    y_offset=0.02,
    label_size=16,
    color='white',
    ax=ax
)
```

## Tips & Best Practices

### Finding Bounding Boxes

1. Go to [bboxfinder.com](http://bboxfinder.com)
2. Navigate to your location
3. Draw a box around the area
4. Copy coordinates in the format shown
5. Use as `bbox = (lon_min, lat_min, lon_max, lat_max)`

**Size Guidelines:**
- Small (5-10km): ±0.05 degrees
- Medium (15-20km): ±0.10 degrees
- Large (30-50km): ±0.20 degrees

### Parameter Selection

**For flat terrain (coastal, plains):**
```python
num_lines = 60-80
elevation_pts = 300
linewidth = 1.5
```

**For mountains (dramatic relief):**
```python
num_lines = 100-120
elevation_pts = 400-500
linewidth = 1.2
```

**For minimalist art:**
```python
num_lines = 30-50
elevation_pts = 200
linewidth = 2.0
```

### Color Schemes

**Classic combinations:**
- White on black: `line_color='white'`, `background_color='black'`
- Black on white: `line_color='black'`, `background_color='white'`

**Modern vibrant:**
- Neon green: `'#00ff00'` on black
- Hot magenta: `'#ff1493'` on dark purple `(0.05, 0.01, 0.13)`
- Cyan: `'#00ffff'` on navy `(0.04, 0.05, 0.15)`

**Metallic:**
- Gold: `'#ffd700'` on dark gray
- Silver: `'#c0c0c0'` on black
- Bronze: `'#cd7f32'` on brown

### Saving Files

**Always match facecolor to background:**
```python
plt.savefig(
    'output.png',
    dpi=300,
    bbox_inches='tight',
    facecolor='black'  # Match your background_color!
)
```

**DPI recommendations:**
- Web/screen: 150-200
- Print: 300
- High-quality poster: 600

### Performance

**First run is slower:**
- Elevation data is downloaded from SRTM servers
- Data is cached locally for subsequent runs
- Be patient on first generation (~30-60 seconds)

**Faster rendering:**
- Lower `num_lines` (50-70)
- Lower `elevation_pts` (200-250)
- Smaller bounding box

**Best quality:**
- Higher `num_lines` (100-150)
- Higher `elevation_pts` (400-500)
- But slower to render

## Common Issues

### "No elevation data available"

**Problem:** SRTM data not available for area  
**Solution:** Check your bbox coordinates, ensure format is `(lon, lat, lon, lat)`

### Lines look jagged

**Problem:** Not enough elevation points  
**Solution:** Increase `elevation_pts` to 400-500

### Rendering is slow

**Problem:** Too many lines or points  
**Solution:** Decrease `num_lines` to 60-80 and `elevation_pts` to 250-300

### Background color wrong in saved file

**Problem:** Didn't set `facecolor` when saving  
**Solution:** Add `facecolor` parameter to `plt.savefig()`

### Label is off-screen

**Problem:** Label position outside 0-1 range  
**Solution:** Adjust `label_x` and `label_y` between 0 and 1

## Use Cases

Perfect for:
- 🎵 Album covers (Unknown Pleasures homage)
- 🖼️ Wall art and posters
- 👕 T-shirt designs and merchandise
- 📱 Digital wallpapers
- 🎁 Personalized location gifts
- 📚 Scientific publications
- 🏢 Location-based branding

## Resources

- **ridge_map GitHub**: https://github.com/ColCarroll/ridge_map
- **bbox finder**: http://bboxfinder.com
- **SRTM Data**: Global 90m resolution elevation data
- **Joy Division cover**: Original inspiration from 1979 album

## Examples in This Repository

See notebook `05_joydivision_style.ipynb` for:
- ✅ Classic black & white Joy Division style
- ✅ Inverted color schemes
- ✅ Dramatic terrain (Calanques cliffs)
- ✅ Colorful modern variations
- ✅ Gradient line styles
- ✅ Line density comparisons
- ✅ Annotated maps with landmarks

Generated output files are in the `output/` directory:
- `marseille_ridgemap_classic.png`
- `marseille_ridgemap_inverted.png`
- `marseille_calanques_ridgemap.png`
- `marseille_ridgemap_*.png` (colorful variations)
- `marseille_ridgemap_gradient.png`
- `marseille_ridgemap_density_*.png`
- `marseille_ridgemap_annotated.png`

## Credits

- **ridge_map library**: Colin Carroll
- **Original design**: Peter Saville (Joy Division album)
- **Original data**: Harold Craft (CP 1919 pulsar data)
- **Elevation data**: NASA SRTM mission

---

**Happy ridge mapping! 🎵🏔️**
