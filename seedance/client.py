import time
import uuid
import random
from .models import VideoAsset, VolumetricAsset

class Client:
    """
    Main entry point for the Seedance 2.0 SDK.
    Handles authentication and API requests.
    """

    def __init__(self, api_key=None):
        # In a real app, we would validate the key here
        self.api_key = api_key or "sd_mock_key"
        self.base_url = "https://api.seedance.byte/v2"
        print(f"[Seedance] Client initialized. Connected to {self.base_url}")

    def _simulate_processing(self, task_name, duration=2.0):
        """Helper to simulate server-side processing time."""
        print(f"[API] Sending task: {task_name}...")
        time.sleep(0.5)
        print(f"[Server] Processing... (AI Magic in progress)")
        
        # Simple progress bar simulation
        steps = 5
        for i in range(steps):
            time.sleep(duration / steps)
            print(f"  └── Render pass {i+1}/{steps}: {(i+1)*20}% completed")
        
        print("[Server] Task completed.")

    def generate(self, prompt, resolution="1080p", duration=5):
        """
        Generates a video from text prompt.
        
        Args:
            prompt (str): Description of the scene.
            resolution (str): Output quality (e.g., '2k', '1080p').
            duration (int): Length in seconds.
            
        Returns:
            VideoAsset: The generated video object.
        """
        task_id = str(uuid.uuid4())[:8]
        print(f"\n--- Starting Generation Task [{task_id}] ---")
        print(f"  Prompt: '{prompt}'")
        print(f"  Config: {resolution} @ {duration}s")

        self._simulate_processing("Text-to-Video Generation", duration=2.5)
        
        return VideoAsset(asset_id=task_id, duration=duration, resolution=resolution)

    def generate_3d(self, prompt, format="gaussian_splat"):
        """
        Generates a 3D volumetric scene.
        """
        task_id = str(uuid.uuid4())[:8]
        print(f"\n--- Starting 3D Export Task [{task_id}] ---")
        print(f"  Prompt: '{prompt}'")
        print(f"  Format: {format}")

        self._simulate_processing("NeRF/Splat Synthesis", duration=3.5)
        
        return VolumetricAsset(asset_id=task_id, polygons=random.randint(50000, 100000))
