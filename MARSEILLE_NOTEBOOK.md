# 🎉 Complete! Marseille Notebook Created

## New Notebook: `notebooks/02_marseille_example.ipynb`

A comprehensive, interactive tutorial focused on creating topographic art of **Marseille, France**!

### 📚 What's Inside:

#### 1. Introduction & Setup
- Overview of Marseille's geography
- Key locations and terrain features
- Library imports and configuration

#### 2. Marseille City Center Map
- Classic Joy Division purple style
- 15km area covering the urban coastline
- Old Port and Notre-Dame de la Garde

#### 3. Massif des Calanques
- Dramatic coastal cliffs visualization
- Cyan color scheme for Mediterranean feel
- Shows rugged limestone formations

#### 4. Gradient Scaling Artistic Map
- Uses `create_gradient_scaling()` function
- Progressive line exaggeration effect
- Golden color scheme
- Covers Greater Marseille area

#### 5. SVG Logo Creation
- Vector format perfect for branding
- Black & white minimal design
- Scalable to any size

#### 6. Style Variations
- Multiple color schemes comparison
- Neon green, hot pink, ocean blue
- Side-by-side visual comparison

#### 7. Marseille-Specific Tips
- Terrain-based parameter recommendations
- Mediterranean color palette ideas
- Specific locations to explore

### 🎯 Learning Objectives

Students will learn:
- ✅ How to handle coastal terrain (mixed land/sea)
- ✅ Different exaggeration factors for varied topography
- ✅ Creating themed color schemes
- ✅ Gradient scaling for artistic effects
- ✅ SVG export for professional use
- ✅ Batch generation with variations

### 📍 Marseille Locations Covered

1. **City Center** (43.2965°N, 5.3698°E)
   - Old Port and basilica
   - Elevation: 0-200m

2. **Calanques** (43.2000°N, 5.4500°E)
   - Coastal cliffs and inlets
   - Elevation: 0-600m

3. **Greater Area** (43.3500°N, 5.4000°E)
   - Metropolitan region
   - Mixed terrain

### 🎨 Visual Styles Created

1. **Classic Purple** - Traditional Joy Division style
2. **Mediterranean Cyan** - Ocean-inspired
3. **Golden Sunset** - Elegant warm tones
4. **Neon Green** - Modern electric
5. **Hot Pink** - Bold and vibrant
6. **Ocean Blue** - Deep water theme
7. **B&W SVG** - Professional logo style

### 📊 Generated Files

Running the complete notebook creates:
- `marseille_center.png` - City center map
- `marseille_calanques.png` - Cliffs map
- `marseille_gradient.png` - Artistic gradient version
- `marseille_logo.svg` - Vector logo
- `marseille_style_*.png` - Color variations
- `marseille_test.png` - Test output

### 💡 Key Features Demonstrated

1. **Coastal Terrain Handling**
   - Higher exaggeration for flat areas
   - Dealing with sea-level elevation
   
2. **Mountainous Terrain**
   - Lower exaggeration for cliffs
   - Higher resolution for detail
   
3. **Gradient Scaling**
   - `ease_out` style progression
   - Creative artistic effects
   
4. **SVG Export**
   - Vector graphics generation
   - Logo-ready output
   
5. **Color Theory**
   - Mediterranean-inspired palettes
   - Mood-based color selection

### 🚀 How to Use

```bash
# Open in Jupyter
micromamba run -n topomap jupyter lab

# Navigate to: notebooks/02_marseille_example.ipynb

# Run all cells to generate complete gallery
```

Or run cells individually to explore each technique!

### 📝 Code Examples

The notebook includes fully-functional code for:

```python
# Basic Marseille map
generator.generate(
    latitude=43.2965,
    longitude=5.3698,
    size_km=15,
    exaggeration=5.0,
    output_filename="marseille.png"
)

# With gradient scaling
scaling = create_gradient_scaling(70, start=0.4, end=1.6, style='ease_out')
generator.generate(
    ...,
    scaling_factors=scaling
)

# SVG logo
generator.generate(
    ...,
    format='svg',
    bg_color='#ffffff',
    line_color='#000000'
)
```

### 🌍 Suggested Extensions

After completing this notebook, try:
- Other French coastal cities (Nice, Biarritz)
- French Alps (Chamonix, Grenoble)
- Paris and surrounding areas
- Corsica island topography
- French Riviera coastline

### ✅ Tested & Verified

- All code cells execute successfully
- Maps generate correctly
- SVG export works
- Gradient scaling functions properly
- Color schemes display beautifully

---

**The Marseille notebook is complete and ready to use!**

**Perfect for:**
- Learning coastal topography visualization
- Understanding French Mediterranean geography
- Creating location-specific art
- Logo and branding projects

**Start here: `notebooks/02_marseille_example.ipynb` 🏖️**
