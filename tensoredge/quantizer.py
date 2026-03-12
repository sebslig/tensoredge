import numpy as np
from typing import Dict, Any

class Quantizer:
    """Handles the conversion of float32 weights to int8 for edge deployment."""
    
    def __init__(self, bits: int = 8):
        self.bits = bits
        self.scale = None
        self.zero_point = None

    def compute_params(self, data: np.ndarray):
        """Calculates scaling factors for symmetric quantization."""
        min_val, max_val = data.min(), data.max()
        q_min = -(2**(self.bits - 1))
        q_max = 2**(self.bits - 1) - 1
        
        self.scale = (max_val - min_val) / (q_max - q_min)
        self.zero_point = q_min - (min_val / self.scale)
        return self.scale, int(self.zero_point)

    def quantize(self, data: np.ndarray) -> np.ndarray:
        """Converts float data to quantized integers."""
        if self.scale is None:
            self.compute_params(data)
        
        q_data = (data / self.scale) + self.zero_point
        return np.clip(np.round(q_data), -128, 127).astype(np.int8)

    def dequantize(self, q_data: np.ndarray) -> np.ndarray:
        """Reconstructs float data for validation purposes."""
        return self.scale * (q_data.astype(np.float32) - self.zero_point)
