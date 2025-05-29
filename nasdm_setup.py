import subprocess

def run_command(command):
    """Runs a command in Conda PowerShell or shell."""
    process = subprocess.run(command, shell=True, text=True, capture_output=True)
    if process.returncode == 0:
        print(process.stdout)
    else:
        print(f"Error: {process.stderr}")

def setup_environment():
    """Creates a Conda environment and installs required packages."""
    print("Creating Conda environment: nasdm...")
    run_command("conda create --name nasdm python=3.9 -y")

    print("Installing Conda packages via conda-forge...")
    conda_packages = [
        "pandas", "numpy", "requests", "folium", "rasterio",
        "scikit-learn", "seaborn", "geopandas", "fiona", "skgstat",
        "gstools", "pykrige", "affine", "networkx", "shapely",
        "joblib", "tqdm", "matplotlib"
    ]
    run_command(f"conda run --name nasdm conda install -c conda-forge {' '.join(conda_packages)} -y")

    print("Installing pip-only packages...")
    run_command("conda run --name nasdm pip install notebook pygbif")

    print("Setup complete! Activate with: conda activate nasdm")

if __name__ == "__main__":
    setup_environment()
