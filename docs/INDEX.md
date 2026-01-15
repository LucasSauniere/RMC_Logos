# 📁 Project Index

Welcome to the Topographic Line Art Generator!

This project creates "Joy Division" style visualizations from real elevation data anywhere on Earth.

---

## 🚀 START HERE

### First Time?
1. **Run the test**: `micromamba run -n topomap python test_v2.py`
2. **Read**: [QUICKSTART.md](QUICKSTART.md)
3. **Create your map**: Edit and run `simple_example.py`

### Quick Links
- 📖 [**Complete Documentation**](README.md) - Full guide with all details
- ⚡ [**Quick Start Guide**](QUICKSTART.md) - Fast reference for common tasks  
- 💻 [**Command Reference**](COMMANDS.md) - All available commands
- 📊 [**Project Summary**](PROJECT_SUMMARY.md) - Technical overview

---

## 📝 Python Scripts

### Ready-to-Use Scripts
| File | Purpose | How to Use |
|------|---------|------------|
| `test_v2.py` | Test installation | `micromamba run -n topomap python test_v2.py` |
| `simple_example.py` | **Main script for creating maps** | Edit parameters, then run |
| `generate_mayotte.py` | Example: Mayotte island | Run directly |

### Core Library
| File | Purpose | Note |
|------|---------|------|
| `topomap_generator_v2.py` | **Main generator class (recommended)** | Import and use |
| `topomap_generator.py` | Original version | Requires GDAL setup |

### Legacy/Alternative
| File | Purpose | Note |
|------|---------|------|
| `example_usage.py` | Old example script | Use `simple_example.py` instead |
| `test_installation.py` | Old test script | Use `test_v2.py` instead |

---

## 📚 Documentation Files

### User Guides
- **[README.md](README.md)** - Complete documentation
  - Installation instructions
  - Full parameter reference
  - Troubleshooting guide
  - Examples and tips

- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference
  - 3-step getting started
  - Interesting locations
  - Style variations
  - Common issues

- **[COMMANDS.md](COMMANDS.md)** - Command reference
  - All terminal commands
  - Code examples
  - Batch processing
  - Debugging tips

### Technical Documentation
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Technical overview
  - File descriptions
  - Environment details
  - Processing pipeline
  - Feature list

- **[requirements.txt](requirements.txt)** - Python dependencies
  - Package versions
  - For pip install

---

## 📂 Directories

### Output
- **`output/`** - Generated images are saved here
  - Currently contains: `test_yosemite.png` (test image)
  - Your maps will appear here

### Cache (Hidden)
- **`~/.cache/srtm/`** - Cached elevation data
  - Automatically managed
  - Speeds up repeated requests

---

## 🎯 Recommended Workflow

### For Beginners
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Run `test_v2.py`
3. Edit `simple_example.py`
4. Generate your first map!

### For Advanced Users
1. Read [README.md](README.md)
2. Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
3. Import `TopomapGenerator` in your own scripts
4. Customize as needed

### For Troubleshooting
1. Check [QUICKSTART.md](QUICKSTART.md) - Common Issues section
2. See [COMMANDS.md](COMMANDS.md) - Debugging section
3. Review [README.md](README.md) - Troubleshooting section

---

## 💡 What Can You Do?

### Create Maps
- ✅ Any location on Earth
- ✅ Customize colors and style
- ✅ Adjust terrain exaggeration
- ✅ High-resolution output (300 DPI)

### Example Uses
- 🖼️ Wall art / prints
- 📱 Phone wallpapers
- 🎁 Personalized gifts
- 📊 Data visualization
- 🎨 Generative art projects

---

## 🛠️ Environment

**Name**: `topomap`  
**Python**: 3.11  
**Status**: ✅ Ready to use

**Main Packages**:
- numpy, matplotlib, scipy
- srtm.py (elevation data)
- rasterio, gdal (geospatial)
- pillow (image processing)

**Activate**:
```bash
micromamba activate topomap
```

**Run without activating**:
```bash
micromamba run -n topomap python script.py
```

---

## 📖 Documentation Map

```
INDEX.md (YOU ARE HERE)
│
├── QUICKSTART.md          ← Start here for basics
│   ├── 3-step guide
│   ├── Location examples
│   └── Style variations
│
├── README.md              ← Complete documentation
│   ├── Installation
│   ├── Parameters
│   ├── Examples
│   └── Troubleshooting
│
├── COMMANDS.md            ← Command reference
│   ├── All commands
│   ├── Code examples
│   └── Debugging
│
└── PROJECT_SUMMARY.md     ← Technical details
    ├── File descriptions
    ├── Pipeline explanation
    └── Architecture
```

---

## 🎨 Inspiration

This project creates visualizations inspired by:
- **Joy Division's "Unknown Pleasures" album cover** (1979)
- **Traditional topographic visualization techniques**
- **Data-driven generative art**

The horizontal line representation with vertical displacement based on elevation is a classic method that gained iconic cultural status through the album design.

---

## 📞 Quick Help

**"I just want to create a map!"**
→ Edit `simple_example.py` and run it

**"How do I change the location?"**
→ Edit `LATITUDE` and `LONGITUDE` in `simple_example.py`

**"Where's my output?"**
→ Check the `output/` directory

**"It's too slow!"**
→ Reduce `RESOLUTION`, `SIZE_KM`, or `NUM_LINES`

**"Lines are too flat!"**
→ Increase `EXAGGERATION` value

**"Something's broken!"**
→ Check [QUICKSTART.md](QUICKSTART.md) Common Issues section

---

## ✨ Examples Gallery

After running the scripts, you'll have maps like:
- `test_yosemite.png` - Yosemite Valley (already generated!)
- `mayotte_relief.png` - Mayotte island
- `mount_rainier.png` - Mount Rainier
- `grand_canyon.png` - Grand Canyon
- `mont_blanc.png` - Mont Blanc

---

**Ready to create amazing topographic art? Start with [QUICKSTART.md](QUICKSTART.md)! 🗺️✨**
