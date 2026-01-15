# Halftone Style Topographic Visualization

## Overview

The halftone style visualization uses dots of varying sizes to represent elevation data, creating a newspaper/print-style artistic effect reminiscent of vintage comics, pop art, and traditional print media.

## What is Halftone?

Halftone is a printing technique that simulates continuous tones using dots of varying sizes. In our implementation:
- **Larger dots** represent higher elevations
- **Smaller dots** represent lower elevations  
- **No dots** represent sea level or areas below the threshold

This creates a unique, retro aesthetic that's perfect for artistic projects, print media, and pop art style visualizations.

## Usage

### Basic Example

```python
from topomap import TopomapGenerator

generator = TopomapGenerator()

# Generate halftone map
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    output_filename="marseille_halftone.png",
    format='halftone',  # Use halftone style!
    
    # Halftone-specific parameters
    dot_size_range=(0.5, 8.0),    # Min/max dot sizes
    grid_spacing=10,               # Distance between dots
    bg_color='#ffffff',            # White background
    dot_color='#000000',           # Black dots
    invert=False,                  # Normal pattern
    skip_zero_elevation=True       # Skip sea areas
)
```

## Parameters

### Halftone-Specific Parameters

#### `format='halftone'`
**Required**. Specifies halftone rendering instead of lines or SVG.

#### `dot_size_range=(min, max)`
**Default**: `(0.5, 8.0)`

Controls the size range of dots in pixels:
- `min`: Minimum dot size (for lowest elevations)
- `max`: Maximum dot size (for highest elevations)

**Examples:**
```python
# Subtle effect
dot_size_range=(0.5, 3.0)

# Balanced (recommended)
dot_size_range=(0.5, 8.0)

# Dramatic effect
dot_size_range=(1.0, 15.0)

# Extreme/abstract
dot_size_range=(2.0, 25.0)
```

#### `grid_spacing=pixels`
**Default**: `10`

Distance between dot centers in pixels. Controls density:

```python
# Dense (high detail, slower)
grid_spacing=5-8

# Balanced (recommended)
grid_spacing=10-12

# Sparse (minimalist, faster)
grid_spacing=15-20

# Very sparse (abstract)
grid_spacing=25-40
```

**Performance Note:** Smaller spacing = more dots = longer render time.

#### `bg_color=color`
**Default**: `'#ffffff'` (white)

Background color. Supports hex codes, named colors, or RGB tuples.

#### `dot_color=color`
**Default**: `'#000000'` (black)

Dot color. Supports hex codes, named colors, or RGB tuples.

#### `invert=bool`
**Default**: `False`

Reverse the dot size pattern:
- `False`: Larger dots = higher elevation (normal)
- `True`: Larger dots = lower elevation (inverted)

#### `skip_zero_elevation=bool`
**Default**: `True`

Skip drawing dots where elevation is ≤ 0 meters (sea level).

### Standard Parameters

All standard parameters still apply:
- `latitude`, `longitude`: Center coordinates
- `size_km`: Area size in kilometers
- `resolution`: Elevation sample resolution
- `smoothing`: Apply Gaussian smoothing
- `figsize`: Figure size in inches
- `dpi`: Output resolution

## Examples

### 1. Classic Black & White

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    output_filename="classic_halftone.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#ffffff',
    dot_color='#000000'
)
```

### 2. Inverted (White on Black)

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    output_filename="inverted_halftone.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#000000',  # Black background
    dot_color='#ffffff'   # White dots
)
```

### 3. Pop Art Red

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    output_filename="popart_halftone.png",
    format='halftone',
    dot_size_range=(0.5, 10.0),
    grid_spacing=10,
    bg_color='#fff5f5',  # Light pink
    dot_color='#dc143c'   # Crimson red
)
```

### 4. Sepia Vintage

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=100,
    output_filename="vintage_halftone.png",
    format='halftone',
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#f5e6d3',  # Tan/cream
    dot_color='#704214'   # Brown
)
```

### 5. High-Resolution Print

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=150,      # High resolution
    output_filename="print_halftone.png",
    format='halftone',
    dot_size_range=(0.3, 6.0),
    grid_spacing=6,      # Dense
    bg_color='#ffffff',
    dot_color='#000000',
    figsize=(16, 20),    # Large format
    dpi=600              # Print quality
)
```

### 6. Minimalist Abstract

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=20,
    resolution=60,       # Lower resolution
    output_filename="abstract_halftone.png",
    format='halftone',
    dot_size_range=(2.0, 20.0),  # Large dots
    grid_spacing=25,              # Very sparse
    bg_color='#ffffff',
    dot_color='#000000'
)
```

## Parameter Recommendations

### By Terrain Type

#### Flat Coastal Areas
```python
dot_size_range=(0.5, 10.0)  # Wide range to show subtle changes
grid_spacing=10
resolution=80-100
```

#### Mountainous Terrain
```python
dot_size_range=(0.3, 15.0)  # Very wide range for drama
grid_spacing=6-8            # Dense for detail
resolution=120-150
```

#### Rolling Hills
```python
dot_size_range=(0.5, 8.0)   # Medium range
grid_spacing=10-12
resolution=100
```

### By Use Case

#### Web/Screen Display
```python
grid_spacing=10-12
figsize=(10, 12)
dpi=150-250
resolution=80-100
```

#### Print/Poster
```python
grid_spacing=6-8
figsize=(16, 20)
dpi=600
resolution=150-200
```

#### Social Media
```python
grid_spacing=12-15
figsize=(8, 10)
dpi=150
resolution=60-80
```

#### Gallery/Exhibition
```python
grid_spacing=4-6
figsize=(20, 24)
dpi=600-1200
resolution=200+
```

### By Artistic Style

#### Classic Halftone
```python
bg_color='#ffffff'
dot_color='#000000'
dot_size_range=(0.5, 8.0)
grid_spacing=10
```

#### Pop Art
```python
bg_color='#fff5f5'  # Light background
dot_color='#dc143c'  # Bright color
dot_size_range=(0.5, 12.0)
grid_spacing=10
```

#### Vintage/Retro
```python
bg_color='#f5e6d3'  # Sepia tone
dot_color='#704214'
dot_size_range=(0.5, 8.0)
grid_spacing=10-12
```

#### Abstract/Minimal
```python
bg_color='#ffffff'
dot_color='#000000'
dot_size_range=(2.0, 25.0)  # Large dots
grid_spacing=20-30          # Sparse
```

## Color Schemes

### Recommended Combinations

```python
# Classic
{"bg": "#ffffff", "dot": "#000000"}  # Black on white
{"bg": "#000000", "dot": "#ffffff"}  # White on black

# Pop Art
{"bg": "#fff5f5", "dot": "#dc143c"}  # Red
{"bg": "#f0f8ff", "dot": "#1e3a8a"}  # Blue
{"bg": "#fffacd", "dot": "#ff6b35"}  # Orange

# Vintage
{"bg": "#f5e6d3", "dot": "#704214"}  # Sepia
{"bg": "#faf0e6", "dot": "#8b4513"}  # Brown

# Neon
{"bg": "#1a0a1a", "dot": "#ff1493"}  # Pink
{"bg": "#0a0a1a", "dot": "#00ff00"}  # Green
{"bg": "#0a1a1a", "dot": "#00ffff"}  # Cyan
```

## Performance Considerations

### Render Time Factors

The number of dots affects rendering time:

```
Number of dots ≈ (resolution / grid_spacing)²
```

**Examples:**
- `resolution=100, grid_spacing=10`: ~100 dots, ~5-10 seconds
- `resolution=100, grid_spacing=5`: ~400 dots, ~15-30 seconds
- `resolution=150, grid_spacing=6`: ~625 dots, ~30-60 seconds

### Optimization Tips

1. **For testing**: Use lower resolution and larger grid_spacing
2. **For final output**: Increase resolution and decrease grid_spacing
3. **Balance**: `resolution=100, grid_spacing=10` is usually good

## Comparison: Lines vs Halftone

| Aspect | Lines | Halftone |
|--------|-------|----------|
| **Style** | Modern, clean | Retro, artistic |
| **Detail** | Continuous | Dotted/discrete |
| **Aesthetic** | Joy Division | Pop art/comics |
| **Best for** | Technical, modern | Artistic, vintage |
| **Render time** | Fast | Medium |
| **Print** | Good | Excellent |
| **Resolution** | Scalable | Fixed grid |

## Technical Details

### Implementation

The halftone renderer:
1. Creates a regular grid of positions
2. Samples elevation at each position
3. Calculates dot size based on elevation
4. Skips dots where elevation ≤ 0 (if enabled)
5. Draws circles at each position

### Formula

```python
if invert:
    dot_size = min_size + (1 - normalized_elevation) * size_range
else:
    dot_size = min_size + normalized_elevation * size_range
```

Where:
- `normalized_elevation` ∈ [0, 1]
- `size_range = max_size - min_size`

## Troubleshooting

### Issue: Dots too small/invisible
**Solution**: Increase `dot_size_range` maximum value

### Issue: Dots overlapping too much
**Solution**: Increase `grid_spacing` or decrease `dot_size_range`

### Issue: Not enough detail
**Solution**: Decrease `grid_spacing` or increase `resolution`

### Issue: Slow rendering
**Solution**: Increase `grid_spacing` or decrease `resolution`

### Issue: Can't see elevation differences
**Solution**: Increase `dot_size_range` spread (wider range)

## Examples Gallery

See the `notebooks/03_halftone_style.ipynb` notebook for:
- Complete examples
- Parameter comparisons
- Color scheme variations
- Step-by-step tutorials
- Best practices

## Related Documentation

- `docs/ZERO_ELEVATION_MASKING.md` - How sea-level masking works
- `notebooks/01_getting_started.ipynb` - General introduction
- `notebooks/02_marseille_example.ipynb` - Traditional line style
- `notebooks/03_halftone_style.ipynb` - Halftone tutorial

## Conclusion

Halftone style visualization offers a unique, artistic way to represent elevation data. It's perfect for:
- 🎨 Art projects and exhibitions
- 📰 Retro/vintage aesthetics  
- 🖼️ Print media and posters
- 💿 Album covers and branding
- 📚 Book illustrations
- 👕 Textile and apparel design

Experiment with parameters to find your perfect style!
