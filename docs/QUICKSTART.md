# Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Test the Installation
```bash
micromamba run -n topomap python test_v2.py
```
This will generate a test map of Yosemite Valley and verify everything works.

### Step 2: Create Your First Custom Map
Edit `simple_example.py` and change these values:
```python
LATITUDE = 48.8566      # Your location's latitude
LONGITUDE = 2.3522      # Your location's longitude
SIZE_KM = 15            # Size of area (10-30 km recommended)
TITLE = "MY MAP"        # Your map title
```

Then run:
```bash
micromamba run -n topomap python simple_example.py
```

### Step 3: Check Your Output
Your maps will be saved in the `output/` directory!

---

## 📍 Interesting Locations to Try

### Mountains
```python
# Mount Everest
LATITUDE, LONGITUDE = 27.9881, 86.9250
EXAGGERATION = 3.0

# Mount Fuji
LATITUDE, LONGITUDE = 35.3606, 138.7278
EXAGGERATION = 4.0

# Matterhorn
LATITUDE, LONGITUDE = 45.9763, 7.6586
EXAGGERATION = 3.5
```

### Canyons
```python
# Grand Canyon
LATITUDE, LONGITUDE = 36.1069, -112.1129
EXAGGERATION = 5.0

# Death Valley
LATITUDE, LONGITUDE = 36.5323, -116.9325
EXAGGERATION = 5.0
```

### Volcanoes
```python
# Mount St. Helens
LATITUDE, LONGITUDE = 46.1914, -122.1956
EXAGGERATION = 4.0

# Mauna Kea (Hawaii)
LATITUDE, LONGITUDE = 19.8207, -155.4680
EXAGGERATION = 4.0
```

### Coastal Features
```python
# Big Sur Coast
LATITUDE, LONGITUDE = 36.2704, -121.8081
EXAGGERATION = 4.5

# Norwegian Fjords
LATITUDE, LONGITUDE = 61.0, 7.0
EXAGGERATION = 4.0
```

---

## 🎨 Style Variations

### Classic Joy Division Style
```python
BACKGROUND_COLOR = '#2B1B4D'  # Deep purple
LINE_COLOR = 'white'
LINE_WIDTH = 1.5
SMOOTHING = True
```

### Minimal Black & White
```python
BACKGROUND_COLOR = '#000000'  # Black
LINE_COLOR = 'white'
LINE_WIDTH = 1.0
SMOOTHING = True
```

### Neon Green on Black
```python
BACKGROUND_COLOR = '#000000'  # Black
LINE_COLOR = '#00ff00'        # Bright green
LINE_WIDTH = 1.5
SMOOTHING = True
```

### Retro Cyan
```python
BACKGROUND_COLOR = '#0a0e27'  # Dark navy
LINE_COLOR = '#00ffff'        # Cyan
LINE_WIDTH = 1.5
SMOOTHING = True
```

### Gold on Black
```python
BACKGROUND_COLOR = '#000000'  # Black
LINE_COLOR = '#ffd700'        # Gold
LINE_WIDTH = 2.0
SMOOTHING = True
```

---

## ⚙️ Performance Tips

### For Quick Testing
```python
RESOLUTION = 80       # Lower resolution
SIZE_KM = 10          # Smaller area
NUM_LINES = 50        # Fewer lines
```

### For Final Output
```python
RESOLUTION = 150      # Higher resolution
SIZE_KM = 20          # Medium area
NUM_LINES = 100       # More lines
```

### For Large Prints
```python
RESOLUTION = 200      # Very high resolution
SIZE_KM = 25          # Larger area
NUM_LINES = 120       # Many lines
```

---

## 🐛 Common Issues

### "No elevation data"
- Try a different location
- Check that coordinates are on land (not ocean)
- Verify internet connection

### Too slow
- Reduce `RESOLUTION` (try 80)
- Reduce `SIZE_KM` (try 10-15)
- Reduce `NUM_LINES` (try 50-60)

### Lines too flat
- Increase `EXAGGERATION` to 5.0 or 6.0
- Ensure location has terrain variation

### Lines too spiky
- Decrease `EXAGGERATION` to 2.0 or 2.5
- Enable `SMOOTHING = True`

---

## 📂 File Organization

```
Club_RMC/
├── simple_example.py          ← EDIT THIS to create custom maps
├── test_v2.py                 ← Run this first to test
├── topomap_generator_v2.py    ← Main code (don't need to edit)
├── README.md                  ← Full documentation
├── QUICKSTART.md              ← This file
└── output/                    ← Your maps appear here!
```

---

## 🎯 Pro Tips

1. **Start Small**: Use low resolution for testing, increase for final output
2. **Experiment**: Try different exaggeration values for different terrains
3. **Smooth It Out**: Enable smoothing for cleaner, more artistic results
4. **Color Schemes**: Dark backgrounds with bright lines work best
5. **Location Matters**: Mountain ranges and canyons look most dramatic
6. **Aspect Ratio**: Keep SIZE_KM between 10-30 for best results

---

## 💡 Want to Learn More?

- Check `README.md` for full documentation
- Look at `topomap_generator_v2.py` to understand the code
- Experiment with different locations and settings!

---

**Now go create some amazing topographic art! 🗺️✨**
