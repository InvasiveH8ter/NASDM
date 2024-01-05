# NASDM
Non-Indigenous Aquatic Species habitat suitability prediction toolset

---

## Dependencies
You will need to install Anaconda (Conda) and to create a Google Earth Engine Developers account to use this pipeline.

* Create a Google Earth Engine account: https://code.earthengine.google.com/register
* Download and Install anaconda commandline terminal: https://www.anaconda.com/products/distribution
* Next download and store the scripts from this GitHub on your local drive.

---
## Shorthand
% indicates type this into the terminal (without %)
---
## Setup Conda
Create Conda environment prior to using this package. Replace NAME with your chosen environment name

% conda create -n NAME python=3 

Activate your new environment
% conda activate NAME
```
This should make package installation run faster.
% conda update -n base -c defaults conda
...
Install Packages

% conda install -c conda-forge earthengine-api
% conda install -c conda-forge gdal
% conda install shapely
% conda install fiona
% conda install -c anaconda numpy
% conda install -c anaconda pandas
% conda install geopandas
% conda install jmcmurray::json
% pip install notebook
```

If you are getting an error when installing packages, you may need to copy libcrypto-1_1-x64.* and libssl-1_1-x64.* from anaconda3>library>bin to ananconda3>dlls.

#### Earthengine authentication
Make sure you have access to an Earth Engine account and have installed Python earthengine-api. 

Run the following code and follow the prompts.

% earthengine authenticate 

You should now have an environment variable set up an authentication key, which allows you to directly initialize ee without authenticating it every time.

---

## Workflow

###### Protip: GEE = Google Earth Engine

The two goals of this software are to produce a prediction visualization and produce a testing result histogram.
In order to do both of these, we need a set of environmental data. 

The following sections will walk you through making your yearly environmental rasters.
For this section, it is assumed that your conda environment is properly set up.

### Set up GEE directories
Go to https://developers.google.com/earth-engine
Create folder in your assets tab to store your yearly raster images in.  


### Config: aisconfig.ini
Open the aisconfig.ini file located in the Make_yearly_raster folder. This text document lets you configure your geographic and temporal parameters and indicate  the directory information for where you want the raster(s) stored in GEE. 

* STATE: The US state that contains your presence/absence data points
* STATE_ABBREVIATION: The two letter abbreviation for your chosen state. e.g. Montana = MT
* START_YEAR: First year of interest range
* END_YEAR: Last year of interest range
* GEE_PATH: The GEE path to your Earth Engine user directory. Must end in a forward slash. e.g. `users/kjchristensen93/`
* ASSETID: GEE path to where the covariate files will be exported. This is a directory, it must end in a forward slash.

Save the ini file so that your updates are read by the next script.

#### Make Covariates: ./make_covariates.py
Go back to your Conda terminal. Change to the directory where you stored the Make_yearly_raster folder.  

% cd C:/Users/YOUR_DIRECTORY/Make_yearly_raster

This code will produce yearly environmental rasters for your selected state and timeframe at 100-meter resolution.

% python make_covariates.py

This can take a while.  You can view the upload status within the task tab of your GEE developers dashboard.

#### Open the notebook
Open model script notebook using Conda by runnning:

% python -m notebook

Navigate to the directory with the model script and open the notebook.




