import json
import numpy as np

def save_tedge_model(path, layers):
    """Saves a dictionary of layers into a flat binary format."""
    with open(path, 'wb') as f:
        # Header: Number of layers
        f.write(np.int32(len(layers)).tobytes())
        for name, weights in layers.items():
            # Layer name length + name
            name_bytes = name.encode('utf-8')
            f.write(np.int32(len(name_bytes)).tobytes())
            f.write(name_bytes)
            # Shape
            f.write(np.int32(len(weights.shape)).tobytes())
            for dim in weights.shape:
                f.write(np.int32(dim).tobytes())
            # Data
            f.write(weights.tobytes())

def load_tedge_summary(path):
    """Utility to print metadata of a .tedge file."""
    print(f"Analyzing model: {path}")
    # Implementation omitted for brevity
