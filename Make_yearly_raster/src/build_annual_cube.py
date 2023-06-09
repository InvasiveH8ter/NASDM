import ee
import src.gee_funs as gf

def build_all_cubes(start_year, end_year):

    #Build Big Raster Image
    ## Import assets
    # MODIS Mission
    modusGlobal = ee.ImageCollection("MODIS/006/MYD11A2")

    # Primary Productivity
    GPP = ee.ImageCollection("UMT/NTSG/v2/LANDSAT/GPP")

    # Surface water
    pikelSurfaceWater = ee.Image("JRC/GSW1_1/GlobalSurfaceWater")

    # Elevation
    DEM = ee.Image("USGS/NED")

    # Enhanced Vegetation Index and NDVI
    modusVeg = ee.ImageCollection("MODIS/006/MYD13A2")

    # Heat Isolation Load
    CHILI = ee.Image("CSP/ERGo/1_0/Global/SRTM_CHILI")

    # Topographic Diversity
    topoDiversity = ee.Image("CSP/ERGo/1_0/Global/ALOS_topoDiversity")

    # Vegetation Continuous Field product - percent tree cover, etc
    VCF = ee.ImageCollection("MODIS/006/MOD44B")

    # Human Modification index
    gHM = ee.ImageCollection("CSP/HM/GlobalHumanModification")

    # Climate information
    NLDAS = ee.ImageCollection("NASA/NLDAS/FORA0125_H002")

    # Shape file containing Country Boundaries
    # countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")

    # Shape file containing HUC polygons
    # HUC = ee.FeatureCollection("USGS/WBD/2017/HUC12")

    # Dynamic Surface Water metric
    pekel_monthly_water = ee.ImageCollection("JRC/GSW1_2/MonthlyHistory")

    # Static surface water metric
    pekel_static_water = ee.ImageCollection('JRC/GSW1_2/MonthlyRecurrence')

    # pH
    pH = ee.Image("OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M/v02")

    # Soil Taxonomy
    soiltax = ee.Image("OpenLandMap/SOL/SOL_GRTGROUP_USDA-SOILTAX_C/v01")

    # lithology
    lithology = ee.Image("CSP/ERGo/1_0/US/lithology")


    ## Select features, etc
    #========================================================
    #Rename Bands and select bands, etc
    #========================================================
    
    pH_asset = pH.select("b0")
    soil_asset = soiltax.select("grtgroup")
    lithology_asset = lithology.select("b1")	

    NLDAS_precip = NLDAS.select("total_precipitation")
    NLDAS_temp = NLDAS.select("temperature")
    NLDAS_humid = NLDAS.select("specific_humidity")
    # NLDAS_potEvap = NLDAS.select("potential_evaporation")


    CHILI = CHILI.rename(['Heat_Insolation_Load'])
    srtmChili = CHILI.select('Heat_Insolation_Load')
    topoDiversity = topoDiversity.rename(["Topographic_Diversity"])
    topoDiv = topoDiversity.select("Topographic_Diversity")
    footprint = ee.Image(gHM.first().select("gHM"))

    # Surface water occurrence
    sw_occurrence = pekel_static_water\
                        .select('monthly_recurrence')\
                        .mean()\
                        .rename(['SurfaceWaterOccurrence'])\
                        .unmask()

    ## Mask features by quality control bands
    GPP_QC = GPP.map(gf.gpp_qc)


    LST = modusGlobal.map(gf.lst_qc) \
                    .select("LST_Day_1km")

    modusVeg_QC = modusVeg.map(gf.modusQC)
    EVI = modusVeg_QC.select("EVI")
    NDVI = modusVeg_QC.select("NDVI")

    VCF_qc = VCF.map(gf.VCFqc)

    ee_dates = ee.List(list(map( \
        lambda x: ee.Date(str(x) + '-01-01'), \
        range(start_year,end_year) )))

    ## Annual Cube function
    #========================================================
    # "Builder Function" -- processes each annual variable into a list of images
    #========================================================

    def build_annual_cube(d):
        # Set start and end dates for filtering time dependent predictors (SR, NDVI, Phenology)
        # Advance startDate by 1 to begin with to account for water year (below)
        startDate = (ee.Date(d).advance(1.0,'year').millis()) 
        endDate = ee.Date(d).advance(2.0,'year').millis()

        #========================================================
        #Define function to compute seasonal information for a given variable
        #========================================================
        def add_seasonal_info(imgCol,name):

            # Set up Seasonal dates for precip, seasonal predictors
            spring_start = ee.Date(startDate).advance(3,'month')
            summer_start = ee.Date(startDate).advance(6,'month')
            fall_start = ee.Date(startDate).advance(9,'month')
            
            # pixelwise sum of imageCollection for each season, resulting in a
            # image with total value at each pixel, e.g. total precip over the 
            # season at each pixel
            winter_tot = imgCol.filterDate(startDate,spring_start).sum()
            spring_tot = imgCol.filterDate(spring_start,summer_start).sum()
            summer_tot = imgCol.filterDate(summer_start,fall_start).sum()
            fall_tot = imgCol.filterDate(fall_start,endDate).sum()

            names = ['winter_total'+name,'spring_total'+name,'summer_total'+name,
                          'fall_total'+name]

            return winter_tot.addBands([spring_tot,summer_tot,fall_tot]) \
                            .rename(names)

        # Aggregate seasonal info for each variable of interest (potEvap neglected purposefully)
        seasonal_precip = add_seasonal_info(NLDAS_precip,"Precip")
        seasonal_temp = add_seasonal_info(NLDAS_temp,"Temp")
        seasonal_humid = add_seasonal_info(NLDAS_humid,"Humidity")
	   
										

	  # waterYear_start = ee.Date(startDate).advance(10,'month')
        # waterYear_end = waterYear_start.advance(1,'year')




        #========================================================
        # Aggregate Other Covariates
        #========================================================

        # Vegetative Continuous Fields
        meanVCF = VCF_qc.filterDate(startDate, endDate)\
                    .mean() \
			  
          
        

        # Filter Precip by water year to get total precip annually

        waterYearTot = NLDAS_precip.filterDate(startDate, endDate) \
                                    .sum()

        # Find mean EVI per year:
        meanEVI = EVI.filterDate(startDate,endDate) \
                      .mean() \
                      .rename(['Mean_EVI'])

        #Find mean NDVI per year:
        meanNDVI = NDVI.filterDate(startDate,endDate) \
                        .mean() \
                        .rename(['Mean_NDVI'])

        # Find flashiness per year by taking a Per-pixel Standard Deviation:
        flashiness_yearly = ee.Image(pekel_monthly_water.filterDate(startDate,endDate) \
                                                          .reduce(ee.Reducer.sampleStdDev()) \
                                                          .select(["water_stdDev"])) \
                                                          .rename("Flashiness")

	  
		
        # Find max LST per year:
        maxLST = LST.max().rename(['Max_LST_Annual'])

	  # Find min LST per year:
        minLST = LST.min().rename(['Min_LST_Annual'])
	  
  	  # Find mean LST per year:
        meanLST = LST.mean().rename(['Mean_LST_Annual'])

        # Find mean GPP per year:
        meanGPP = GPP_QC.filterDate(startDate,endDate) \
                          .mean() \
                          .rename(['Mean_GPP','QC'])

	  # Find min GPP per year:
        minGPP = GPP_QC.filterDate(startDate,endDate) \
                          .mean() \
                          .rename(['Min_GPP','QC'])

        # Construct huge banded image
        banded_image = sw_occurrence \
            .addBands(DEM.select("elevation")) \
		.addBands(srtmChili) \
            .addBands(pH_asset) \
		.addBands(soil_asset) \
		.addBands(lithology_asset) \
            .addBands(topoDiv) \
            .addBands(footprint) \
            .addBands(srcImg = maxLST, names = ["Max_LST_Annual"]) \
            .addBands(srcImg = minLST, names = ["Min_LST_Annual"]) \
		.addBands(srcImg = meanLST, names = ["Mean_LST_Annual"]) \
		.addBands(srcImg = meanGPP, names = ["Mean_GPP"]) \
		.addBands(srcImg = minGPP, names = ["Min_GPP"]) \
            .addBands(srcImg = meanNDVI, names = ["Mean_NDVI"]) \
            .addBands(srcImg = meanEVI, names = ["Mean_EVI"]) \
            .addBands(meanVCF.select("Percent_Tree_Cover")) \
            .addBands(seasonal_precip) \
		.addBands(seasonal_temp) \
		.addBands(seasonal_humid) \
            .addBands(flashiness_yearly) \
		.addBands(waterYearTot) \
            .set("system:time_start",startDate)

        return banded_image.unmask()

    return ee.List(ee_dates.map(build_annual_cube))


