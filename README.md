# NASDM
Non-Indigenous Aquatic Species Distribution Modeling Toolset
----
The Following provides detailed instructions to produce yearly environmental images, pull occurence data from the USGS NAS database and to produce a visualization of risk for spread with performance metrics. 
These instructions include screenshots to help walk you through setup and running of this workflow. Instructions for customization are also integrated throughout the various scripts used for this workflow. The locations for the blocks of code for specific customization are provided at the end of this document.

---

# Download GitHub Repository

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/1e320f02-4ef5-43c4-b513-fc57252bc618)

----

# Install Anaconda (or other Python package management software)

## Download the latest version of Conda: https://www.anaconda.com/products/distribution

## Run setup file from download folder

----
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/7c07293e-0878-46d6-a46b-bd4dab9d5ea0)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/b0cb5d7e-2c4d-47ee-ad03-8bd4df5d228e)

----
# Setup Environment & Install Packages

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
# Create a Google Earth Engine (GEE) account w/ noncommercial cloud project: https://code.earthengine.google.com/register

---

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/1c2982bb-f6ef-4569-a0db-a95fe87016c1)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/504e8717-a27f-488a-b85c-5c6d0922c429)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/13683670-df92-4011-8101-089dc0d3b05d)


----


# Open the notebook (start here if you already have the initial set up completed)

Open the Jupyter notebook using Conda by runnning:
```
python -m notebook
```
This will open a tab named Home in your browser which functions just like your Windows file folders.

Navigate to where you unziped the repository files

You should see the 2 notebooks you downloaded:

Make_Covariates_github.ipynb

Model_script_github.ipynb

----

# Make Yearly Covariate Rasters
Open the Make_Covariates_github notebook.  

Run the first 2 cells using the play button at the top

GEE authentication will open a new window asking you to generate a token.  

You must Choose/Create a Cloud Project for your notebook.  

#### Do not check the read-only options!!! We want to be able to write assets 

Generate the token and then paste the info at the bottom of the final screen into the field that is now available back in your Jupyter notebook.

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/903ad78b-a034-406c-bf76-4021a82ab827)
----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/e7605af3-f680-4889-aab1-6c19a21c9499)
---
Run the rest of the cells to start creating yearly covariate rasters. 

It takes between 10 and 40 minutes to create a yearly parameter raster depending on pixel size (scale) and the size of the state.
Fortunately, Earth Engine uploads multiple assets at the same time.

Progress can be examined on the task tab on your GEE Developers Dashboard

----

# Run the model

Open the Model_script_github notebook

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/ed525c72-ec18-4dbc-9fb6-0a3d7ef5ca86)
----

Run all cells to produce a heatmap and histogram of false negatives.

----

# Customization 
It is recommended that you build a functioning model for a single taxa and single state before attempting to customize.

Through out the code you will notice lines which have been "commented out" by adding # in front. This means that the line is read as text. 

By removing the # from each line, you can run the block/cell.

These contain example script and instructions for adding your own environmental data (both static and timeseries) and occurence data 

as well as for customizing the timeframe, extent modeled and resolution of inputs and model outputs.

The following will direct you to where the specific customization examples can be found.

It is recommended that you store any of your own files within the same folder as your scripts which will allow you to just use the filename as the path when importing your data.

# Spatial Extent

Instructions to reduce the modeled extent or to increase it to multiple states can be found in the Model_script_github Jupyter Notebook

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







