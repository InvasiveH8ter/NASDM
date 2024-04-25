# Non-Indigenous Aquatic Species Distribution Modeling Toolset (NASDM)
----
## The following provides background and detailed instructions to produce environmental images, pull occurrence data from the USGS NAS database and relevant environmental data (e.g. remote sensing, see next section), to produce risk-maps for invasive species spread. This toolset also produces performance metrics to allowing managers to asses uncertainty in hotspot rankings (e.g., false AIS detection rates). The instructions below include screenshots to help walk you through the setup and running of this workflow (to model and map AIS-invasion hotspots). Instructions for customization (for your species or geographic area of interest) are also integrated throughout the various scripts used for this workflow. The locations for the blocks of code for specific customization are provided at the end of this document. The following tools and workflow can be applied to other species of interest including threatened native species to understand and predict habitat suitability and species distribution modeling (SDMs) (e.g, Carter et al. 2021 & van Reese et al. 2022?)

## *development Sponsored by NASA

----
## Definitions
The USGS Non-Indigenous Aquatic Species (NAS) database = The most comprehensive North American record of occurences for more than 2,000 NAS.  This script is designed to pull data directly from this database via species ID and can be used to model any taxa on the NAS database. Information for obtaining these species ID's is provided below and within the model script. To see the current distributions of a NAS visit: https://nas.er.usgs.gov/default.aspx.

Google Earth Engine (GEE) = Interactive online development environment for using RSD w/ built-in modeling functions. Earth Engine has emerged as a solution to democratizing the use of big data. Here we combine publically available RSD products from NASA and other sources with the computing power of Google to provide a solution to predicting the risk of spread for NAS. Instructions for registering your non-commercial (academic/research) project are provided below. 

Jupyter Notebook = Application for writing and organizing Python code into blocks. We provide (below) Jupiter Notebooks with code (scripts) you can use to quickly start running models to predict and map AIS.

Python = High-level programing language for data manipulation and communicating with online databases. 

Anaconda (Conda) = Interface for Python package management and deployment. Instructions for download, installation and setup of Conda are provided below.

Packages = A way to organize and structure your Python code into reusable components. Script can be easilly copied below to install required packages

Environments = Directories that contains a specific collection of packages that you have installed. Script can be easilly copied below to create your Conda environment.

API’s = Application Programming Interface, which is a software interface that allows two or more computer programs to communicate with each other. Here you will use the USGS NAS database API to retrieve training data and the Google Earth Engine API to talk to your Earth Engine Account.

----

# Environmental Data
 
## MODIS AQUA LST MYD11A2 (V6)

- Land Surface Temperature

## MODIS AQUA MYD13A2 (V6)

-  Normalized Vegetation Index (NDVI) = 

## MODIS TERRA MOD44B

- Percent Tree Cover

## National Land Data Assimilation System

- Precipitation

## MODIS Surface Reflectance (CONUS)

- Gross Primary Productivity

## Shuttle Radar Topography Mission (SRTM) 

- Heat Insolation Load
- Topographic Diversity

## Landsat 5, 7, and 8 

- Flashiness

----

# Machine Learning Algorithm: MaxEnt
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/b3ba2615-3e1d-4b70-86e1-1f85b2d54c28)

## MaxEnt is a well validated approach for  presence-only species distribution modeling that can deal with noisy data and has been used in many taxa including nonequilibrium organisms like invasive species (Phillips, 2004; Villero et al., 2017; Valavi et al., 2023). When applied to SDMs, information on environmental parameters at presence locations are used to create a probability distribution of ideal conditions with respect to the distribution of the parameters across the study area as defined by the background points (Phillips, 2004).

----
# Start of Instructions
----

# Step 1) Download GitHub Repository

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/107a3a6a-5075-4baa-a6bc-dffdc680d64f)

----

# Step 2) Install Anaconda (or other Python package management software)

## Download the latest version of Conda: https://www.anaconda.com/products/distribution

## Run setup file from download folder

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/b0cb5d7e-2c4d-47ee-ad03-8bd4df5d228e)

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/7c07293e-0878-46d6-a46b-bd4dab9d5ea0)

```
conda create -n NASDM python=3 
```

```
conda activate NASDM
```

```
pip install earthengine-api
```
```
conda install pandas
```
```
conda install geopandas
```
```
conda install geemap
```
```
conda install jmcmurray::json
```
```
pip install notebook
```
----
# Step 3) Create a Google Earth Engine (GEE) account w/ noncommercial cloud project: https://code.earthengine.google.com/register

---

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/1c2982bb-f6ef-4569-a0db-a95fe87016c1)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/a204a0d4-ddc8-4f94-aea7-206a183dae05)


----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/13683670-df92-4011-8101-089dc0d3b05d)


----


# Step 4) Open the notebook (start here if you already have the initial set up completed)

## Open the Jupyter notebook using Conda by runnning:
```
python -m notebook
```
## This will open a tab named Home in your browser which functions just like your Windows file folders.

## Navigate to where you unziped the repository files

## You should see the 2 notebooks you downloaded:

## Make_Covariates_github.ipynb

## Model_script_github.ipynb

----

# Step 5) Make Yearly Covariate Rasters
## Open the Make_Covariates_github notebook.  

----
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/9bf63863-f12e-472a-a3ed-8df95a6b8091)
----

## Run the first 2 cells using the play button at the top

## GEE authentication will open a new window asking you to generate a token which is like a temporary password which you will plug into the Jupyter Notebook to allow it to access your GEE repository. 

## You must Choose/Create a Cloud Project for your notebook.  

# Do not check the read-only options!!! We want to be able to write data and files to your GEE repository 

## Generate the token and then paste the info at the bottom of the final screen into the field that is now available back in your Jupyter notebook.

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/903ad78b-a034-406c-bf76-4021a82ab827)
----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/e7605af3-f680-4889-aab1-6c19a21c9499)
---
## Run the rest of the cells to start creating yearly covariate rasters. 

## It takes between 10 and 40 minutes to create a yearly parameter raster depending on pixel size (scale) and the size of the state. Fortunately, Earth Engine uploads multiple assets at the same time.

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/ba5c98cf-a339-4c93-8586-18ad027a998d)


----

# Step 6) Run the model

## Open the Model_script_github notebook

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/149286da-0106-41ce-8683-7fa14d44bdf3)

----

# Run all cells to produce a heatmap, histogram of testing results and to plot parameter importance.

----
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/809f97f8-afe5-435a-8004-fc7f1f4ba8dd)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/6586eca5-8bae-41bf-b668-41270f40e569)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/512106a7-89bc-4ba4-a5b6-57e827fdabd2)


----
# Export your files and build Earth Engine Web App to explore and share your heatmaps with others

Once you have exported your heatmap and nas data points assets click this link 

## https://code.earthengine.google.com/5e256daa090142adcb8a62d3d8c41b6f

Instructions for setup are provided within the linked script (Under-Construction)

----
# Customization 
----
It is recommended that you build a functioning model for a single taxa and single state before attempting to customize.

Through out the code you will notice lines which have been "commented out" by adding # in front. This means that the line is read as text. 

By removing the # from each line, you can run the block/cell.

These contain example script and instructions for adding your own environmental data (both static and timeseries) and occurence data 

as well as for customizing the timeframe, extent modeled and resolution of inputs and model outputs.

The following will direct you to where the specific customization examples can be found.

It is recommended that you store any of your own files within the same folder as your scripts which will allow you to just use the filename as the path when importing your data.

# Spatial Extent

Instructions to reduce the modeled extent can be found in the Model_script_github Jupyter Notebook

# Extrapolate Trained Model

Instructions to train the model with data from states with presences to states without presences can be found in the Model_script_github Jupyter Notebook

# Resolution

Changing the scale parameters in both Jupyter notebooks will change resolution for environmental data aggregation and for the pixel size for outputs

# Timeframe

Instructions for customizing the timeframe of your model can be found in in the Model_script_github Jupyter Notebook

# Add Environmental Parameters

See commented out cells in Make_Covariates_github

Follow the example for adding NDSI for adding time series data from GEE to the modeling parameters. Note: Datasets like Modis and Landsat require quality filtering as shown in the example script.  The configuration may differ between datasets, but you can swap out bit and quality flag info as needed.

There is also a commented out example for how to add a static parameter to your environmental rasters.

# Add your own occurence or background data

See commented out cells in Model_script_github

Follow the example to upload occurence data or background data from CSVs.

# Change the model algorithm

Earth Engine has many built in functions for machine learning.  MaxEnt was chosen because of the presence-only nature of the data available. 

If you have absence data, the algorithm can be changed to something like Random Forest see: https://developers.google.com/earth-engine/apidocs/ee-classifier-smilerandomforest#colab-python 







