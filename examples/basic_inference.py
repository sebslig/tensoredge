import numpy as np
from tensoredge.quantizer import Quantizer
from tensoredge.agents import EdgeAgent

def run_example():
    # 1. Create fake weights
    print("--- 1. Generating Model Weights ---")
    weights = np.random.randn(10, 10).astype(np.float32)
    
    # 2. Quantize
    print("--- 2. Quantizing to Int8 ---")
    q = Quantizer(bits=8)
    q_weights = q.quantize(weights)
    print(f"Quantized weights shape: {q_weights.shape}, Type: {q_weights.dtype}")
    
    # 3. Create Agent
    print("--- 3. Initializing Edge Agent ---")
    agent = EdgeAgent(model_path="example.tedge", role="SecurityGuard")
    
    # 4. Process Data
    print("--- 4. Running Inference ---")
    response = agent.process({"motion": True})
    print(f"Agent response: {response}")

if __name__ == "__main__":
    run_example()
