import pytest
import numpy as np
from tensoredge.quantizer import Quantizer

def test_quantization_range():
    q = Quantizer(bits=8)
    data = np.random.uniform(-1.0, 1.0, (100,))
    q_data = q.quantize(data)
    
    assert q_data.dtype == np.int8
    assert q_data.max() <= 127
    assert q_data.min() >= -128

def test_dequantization_error():
    q = Quantizer(bits=8)
    data = np.array([-1.0, 0.0, 1.0], dtype=np.float32)
    q_data = q.quantize(data)
    dq_data = q.dequantize(q_data)
    
    # Check if reconstruction error is low
    np.testing.assert_allclose(data, dq_data, atol=0.1)
