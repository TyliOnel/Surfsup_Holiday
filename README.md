# Surfsup Holiday
I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with the trip planning, I've decide to do a climate analysis about the area. The following sections outline the steps I need to take to analyse the climate

Using Python and SQLAlchemy; specifically, using SQLAlchemy ORM queries, Pandas, and Matplotlib to do a basic climate analysis and data exploration of your climate database.

Part 1: Analyze and Explore the Climate Data:
Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, as the following image shows:
   ![Screenshot 2024-03-09 133153](https://github.com/TyliOnel/Surfsup_Holiday/assets/153153538/c1813e61-cce4-4d0f-a6c8-e931c0b8ba06)
7. Use Pandas to print the summary statistics for the precipitation data.

Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows).
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data, as the following image shows:
   ![Screenshot 2024-03-09 133413](https://github.com/TyliOnel/Surfsup_Holiday/assets/153153538/c284432b-829b-405e-97b5-9b7e1bfbbbd6)
6. Close your session.

Part 2: Design Your Climate App:
Design a Flask API based on the queries that you just developed.
1. A precipitation route that returns json with the date as the key and the value as the precipitation
2. A stations route that returns jsonified data of all of the stations in the database
3. A tobs route that returns jsonified data for the most active station (USC00519281)
4. A start/end route that returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
