# Recent updates to the versions described below include:
- Repository includes a setup file which creates your Conda environment and installs required packages.
- Data is directly sourced from USGS NAS API at time of running the model.  This allows the most current data to be used and any taxa can be modeled by changing the species ID value.
- The python model script now produces an interactive map, predictor variable importance and performance plots. 
- Earth Engine is only used to produce your initial RSD predictor variables.

# Upcoming improvements to the versions described below include:
 - Scripts to produce water quality features (e.g., Ca, pH & DO)
 - Scripts to produce native and invasive community composition related predictors
 - Background data will be automatically created when creating invasive community composition related predictors
 - Scripts to produce Boater movement and distance to source via road and river network for additional states
 - Functionality to cache and compare heatmaps and model analytics between models run with different parameter settings.
 - Multi-taxa modeling options.
 - Functionality to simulate and quantify the impact of management actions (or inaction) and the effect on predicted risk (including watercraft inspection station placement and monitoring).
----

# There is now a Shiny App version which can be downloaded via this link:

https://drive.google.com/file/d/1e9WupEBT_dPEzuudrdVNDB1FcDurpdc8/view?usp=sharing

To install and run the shiny app version locally, download the zipfile from this link. Make sure you have Anaconda installed and then follow the steps in the instructions_readme.txt file.

# To access the point-and-click demo open this link in a new browser tab:

https://nasdm-shiny.shinyapps.io/nasdm_shiny_app/

Please note that this takes quite a while to produce the heatmap and analytical plots in the model analytics tab.  These are among the bugs to be addressed as we polish this decision support tool.
The Shiny apps run on the same back-end script and will be updated similarly to the Jupyter Notebook version as new features are added.

Upcoming revisions unique to these shiny apps include:

 - Moving model variable selection boxes to a new panel on the right to allow visability above the fold of the page.
 - Available states will be expanded to include ID, IA, IL, MT, MO, OR and WA. 
 - The current map function will be swapped out with an interactive mapping function to allow additional interaction with the output.
 - An additional navigation tab will be added with functionality to compare between model runs.

----

# Non-Indigenous Aquatic Species Data/Modeling Toolset (NASDM)
----
## The following provides background and detailed instructions to produce environmental images, pull occurrence data from the USGS NAS database and relevant environmental data (e.g. remote sensing, see next section), to produce risk-maps for invasive species spread. This toolset also produces performance metrics to allowing managers to asses uncertainty in hotspot rankings (e.g., false AIS detection rates). The instructions below include screenshots to help walk you through the setup and running of this workflow (to model and map AIS-invasion hotspots). Instructions for customization (for your species or geographic area of interest) are also integrated throughout the various scripts used for this workflow. The locations for the blocks of code for specific customization are provided at the end of this document. The following tools and workflow can be applied to other species of interest including threatened native species to understand and predict habitat suitability and species distribution modeling (SDMs) (e.g, Carter et al. 2021 & van Reese et al. 2022?)

## *Development Sponsored by NASA
![thumbnail_image002](https://github.com/InvasiveH8ter/NASDM/assets/109878461/a98768bc-9eec-4414-84fc-229ca4e9e4b2)
----

# WHY USE REMOTE SENSING DATA TO Model AIS SPREAD?

Remote-sensing data products are extremely valuable in predicting AIS spread because they represent relevant environmental data, such as stream and lake surface temperature, flow, flooding, riparian vegetation, and disturbance, for the construction of predictive models and maps needed to identify locations of likely AIS spread (Table 1). 

# Remote-sensing products in our web tool
We chose environmental predictors based on a priori knowledge of their biological relevance across many invasive aquatic taxa. Surface temperature is highly correlated with stream and water body temperatures, which influence the energetics and habitats of aquatic species (Gardner et al. 2003; Caissie 2006; Oyler et al. 2015). Land surface temperature (LST) observed from satellite thermal infrared remote-sensing represents integrated surface “skin” temperatures, vegetation canopy, water, snow (when present), and soil elements within the satellite footprint. Relatively long-term and well-calibrated LST records from Terra and Aqua MODIS, and Landsat have been effective in representing water temperature patterns influencing AIS spread (Carter et al. 2021; Tavares et al. 2019). We generally use best quality (QC) 1-km resolution, 8-day composite LST records from MODIS as a proxy for temperature conditions influencing aquatic habitat quality, presence of AIS, and species vulnerability to AIS (Kanno et al. 2015; Wade et al. 2016); similar LST records are produced from SNP/JPS1 VIIRS, which can be calibrated to provide LST continuity beyond the EOS MODIS era (Hulley et al. 2017). We also use finer scale (100m) LST retrievals available in Landsat 8 TIRS records to evaluate local temperature spatial heterogeneity in relation to surface water cover, vegetation, and terrain conditions, beneath the effective grain of MODIS LST.  
 
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/30a2a8d5-561a-4c82-ba7d-284a870429fa)
Surface water cover dynamics records are available from long-term Landsat data and can capture local (30m) water body distributions, inundation persistence or flashiness (flooding), and longer-term wetting/drying trends (Pekel et al. 2016; Jones 2019; Lehner et al. 2022). Fast water and flooding of spawning nests can prevent non-native fish invasion (rainbow & brook trout, and bass). We have used these data as indicators of surface water connectivity and persistence to model aquatic habitats and AIS spread (Whited et al. 2012; Carter et al. 2021), which can distinguish lakes and their connectivity to adjacent river networks and riparian wetlands down to the level of a 4th order stream channel network (Luck et al. 2010; Whited et al. 2013). Water occurrence and persistence metrics from the historical Landsat record (1984-present) also capture transient inundation from seasonal flooding, which can influence connectivity within and between catchments and affect aquatic habitats and AIS spread. Potential enhancements to the ML framework include analyzing LST over large lakes identified from Landsat and other ancillary data (Lehner et al. 2022) to estimate LST patterns and trends affecting water quality and habitat conditions suitable for colonization by AIS like mussels, milfoil, brook trout, etc. (Loppnow et al. 2013).

Vegetation cover and ecosystem productivity derived from RSD can provide effective proxies for riparian habitats and terrestrial carbon and nutrient inputs affecting aquatic food webs (Finstad et al. 2016). Our ML framework uses MODIS 250m estimates of fractional tree cover (Hansen et al. 2003) and canopy greenness (Didan 2015), which we found to be significant predictors of AIS presence (Carter et al. 2021). Alternative, finer scale (30m) estimates of greenness and productivity are available from Landsat (Robinson 2018) and evaluated here for model improvement. Forest biomass maps derived from satellite LIDAR and radar are becoming available (Silva et al. 2021) to enhance our information on standing biomass cover potentially affecting aquatic habitats.

----

# Machine Learning Algorithm: MaxEnt
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/b3ba2615-3e1d-4b70-86e1-1f85b2d54c28)

MaxEnt is a well validated approach for  presence-only species distribution modeling that can deal with noisy data and has been used in many taxa including nonequilibrium organisms like invasive species (Phillips, 2004; Villero et al., 2017; Valavi et al., 2023). When applied to SDMs, information on environmental parameters at presence locations are used to create a probability distribution of ideal conditions with respect to the distribution of the parameters across the study area as defined by the background points (Phillips, 2004).

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

# Start of Instructions
----

# Step 1) Download GitHub Repository
# Remember where you put this because you need the folder path later!!!
----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/107a3a6a-5075-4baa-a6bc-dffdc680d64f)

----

# Step 2) Install Anaconda (or other Python package management software)

## Download and install the latest version of Conda: https://www.anaconda.com/products/distribution

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/b0cb5d7e-2c4d-47ee-ad03-8bd4df5d228e)

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/7c07293e-0878-46d6-a46b-bd4dab9d5ea0)

```
cd C:/Users/your_folderpath
```

```
python nasdm_setup.py
```

## If you encounter an error during package installation try a different installation package. For example if conda install fails, try pip install of conda forge.  When all else fails, copy the text from the error message and paste it into your browser search bar.  I gaurantee you are not the first person to get this error.

----
# Step 3) Create a Google Earth Engine (GEE) account w/ noncommercial cloud project: https://code.earthengine.google.com/register

---

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/1c2982bb-f6ef-4569-a0db-a95fe87016c1)

----

![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/a204a0d4-ddc8-4f94-aea7-206a183dae05)


----


## Create your environmental data by running this script:
https://code.earthengine.google.com/935e3840bd5a63f1e40097b1f0c6ad45

## Note this GEE code exports the RSD raster as a geotiff to your google drive repository.  You then need to download it and save it in the same folder as the rest of your files

# Step 4) Open the notebook (start here if you already have the initial set up completed)

## Open the Jupyter notebook using Conda by runnning:
```
python -m notebook
```
## This will open a tab named Home in your browser which functions just like your Windows file folders.

## Navigate to where you unziped the repository files (you are probably already there if you changed to your file directory in Conda)

## Open the model-GitHub.ipynb notebook

## Use the run button in the header to run blocks of code in Juptyer Notebook

## You will need to define these values in the second block of code
my_state = 'MN'
my_nas_id = 5
MY_scale = 1000

 
----



## Run the rest of the cells to start modelling. 


# Run all cells to produce a heatmap, histogram of testing results and to plot parameter importance.

----
![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/809f97f8-afe5-435a-8004-fc7f1f4ba8dd)

----


![image](https://github.com/InvasiveH8ter/NASDM/assets/109878461/512106a7-89bc-4ba4-a5b6-57e827fdabd2)


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







