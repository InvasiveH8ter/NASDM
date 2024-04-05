# NASDM
Non-Indigenous Aquatic Species Distribution Modeling Toolset
----
The Following provides detailed instructions to produce yearly environmental images, pull occurence data from the USGS NAS database and to produce a visualization of risk for spread with performance metrics. 

---
## Setup (for Windows OS)

First, create a Google Earth Engine (GEE) account w/ noncommercial cloud project: https://code.earthengine.google.com/register

---

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/1c2982bb-f6ef-4569-a0db-a95fe87016c1)
----
## Finalize GEE Account Registration

You will receive an email with a link to the Earth Engine Code Editor.

Follow this link to your Earth Engine account.

Click on the Assets tab and then click on the NEW dropdown. 

You will be asked to create your username here, which can simply be left as is.

After this, you should now have a GEE Cloud Project that you can add folders and upload data to.

----

## Install Anaconda (or other Python package management software)

Download the latest version of Conda: https://www.anaconda.com/products/distribution

Run setup file from download folder

----

## Setup Conda

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/6b32d5b1-996f-4dae-8d26-3f2b6148e4ca)
----

Create a Conda environment by copying the code below and pasting into your powershell prompt as shown here.  

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/12ca51d3-0020-4d1a-9038-d54681cd69d5)
----

Here we will be creating an environment called NASDM that runs python 3.  You can change the name to whatever you want, but the example here works as is.
```
conda create -n NASDM python=3 
```
Note:The script will pause and ask you if you wish to proceed.  Type y and hit enter.

Next, activate your new environment
```
conda activate NASDM
```
----

#### Install Packages

The script will pause and ask you if you wish to proceed.  Type y and hit enter. You only have to install packages into your environment once.
In the future, you can simpley activate your environment and open your Jupyter notebook as described below.

```
conda install earthengine-api
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
* Finally, download the zipped GitHu and store the files from this GitHub on your local drive.
---
## Workflow
----

First, you need a set of environmental data. 

The following sections will walk you through making your yearly environmental rasters.
For this section, it is assumed that your Conda environment is properly set up.

----

#### Open the notebook (start here if you already have the initial set up completed)

Open the Jupyter notebook using Conda by runnning:
```
python -m notebook
```
This will open a tab named Home in your browser which functions just like your Windows file folders.

You should see the 2 notebooks you downloaded:

Make_Covariates_github.ipynb

Model_script_github.ipynb
----

#### Make Yearly Covariate Rasters
Open the Make_Covariates_github notebook.  

Run the first 2 cells using the play button at the top

GEE authentication will open a new window asking you to generate a token.  

You must Choose/Create a Cloud Project for your notebook.  

#### Do not check the read-only options!!! We want to be able to write assets 

Generate the token and then paste the info at the bottom of the final screen into the field that is now available back in your Jupyter notebook.

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/903ad78b-a034-406c-bf76-4021a82ab827)
----

## Configure the temporal and spatial settings for your taxa.


You can create covariate images from 2003 to 2023. Every year, you will be able to add an additional covariate raster image to update your model.

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/e7605af3-f680-4889-aab1-6c19a21c9499)
---
Run the rest of the cells to start creating yearly covariate rasters. 

It takes between 10 and 40 minutes to create a yearly parameter raster depending on pixel size (scale) and the size of the state.
Fortunately, Earth Engine uploads multiple assets at the same time.

Progress can be examined on the task tab on your GEE Developers Dashboard

----

## Troubleshooting
If you receive an error during authenication, you may need to enable the Earth Engine API or add additional permissions to allow the writing of assets.

In the top right of the GEE developers screen the name of your cloud project shown.  If you click on it a dropdown appears as shown above.  

Click on Project Info and then on the Manage Cloud Project link. 
----

## Upload Background files to Earth Engine

Upload the background shapefile by clicking on NEW and selecting shapefile from the drop down.

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/2f09985d-aece-4b91-86e9-16a399339bfb)
----

#### Run the model

Open the Model_script_github notebook

Configure paths for your covariate rasters and background GEE assets.

Obtain species ID via the link in the notebook. This will open a window where you can click control f to search for your target NAS.

Configure MY_state_abbrev and MY_state

Run all cells to produce a heatmap and histogram of false negatives.

----

### Customization 
It is recommended that you build a functioning model for a single taxa and single state before attempting to customize.

Through out the code you will notice lines which have been "commented out" by adding # in front. This means that the line is read as text. 

By removing the # from each line, you can run the block/cell.

These contain example script and instructions for adding your own environmental data (both static and timeseries) and occurence data 

as well as for customizing the timeframe, extent modeled and resolution of inputs and model outputs.

The following will direct you to where the specific customization examples can be found.

It is recommended that you store any of your own files within the same folder as your scripts which will allow you to just use the filename as the path when importing your data.

#### Spatial Extent

Instructions to reduce the modeled extent or to increase it to multiple states can be found in the Model_script_github Jupyter Notebook

#### Resolution

Changing the scale parameters in both Jupyter notebooks will change resolution for environmental data aggregation and for the pixel size for outputs

#### Timeframe

Instructions for customizing the timeframe of your model can be found in in the Model_script_github Jupyter Notebook

#### Add Environmental Parameters

See commented out cells in Make_Covariates_github

Follow the example for adding NDSI for adding time series data from GEE to the modeling parameters. Note: Datasets like Modis and Landsat require quality filtering as shown in the example script.  The configuration may differ between datasets, but you can swap out bit and quality flag info as needed.

There is also a commented out example for how to add a static parameter to your environmental rasters.

#### Add your own occurence or background data

See commented out cells in Model_script_github

Follow the example to upload occurence data or background data from CSVs.







