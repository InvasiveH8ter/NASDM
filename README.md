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
Install Packages

% conda install -c conda-forge earthengine-api
% conda install -c anaconda pandas
% conda install -c anaconda geopandas
% conda install -c anaconda numpy
% conda install-c conda-forge json-e
% conda install-c requests
% conda install-c shapely
% conda install-c functools
% pip install notebook
```

#### Earthengine authentication
Make sure you have access to an Earth Engine account and have installed Python earthengine-api. 

Run the following code and follow the prompts.

% earthengine authenticate 

You should now have an environment variable set up an authentication key, which allows you to directly initialize ee without authenticating it every time.

---

## Workflow

###### Protip: GEE = Google Earth Engine

The two goals of this software are to produce a prediction visualization and produce a testing result histogram.
In order to do both of these, we need a set of environmental training data. 

The following sections will walk you through making your yearly covariate rasters.
For this section, it is assumed that your conda environment is properly set up.

### Config: aisconfig.ini
Open the aisconfig.ini file

* STATE: The US state that contains your presence/absence data points
* STATE_ABBREVIATION: The two letter abbreviation for your chosen state. e.g. Montana = MT
* START_YEAR: First year of interest range
* END_YEAR: Last year of interest range
* GEE_PATH: The GEE path to your Earth Engine user directory. Must end in a forward slash. e.g. `users/kjchristensen93/`
* ASSETID: GEE path to where the covariate files will be exported. This is a directory, it must end in a forward slash.

#### Make Covariates: ./make_covariates.py
% cd C:/Users/Where_you_stored_make_covariates.py

% python run make_covariates.py

#### Open the notebook
Open model script notebook using Conda by runnning:

% python -m notebook

Navigate to the directory with the model script and open the notebook.




