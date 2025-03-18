import sqlite3
import pandas as pd
import folium


def read_sensordb(db_path: str, table_name= "BUMP", sql_querry=None, time_column="TIMESTAMP"):
    """
    Reads in SQL `.db` file and returns Pandas DataFrame
    
    Parameters:
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table to export.
    Returns:
        Pandas DataFrame
    """

    if not sql_querry:
        sql_querry = f"SELECT * FROM {table_name};"

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql(sql_querry, conn)
    return CreansorDataFrame(df, time_column=time_column)



class CreansorDataFrame(pd.DataFrame):
    def __init__(
            self,
            *args,
            time_column = "TIMESTAMP",
            **kwargs
        ):

        super().__init__(*args, **kwargs)
        self.time_column = time_column

    def time_correction(self):
        """
        Correct the TIMESTAMP column to Proper Pandas Datetime object

        """
        self[self.time_column] = pd.to_datetime(self[self.time_column])
        return self


    def gps_correction(self, lat_column="LATITUDE", lon_column="LONGITUDE"):
        """
        correct the gps column to proper angles

        """
        self["lat"] = self[lat_column].apply(lambda x: float(x.replace("W", "").strip()))
        self["lon"] = self[lon_column].apply(lambda x: 0 - float(x.replace("N", "").strip()))
        return self

    def get_node(self, node:int, column="NODE"):
        """
        get certain node data from dataset

        """

        filter = ( self[column] == f"Node{node}" )
        return self[filter]


    def show_map(self, feature_column=None, show_start_stop=True, lat_column="lat", lon_column="lon"):
        """
        display travel map. optionally mark a defined feature from the dataset

        """

        map_center = [self[lat_column].mean(), self[lon_column].mean()]
        m = folium.Map(location=map_center, zoom_start=12)


        folium.PolyLine(self.loc[:, [lat_column, lon_column]], color="blue", weight=2.5, opacity=0.7).add_to(m)

        # add road condition markers

        if feature_column:
            for _, row in self.iterrows():
                folium.CircleMarker(
                    location=(row[lat_column], row[lon_column]),
                    radius=5,
                    color="red",
                    fill=True,
                    fill_color="red",
                    popup=f"timestamp: {row[self.time_column]}\n {feature_column}: {row[feature_column]:.2f}",
                ).add_to(m)

        if show_start_stop:

            start_coords = self.loc[self[self.time_column] == self[self.time_column].min(), [lat_column, lon_column]].head(1)
            folium.Marker(
                location=start_coords,
                popup="travel start",
                icon=folium.Icon(icon="play", prefix='fa'),
            ).add_to(m)

            end_coords = self.loc[self[self.time_column] == self[self.time_column].max(), [lat_column, lon_column]].head(1)
            folium.Marker(
                location=end_coords,
                popup="travel end",
                icon=folium.Icon(icon="flag", prefix='fa'),
            ).add_to(m)

        return m








# def get_node(node:int, df:pd.dataframe, column="node"):
#     """
#     get certain node data from dataset

#     """

#     filter = ( df[column] == f"node{node}" )
#     return df[filter]


# def time_correction(df:pd.dataframe, time_column="timestamp"):
#     """
#     correct the timestamp column to proper pandas datetime object

#     """
#     df[time_column] = pd.to_datetime(df[time_column])
#     return df


# def gps_correction(df:pd.dataframe, lat_column="latitude", lon_column="longitude"):
#     """
#     correct the gps column to proper angles

#     """
#     df["lat"] = df[lat_column].apply(lambda x: float(x.replace("w", "").strip()))
#     df["lon"] = df[lon_column].apply(lambda x: 0 - float(x.replace("n", "").strip()))
#     return df


# def show_map(df:pd.dataframe, feature_column=None, show_start_stop=False, time_column="timestamp", lat_column="lat", lon_column="lon"):
#     """
#     display travel map. optionally mark a defined feature from the dataset

#     """

#     map_center = [df[lat_column].mean(), df[lon_column].mean()]
#     m = folium.map(location=map_center, zoom_start=12)


#     folium.polyline(df.loc[:, [lat_column, lon_column]], color="blue", weight=2.5, opacity=0.7).add_to(m)

# # add road condition markers

#     if feature_column:
#         for _, row in df.iterrows():
#             folium.circlemarker(
#                 location=(row[lat_column], row[lon_column]),
#                 radius=5,
#                 color="red",
#                 fill=True,
#                 fill_color="red",
#                 popup=f"timestamp: {row[time_column]}\n {feature_column}: {row[feature_column]:.2f}",
#             ).add_to(m)

#     if show_start_stop:

#         start_coords = df.loc[df[time_column] == df[time_column].min(), [lat_column, lon_column]].head(1)
#         folium.marker(
#             location=start_coords,
#             popup="travel start",
#             icon=folium.icon(icon="play", prefix='fa'),
#         ).add_to(m)

#         end_coords = df.loc[df[time_column] == df[time_column].max(), [lat_column, lon_column]].head(1)
#         folium.marker(
#             location=end_coords,
#             popup="travel end",
#             icon=folium.icon(icon="flag", prefix='fa'),
#         ).add_to(m)

#     return m
