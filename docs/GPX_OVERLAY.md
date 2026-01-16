# GPX Track Overlay Feature

## Overview

The GPX overlay feature allows you to superimpose GPS tracks (from hiking, cycling, running, or any GPS activity) onto your topographic art. This creates personalized maps that combine elevation visualization with your actual routes and journeys.

## Features

- ✅ **Full GPX Support** - Import tracks from any GPS app or device
- ✅ **Automatic Coordinate Conversion** - Lat/lon to image coordinates
- ✅ **Customizable Styling** - Color, width, style, transparency
- ✅ **Works with All Formats** - PNG lines, halftone, and SVG (coming soon)
- ✅ **Smart Clipping** - Only draws track within map bounds
- ✅ **High Resolution** - Perfect for print-quality output

## Quick Start

### Basic Usage

```python
from topomap import TopomapGenerator

generator = TopomapGenerator(output_dir="output")

generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    resolution=150,
    format='halftone',
    
    # ... your regular parameters ...
    
    # GPX overlay
    gpx_file="path/to/your/track.gpx",
    gpx_color='#000000',  # Black
    gpx_width=3.0
)
```

## Parameters

### Required Parameters

- **`gpx_file`** (str): Path to your GPX file
  - Exported from Strava, Garmin, AllTrails, Komoot, etc.
  - Must contain track data (not just waypoints)

### Optional Styling Parameters

- **`gpx_color`** (str, default: `'#000000'`): Track color
  - Hex color code or named color
  - Examples: `'#FF0000'` (red), `'#00FF00'` (green), `'white'`

- **`gpx_width`** (float, default: `2.0`): Line width in pixels
  - Smaller values (1-2) for subtle tracks
  - Larger values (3-5) for prominent routes
  - Very large (6+) for bold artistic effect

- **`gpx_style`** (str, default: `'-'`): Line style
  - `'-'` - Solid line (default)
  - `'--'` - Dashed line
  - `':'` - Dotted line
  - `'-.'` - Dash-dot line

- **`gpx_alpha`** (float, default: `1.0`): Transparency
  - `1.0` - Fully opaque
  - `0.5` - Semi-transparent
  - `0.0` - Fully transparent (invisible)

- **`gpx_zorder`** (int, default: `10`): Drawing order
  - Higher values draw on top
  - `10` ensures track is above the map
  - Decrease if you want track under some elements

## Examples

### Example 1: Hiking Trail on Halftone Map

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=20,
    resolution=200,
    output_filename="hiking_trail.png",
    format='halftone',
    
    # Halftone style
    dot_size_range=(0.5, 8.0),
    grid_spacing=10,
    bg_color='#FFF8F0',      # Cream background
    dot_color='#8B4513',     # Brown dots (earth tones)
    skip_zero_elevation=True,
    
    # Hiking trail overlay
    gpx_file="hike_calanques.gpx",
    gpx_color='#FF0000',     # Red trail
    gpx_width=4.0,           # Bold line
    gpx_alpha=0.9,           # Slightly transparent
    
    figsize=(16, 20),
    dpi=300
)
```

### Example 2: Cycling Route on Traditional Lines

```python
generator.generate(
    latitude=45.8326,
    longitude=6.8652,
    size_km=30,
    resolution=150,
    num_lines=80,
    exaggeration=5.0,
    output_filename="cycling_alps.png",
    format='png',
    
    # Dark mountain theme
    bg_color='#1a1a2e',
    line_color='#e94560',
    line_width=1.5,
    fill_below=True,
    
    # Cycling route
    gpx_file="tour_de_alps.gpx",
    gpx_color='#FFD700',     # Golden route
    gpx_width=5.0,           # Very visible
    gpx_style='--',          # Dashed for style
    gpx_alpha=1.0,
    
    figsize=(14, 18),
    dpi=300
)
```

### Example 3: Running Track with Subtle Overlay

```python
generator.generate(
    latitude=48.8566,
    longitude=2.3522,
    size_km=10,
    resolution=120,
    output_filename="paris_run.png",
    format='halftone',
    
    # Minimalist halftone
    dot_size_range=(0.3, 5.0),
    grid_spacing=12,
    bg_color='#ffffff',
    dot_color='#2c3e50',
    
    # Subtle running track
    gpx_file="paris_marathon.gpx",
    gpx_color='#e74c3c',     # Subtle red
    gpx_width=2.0,           # Thin line
    gpx_alpha=0.7,           # Semi-transparent
    
    figsize=(12, 16),
    dpi=250
)
```

### Example 4: Multi-Day Trek

```python
# Create a series showing your journey progression
for day in range(1, 6):
    generator.generate(
        latitude=27.9881,
        longitude=86.9250,
        size_km=50,
        resolution=200,
        output_filename=f"everest_base_camp_day{day}.png",
        format='halftone',
        
        dot_size_range=(0.5, 10.0),
        grid_spacing=8,
        bg_color='#f0f8ff',
        dot_color='#1e3a8a',
        
        # Each day's GPX file
        gpx_file=f"trek_day_{day}.gpx",
        gpx_color='#ff0000',
        gpx_width=3.5,
        
        title=f"Day {day}",
        figsize=(14, 18),
        dpi=300
    )
```

## Obtaining GPX Files

### From Fitness Apps

Most fitness and hiking apps can export GPX files:

1. **Strava**
   - Open activity → ⚙️ (gear icon) → Export GPX

2. **Garmin Connect**
   - Open activity → ⚙️ → Export → Export to GPX

3. **AllTrails**
   - Open trail → Download GPX

4. **Komoot**
   - Open tour → Share → Export as GPX

5. **Ride with GPS**
   - Open route → Export → GPX Track

6. **Apple Health/Fitness**
   - Use third-party apps like HealthFit to export

### Creating Custom Routes

You can create custom GPX files using:
- **GPX Studio** (gpxstudio.github.io) - Web-based
- **RideWithGPS** - Route planning
- **Komoot** - Trail planning
- **Google Earth** - Save path as KML, convert to GPX

## Color Palette Suggestions

### For Light Backgrounds

```python
# Classic
gpx_color='#000000'  # Black

# Vibrant
gpx_color='#FF0000'  # Red
gpx_color='#0066CC'  # Blue
gpx_color='#FF6600'  # Orange

# Nature
gpx_color='#228B22'  # Forest green
gpx_color='#8B4513'  # Saddle brown
```

### For Dark Backgrounds

```python
# High contrast
gpx_color='#FFFFFF'  # White
gpx_color='#FFD700'  # Gold

# Neon
gpx_color='#00FF00'  # Neon green
gpx_color='#FF1493'  # Deep pink
gpx_color='#00FFFF'  # Cyan

# Pastel
gpx_color='#FFB6C1'  # Light pink
gpx_color='#87CEEB'  # Sky blue
```

### For Artistic Effect

```python
# Complementary to orange halftone
gpx_color='#0066CC'  # Blue (opposite of orange)

# Analogous harmony
gpx_color='#FF0000'  # Red (near orange)
gpx_color='#FFD700'  # Gold (near orange)
```

## Best Practices

### 1. Map Coverage

Ensure your GPX track is within the map bounds:
```python
# If your track spans 15km, make the map at least that size
size_km=20  # Gives some margin around the track
```

### 2. Track Visibility

Choose colors that contrast with your base map:
```python
# Orange dots + black track = good contrast
dot_color='#ff6900'
gpx_color='#000000'

# Dark lines + bright track = good contrast
line_color='#2B1B4D'
gpx_color='#FFD700'
```

### 3. Line Width for Different Uses

```python
# Web/screen (150-250 DPI)
gpx_width=2.0-3.0

# Print/poster (300-600 DPI)
gpx_width=3.0-5.0

# Large format
gpx_width=5.0-8.0
```

### 4. Layering

Use `gpx_zorder` to control overlap:
```python
# Track on top of everything
gpx_zorder=10  # Default

# Track under title/text
gpx_zorder=5

# Track integrated with map
gpx_zorder=2
```

## Troubleshooting

### Issue: "No GPS points found in GPX file"

**Solution:**
- Ensure your GPX file contains `<trk>` (track) data, not just waypoints
- Check the file is not corrupted
- Try re-exporting from your app

### Issue: "Not enough points in map bounds to draw track"

**Solution:**
- Increase `size_km` to cover more area
- Check the latitude/longitude of your map vs. track
- Verify track coordinates are in the right hemisphere

### Issue: Track not visible

**Solution:**
```python
# Increase width
gpx_width=5.0

# Increase contrast
gpx_color='#FF0000'  # Bright red

# Make fully opaque
gpx_alpha=1.0

# Ensure it's on top
gpx_zorder=10
```

### Issue: Track looks pixelated

**Solution:**
```python
# Increase resolution
resolution=200

# Increase DPI
dpi=600

# Smooth the line (automatic with matplotlib)
```

## Use Cases

### Personal Art

- **Memory Maps** - Visualize your favorite hikes, runs, or rides
- **Travel Journals** - Show your journey through mountains
- **Achievement Prints** - Marathon courses, long-distance treks
- **Gift Art** - Create personalized maps for outdoor enthusiasts

### Professional Use

- **Trail Guides** - Official trail maps with elevation context
- **Race Courses** - Ultra-marathon or cycling race visualizations
- **Tourism** - Promotional materials for hiking destinations
- **Education** - Geography lessons with real-world routes

### Social Media

Perfect for sharing your adventures:
- Instagram posts with your route
- Strava art that stands out
- Blog illustrations
- YouTube thumbnails

## Advanced Techniques

### Multiple Tracks

To overlay multiple GPX tracks, call the generation multiple times or use image editing:

```python
# Generate base map
base_map = generator.generate(...)

# Load and composite in post-processing
# (future feature: native multi-track support)
```

### Animated Routes

Create a series showing route progression:

```python
# Split GPX into segments
for segment in range(1, 11):
    generator.generate(
        ...,
        gpx_file=f"route_segment_{segment}.gpx",
        output_filename=f"frame_{segment:03d}.png"
    )

# Combine frames into video/GIF with ffmpeg or similar
```

### Custom GPX Processing

```python
from topomap import TopomapGenerator

gen = TopomapGenerator()

# Load and process GPX manually
points = gen.load_gpx_track("mytrack.gpx")

# Filter, smooth, or modify points
filtered_points = [p for p in points if elevation_filter(p)]

# Use custom overlay logic
# (See source code for implementation details)
```

## Technical Details

### Coordinate Conversion

The overlay feature automatically converts:
1. GPX lat/lon (WGS84) → Map bounds
2. Normalized coordinates → Image pixels
3. Y-axis inversion (geo up vs. image down)

### Performance

- GPX loading: < 1 second for typical files
- Coordinate conversion: < 0.1 seconds for 1000 points
- Rendering: Included in normal map generation time

### Limitations

- Currently supports track segments (`<trk>`)
- Waypoints (`<wpt>`) not visualized (future feature)
- Routes (`<rte>`) not supported (future feature)
- SVG output: GPX overlay coming soon

## Future Enhancements

Planned features:
- [ ] Multiple GPX tracks in single map
- [ ] Waypoint markers with labels
- [ ] Elevation profile alongside map
- [ ] SVG format support
- [ ] Interactive web output
- [ ] GPX statistics overlay (distance, elevation gain)
- [ ] Start/end markers
- [ ] Direction arrows

---

**Start creating personalized topographic art with your GPS adventures! 🗺️🚶‍♂️🚴‍♀️**
