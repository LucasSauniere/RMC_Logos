# Hosting Your Ridge Map Package Online - Complete Guide

## 🌐 Multiple Options for Web Hosting

### Option 1: GitHub Pages (Recommended for Documentation)
**Best for:** Documentation, examples gallery, interactive demos

### Option 2: PyPI (Python Package Index)
**Best for:** Making package installable via `pip install rmclogo`

### Option 3: Streamlit/Gradio Web App
**Best for:** Interactive web application where users can generate maps

### Option 4: GitHub Actions + Binder
**Best for:** Interactive Jupyter notebooks in the browser

---

## 🎯 Option 1: GitHub Pages (Documentation Site)

### Step 1: Create a Documentation Website

Create a `docs/` folder with a static site or use a generator like MkDocs:

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Initialize MkDocs project
mkdocs new .

# Preview locally
mkdocs serve

# Build and deploy to GitHub Pages
mkdocs gh-deploy
```

### Step 2: Create an Examples Gallery

Create `docs/gallery/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RMC Logo - Ridge Map Gallery</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .gallery-item {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .gallery-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .gallery-item img {
            width: 100%;
            height: 400px;
            object-fit: cover;
        }
        .gallery-item h3 {
            padding: 15px;
            margin: 0;
            font-size: 18px;
        }
        .gallery-item p {
            padding: 0 15px 15px;
            margin: 0;
            color: #666;
        }
        header {
            text-align: center;
            padding: 40px 0;
        }
        h1 {
            font-size: 48px;
            margin: 0;
            color: #333;
        }
        .subtitle {
            font-size: 20px;
            color: #666;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>🏔️ RMC Logo Gallery</h1>
        <p class="subtitle">Beautiful ridge maps generated from real elevation data</p>
    </header>
    
    <div class="gallery">
        <div class="gallery-item">
            <img src="../output/marseille_ridgemap_classic.png" alt="Marseille Classic">
            <h3>Marseille - Classic</h3>
            <p>Black on white, Joy Division style</p>
        </div>
        
        <div class="gallery-item">
            <img src="../output/marseille_ridgemap_neon.svg" alt="Marseille Neon">
            <h3>Marseille - Neon</h3>
            <p>Neon green on black, perfect for logos</p>
        </div>
        
        <div class="gallery-item">
            <img src="../output/marseille_calanques_ridgemap.png" alt="Les Calanques">
            <h3>Les Calanques</h3>
            <p>Cyan on dark blue, Mediterranean vibes</p>
        </div>
    </div>
    
    <footer style="text-align: center; margin-top: 50px; padding: 20px; color: #666;">
        <p>Made with ❤️ using the RMC Logo package</p>
        <a href="https://github.com/yourusername/Club_RMC">View on GitHub</a>
    </footer>
</body>
</html>
```

### Step 3: Enable GitHub Pages

1. Go to your GitHub repository
2. Settings → Pages
3. Source: Deploy from branch
4. Branch: `main` or create `gh-pages`
5. Folder: `/docs` or `/` (root)
6. Save

Your site will be at: `https://yourusername.github.io/Club_RMC/`

---

## 🎯 Option 2: Publish to PyPI

Make your package installable worldwide with `pip install rmclogo`

### Step 1: Update `setup.py`

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rmclogo",  # Your package name on PyPI
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Generate beautiful Joy Division-style ridge maps from elevation data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Club_RMC",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "scipy>=1.10.0",
        "srtm.py>=0.3.7",
        "svgwrite>=1.4.3",
        "scikit-image>=0.20.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "black>=23.0", "flake8>=6.0"],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/Club_RMC/issues",
        "Source": "https://github.com/yourusername/Club_RMC",
        "Gallery": "https://yourusername.github.io/Club_RMC/gallery",
    },
)
```

### Step 2: Publish to PyPI

```bash
# Install publishing tools
pip install build twine

# Build distribution packages
python -m build

# Upload to PyPI (you'll need an account)
python -m twine upload dist/*

# Or use TestPyPI first
python -m twine upload --repository testpypi dist/*
```

After publishing, anyone can install:
```bash
pip install rmclogo
```

---

## 🎯 Option 3: Streamlit Web App (Interactive!)

Create an interactive web app where users can generate maps!

### Create `streamlit_app.py`:

```python
"""
Streamlit Web App for RMC Logo Generator
Run with: streamlit run streamlit_app.py
"""

import streamlit as st
import sys
sys.path.insert(0, '.')

from src import RidgeMap
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(
    page_title="RMC Logo Generator",
    page_icon="🏔️",
    layout="wide"
)

st.title("🏔️ RMC Ridge Map Generator")
st.markdown("Create beautiful Joy Division-style ridge maps from any location!")

# Sidebar controls
st.sidebar.header("Map Configuration")

# Location selection
st.sidebar.subheader("📍 Location")
location = st.sidebar.selectbox(
    "Choose a location or enter custom coordinates:",
    ["Marseille", "Calanques", "Custom"]
)

if location == "Custom":
    col1, col2 = st.sidebar.columns(2)
    with col1:
        lat_min = st.number_input("Lat Min", value=43.22, format="%.4f")
        lon_min = st.number_input("Lon Min", value=5.29, format="%.4f")
    with col2:
        lat_max = st.number_input("Lat Max", value=43.37, format="%.4f")
        lon_max = st.number_input("Lon Max", value=5.45, format="%.4f")
    bbox = (lon_min, lat_min, lon_max, lat_max)
elif location == "Marseille":
    bbox = (5.29, 43.22, 5.45, 43.37)
else:  # Calanques
    bbox = (5.38, 43.15, 5.52, 43.25)

# Styling options
st.sidebar.subheader("🎨 Styling")
label = st.sidebar.text_input("Label", value=location.upper())
line_color = st.sidebar.color_picker("Line Color", value="#000000")
bg_color = st.sidebar.color_picker("Background Color", value="#FFFFFF")
num_lines = st.sidebar.slider("Number of Lines", 20, 150, 80)
linewidth = st.sidebar.slider("Line Width", 0.5, 3.0, 1.5, 0.1)

# Format selection
format_type = st.sidebar.radio("Output Format", ["PNG", "SVG"])

# Generate button
if st.sidebar.button("🎨 Generate Map", type="primary"):
    with st.spinner("Generating ridge map... This may take a minute."):
        try:
            # Create RidgeMap
            rm = RidgeMap(bbox=bbox)
            
            # Get elevation data
            values = rm.get_elevation_data(
                num_lines=num_lines,
                elevation_pts=300
            )
            
            if format_type == "PNG":
                # Generate PNG
                fig, ax = plt.subplots(figsize=(12, 16))
                rm.plot_map(
                    values=values,
                    label=label,
                    label_x=0.5,
                    label_y=0.12,
                    label_size=70,
                    line_color=line_color,
                    background_color=bg_color,
                    kind='elevation',
                    linewidth=linewidth,
                    ax=ax
                )
                
                # Display
                st.pyplot(fig)
                
                # Download button
                buf = BytesIO()
                fig.savefig(buf, format='png', dpi=300, bbox_inches='tight', 
                           facecolor=bg_color)
                buf.seek(0)
                st.download_button(
                    label="📥 Download PNG",
                    data=buf,
                    file_name=f"{label.lower()}_ridgemap.png",
                    mime="image/png"
                )
                
            else:  # SVG
                # Generate SVG
                svg_output = "/tmp/ridgemap.svg"
                rm.save_svg(
                    output_path=svg_output,
                    values=values,
                    label=label,
                    label_x=0.5,
                    label_y=0.15,
                    label_size=80,
                    line_color=line_color,
                    background_color=bg_color,
                    linewidth=linewidth,
                    width=1200,
                    height=1600
                )
                
                # Display and download
                with open(svg_output, 'r') as f:
                    svg_content = f.read()
                st.image(svg_output)
                st.download_button(
                    label="📥 Download SVG",
                    data=svg_content,
                    file_name=f"{label.lower()}_ridgemap.svg",
                    mime="image/svg+xml"
                )
            
            st.success("✅ Map generated successfully!")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Info section
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📐 SVG Benefits")
    st.markdown("""
    - Infinitely scalable
    - Small file size
    - Perfect for printing
    - Easy to edit
    """)

with col2:
    st.markdown("### 🎨 Use Cases")
    st.markdown("""
    - Logos and branding
    - Posters and prints
    - Merchandise
    - Social media
    """)

with col3:
    st.markdown("### 🔗 Links")
    st.markdown("""
    - [GitHub](https://github.com/yourusername/Club_RMC)
    - [Documentation](https://yourusername.github.io/Club_RMC)
    - [Gallery](https://yourusername.github.io/Club_RMC/gallery)
    """)
```

### Deploy to Streamlit Cloud:

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Select `streamlit_app.py`
5. Deploy!

Your app will be at: `https://share.streamlit.io/yourusername/club_rmc`

---

## 🎯 Option 4: Binder (Interactive Notebooks)

Allow users to run your notebooks in the browser!

### Step 1: Create `requirements.txt` for Binder

Already exists, just ensure it's up to date.

### Step 2: Create `environment.yml` (optional)

```yaml
name: rmclogo
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pip
  - pip:
    - numpy>=1.24.0
    - matplotlib>=3.7.0
    - scipy>=1.10.0
    - srtm.py>=0.3.7
    - svgwrite>=1.4.3
    - jupyterlab
```

### Step 3: Add Binder Badge to README

```markdown
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yourusername/Club_RMC/main?labpath=notebooks%2F05_joydivision_style.ipynb)
```

Users can click and run your notebooks instantly!

---

## 📝 Complete Deployment Checklist

### GitHub Repository Setup
- [ ] Add comprehensive README.md
- [ ] Add LICENSE file (MIT recommended)
- [ ] Create .gitignore for Python
- [ ] Add requirements.txt
- [ ] Create docs/ folder
- [ ] Add example outputs to docs/gallery/

### GitHub Pages Setup
- [ ] Create docs/index.html or use MkDocs
- [ ] Create gallery page
- [ ] Enable GitHub Pages in settings
- [ ] Add custom domain (optional)

### PyPI Publishing
- [ ] Update setup.py with correct info
- [ ] Create PyPI account
- [ ] Generate API token
- [ ] Build and upload package
- [ ] Test installation

### Web App (Optional)
- [ ] Create streamlit_app.py
- [ ] Deploy to Streamlit Cloud
- [ ] Add to README

### Binder Setup (Optional)
- [ ] Verify requirements.txt
- [ ] Add Binder badge to README
- [ ] Test launching

---

## 🚀 Quick Start Guide

### For GitHub Pages Only (Easiest):

```bash
# 1. Create docs folder structure
mkdir -p docs/gallery
mkdir -p docs/images

# 2. Copy outputs to docs
cp -r output/* docs/gallery/

# 3. Create simple index.html
cat > docs/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>RMC Logo Gallery</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        img { width: 100%; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>🏔️ RMC Logo Gallery</h1>
    <div class="gallery">
        <img src="gallery/marseille_ridgemap_classic.png">
        <img src="gallery/marseille_ridgemap_neon.svg">
        <img src="gallery/marseille_calanques_ridgemap.png">
    </div>
</body>
</html>
EOF

# 4. Push to GitHub
git add docs/
git commit -m "Add GitHub Pages site"
git push

# 5. Enable GitHub Pages in repo settings
# Settings → Pages → Source: /docs folder
```

---

## 🎨 Recommended Approach

**Phase 1 (Start here):**
1. ✅ Create GitHub Pages with gallery
2. ✅ Add comprehensive README
3. ✅ Add examples and documentation

**Phase 2 (Next):**
4. ✅ Publish to PyPI
5. ✅ Add Binder support

**Phase 3 (Advanced):**
6. ✅ Create Streamlit web app
7. ✅ Add API endpoint
8. ✅ Create video tutorials

---

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Binder Documentation](https://mybinder.readthedocs.io/)

Let me know which option you'd like to implement first, and I can help you set it up! 🚀
