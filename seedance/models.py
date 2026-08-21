import time
import os

class BaseAsset:
    """Base class for all generated assets."""
    def __init__(self, asset_id, format_type):
        self.asset_id = asset_id
        self.format_type = format_type

    def save(self, filename):
        """Simulates saving the asset to the local disk."""
        print(f"  [IO] Downloading asset {self.asset_id}...")
        time.sleep(1.0)  # Simulate network download
        
        # Create a dummy file to verify it works
        with open(filename, 'w') as f:
            f.write(f"Dummy content for asset {self.asset_id}")
            
        print(f"  [IO] Saved successfully to: {os.path.abspath(filename)}")

class VideoAsset(BaseAsset):
    """Represents a generated video file."""
    def __init__(self, asset_id, duration, resolution):
        super().__init__(asset_id, "mp4")
        self.duration = duration
        self.resolution = resolution

class VolumetricAsset(BaseAsset):
    """Represents a 3D NeRF or Gaussian Splat export."""
    def __init__(self, asset_id, polygons):
        super().__init__(asset_id, "ply")
        self.polygons = polygons
