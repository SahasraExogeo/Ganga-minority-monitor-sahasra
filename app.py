import ee
import geemap

#step1- Initialize Earth engine 
ee.Initialize()
#step2- define area of interest
roi= ee.Geometry.BBox(82.95, 25.25, 83.05, 25.35)
#step3- query, filter, clean the sentinel data
collection= (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
            .filterBounds(roi)
            .filterDate('2023-01-01', '2023-12-31')
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)))
#STEP4- process and apply math 
image= collection.median().clip(roi)
#print metadata to verify the data processed successfully
print("Coolection size foun:", collection.size().getInfo())
print("Pipeline executed successfully over Varanasi AOI!")