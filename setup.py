from setuptools import setup, find_packages

setup(
    name="tensoredge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
    ],
    author="EdgeAI Ops",
    description="Quantized AI agents for edge devices",
    python_requires=">=3.8",
)
