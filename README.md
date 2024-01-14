# NASDM
Non-Indigenous Aquatic Species Distribution Modeling Toolset

---

## Dependencies
You will need to install Anaconda (Conda) and to create a Google Earth Engine Developers account to use this pipeline.

* Download and Install anaconda commandline terminal: https://www.anaconda.com/products/distribution
* Next download and store the scripts and background shapefile from this GitHub on your local drive.


* Create a Google Earth Engine (GEE) account:
* visit https://code.earthengine.google.com/register

Below the main registration link is the text, "Noncommercial users can also use Earth Engine without creating Cloud projects. Click here for the signup form."

Click this link and fill in the required fields making sure to select research or academia wherever asked.

You will receive an email with a link to the Earth Engine Code Editor.

Follow this link to your Earth Engine account.
Click on the Assets tab and then click on the NEW dropdown. 
You will be asked to create your username here, which can simply be left as is.
After this, you should now have a Legacy Asset that you can add folders and upload data to.

---

#### Setup Conda

Open the Anaconda PowerShell Terminal from your start menu.

First, create a Conda environment by copying the code below and pasting into your powershell prompt. Here we will be creating an environment called NASDM that runs python 3.  You can change the name to whatever you want, but the example here works as is. 

Note: Right clicking will automatically paste the code you copy into the conda prompt.

Also, clicking the up arrow will toggle back through your previous commands that you have run.

```
conda create -n NASDM python=3 
```
Note:The script will pause and ask you if you wish to proceed.  Type y and hit enter.

Next, activate your new environment
```
conda activate NASDM
```
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
---

## Workflow

The goals of this workflow are to produce yearly environmental raster images, pull occurence data from the USGS NAS database and to produce a visualization of risk for spread with performance metrics. 

First, you need a set of environmental data. 

The following sections will walk you through making your yearly environmental rasters.
For this section, it is assumed that your Conda environment is properly set up.

#### Set up GEE folders
Go to https://developers.google.com/earth-engine
Create folder in your assets tab to store your yearly covariate images.  
Upload the background shapefile by clicking on NEW and selecting shapefile from the drop down.  

#### Open the notebook

You can start here if you already have the initial set up completed above.

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
Open the Make_Covariates_github notebook.  

Run the first 2 cells using the play button at the top 
GEE authentication will open a new window asking you to generate a token.  You must Choose/Create a Cloud Project for your notebook.  Here you need to click the link and accept the terms and conditions.
Then click the button to create a new cloud project.
This will take you back to the initial generate token screen where you should see your new cloud project name in the cloud project field.  Generate the token and then paste the info at the bottom of the final screen into the field that is now available back in your Jupyter notebook.

You should only need to complete this process once and then you shouldn't need to authenticate again.

#### Configure the temporal and spatial settings for your taxa.

You can create covariate images from 2003 to 2023. Every year, you will be able to add an additional covariate raster image to update your model.

state_abbrev = 'XX' # 2-digit postal abbreviation

start_year = YYYY

end_year = YYYY

description = 'covariate'  this is the name displayed on the task tab in GEE developer dashboard

assetId = 'users/ee-Your-GEE-Cloud-ID/covariates_' # GEE path and name for where to store your yearly covariate rasters.

Run the rest of the cells to start creating yearly covariate rasters. These can take up to an hour depending on the size of the state. Progress can be examined on the task tab on your GEE Developers Dashboard

#### Run the model

Open the Model_script_github notebook

Configure paths for your covariate rasters and background GEE assets.

Obtain species ID via the link in the notebook. This will open a window where you can click control f to search for your target NAS.

Run all cells to produce a heatmap and histogram of false negatives.
----



### Customization 
You will notice there are lines of code which have been "commented out" by adding # in front. This means that the line is read as text. 

These contain example script and instructions for adding your own environmental data (both static and timeseries) and occurence data.

By removing the # from each line, you can run the block/cell.

The following will direct you to where the specific customization examples are located

#### Add Environmental Parameters

See commented out cells in Make_Covariates_github

Follow the example for adding NDSI for adding time series data from GEE to the modeling parameters. Note: Datasets like Modis and Landsat require quality filtering as shown in the example script.  The configuration may differ between datasets, but you can swap out bit and quality flag info as needed.

There is also a commented out example for how to add a static parameter to your environmental rasters.

#### Add your own occurence or background data

See commented out cells in Model_script_github

Follow the example to upload occurence data or background data from CSVs.







