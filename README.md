Bike Volume Estimation: Transformer + Attention

Deep-learning pipeline for estimating bicycle volumes from Strava and static features. The repo includes:


Feature selection (correlation and Random Forest)

Sequence modeling with a Transformer encoder + attention for daily/monthly/annual data

Transferability experiments (train on one year, test on another)


A-Time-Series-Transformer-Attention-Model-for-Bicyclist-Volume-Estimation-Using-Feature-Selection

├── feature selection.py          # Correlation + RF feature selection

├── main.py                       # End-to-end training/eval on a single dataset

├── main.Transferability.py       # Train on 2022, test on 2019

├── features.py                   # Curated feature lists (Strava / Static / Combined)

└── config.py                     # All hyperparameters & file paths


Data overview:

The code expects CSVs with the following:

Static (df1-YYYY.csv): road/bikeway, land-use, demographics, distances to POIs, slopes, etc.

Monthly counts (combined-pc-counts-monthly-stvYYYY.csv): site_id, year, month, Counts, valid_days, valid_dayofweek, madb, stv_monthly, stv_c_monthly, n_links

Daily counts (combined-pc-counts-daily-stvYYYY.csv): site_id, Date, year, month, dayofweek, Counts, stv_daily, stv_c_daily, …

Annual counts: aadb, stv_adb, stv_c_adb, …

Targets supported: aadb (annual) and madb (monthly). Choose via config.py.


Data paths:

data_file_path_2019 = "/path/to/df1-2019.csv"

data_file_path_2022 = "/path/to/df1-2022.csv"

data_file_path_m_2019 = "/path/to/combined-pc-counts-monthly-stv2019.csv"

data_file_path_m_2022 = "/path/to/combined-pc-counts-monthly-stv2022.csv"

data_file_path_d_2019 = "/path/to/combined-pc-counts-daily-stv2019.csv"

data_file_path_d_2022 = "/path/to/combined-pc-counts-daily-stv2022.csv"
