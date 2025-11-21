import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

wildlife = pd.read_csv("wildlife_with_parks.csv")

if "index_right" in wildlife.columns:
    wildlife = wildlife.drop(columns=["index_right"])

LON_COL = "decimalLongitude"
LAT_COL = "decimalLatitude"

wildlife["geometry"] = gpd.points_from_xy(
    wildlife[LON_COL],
    wildlife[LAT_COL]
)
wildlife_gdf = gpd.GeoDataFrame(wildlife, geometry="geometry", crs="EPSG:4326")

trails = gpd.read_file("~/Downloads/jcos_trails.geojson")

crs_proj = "EPSG:2232"
wild_proj   = wildlife_gdf.to_crs(crs_proj)
trails_proj = trails.to_crs(crs_proj)

joined_trails = gpd.sjoin_nearest(
    wild_proj,
    trails_proj,
    how="left",
    distance_col="dist_to_trail_ft",
    max_distance=30
)

joined_trails_ll = joined_trails.to_crs("EPSG:4326")
joined_trails_ll.drop(columns=["geometry"]).to_csv(
    "wildlife_with_parks_and_trails.csv",
    index=False
)
