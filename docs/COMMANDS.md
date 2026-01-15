# Command Reference

Quick reference for all available commands in this project.

---

## 🔧 Environment Management

### Activate Environment
```bash
micromamba activate topomap
```

### Deactivate Environment
```bash
micromamba deactivate
```

### Run Command Without Activating
```bash
micromamba run -n topomap python your_script.py
```

### Check Environment Info
```bash
micromamba info -e
```

### List Installed Packages
```bash
micromamba list -n topomap
```

---

## 🧪 Testing & Verification

### Run Installation Test
```bash
micromamba run -n topomap python test_v2.py
```
Generates a test map of Yosemite Valley.

---

## 🗺️ Generate Maps

### Quick Custom Map
```bash
# 1. Edit simple_example.py with your location
# 2. Run:
micromamba run -n topomap python simple_example.py
```

### Mayotte Example (From Your Image)
```bash
micromamba run -n topomap python generate_mayotte.py
```

### Multiple Example Maps
```bash
micromamba run -n topomap python topomap_generator_v2.py
```
Generates Mount Rainier, Grand Canyon, and Mont Blanc.

---

## 📝 Example: Create Custom Map

### 1. Using simple_example.py (Recommended)
Edit the file and change these values:
```python
LATITUDE = 48.8566
LONGITUDE = 2.3522
SIZE_KM = 20
TITLE = "PARIS"
```

Then run:
```bash
micromamba run -n topomap python simple_example.py
```

### 2. Using Python Directly
Create a new file `my_map.py`:
```python
from topomap_generator_v2 import TopomapGenerator

generator = TopomapGenerator(output_dir="output")
generator.generate(
    latitude=48.8566,
    longitude=2.3522,
    size_km=20,
    resolution=120,
    num_lines=80,
    exaggeration=3.0,
    output_filename="paris.png",
    title="PARIS",
    smoothing=True
)
```

Run it:
```bash
micromamba run -n topomap python my_map.py
```

### 3. Interactive Python Session
```bash
micromamba run -n topomap python
```

Then in Python:
```python
from topomap_generator_v2 import TopomapGenerator
generator = TopomapGenerator()
generator.generate(latitude=46.8523, longitude=-121.7603, 
                   size_km=20, output_filename="test.png",
                   title="MY MAP")
```

---

## 📦 Package Management

### Install New Package
```bash
micromamba run -n topomap pip install package_name
```

### Update Package
```bash
micromamba run -n topomap pip install --upgrade package_name
```

### Reinstall All Packages
```bash
micromamba run -n topomap pip install -r requirements.txt --force-reinstall
```

---

## 📂 File Operations

### List Output Files
```bash
ls -lh output/
```

### View Output Directory
```bash
open output/
```

### Copy Map to Desktop
```bash
cp output/your_map.png ~/Desktop/
```

### Create Backup
```bash
cp -r output/ output_backup_$(date +%Y%m%d)
```

---

## 🔍 Debugging

### Check Python Version
```bash
micromamba run -n topomap python --version
```

### Test Package Import
```bash
micromamba run -n topomap python -c "import matplotlib; print(matplotlib.__version__)"
micromamba run -n topomap python -c "import srtm; print('SRTM OK')"
```

### Verbose Output
```bash
micromamba run -n topomap python -v your_script.py
```

### Check for Errors
```bash
micromamba run -n topomap python your_script.py 2>&1 | less
```

---

## 🎨 Quick Generation Recipes

### High Quality Print
```bash
# Edit simple_example.py:
RESOLUTION = 200
SIZE_KM = 25
NUM_LINES = 120
```

### Fast Preview
```bash
# Edit simple_example.py:
RESOLUTION = 60
SIZE_KM = 10
NUM_LINES = 40
```

### Dramatic Mountains
```bash
# Edit simple_example.py:
EXAGGERATION = 2.5
SMOOTHING = True
```

### Flat Terrain Enhancement
```bash
# Edit simple_example.py:
EXAGGERATION = 6.0
SMOOTHING = True
```

---

## 🌍 Coordinate Finding

### Use Google Maps
1. Go to maps.google.com
2. Right-click on location
3. Click the coordinates
4. Format: Latitude, Longitude

### Example Coordinates
```python
# Mountains
MOUNT_EVEREST = (27.9881, 86.9250)
MOUNT_FUJI = (35.3606, 138.7278)
MATTERHORN = (45.9763, 7.6586)

# Canyons
GRAND_CANYON = (36.1069, -112.1129)
DEATH_VALLEY = (36.5323, -116.9325)

# Volcanoes
MOUNT_ST_HELENS = (46.1914, -122.1956)
KRAKATOA = (-6.1024, 105.4230)

# Islands
MAYOTTE = (-12.8275, 45.1662)
HAWAII = (19.8207, -155.4680)
```

---

## 📊 Batch Processing

### Generate Multiple Maps
Create `batch_generate.py`:
```python
from topomap_generator_v2 import TopomapGenerator

generator = TopomapGenerator(output_dir="output")

locations = [
    (48.8566, 2.3522, "Paris"),
    (35.6762, 139.6503, "Tokyo"),
    (40.7128, -74.0060, "New York"),
]

for lat, lon, name in locations:
    generator.generate(
        latitude=lat,
        longitude=lon,
        size_km=20,
        output_filename=f"{name.lower()}.png",
        title=name.upper()
    )
```

Run:
```bash
micromamba run -n topomap python batch_generate.py
```

---

## 🧹 Cleanup

### Remove Old Outputs
```bash
rm output/*.png
```

### Clear Cache
```bash
rm -rf ~/.cache/srtm/
```

### Remove Environment (if needed)
```bash
micromamba env remove -n topomap
```

---

## 📖 Help & Documentation

### View README
```bash
less README.md
```

### View Quickstart
```bash
less QUICKSTART.md
```

### Python Help
```bash
micromamba run -n topomap python -c "from topomap_generator_v2 import TopomapGenerator; help(TopomapGenerator.generate)"
```

---

## 🎯 Most Common Commands

```bash
# 1. Test installation
micromamba run -n topomap python test_v2.py

# 2. Create custom map (edit simple_example.py first)
micromamba run -n topomap python simple_example.py

# 3. View output
open output/

# 4. Generate Mayotte example
micromamba run -n topomap python generate_mayotte.py
```

---

**For more details, see README.md or QUICKSTART.md**
