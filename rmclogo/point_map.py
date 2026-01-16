"""
Topographic Line Art Generator Library

Main library for generating Joy Division-style topographic visualizations
with support for PNG and SVG output, custom scaling, and advanced styling.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import srtm
import os
from scipy.ndimage import gaussian_filter
import svgwrite
import gpxpy
import gpxpy.gpx
from typing import Optional, Tuple, List


class TopomapGenerator:
    """
    Generates topographic line art from elevation data for any location on Earth.
    
    Features:
    - Worldwide coverage using SRTM elevation data
    - PNG and SVG output formats
    - Customizable styling and scaling
    - High-resolution output support
    """
    
    def __init__(self, output_dir: str = "output", cache_data: bool = True):
        """
        Initialize the generator.
        
        Args:
            output_dir: Directory to save output files
            cache_data: Whether to cache downloaded elevation data
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.elevation_data_handler = srtm.get_data()
        self.cache_data = cache_data
        
    def get_elevation_matrix(self, lat_min: float, lat_max: float, 
                            lon_min: float, lon_max: float, 
                            resolution: int = 100) -> np.ndarray:
        """
        Fetch elevation data for the specified bounds.
        
        Args:
            lat_min, lat_max: Latitude bounds
            lon_min, lon_max: Longitude bounds
            resolution: Number of sample points per dimension
            
        Returns:
            2D numpy array of elevation values in meters
        """
        print(f"Fetching elevation data...")
        print(f"Bounds: lat [{lat_min:.4f}, {lat_max:.4f}], lon [{lon_min:.4f}, {lon_max:.4f}]")
        
        lats = np.linspace(lat_min, lat_max, resolution)
        lons = np.linspace(lon_min, lon_max, resolution)
        
        elevation_matrix = np.zeros((resolution, resolution))
        
        for i, lat in enumerate(lats):
            for j, lon in enumerate(lons):
                try:
                    elev = self.elevation_data_handler.get_elevation(lat, lon)
                    elevation_matrix[i, j] = elev if elev is not None else np.nan
                except:
                    elevation_matrix[i, j] = np.nan
        
        # Fill nan values with mean of valid data
        mask = np.isnan(elevation_matrix)
        if mask.any():
            valid_mean = np.nanmean(elevation_matrix)
            elevation_matrix[mask] = valid_mean if not np.isnan(valid_mean) else 0
        
        print(f"Elevation data shape: {elevation_matrix.shape}")
        print(f"Elevation range: {np.nanmin(elevation_matrix):.1f}m to {np.nanmax(elevation_matrix):.1f}m")
        
        return elevation_matrix
    
    def process_elevation_data(self, elevation_data: np.ndarray, 
                              smoothing: bool = True,
                              sigma: float = 1.5) -> Tuple[np.ndarray, np.ndarray, float, float]:
        """
        Process and normalize elevation data.
        
        Args:
            elevation_data: Raw elevation matrix
            smoothing: Apply Gaussian smoothing
            sigma: Smoothing parameter
            
        Returns:
            Tuple of (normalized_data, raw_smoothed_data, min_elevation, max_elevation)
        """
        raw_smoothed = elevation_data.copy()
        if smoothing:
            raw_smoothed = gaussian_filter(elevation_data, sigma=sigma)
        
        elevation_min = np.nanmin(raw_smoothed)
        elevation_max = np.nanmax(raw_smoothed)
        elevation_range = elevation_max - elevation_min
        
        if elevation_range == 0:
            elevation_range = 1
            
        elevation_normalized = (raw_smoothed - elevation_min) / elevation_range
        
        return elevation_normalized, raw_smoothed, elevation_min, elevation_max
    
    def generate_line_profiles(self, elevation_normalized: np.ndarray,
                              num_lines: int,
                              exaggeration: float = 3.0,
                              scaling_factors: Optional[List[float]] = None) -> List[np.ndarray]:
        """
        Generate line profiles from elevation data.
        
        Args:
            elevation_normalized: Normalized elevation data (0-1)
            num_lines: Number of horizontal lines
            exaggeration: Vertical exaggeration factor
            scaling_factors: Optional per-line scaling factors (length must match num_lines)
            
        Returns:
            List of (x, y) coordinate arrays for each line
        """
        height, width = elevation_normalized.shape
        lines = []
        
        # Default scaling factors (1.0 for all lines)
        if scaling_factors is None:
            scaling_factors = [1.0] * num_lines
        elif len(scaling_factors) != num_lines:
            raise ValueError(f"scaling_factors length ({len(scaling_factors)}) must match num_lines ({num_lines})")
        
        for i in range(num_lines):
            row_idx = int((i / num_lines) * (height - 1))
            profile = elevation_normalized[row_idx, :]
            
            x = np.linspace(0, width, width)
            y = profile * exaggeration * scaling_factors[i]
            
            lines.append((x, y))
        
        return lines
    
    def create_png(self, elevation_data: np.ndarray, 
                   num_lines: int = 80,
                   exaggeration: float = 3.0,
                   scaling_factors: Optional[List[float]] = None,
                   line_spacing: float = 1.0,
                   bg_color: str = '#2B1B4D',
                   line_color: str = 'white',
                   line_width: float = 1.5,
                   fill_below: bool = True,
                   smoothing: bool = True,
                   skip_zero_elevation: bool = True,
                   figsize: Tuple[int, int] = (12, 16),
                   dpi: int = 300) -> plt.Figure:
        """
        Create PNG visualization of topographic data.
        
        Args:
            elevation_data: 2D elevation array
            num_lines: Number of horizontal lines
            exaggeration: Vertical exaggeration factor
            scaling_factors: Optional per-line scaling factors
            line_spacing: Vertical spacing between lines
            bg_color: Background color
            line_color: Line color
            line_width: Line thickness
            fill_below: Fill area below lines
            smoothing: Apply smoothing
            skip_zero_elevation: Skip drawing lines where elevation <= 0 (e.g., sea)
            figsize: Figure size in inches
            dpi: Dots per inch
            
        Returns:
            matplotlib Figure object
        """
        elevation_normalized, raw_elevation, _, _ = self.process_elevation_data(elevation_data, smoothing)
        height, width = elevation_data.shape
        
        # Create figure
        fig, ax = plt.subplots(figsize=figsize, facecolor=bg_color)
        ax.set_facecolor(bg_color)
        
        # Calculate line positions
        y_positions = np.linspace(0, num_lines * line_spacing, num_lines)
        
        # Default scaling factors
        if scaling_factors is None:
            scaling_factors = [1.0] * num_lines
        
        # Draw each line
        for i, y_pos in enumerate(y_positions):
            row_idx = int((i / num_lines) * (height - 1))
            profile = elevation_normalized[row_idx, :]
            raw_profile = raw_elevation[row_idx, :]
            
            x = np.linspace(0, width, width)
            y = y_pos - profile * exaggeration * line_spacing * scaling_factors[i]
            
            if skip_zero_elevation:
                # Split into segments where elevation > 0
                segments = self._split_line_by_elevation(x, y, raw_profile)
                
                if fill_below:
                    for seg_x, seg_y in segments:
                        if len(seg_x) < 2:
                            continue
                        vertices = []
                        codes = []
                        
                        vertices.append([seg_x[0], y_pos + line_spacing])
                        codes.append(Path.MOVETO)
                        
                        for xi, yi in zip(seg_x, seg_y):
                            vertices.append([xi, yi])
                            codes.append(Path.LINETO)
                        
                        vertices.append([seg_x[-1], y_pos + line_spacing])
                        codes.append(Path.LINETO)
                        vertices.append([seg_x[0], y_pos + line_spacing])
                        codes.append(Path.CLOSEPOLY)
                        
                        path = Path(vertices, codes)
                        patch = patches.PathPatch(path, facecolor=bg_color, 
                                                 edgecolor=line_color, 
                                                 linewidth=line_width,
                                                 zorder=num_lines - i)
                        ax.add_patch(patch)
                else:
                    for seg_x, seg_y in segments:
                        if len(seg_x) >= 2:
                            ax.plot(seg_x, seg_y, color=line_color, linewidth=line_width, 
                                   zorder=num_lines - i)
            else:
                # Draw continuous line (original behavior)
                if fill_below:
                    vertices = []
                    codes = []
                    
                    vertices.append([x[0], y_pos + line_spacing])
                    codes.append(Path.MOVETO)
                    
                    for xi, yi in zip(x, y):
                        vertices.append([xi, yi])
                        codes.append(Path.LINETO)
                    
                    vertices.append([x[-1], y_pos + line_spacing])
                    codes.append(Path.LINETO)
                    vertices.append([x[0], y_pos + line_spacing])
                    codes.append(Path.CLOSEPOLY)
                    
                    path = Path(vertices, codes)
                    patch = patches.PathPatch(path, facecolor=bg_color, 
                                             edgecolor=line_color, 
                                             linewidth=line_width,
                                             zorder=num_lines - i)
                    ax.add_patch(patch)
                else:
                    ax.plot(x, y, color=line_color, linewidth=line_width, 
                           zorder=num_lines - i)
        
        ax.set_xlim(0, width)
        ax.set_ylim(-line_spacing, num_lines * line_spacing + line_spacing)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout(pad=0)
        
        return fig
    
    def _split_line_by_elevation(self, x: np.ndarray, y: np.ndarray, 
                                  raw_elevation: np.ndarray, 
                                  threshold: float = 0.0) -> List[Tuple[np.ndarray, np.ndarray]]:
        """
        Split a line into segments where elevation is above threshold.
        
        Args:
            x: X coordinates
            y: Y coordinates
            raw_elevation: Raw elevation values
            threshold: Elevation threshold (default 0.0 for sea level)
            
        Returns:
            List of (x, y) segment tuples
        """
        segments = []
        current_x = []
        current_y = []
        
        for i, elev in enumerate(raw_elevation):
            if elev > threshold:
                current_x.append(x[i])
                current_y.append(y[i])
            else:
                if len(current_x) >= 2:
                    segments.append((np.array(current_x), np.array(current_y)))
                current_x = []
                current_y = []
        
        # Add final segment if exists
        if len(current_x) >= 2:
            segments.append((np.array(current_x), np.array(current_y)))
        
        return segments
    
    def create_svg(self, elevation_data: np.ndarray,
                   output_path: str,
                   num_lines: int = 80,
                   exaggeration: float = 3.0,
                   scaling_factors: Optional[List[float]] = None,
                   line_spacing: float = 1.0,
                   bg_color: str = '#2B1B4D',
                   line_color: str = 'white',
                   line_width: float = 1.5,
                   smoothing: bool = True,
                   skip_zero_elevation: bool = True,
                   width: int = 1200,
                   height: int = 1600) -> str:
        """
        Create SVG visualization (vector format, perfect for logos).
        
        Args:
            elevation_data: 2D elevation array
            output_path: Path to save SVG file
            num_lines: Number of horizontal lines
            exaggeration: Vertical exaggeration factor
            scaling_factors: Optional per-line scaling factors
            line_spacing: Vertical spacing between lines
            bg_color: Background color
            line_color: Line color
            line_width: Line thickness
            smoothing: Apply smoothing
            skip_zero_elevation: Skip drawing lines where elevation <= 0 (e.g., sea)
            width: SVG width in pixels
            height: SVG height in pixels
            
        Returns:
            Path to saved SVG file
        """
        elevation_normalized, raw_elevation, _, _ = self.process_elevation_data(elevation_data, smoothing)
        data_height, data_width = elevation_data.shape
        
        # Create SVG drawing
        dwg = svgwrite.Drawing(output_path, size=(width, height), profile='full')
        dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill=bg_color))
        
        # Calculate scaling
        scale_x = width / data_width
        scale_y = height / (num_lines * line_spacing + 2 * line_spacing)
        
        # Default scaling factors
        if scaling_factors is None:
            scaling_factors = [1.0] * num_lines
        
        # Draw each line
        for i in range(num_lines):
            row_idx = int((i / num_lines) * (data_height - 1))
            profile = elevation_normalized[row_idx, :]
            raw_profile = raw_elevation[row_idx, :]
            
            y_base = (i * line_spacing + line_spacing) * scale_y
            
            points = []
            for j, elev in enumerate(profile):
                x = j * scale_x
                y = y_base - elev * exaggeration * line_spacing * scale_y * scaling_factors[i]
                points.append((x, y, raw_profile[j]))
            
            if skip_zero_elevation:
                # Split into segments where elevation > 0
                segments = self._split_svg_points_by_elevation(points)
                
                for segment in segments:
                    if len(segment) >= 2:
                        # Create polyline for this segment
                        seg_points = [(p[0], p[1]) for p in segment]
                        polyline = dwg.polyline(points=seg_points, 
                                               stroke=line_color,
                                               stroke_width=line_width,
                                               fill='none')
                        dwg.add(polyline)
            else:
                # Draw continuous line (original behavior)
                line_points = [(p[0], p[1]) for p in points]
                polyline = dwg.polyline(points=line_points, 
                                       stroke=line_color,
                                       stroke_width=line_width,
                                       fill='none')
                dwg.add(polyline)
        
        dwg.save()
        print(f"SVG saved to: {output_path}")
        return output_path
    
    def _split_svg_points_by_elevation(self, points: List[Tuple[float, float, float]], 
                                       threshold: float = 0.0) -> List[List[Tuple[float, float, float]]]:
        """
        Split SVG points into segments where elevation is above threshold.
        
        Args:
            points: List of (x, y, elevation) tuples
            threshold: Elevation threshold (default 0.0 for sea level)
            
        Returns:
            List of point segment lists
        """
        segments = []
        current_segment = []
        
        for point in points:
            x, y, elev = point
            if elev > threshold:
                current_segment.append(point)
            else:
                if len(current_segment) >= 2:
                    segments.append(current_segment)
                current_segment = []
        
        # Add final segment if exists
        if len(current_segment) >= 2:
            segments.append(current_segment)
        
        return segments
    
    def generate(self, latitude: float, longitude: float,
                size_km: float = 10,
                resolution: int = 100,
                num_lines: int = 80,
                exaggeration: float = 3.0,
                scaling_factors: Optional[List[float]] = None,
                output_filename: str = "topomap.png",
                title: Optional[str] = None,
                format: str = 'png',
                **kwargs) -> str:
        """
        Generate a topographic line art image.
        
        Args:
            latitude: Center latitude
            longitude: Center longitude
            size_km: Square area size in kilometers
            resolution: Elevation sample points per dimension
            num_lines: Number of horizontal lines
            exaggeration: Vertical exaggeration factor
            scaling_factors: Optional per-line scaling factors
            output_filename: Output file name
            title: Optional title text
            format: Output format ('png' or 'svg')
            **kwargs: Additional format-specific arguments
            
        Returns:
            Path to saved file
        """
        # Calculate bounds
        lat_offset = (size_km / 111.0) / 2
        lon_offset = (size_km / (111.0 * np.cos(np.radians(latitude)))) / 2
        
        lat_min = latitude - lat_offset
        lat_max = latitude + lat_offset
        lon_min = longitude - lon_offset
        lon_max = longitude + lon_offset
        
        print(f"\n{'='*60}")
        print(f"Generating topographic art for: {latitude:.4f}, {longitude:.4f}")
        print(f"Area: {size_km}km × {size_km}km")
        print(f"Format: {format.upper()}")
        print(f"{'='*60}\n")
        
        # Get elevation data
        elevation_data = self.get_elevation_matrix(lat_min, lat_max, lon_min, lon_max, resolution)
        
        # Generate output
        output_path = os.path.join(self.output_dir, output_filename)
        
        if format.lower() == 'svg':
            print("\nCreating SVG visualization...")
            self.create_svg(elevation_data, output_path, num_lines, exaggeration,
                          scaling_factors, **kwargs)
        elif format.lower() == 'halftone':
            print("\nCreating halftone visualization...")
            
            # Separate GPX parameters from halftone parameters
            gpx_params = ['gpx_file', 'gpx_color', 'gpx_width', 'gpx_style', 'gpx_alpha', 'gpx_zorder']
            halftone_kwargs = {k: v for k, v in kwargs.items() if k not in gpx_params}
            
            fig = self.create_halftone(elevation_data, **halftone_kwargs)
            
            # Get axes for overlay
            ax = fig.axes[0] if fig.axes else None
            height, width = elevation_data.shape
            
            # Add GPX overlay if specified
            if 'gpx_file' in kwargs and kwargs['gpx_file'] and ax:
                print("\nAdding GPX track overlay...")
                self.overlay_gpx_track(
                    fig, ax, kwargs['gpx_file'],
                    lat_min, lat_max, lon_min, lon_max,
                    height, width,
                    line_color=kwargs.get('gpx_color', '#000000'),
                    line_width=kwargs.get('gpx_width', 2.0),
                    line_style=kwargs.get('gpx_style', '-'),
                    alpha=kwargs.get('gpx_alpha', 1.0),
                    zorder=kwargs.get('gpx_zorder', 10)
                )
            
            if title:
                fig.text(0.5, 0.98, title, ha='center', va='top',
                        color=kwargs.get('dot_color', '#000000'), 
                        fontsize=16, weight='bold')
            
            fig.savefig(output_path, dpi=kwargs.get('dpi', 300),
                       bbox_inches='tight', facecolor=fig.get_facecolor(),
                       edgecolor='none')
            plt.close(fig)
        else:  # png
            print("\nCreating PNG visualization...")
            
            # Separate GPX parameters from PNG parameters
            gpx_params = ['gpx_file', 'gpx_color', 'gpx_width', 'gpx_style', 'gpx_alpha', 'gpx_zorder']
            png_kwargs = {k: v for k, v in kwargs.items() if k not in gpx_params}
            
            fig = self.create_png(elevation_data, num_lines, exaggeration,
                                scaling_factors, **png_kwargs)
            
            # Get axes for overlay
            ax = fig.axes[0] if fig.axes else None
            height, width = elevation_data.shape
            
            # Add GPX overlay if specified
            if 'gpx_file' in kwargs and kwargs['gpx_file'] and ax:
                print("\nAdding GPX track overlay...")
                self.overlay_gpx_track(
                    fig, ax, kwargs['gpx_file'],
                    lat_min, lat_max, lon_min, lon_max,
                    height, width,
                    line_color=kwargs.get('gpx_color', '#000000'),
                    line_width=kwargs.get('gpx_width', 2.0),
                    line_style=kwargs.get('gpx_style', '-'),
                    alpha=kwargs.get('gpx_alpha', 1.0),
                    zorder=kwargs.get('gpx_zorder', 10)
                )
            
            if title:
                fig.text(0.5, 0.98, title, ha='center', va='top',
                        color='white', fontsize=16, weight='bold')
            
            fig.savefig(output_path, dpi=kwargs.get('dpi', 300),
                       bbox_inches='tight', facecolor=fig.get_facecolor(),
                       edgecolor='none')
            plt.close(fig)
        
        print(f"\n✅ Topographic art saved to: {output_path}\n")
        return output_path
    
    def create_halftone(self, elevation_data: np.ndarray,
                       dot_size_range: Tuple[float, float] = (0.5, 8.0),
                       grid_spacing: int = 10,
                       bg_color: str = '#ffffff',
                       dot_color: str = '#000000',
                       invert: bool = False,
                       smoothing: bool = True,
                       skip_zero_elevation: bool = True,
                       figsize: Tuple[int, int] = (12, 16),
                       dpi: int = 300,
                       fast_render: bool = True) -> plt.Figure:
        """
        Create halftone visualization of topographic data.
        
        Uses dots of varying sizes to represent elevation - larger dots for
        higher elevations, creating a newspaper/print-style artistic effect.
        
        Args:
            elevation_data: 2D elevation array
            dot_size_range: Tuple of (min_size, max_size) for dots
            grid_spacing: Spacing between dot centers in pixels
            bg_color: Background color
            dot_color: Dot color
            invert: If True, larger dots = lower elevation
            smoothing: Apply smoothing to elevation data
            skip_zero_elevation: Skip dots where elevation <= 0
            figsize: Figure size in inches
            dpi: Dots per inch
            fast_render: Use optimized vectorized rendering (recommended)
            
        Returns:
            matplotlib Figure object
        """
        elevation_normalized, raw_elevation, _, _ = self.process_elevation_data(
            elevation_data, smoothing
        )
        
        height, width = elevation_data.shape
        
        # Create figure
        fig, ax = plt.subplots(figsize=figsize, facecolor=bg_color)
        ax.set_facecolor(bg_color)
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Create grid of dot positions
        x_positions = np.arange(0, width, grid_spacing)
        y_positions = np.arange(0, height, grid_spacing)
        
        min_dot_size, max_dot_size = dot_size_range
        
        if fast_render:
            # OPTIMIZED: Vectorized approach (10-50x faster!)
            # Create meshgrid of all dot positions at once
            xx, yy = np.meshgrid(x_positions, y_positions)
            
            # Flatten to 1D arrays
            x_flat = xx.ravel()
            y_flat = yy.ravel()
            
            # Get elevation values at all positions (vectorized)
            y_indices = np.clip(y_flat.astype(int), 0, height - 1)
            x_indices = np.clip(x_flat.astype(int), 0, width - 1)
            
            elevation_norm_flat = elevation_normalized[y_indices, x_indices]
            elevation_raw_flat = raw_elevation[y_indices, x_indices]
            
            # Apply masking if needed (vectorized)
            if skip_zero_elevation:
                mask = elevation_raw_flat > 0
                x_flat = x_flat[mask]
                y_flat = y_flat[mask]
                elevation_norm_flat = elevation_norm_flat[mask]
            
            # Calculate all dot sizes at once (vectorized)
            if invert:
                dot_sizes = min_dot_size + (1 - elevation_norm_flat) * (max_dot_size - min_dot_size)
            else:
                dot_sizes = min_dot_size + elevation_norm_flat * (max_dot_size - min_dot_size)
            
            # Draw all dots at once using scatter (much faster than individual patches)
            # Note: scatter size is area, so we square the radius
            ax.scatter(x_flat, y_flat, s=(dot_sizes * 2)**2, c=dot_color, 
                      alpha=1.0, edgecolors='none', zorder=1)
        else:
            # LEGACY: Original loop-based approach (slower but more precise)
            for y_idx, y in enumerate(y_positions):
                for x_idx, x in enumerate(x_positions):
                    # Get elevation at this position
                    y_data = min(int(y), height - 1)
                    x_data = min(int(x), width - 1)
                    
                    elevation_norm = elevation_normalized[y_data, x_data]
                    elevation_raw = raw_elevation[y_data, x_data]
                    
                    # Skip if elevation is zero or below (sea level)
                    if skip_zero_elevation and elevation_raw <= 0:
                        continue
                    
                    # Calculate dot size based on elevation
                    if invert:
                        dot_size = min_dot_size + (1 - elevation_norm) * (max_dot_size - min_dot_size)
                    else:
                        dot_size = min_dot_size + elevation_norm * (max_dot_size - min_dot_size)
                    
                    # Draw dot
                    circle = plt.Circle((x, y), dot_size, color=dot_color, zorder=1)
                    ax.add_patch(circle)
        
        plt.tight_layout(pad=0)
        return fig
    
    def load_gpx_track(self, gpx_file: str) -> List[Tuple[float, float]]:
        """
        Load GPS track from GPX file.
        
        Args:
            gpx_file: Path to GPX file
            
        Returns:
            List of (latitude, longitude) tuples
        """
        with open(gpx_file, 'r') as f:
            gpx = gpxpy.parse(f)
        
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append((point.latitude, point.longitude))
        
        return points
    
    def latlon_to_image_coords(self, lat: float, lon: float,
                              lat_min: float, lat_max: float,
                              lon_min: float, lon_max: float,
                              height: int, width: int) -> Tuple[float, float]:
        """
        Convert latitude/longitude to image coordinates.
        
        Args:
            lat, lon: Point coordinates
            lat_min, lat_max: Map latitude bounds
            lon_min, lon_max: Map longitude bounds
            height, width: Image dimensions
            
        Returns:
            (x, y) image coordinates
        """
        # Normalize to [0, 1]
        lat_norm = (lat - lat_min) / (lat_max - lat_min)
        lon_norm = (lon - lon_min) / (lon_max - lon_min)
        
        # Convert to image coordinates
        # For matplotlib: Y-axis has 0 at bottom (standard Cartesian)
        x = lon_norm * width
        y = lat_norm * height
        
        return x, y
    
    def overlay_gpx_track(self, fig: plt.Figure, ax: plt.Axes,
                         gpx_file: str,
                         lat_min: float, lat_max: float,
                         lon_min: float, lon_max: float,
                         height: int, width: int,
                         line_color: str = '#000000',
                         line_width: float = 2.0,
                         line_style: str = '-',
                         alpha: float = 1.0,
                         zorder: int = 10) -> None:
        """
        Overlay GPX track on existing figure.
        
        Args:
            fig: Matplotlib figure
            ax: Matplotlib axes
            gpx_file: Path to GPX file
            lat_min, lat_max: Map latitude bounds
            lon_min, lon_max: Map longitude bounds
            height, width: Image dimensions
            line_color: Track color
            line_width: Track width in pixels
            line_style: Line style ('-', '--', ':', '-.')
            alpha: Line transparency (0-1)
            zorder: Drawing order (higher = on top)
        """
        # Load GPX track
        points = self.load_gpx_track(gpx_file)
        
        if not points:
            print("Warning: No GPS points found in GPX file")
            return
        
        # Convert to image coordinates
        x_coords = []
        y_coords = []
        
        for lat, lon in points:
            # Skip points outside the map bounds
            if not (lat_min <= lat <= lat_max and lon_min <= lon <= lon_max):
                continue
            
            x, y = self.latlon_to_image_coords(
                lat, lon, lat_min, lat_max, lon_min, lon_max, height, width
            )
            x_coords.append(x)
            y_coords.append(y)
        
        if len(x_coords) < 2:
            print("Warning: Not enough points in map bounds to draw track")
            return
        
        # Draw the track
        ax.plot(x_coords, y_coords,
               color=line_color,
               linewidth=line_width,
               linestyle=line_style,
               alpha=alpha,
               zorder=zorder,
               solid_capstyle='round',
               solid_joinstyle='round')
        
        print(f"✅ GPX track overlaid: {len(x_coords)} points plotted")


def create_gradient_scaling(num_lines: int, start: float = 0.5,
                           end: float = 1.5, style: str = 'linear') -> List[float]:
    """
    Create gradient scaling factors for lines.
    
    Args:
        num_lines: Number of lines
        start: Starting scale factor
        end: Ending scale factor
        style: Gradient style ('linear', 'ease_in', 'ease_out')
        
    Returns:
        List of scaling factors
    """
    t = np.linspace(0, 1, num_lines)
    
    if style == 'linear':
        factors = start + (end - start) * t
    elif style == 'ease_in':
        factors = start + (end - start) * t**2
    elif style == 'ease_out':
        factors = start + (end - start) * (1 - (1-t)**2)
    else:
        factors = np.ones(num_lines)
    
    return factors.tolist()
