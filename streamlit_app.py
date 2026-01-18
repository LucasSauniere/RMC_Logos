"""
RMC Ridge Map Generator - Streamlit Web App
===========================================

Interactive web application for generating beautiful Joy Division-style
ridge maps from any location on Earth.

Run with: streamlit run streamlit_app.py
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src import RidgeMap
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

# Page configuration
st.set_page_config(
    page_title="RMC Ridge Map Generator",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏔️ RMC Ridge Map Generator</h1>
    <p>Create beautiful Joy Division-style ridge maps from real elevation data</p>
</div>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.header("⚙️ Map Configuration")

# Preset locations
st.sidebar.subheader("📍 Location")
preset_locations = {
    "Marseille (France)": (5.29, 43.22, 5.45, 43.37),
    "Les Calanques (France)": (5.38, 43.15, 5.52, 43.25),
    "Mont Blanc (Alps)": (6.8, 45.8, 7.0, 45.9),
    "Pyrenees": (-0.5, 42.6, 0.5, 42.9),
    "Corsica": (8.9, 42.0, 9.6, 43.0),
    "Custom Coordinates": None
}

location_choice = st.sidebar.selectbox(
    "Choose a location:",
    list(preset_locations.keys())
)

if preset_locations[location_choice] is not None:
    bbox = preset_locations[location_choice]
    st.sidebar.success(f"✅ Using preset: {location_choice}")
else:
    st.sidebar.info("Enter custom coordinates below:")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        lon_min = st.number_input("West Longitude", value=5.29, format="%.4f")
        lat_min = st.number_input("South Latitude", value=43.22, format="%.4f")
    with col2:
        lon_max = st.number_input("East Longitude", value=5.45, format="%.4f")
        lat_max = st.number_input("North Latitude", value=43.37, format="%.4f")
    bbox = (lon_min, lat_min, lon_max, lat_max)

# Map parameters
st.sidebar.subheader("🗺️ Map Parameters")
num_lines = st.sidebar.slider("Number of Ridge Lines", 20, 150, 80, 5,
                               help="More lines = more detail but slower generation")
elevation_pts = st.sidebar.slider("Points per Line", 100, 500, 300, 50,
                                  help="Higher = smoother lines but slower")

# Styling
st.sidebar.subheader("🎨 Styling")
label = st.sidebar.text_input("Map Label", value=location_choice.split(" ")[0].upper())

# Color presets
color_presets = {
    "Classic (Black on White)": ("#000000", "#FFFFFF"),
    "Inverted (White on Black)": ("#FFFFFF", "#000000"),
    "Neon Green": ("#00FF00", "#000000"),
    "Hot Magenta": ("#FF1493", "#0D010D"),
    "Electric Blue": ("#00D4FF", "#001F40"),
    "Sunset Orange": ("#FF6B35", "#1A0F0A"),
    "Purple Haze": ("#DA70D6", "#2B1C4D"),
    "Custom Colors": None
}

color_choice = st.sidebar.selectbox("Color Preset:", list(color_presets.keys()))

if color_presets[color_choice] is not None:
    line_color, bg_color = color_presets[color_choice]
else:
    col1, col2 = st.sidebar.columns(2)
    with col1:
        line_color = st.color_picker("Line Color", value="#000000")
    with col2:
        bg_color = st.color_picker("Background", value="#FFFFFF")

linewidth = st.sidebar.slider("Line Width", 0.5, 4.0, 1.5, 0.1)

# Output format
st.sidebar.subheader("💾 Output Format")
format_type = st.sidebar.radio("Format:", ["PNG (Raster)", "SVG (Vector)"],
                               help="SVG is scalable and perfect for printing!")

# Main content area
tab1, tab2, tab3 = st.tabs(["🎨 Generator", "📖 About", "🖼️ Gallery"])

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.markdown("### Quick Tips")
        st.info("""
        **📐 SVG Benefits:**
        - Infinitely scalable
        - Small file size
        - Perfect for logos
        - Easy to edit
        
        **🎨 Best Practices:**
        - Start with 80 lines
        - Use 300 points/line
        - Try presets first
        """)
    
    with col1:
        generate_button = st.button("🎨 Generate Ridge Map", type="primary", 
                                    use_container_width=True)
        
        if generate_button:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Step 1: Create RidgeMap
                status_text.text("🗺️ Creating map instance...")
                progress_bar.progress(20)
                rm = RidgeMap(bbox=bbox)
                
                # Step 2: Fetch elevation data
                status_text.text("📡 Fetching elevation data... (this may take a minute)")
                progress_bar.progress(40)
                values = rm.get_elevation_data(
                    num_lines=num_lines,
                    elevation_pts=elevation_pts
                )
                
                # Step 3: Generate map
                status_text.text("🎨 Generating beautiful ridge lines...")
                progress_bar.progress(60)
                
                if "PNG" in format_type:
                    # Generate PNG
                    fig, ax = plt.subplots(figsize=(12, 16), facecolor=bg_color)
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
                        size_scale=12,
                        ax=ax
                    )
                    
                    progress_bar.progress(80)
                    status_text.text("📐 Rendering image...")
                    
                    # Display
                    st.pyplot(fig)
                    
                    # Download button
                    buf = BytesIO()
                    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight',
                               facecolor=bg_color)
                    buf.seek(0)
                    
                    progress_bar.progress(100)
                    status_text.empty()
                    
                    st.success("✅ PNG generated successfully!")
                    st.download_button(
                        label="📥 Download High-Res PNG",
                        data=buf,
                        file_name=f"{label.lower().replace(' ', '_')}_ridgemap.png",
                        mime="image/png",
                        use_container_width=True
                    )
                    
                    # Show stats
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Lines", f"{num_lines}")
                    col2.metric("Points/Line", f"{elevation_pts}")
                    col3.metric("Resolution", f"{values.shape[0]}×{values.shape[1]}")
                    
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
                    
                    progress_bar.progress(80)
                    status_text.text("📐 Creating SVG file...")
                    
                    # Read and display
                    with open(svg_output, 'r') as f:
                        svg_content = f.read()
                    
                    progress_bar.progress(100)
                    status_text.empty()
                    
                    st.success("✅ SVG generated successfully!")
                    
                    # Display SVG
                    st.image(svg_output, use_column_width=True)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Scalable SVG",
                        data=svg_content,
                        file_name=f"{label.lower().replace(' ', '_')}_ridgemap.svg",
                        mime="image/svg+xml",
                        use_container_width=True
                    )
                    
                    # File size info
                    svg_size = len(svg_content) / 1024
                    st.info(f"📊 SVG file size: {svg_size:.1f} KB (infinitely scalable!)")
                
            except Exception as e:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ Error: {str(e)}")
                st.exception(e)

with tab2:
    st.markdown("""
    ## 🏔️ About Ridge Map Generator
    
    This web app generates beautiful **Joy Division-style ridge maps** from real elevation data
    for any location on Earth! Inspired by the iconic album cover of "Unknown Pleasures".
    
    ### ✨ Features
    - 🌍 **Worldwide Coverage** - Generate maps for any location
    - 🎨 **Customizable** - Choose colors, styles, and parameters
    - 📐 **Vector Output** - SVG format for infinite scalability
    - 🖨️ **Print-Ready** - Perfect for posters, logos, and merchandise
    - ⚡ **Real-Time** - Generate maps in seconds
    
    ### 🎯 Use Cases
    - **Logos & Branding** - Create unique geographic logos
    - **Art Prints** - Beautiful wall art from your favorite places
    - **Merchandise** - T-shirts, mugs, stickers
    - **Presentations** - Eye-catching visualizations
    - **Social Media** - Unique profile graphics
    
    ### 🔧 How It Works
    1. Select or enter geographic coordinates
    2. Choose styling and parameters
    3. Generate PNG or SVG output
    4. Download and use your map!
    
    ### 📚 Technical Details
    - **Data Source**: SRTM elevation data (90m resolution)
    - **Algorithm**: Joy Division-style ridge line rendering
    - **Formats**: PNG (raster) and SVG (vector)
    - **Open Source**: Built with Python, matplotlib, and svgwrite
    
    ### 🔗 Links
    - [GitHub Repository](https://github.com/yourusername/Club_RMC)
    - [Documentation](https://github.com/yourusername/Club_RMC/blob/main/README.md)
    - [Examples Gallery](https://yourusername.github.io/Club_RMC/gallery)
    
    ### 👨‍💻 Made With
    Python • matplotlib • numpy • srtm.py • svgwrite • Streamlit
    """)

with tab3:
    st.markdown("## 🖼️ Example Gallery")
    st.markdown("See what's possible with the Ridge Map Generator!")
    
    # Example gallery (you can add actual images here)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Marseille Classic")
        st.markdown("Black on white, timeless style")
        # st.image("docs/gallery/marseille_classic.png")
        
    with col2:
        st.markdown("### Neon Style")
        st.markdown("Perfect for modern logos")
        # st.image("docs/gallery/marseille_neon.png")
        
    with col3:
        st.markdown("### Les Calanques")
        st.markdown("Mediterranean vibes")
        # st.image("docs/gallery/calanques.png")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    Made with ❤️ using RMC Logo Package | 
    <a href='https://github.com/yourusername/Club_RMC'>View on GitHub</a> |
    <a href='mailto:your.email@example.com'>Contact</a>
</div>
""", unsafe_allow_html=True)
