"""
Example: Overlay GPX Track on Topographic Art

This example demonstrates how to overlay a GPX track (GPS route)
on top of topographic visualizations.
"""

from topomap import TopomapGenerator

def main():
    generator = TopomapGenerator(output_dir="output")
    
    print("=" * 70)
    print("GPX OVERLAY DEMONSTRATION")
    print("=" * 70)
    print("\nThis example shows how to overlay a GPX track on topographic art.")
    print("Perfect for hiking trails, cycling routes, or travel journeys!\n")
    
    # Example 1: Halftone with GPX overlay
    print("\n📍 Example 1: Halftone Style with GPX Track")
    print("-" * 70)
    
    try:
        halftone_with_gpx = generator.generate(
            latitude=43.2965,
            longitude=5.3698,
            size_km=15,
            resolution=150,
            output_filename="marseille_halftone_gpx.png",
            format='halftone',
            
            # Halftone parameters
            dot_size_range=(0.5, 8.0),
            grid_spacing=10,
            bg_color='#ffffff',
            dot_color='#ff6900',  # Orange dots
            skip_zero_elevation=True,
            
            # GPX overlay parameters
            gpx_file="path/to/your/track.gpx",  # Replace with your GPX file
            gpx_color='#000000',     # Black track
            gpx_width=3.0,           # Line width
            gpx_style='-',           # Solid line
            gpx_alpha=1.0,           # Fully opaque
            gpx_zorder=10,           # Draw on top
            
            figsize=(12, 16),
            dpi=300
        )
        
        print(f"\n✅ Halftone with GPX saved: {halftone_with_gpx}")
    
    except FileNotFoundError:
        print("\n⚠️  GPX file not found. Please provide a valid GPX file path.")
        print("   You can export GPX files from apps like:")
        print("   - Strava, Garmin Connect, AllTrails, Komoot, etc.")
    
    # Example 2: Traditional lines with GPX overlay
    print("\n\n📍 Example 2: Traditional Line Style with GPX Track")
    print("-" * 70)
    
    try:
        lines_with_gpx = generator.generate(
            latitude=43.2965,
            longitude=5.3698,
            size_km=15,
            resolution=100,
            num_lines=60,
            exaggeration=4.0,
            output_filename="marseille_lines_gpx.png",
            format='png',
            
            # Line style parameters
            bg_color='#2B1B4D',
            line_color='white',
            line_width=1.5,
            fill_below=True,
            
            # GPX overlay parameters
            gpx_file="path/to/your/track.gpx",  # Replace with your GPX file
            gpx_color='#FF0000',     # Red track for contrast
            gpx_width=4.0,           # Thicker line
            gpx_style='-',
            gpx_alpha=0.9,
            gpx_zorder=10,
            
            figsize=(12, 16),
            dpi=300
        )
        
        print(f"\n✅ Lines with GPX saved: {lines_with_gpx}")
    
    except FileNotFoundError:
        print("\n⚠️  GPX file not found.")
    
    print("\n" + "=" * 70)
    print("TIPS FOR USING GPX OVERLAYS")
    print("=" * 70)
    print("""
    1. Export GPX files from fitness/hiking apps
    2. Ensure the GPX track covers the map area
    3. Adjust gpx_color for contrast with your map style
    4. Use gpx_alpha < 1.0 for semi-transparent tracks
    5. Increase gpx_width for more visible routes
    
    Color suggestions:
    - Black (#000000) on light backgrounds
    - White (#FFFFFF) on dark backgrounds
    - Red (#FF0000) for dramatic effect
    - Yellow (#FFD700) for sun-lit trails
    """)

if __name__ == "__main__":
    main()
