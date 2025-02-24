import subprocess

def run_command(command):
    """Runs a command in Conda PowerShell."""
    process = subprocess.run(command, shell=True, text=True, capture_output=True)
    if process.returncode == 0:
        print(process.stdout)
    else:
        print(process.stderr)

def setup_environment():
    """Creates a Conda environment and installs packages."""
    print("Creating Conda environment: nasdm...")
    run_command("conda create --name nasdm python=3.9 -y")
    
    print("Installing additional dependencies...")
    run_command("conda run --name nasdm conda install -c conda-forge pandas numpy requests folium rasterio scikit-learn seaborn geopandas fiona scikit-gstat  gstools pykrige -y")

    run_command("conda run --name nasdm pip install notebook")

    print("Setup complete! You can now use the nasdm environment by running: conda activate nasdm")

if __name__ == "__main__":
    setup_environment()
