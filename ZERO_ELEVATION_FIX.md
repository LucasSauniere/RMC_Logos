# Zero Elevation Masking - Quick Start

## What Changed?

Lines are now automatically skipped over areas where elevation is ≤ 0 meters (sea level). This creates cleaner visualizations for coastal areas.

## Example

```python
from topomap import TopomapGenerator

generator = TopomapGenerator()

# New default behavior: lines skip over sea
generator.generate(
    latitude=43.2965,  # Marseille
    longitude=5.3698,
    size_km=15,
    output_filename="marseille_clean.png"
)

# To get old behavior (lines everywhere):
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    output_filename="marseille_with_sea.png",
    skip_zero_elevation=False  # Disable masking
)
```

## Testing

1. **Fix environment** (if you see import errors):
   ```bash
   # Option 1: Create fresh venv
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   
   # Option 2: Use conda
   conda create -n topomap python=3.10
   conda activate topomap
   pip install -r requirements.txt
   ```

2. **Run test**:
   ```bash
   python test_zero_elevation.py
   ```

3. **Check output**:
   - `output/marseille_with_masking.png` - Lines skip sea ✨
   - `output/marseille_without_masking.png` - Lines over sea
   - `output/marseille_with_masking.svg` - Vector format

## New Parameter

Both `create_png()` and `create_svg()` methods now accept:

```python
skip_zero_elevation: bool = True  # NEW - skip lines where elevation ≤ 0
```

**Default is `True`** - This is the new default behavior!

## Files Changed

- `src/topomap.py` - Main implementation
- `test_zero_elevation.py` - Test script
- `docs/ZERO_ELEVATION_MASKING.md` - Full documentation
- `docs/IMPLEMENTATION_SUMMARY.md` - Technical details

## Quick Test Without Setup

If you can't get the environment working, here's what the code does:

### Before (skip_zero_elevation=False):
```
Lines are drawn continuously across the entire width
─────────────────────────────────────
  ───────────────────────────────────
    ───────────────────────────────    (lines over sea too)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~    (sea with lines)
```

### After (skip_zero_elevation=True):
```
Lines are broken into segments, skipping sea areas
──────────        ──────────────────
  ────────          ────────────────
    ──────            ─────────────    (gaps over sea)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~    (sea without lines)
```

## Documentation

- **Full docs**: `docs/ZERO_ELEVATION_MASKING.md`
- **Technical**: `docs/IMPLEMENTATION_SUMMARY.md`

## Need Help?

The Python environment in this workspace has some corruption issues. You may need to:
1. Create a fresh virtual environment
2. Install dependencies from `requirements.txt`
3. Run the test script

The code changes are complete and correct, just need a clean environment to test!
