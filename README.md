# PROMICE-2022 Ice Mask

This repository is a forum for data issues related to the [PROMICE-2022 Ice Mask](https://dataverse.geus.dk/dataverse/promice-ice-mask). The PROMICE-2022 Ice Mask is an updated outline of the Greenland Ice Sheet, as part of [PROMICE](https://promice.org) (Programme for Monitoring of the Greenland Ice Sheet) at the [Geological Survey of Denmark and Greenland](https://geus.dk) (GEUS).

## See an issue with the dataset?
We invite users to use this repository to raise issues regarding the ice mask dataset, and contribute with their own delineation efforts where needed.

### How to raise an issue
Issues can be raised in this repository [here](https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/issues). A complete report is essential for issues to be identified, reproducible, and resolved easily. Therefore, issues must include:

- A concise description of the data issue
- The source and version number of the dataset
- The location of the data issue (where applicable)

Once posted, someone from the PROMICE team will respond to the issue with a clear plan of action. It may be the case that further information is needed, in which case, please respond in a timely manner.

See [here](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) for a thorough guide on creating issues in a Github repository.

#### Issue labels
Make use of the issue labels to ensure that data issues are categorised accordingly:

**Issue Type**

https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/invalid-metadata
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/invalid-vertices
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/new-vertices-needed

**Region**

https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/SW
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/SE
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/CE
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/NE
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/NW
https://github.com/GEUS-Glaciology-and-Climate/PROMICE-ice-mask/labels/CW

### How to contribute
If you would like to contribute then you are welcome to propose changes by uploading discrete alterations to the datasets. You will need to be registered as a Github user in order to do so:

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this Github repository
2. [Create a branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) in your forked repository
3. Upload (also referred to as ["push"](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)) your proposed alterations to the branch under the "submitted_changes" directory
4. Open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and include the following information in the PR description:
   - The aim of your changes
   - Details of what these changes are
   - Any limitations or further development needed

A member of the PROMICE team will review your submission once a pull request is open. If/when your pull request is accepted then your changes will be merged and you will be listed as a contributor to the dataset.

## Dataset readme
### Dataset contents
The PROMICE-2022 ice mask is an updated outline of the contiguous ice masses of the Greenland Ice Sheet. The dataset is derived from a mosaic of Sentinel-2 satellite images at 10 m resolution, compiled using the SentinelHub Cloud Processing API. The mosaic was generated using the most recent valid pixels from August 2022, ensuring high temporal and geometric accuracy. Manual editing and mapping was conducted at a scale of around 1:25,000, after which quality assessment was performed independently of the mapping operator, before finally being merged into one coherent dataset. The manual mapping process is further supported by data from the Danish Agency for Climate Data (KDS), including mosaics of Sentinel-2 and SPOT 6/7 imagery, as well as recent vector data from topographical mapping. Please see Luetzenburg et al. (In Prep) for full details on the processing workflow and quality assessment. The following files are included in this dataset:

- ***01-PROMICE-2022-IceMask-line.gpkg***: Outline of the Greenland Ice Sheet from August 2022, provided as line vector feature
- ***02-PROMICE-2022-IceMask-polygon.gpkg***: Outline of the Greenland Ice Sheet from August 2022, provided as polygon vector feature
- ***03-PROMICE-2022-Nunatak-line.gpkg***: Outlines of the nunataks within the Greenland Ice Sheet from August 2022, provided as line vector features
- ***04-PROMICE-2022-Nunatak-polygon.gpkg***: Outlines of the nunataks within the Greenland Ice sheet from August 2022, provided as polygon vector features
- ***05-PROMICE-2022-IceMask-Nunatak-line.gpkg***: Outlines of the Greenland Ice Sheet and the nunataks within from August 2022, provided as line vector features
- ***06-PROMICE-2022-IceMask-Nunatak-polygon.gpkg***: Outline of the Greenland Ice Sheet from August 2022 with the nunataks in its interior cut out, provided as a polygon vector feature
- ***07-PROMICE-2022-IceMask-CL1-polygon.gpkg***: Outline of the Greenland Ice Sheet from August 2022 with the nunataks in its interior cut out, and glaciers with connectivity level CL1 delineated following Rastner et al. 2012, provided as a polygon vector feature
- ***08-PROMICE-2022-IceMask-basins-polygon.gpkg***: Ice mask of the Greenland Ice Sheet from August 2022, divided into drainage basins following Mouginot and Rignot 2019, provided as a polygon vector feature
- ***09-PROMICE-2022-IceMask-Nunatak-basins-polygon.gpkg***: Ice mask of the Greenland Ice Sheet from August 2022 with the nunataks in its interior cut out, divided into drainage basins following Mouginot and Rignot 2019, provided as a polygon vector feature
- ***10-PROMICE-2022-IceMask-raster-150m.gpkg*** Ice Mask of the Greenland Ice Sheet from August 2022, provided as raster file with a cell size of 150x150m
- ***11-PROMICE-2022-DOY-polygon.gpkg***: Polygon vector feature of the Sentinel-2 mosaic extent, annotated with the DOY (day of year) in 2022 on which the corresponding Sentinel-2 imagery was acquired and used for the delianetion of the PROMICE-2022 ice mask
- - ***README-PROMICE-2022-IceMask.md***: This dataset readme file

### Data format
The ice mask is presented as a vector feature in GeoPackage format (.gpkg), with coordinates provided in the WGS NSIDC Sea Ice Polar Stereographic North (EPSG:3413) projected coordinate system.

### Metadata
The following metadata information is included in the corresponding files:

| Variable name       | Description         | Format | 
|---------------------|---------------------|---------|
| `id`  	| Identifying number for each feature    | Integer  |
| `type`  	| Ice sheet outline or nunatak (outline, nunatak)    | String  |
| `area_sqkm`  	| Areal extent of polygon in square km| Float  |
| `length_km`  	| Length of line or polygon perimeter in km    | Float  |
| `termini`  	| Land or marine terminating ice sheet margin (land, marine)    | String  |
| `connectivity`  	| Connectivity level as defined by Rastner et al. 2012 (CL1)    | String  |
| `subregion`  	| Region as defined by Mouginot and Rignot (2019) (NW, NO, NE, CE, SE, SW, CW)    | String  |
| `DOY`  	| Day of year in 2022 on which the corresponding Sentinel-2 imagery was acquired    | Integer  |

### Using the dataset
The dataset is openly available on the [GEUS Dataverse](https://dataverse.geus.dk/dataverse/promice-ice-mask) for downloading, distributed under a [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/). 

The dataset can be opened in spatial mapping and visualisation applications such as [QGIS](https://qgis.org/). It can also be opened and analysed in Python using spatial packages such as [geopandas](https://geopandas.org/en/stable/), like so:

```python
import geopandas as gpd
infile = "promice-2022-ice-mask.gpkg"
gdf = gpd.read_file(infile)
```

### Terms of use
If the dataset is presented or used to support results of any kind then we ask that a reference to the dataset and the dataset description be included in publications, along with any relevant publications from the data production team:

- *Luetzenburg et al. (2025) PROMICE-2022 Ice Mask: A High-Resolution Outline of the Greenland Ice Sheet from August 2022. GEUS Dataverse.*
- *Luetzenburg et al. (In Prep) PROMICE-2022 Ice Mask: A High-Resolution Outline of the Greenland Ice Sheet from August 2022. ESSD.*

And include the following statement in the acknowledgements:

"Ice mask data provided by the Programme for Monitoring of the Greenland Ice Sheet (PROMICE) at the Geological Survey of Denmark and Greenland (GEUS)."

If the dataset is crucial to the main findings, we encourage users to reach out to the authorship team as this will likely improve the quality of the work that uses this product.
