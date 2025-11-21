import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from pathlib import Path


parks = gpd.read_file(str(Path.home() / "Desktop" / "jcos_boundaries.geojson"))
print(parks.columns)
print(parks.crs)

wildlife_path = Path.home() / "Downloads" / "JeffCoAnimalSightings.csv"

wildlife = pd.read_csv(
    wildlife_path,
    sep="\t",      
    engine="python",  
)

LON_COL = "decimalLongitude"
LAT_COL = "decimalLatitude"

wildlife["geometry"] = Point(0, 0) 
wildlife["geometry"] = [
    Point(xy) for xy in zip(wildlife[LON_COL], wildlife[LAT_COL])
]

wildlife_gdf = gpd.GeoDataFrame(wildlife, geometry="geometry", crs="EPSG:4326")

joined = gpd.sjoin(
    wildlife_gdf,
    parks,
    how="left",
    predicate="within"
)

joined.drop(columns=["geometry"]).to_csv("wildlife_with_parks.csv", index=False)
