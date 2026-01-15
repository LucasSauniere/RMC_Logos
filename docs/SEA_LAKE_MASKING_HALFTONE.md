# Sea and Lake Masking in Halftone Style

## Overview

The halftone visualization feature **automatically removes dots over water bodies** by default. This creates clean, professional visualizations where seas, oceans, and lakes appear as blank space, with dots only on land areas.

## How It Works

### The Parameter

```python
skip_zero_elevation=True  # Default behavior
```

When enabled (which is the default), dots are only drawn where elevation > 0 meters.

### What Gets Masked

- **Seas and Oceans** - Below sea level (0m)
- **Coastal Waters** - At sea level (0m)
- **Lakes at Sea Level** - Or below (e.g., Dead Sea at -430m)
- **Any Water Body** - With elevation ≤ 0m

### What Doesn't Get Masked

- **Elevated Lakes** - Above sea level (e.g., Lake Tahoe at 1,897m)
- **All Land** - Even very flat coastal plains (e.g., 1m elevation)

## Visual Comparison

```
WITH Masking (skip_zero_elevation=True):
┌─────────────────────────────────┐
│ ● ●● ●●● ●●●● ●●●● ●●● ●● ●    │  Land (dots)
│ ● ●●● ●●●● ●●●●● ●●● ● ●       │  Land (dots)
│  ● ●●● ●●●●● ●●● ●●            │  Land (dots)
│   ●● ●●●● ●●● ●● ●             │  Coastal area
│                                 │  Sea (blank)
│                                 │  Sea (blank)
└─────────────────────────────────┘

WITHOUT Masking (skip_zero_elevation=False):
┌─────────────────────────────────┐
│ ● ●● ●●● ●●●● ●●●● ●●● ●● ●    │  Land (dots)
│ ● ●●● ●●●● ●●●●● ●●● ● ●       │  Land (dots)
│  ● ●●● ●●●●● ●●● ●●            │  Land (dots)
│   ●● ●●●● ●●● ●● ●             │  Coastal area
│    ● ● ● ● ● ● ● ● ● ● ●       │  Sea (small dots)
│    ● ● ● ● ● ● ● ● ● ● ●       │  Sea (small dots)
└─────────────────────────────────┘
```

## Usage Examples

### Example 1: Coastal City (Recommended)

```python
generator.generate(
    latitude=43.2965,  # Marseille
    longitude=5.3698,
    size_km=15,
    output_filename="marseille.png",
    format='halftone',
    skip_zero_elevation=True,  # Clean coastlines! ✨
    dot_size_range=(0.5, 8.0),
    grid_spacing=10
)
```

**Result**: The Mediterranean Sea appears as blank white space, with dots only on land.

### Example 2: Island Nation

```python
generator.generate(
    latitude=-12.8275,  # Mayotte
    longitude=45.1662,
    size_km=20,
    output_filename="mayotte.png",
    format='halftone',
    skip_zero_elevation=True,  # Essential for islands!
    dot_size_range=(0.5, 10.0),
    grid_spacing=10
)
```

**Result**: Island landmass clearly visible, surrounded by blank ocean.

### Example 3: Disable Masking (Not Recommended)

```python
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    output_filename="marseille_no_mask.png",
    format='halftone',
    skip_zero_elevation=False,  # Dots everywhere
    dot_size_range=(0.5, 8.0),
    grid_spacing=10
)
```

**Result**: Small dots appear over the sea (flat = small dots), creating visual clutter.

## Technical Details

### Implementation

The masking happens in the `create_halftone()` method:

```python
# For each dot position
if skip_zero_elevation and elevation_raw <= 0:
    continue  # Skip this dot
```

### Elevation Data Source

- Uses **SRTM** (Shuttle Radar Topography Mission) data
- Resolution: ~30m to 90m depending on location
- Sea level is defined as 0 meters
- Oceans and seas typically have elevation = 0 or NaN (converted to 0)

### Edge Cases

1. **Dead Sea (-430m)**: Correctly masked (below 0)
2. **Death Valley (-86m)**: Correctly masked (below 0)
3. **Flat coastal plains (0.5m)**: NOT masked (above 0)
4. **Elevated lakes (>0m)**: NOT masked (have elevation)

## Why This Is Important

### For Coastal Areas

Without masking, coastal visualizations look cluttered:
- Small dots cover the sea (since sea is "flat")
- Hard to distinguish land from water
- Less professional appearance

With masking, you get:
- ✅ Clean coastlines
- ✅ Clear land/water boundary
- ✅ Professional, gallery-quality output

### For Islands

Masking is **essential** for island visualizations:
- Shows island shape clearly
- Ocean appears as negative space
- Creates dramatic visual impact

## Comparison with Line Style

Both styles support sea/lake masking:

### Line Style
```python
generator.generate(
    ...,
    format='png',
    skip_zero_elevation=True  # Lines skip over sea
)
```

### Halftone Style
```python
generator.generate(
    ...,
    format='halftone',
    skip_zero_elevation=True  # Dots skip over sea
)
```

Both create clean coastal visualizations!

## Best Practices

### Always Use Masking For:
- ✅ Coastal cities
- ✅ Islands
- ✅ Peninsulas
- ✅ Lake regions
- ✅ Any area with water bodies

### Consider Disabling For:
- ⚠️ Landlocked mountainous areas (no water anyway)
- ⚠️ Experimental/abstract art (if you want full coverage)
- ⚠️ Scientific visualization where you need to see "zero" elevation

### Recommended Default:
```python
skip_zero_elevation=True  # Always recommended!
```

## Performance Impact

Masking has **minimal performance impact**:
- Skipping dots is faster than drawing them
- Slightly faster render times with masking enabled
- No quality degradation

## Troubleshooting

### Problem: I still see dots over the sea

**Possible causes:**
1. `skip_zero_elevation=False` - Check your parameters
2. Elevation data quality issues - SRTM may have voids
3. Very shallow water (>0m) - Technically above sea level

**Solution:**
```python
skip_zero_elevation=True  # Ensure this is set
```

### Problem: Inland lakes are not masked

**This is correct behavior!**

Elevated lakes (above sea level) are NOT masked because:
- They have elevation > 0
- They are topographically part of the landscape
- Masking them would create holes in your visualization

If you want to mask specific lakes, you'd need custom elevation data processing.

### Problem: Some coastal areas are masked

**Possible causes:**
1. Very low-lying coastal areas (at or below 0m)
2. Areas subject to tidal flooding
3. SRTM data resolution limitations

**This is usually correct** - these areas are at or below sea level.

## Integration with Other Features

Sea/lake masking works seamlessly with:
- ✅ **All color schemes** - Masked areas show background color
- ✅ **Inverted patterns** - Masking still applies
- ✅ **Any dot size range** - Masking happens before sizing
- ✅ **Grid spacing** - Masking works at any density
- ✅ **Smoothing** - Applied before masking check

## Examples in the Notebook

The `notebooks/03_halftone_style.ipynb` notebook now includes:
- Section 2: Explanation of automatic sea/lake masking
- Section 3: Side-by-side comparison (masking ON vs OFF)
- Multiple examples showing clean coastlines

## Summary

**Key Points:**
1. ✅ Masking is **ON by default** (`skip_zero_elevation=True`)
2. ✅ Creates **clean, professional** coastal visualizations
3. ✅ Works for seas, oceans, and lakes at/below sea level
4. ✅ **Minimal performance impact**
5. ✅ Works with **all halftone features**

**When in doubt, leave masking enabled!**

It's the recommended default for 99% of use cases, especially coastal areas like Marseille, islands, and any location with visible water bodies.

---

**Happy mapping! 🗺️🌊**
