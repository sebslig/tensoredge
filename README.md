# Tensoredge

Tensoredge is a high-performance, lightweight inference engine designed specifically for edge devices. It bridges the gap between complex neural architectures and hardware-constrained environments by leveraging 8-bit quantization and the OpenClaw agent abstraction layer.

## Key Features

*   **Int8 Quantization**: Custom quantization-aware inference to reduce memory footprint by 75%.
*   **OpenClaw Integration**: First-class support for deploying autonomous agents on the edge.
*   **Zero-Dependency Core**: The C++ inference engine has minimal external dependencies.
*   **Python Bindings**: Seamlessly prototype in Python and deploy on embedded systems.
*   **Hardware Optimized**: Hand-tuned kernels for common activation functions.

## Architecture

Tensoredge operates on a flat memory buffer model. Models are compiled into a proprietary `.tedge` format that maps directly to memory, allowing for zero-copy loading.

## Installation

```bash
# Clone the repository
git clone https://github.com/username/tensoredge.git
cd tensoredge

# Install Python package
pip install .

# Build C++ core
mkdir build && cd build
cmake ..
make
```

## Quick Start: Creating an AI Agent

```python
from tensoredge.agents import EdgeAgent
from tensoredge.quantizer import Quantizer

# Load a pre-trained model
quantizer = Quantizer(bits=8)
model = quantizer.optimize("model_weights.pt")

# Create an OpenClaw enabled agent
agent = EdgeAgent(
    model=model,
    role="Environmental Monitor",
    threshold=0.85
)

# Run inference
result = agent.process({"sensor_id": "temp_01", "value": 24.5})
print(f"Agent Decision: {result}")
```

## Supported Operations

*   Linear / Dense layers
*   ReLU, Sigmoid, Tanh activations
*   1D/2D Convolution (Optimized)
*   Global Average Pooling
*   Softmax

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
