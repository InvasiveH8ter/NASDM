# NASDM
Non-Indigenous Aquatic Species habitat suitability prediction toolset

---

## Dependencies
You will need access to a Google Earth Engine account in order to use this package.
In addidtion, the following software and packages are required:

* anaconda commandline 
* python 3
* earthengine-api 
* pandas
* geopandas
* numpy
* json-e
* requests
* shapely
* functools
* Matplotlib

---

## Setup 
#### Conda
It is recommended that you set up a conda environment prior to using this package.
If you choose not to, continue down to [Earthengine authentication](#earthengine-authentication). 
```
% conda create -n gee python=3
% source activate gee
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
Run `earthengine authenticate` and follow the prompts.\
You should now have an environment variable set up an authentication key, which allows you to directly initialize ee without authenticating it every time.

---

## Workflow

###### Protip: GEE = Google Earth Engine

The two goals of this software are to produce a prediction visualization and produce a testing resukt histogram.
In order to do both of these, we need a set of training data. 

The following sections will walk you through making your yearly covariate rasters.
For this section, it is assumed that your environment is properly set up.

### Config: aisconfig.ini
* STATE: The US state that contains your presence/absence data points
* STATE_ABBREVIATION: The two letter abbreviation for your chosen state. e.g. Montana = MT
* START_YEAR: First year of interest range
* END_YEAR: Last year of interest range

* GEE_PATH: The GEE path to your Earth Engine user directory. Must end in a forward slash. e.g. `users/kjchristensen93/`
* AIS_POINT_PATH: The GEE path to your (unthinned) presence/absence asset. This is the path to an asset, not to a directory. It must NOT end in a forward slash.  
* AIS_THINNED_POINT_PATH: The GEE path to your thinned presence/absence asset. This is a path to an asset, not to a directory. It mush NOT end in a forward slash.
* ASSETID: GEE path to where the covariate files will be exported. This is a directory, it must end in a forward slash.

#### Make Covariates: ./make_covariates.py
Required config variables:\
START_YEAR, END_YEAR, STATE, ASSETID

#### Open the notebook
Open model script notebook using Conda by runnning:

% python -m notebook


## Contributors 
Sean Carter\
Leif Howard\
Myles Stokowski\
Kevin Christensen

