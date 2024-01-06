# NASDM
Non-Indigenous Aquatic Species Distribution Modeling Toolset

---

## Dependencies
You will need to install Anaconda (Conda) and to create a Google Earth Engine Developers account to use this pipeline.

* Create a Google Earth Engine account: https://code.earthengine.google.com/register
* Download and Install anaconda commandline terminal: https://www.anaconda.com/products/distribution
* Next download and store the scripts and background shapefile from this GitHub on your local drive.

---
#### Shorthand

GEE = Google Earth Engine

---
#### Setup Conda

Open the Anaconda PowerShell Terminal from your start menu.

This should make package installation run faster. The script will pause and ask you if you wish to proceed.  Type y and hit enter.
```
conda update -n base -c defaults conda
conda config --set channel_priority flexible
```

Create Conda environment. 

Replace NAME with your chosen environment name. The script will pause and ask you if you wish to proceed.  Type y and hit enter.
```
conda create -n NAME python=3 
```

Activate your new environment
```
conda activate NAME
```

#### Install Packages

The script will pause and ask you if you wish to proceed.  Type y and hit enter.

% means copy and run each line individually in the Conda Terminal
```
% conda install earthengine-api
% conda install geemap
% conda install GDAL
% conda install numpy
% conda install pandas
% conda install geopandas
% conda install jmcmurray::json
% pip install notebook
```
---

## Workflow

The two goals of this software are to produce a prediction visualization and produce a testing result histogram.
In order to do both of these, we need a set of environmental data. 

The following sections will walk you through making your yearly environmental rasters.
For this section, it is assumed that your Conda environment is properly set up.

#### Set up GEE folders
Go to https://developers.google.com/earth-engine
Create folder in your assets tab to store your yearly raster images in.  

#### Open the notebook
Back in Conda (w/ your environment activated) change to the directory containing the scripts you downloaded by running:
```
cd C:/users/YourPath
```
Open the Jupyter notebook using Conda by runnning:
```
python -m notebook
```
This will open a tab named Home in your browser which functions just like your Windows file folders.

You should see the 2 notebooks you downloaded:

Make_Covariates_github.ipynb
Model_script_github.ipynb

#### Make Yearly Covariate Rasters
Open the Make_Covariates notebook.  

Run the first 2 cells using the play button at the top and complete GEE authentication.

#### Configure the temporal and spatial settings for your taxa.
state_abbrev = 'XX' # 2-digit postal abbreviation

start_year = YYYY

end_year = YYYY

description = 'covariate' # this is the name displayed on the task tab in GEE developer dashboard

assetId = 'users/ee-Your-GEE-Cloud-ID/covariates_' # GEE path and name for where to store your yearly covariate rasters.

Run the rest of the cells to start creating yearly covariate rasters. These can take up to an hour depending on the size of the state. Progress can be examined on the task tab on your GEE Developers Dashboard

#### Run the model

Open the Model_script notebook

Configure paths for your covariate rasters and background GEE assets.

Obtain species ID via the link in the notebook.

Run all cells to produce a heatmap and histogram of false negatives.









