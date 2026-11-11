-- Raw Divvy trips, loaded as-is from the monthly CSV files.
-- Columns follow the Divvy trip data format (2020 onward).

CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.divvy_trips (
    ride_id             TEXT PRIMARY KEY,
    rideable_type       TEXT,             -- classic_bike, electric_bike, ...
    started_at          TIMESTAMP NOT NULL,
    ended_at            TIMESTAMP NOT NULL,
    start_station_name  TEXT,
    start_station_id    TEXT,
    end_station_name    TEXT,
    end_station_id      TEXT,
    start_lat           DOUBLE PRECISION,
    start_lng           DOUBLE PRECISION,
    end_lat             DOUBLE PRECISION,
    end_lng             DOUBLE PRECISION,
    member_casual       TEXT              -- member or casual
);

-- Load a downloaded CSV from psql:
--   \copy raw.divvy_trips FROM 'data/raw/202406-divvy-tripdata.csv' WITH (FORMAT csv, HEADER true)
