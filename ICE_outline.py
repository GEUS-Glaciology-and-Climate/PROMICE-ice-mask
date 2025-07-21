#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:17:26 2022

@author: njk
"""

# Import modules
import os
import shutil
from osgeo import gdal
import rasterio as rio
from rasterio.features import shapes
import numpy as np

def folder_mgmt(year, input_filename, ctrl_pgon_str):
    # Managing input and output file locations
    
    # checking if the directory year exists or not.
    PathYear = os.path.join('./results/', str(year))
    if not os.path.exists(PathYear):
          
        # if the demo_folder directory is not present then create it.
        os.mkdir(os.path.join('./results/', str(year)))
   
    
    # checking if the directories year and raw_data exist or not.
    PathRaw = os.path.join('./results/', str(year), 'raw_data/')
    if not os.path.exists(PathRaw):
          
        # if the demo_folder directory is not present then create it.
        os.mkdir(os.path.join('./results/', str(year), 'raw_data'))

    # PathPgon = os.path.join('./results/', str(year), ctrl_pgon_str)
    # if not os.path.exists(PathPgon):
          
    #     # if the directory is not present then create it.
    #     os.mkdir(os.path.join('./results/', str(year), ctrl_pgon_str))
        
    # Make a folder for the rgb output files.
    PathRGB = os.path.join('./results/', str(year), 'RGB')
    if not os.path.exists(PathRGB):
          
        # if the directory is not present then create it.
        os.mkdir(os.path.join('./results/', str(year), 'RGB'))
        
    # Make a folder for the fused raster data files.
    PathData = os.path.join('./results/', str(year), 'Data')
    if not os.path.exists(PathData):
          
        # if the directory is not present then create it.
        os.mkdir(os.path.join('./results/', str(year), 'Data'))

    # Make a folder for the classification vector files.
    PathClass = os.path.join('./results/', str(year), 'Classification')
    if not os.path.exists(PathClass):
          
        # if the directory is not present then create it.
        os.mkdir(os.path.join('./results/', str(year), 'Classification'))
        
    # Make a folder for the time DOY vector files.
    PathDOY = os.path.join('./results/', str(year), 'DOY')
    if not os.path.exists(PathDOY):
          
        # if the directory is not present then create it.
        os.mkdir(os.path.join('./results/', str(year), 'DOY'))
        
        pass


# Builds a list of paths of requested tiff files.
def MakeList4VRT(data_folder):
    VRT_list = []
    # os.walk() returns subdirectories, file from current directory and 
    # And follow next directory from subdirectory list recursively until last directory
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if file.endswith(".tiff"):
                VRT_list.append(os.path.join(root, file))
    return VRT_list


# VRT to GeoTiff
def VRT2GTiff(new_vrt, year, ctrl_pgon_str):
    #Open existing dataset
    # src_ds = gdal.Open( src_filename )
    PathData = os.path.join('./results/', str(year), 'Data')

    #Open output format driver, see gdal_translate --formats for list
    format = "GTiff"
    driver = gdal.GetDriverByName( format )

    #Output to new format
    dst_ds = driver.CreateCopy( '{}/Data_{}.tif'.format(PathData, ctrl_pgon_str), new_vrt, 0 )

    #Properly close the datasets to flush to disk
    dst_ds = None
    src_ds = None


# #Vectorisation function
# def getGeodata(img, trans):
#     '''Get vector features from binary raster image. Raster data is loaded 
#     from array as a rasterio inmemory object, and returns features as a 
#     geopandas dataframe

#     Variables
#     img (arr)                           Binary raster array
#     trans (Affine):                     Raster transformation (computed using
#                                         affine package, or 
#                                         rasterio.transform) 
#     Returns
#     feats (Geodataframe):               Vector features geodataframe
#     '''
#     #Open array as rasterio memory object
#     with rio.io.MemoryFile() as memfile:
#         with memfile.open(
#             driver='GTiff',
#             eight=img.shape[0],
#             width=img.shape[1],
#             count=1,
#             dtype=img.dtype,
#             transform=trans
#         ) as dataset:
#             dataset.write(img, 1)
        
#         #Vectorize array
#         with memfile.open() as dataset:
#                 image = dataset.read(1)
#                 mask = image==255
#                 results = (
#                 {'properties': {'raster_val': v}, 'geometry': s}
#                 for i, (s, v) 
#                 in enumerate(
#                     shapes(image, 
#                            mask=mask, 
#                            transform=rio.transform.from_origin(transf[0], 
#                                                                transf[3], 
#                                                                transf[1], 
#                                                                transf[5]))))
                
#                 ##Transform geometries to geodataframe
#                 geoms = list(results)
#                 feats = gp.GeoDataFrame.from_features(geoms)
                
#     return feats

def makeRGBtiff(ctrl_pgon_str, year):
    # Get input file
    PathData = os.path.join('./results/', str(year), 'Data')
    df = '{}/Data_{}.tif'.format(PathData, ctrl_pgon_str)
    
    src = rio.open(df)

    # Copy file profile
    srcprofile = src.profile.copy()

    # Read arrays
    rgb8 = ((src.read([3, 2, 1]))*0.0122).astype(np.uint8)
   
    # Update the file options to one band before writing
    srcprofile.update(count=3, nodata=None, dtype=rgb8.dtype)
    
    # Write 3 band array to geotiff one index at a time...
    PathRGB = os.path.join('./results/', str(year), 'RGB')
    
    with rio.open('{}/rgb_{}.tif'.format(PathRGB, ctrl_pgon_str), 'w', **srcprofile) as dst:
        for i in range(0, 3):
            dst.write(rgb8[i], i+1)
