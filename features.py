#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# features.py

#1
# (monthly + df) (madb target)

# madb target - 2019 - monthly and df1 - correlation + rf
#strava_static_features_2019 = [
#    'college_om', 'lanes_om', 'avg_slope_hm', 'region', 'valid_month', 'Distance to Park Center', 
#    'employment_density_om', 'pct_female_hm', 
#    'cycleway_track_all_hm', 'Residential_Road_om', 'School_hm', 'avg_slope_om', 'cycleway_lane_all_hm',  
#    'footway_binary', 'Bike_Commuter_hm', 'min_dist_to_maj_uni', 'Water Area_hm', 
#    'population_density_om', 'Commercial Area_om', 'Footway_hm', 'Distance to Forest Center', 'HH_density_hm', 
#    'Distance to Industrial Center', 'Secondary_hm', 'Bike_Commuter_om', 'bridge_hm', 'Commercial Area_hm', 'Path_om', 
#    'Bicycle Parking_hm', 'Intersection_Density_om', 'Point Bridge_om', 'min_dist_to_school', 'Cycleway_hm', 
#    'Bus Stops_hm', 'Bicycle Parking_om', 'sep_bikeway_hm', 'Footway_om', 'Bus Stops_om', 
#    'Distance to Residential Area', 'Distance to Indusaadbtrial Area', 'population_density_hm', 'Tertiary_hm', 
#    'Distance_to_Water_Body_mi', 'Student Access_om', 'Distance to Commercial Area', 
#   'Median_HH_income_om', 'Point Bridge_hm', 'Point Speed_hm', 'min_dist_to_university', 
#    'cycleway_lane_all_om', 'pct_at_least_college_education_om', 'cycleway_track_all_om', 'Number of jobs_om', 
#    'Distance to Water Center', 'University_om', 'HH_density_om', 'Distance to forest', 
#    'Distance to Retail Center', 'Water Area_om', 'BikeFac_onstreet_om', 'employment_density_hm', 'school_college_hm', 
#   'Number of jobs_hm', 'Point Speed_om', 'pct_at_least_college_education_hm', 
#    'Cycleway_om', 'Distance to Water Body', 'Secondary_om', 'lanes_hm', 'pct_white_hm', 'Distance to Retail Area', 
#    'Residential_Road_hm', 'site_id', 'Intersection_Density_hm',
#    'stv_monthly', 'month', 'Counts', 'stv_c_monthly', 'valid_days', 'valid_dayofweek', 
#    'aadb1', 'AADBT', 'aadb', 'aadb2', 
#    'stv_nc_adb', 'adb', 'log_stv_nc_adb', 'stv_adb', 'log_stv_adb', 'log_stv_c_adb', 'reg_num', 'valid_months', 
#    'stv_c_adb', 'valid_days_year', 'valid_year'
#] 

# , 
#    'aadb1', 'AADBT', 'aadb', 'aadb2', 
#   'stv_nc_adb', 'adb', 'log_stv_nc_adb', 'stv_adb', 'log_stv_adb', 'log_stv_c_adb', 'reg_num', 'valid_months', 
#    'stv_c_adb', 'valid_days_year', 'valid_year'

# madb target - 2019 - monthly and df1 - correlation + rf
#static_features_2019 = [
#    'college_om', 'lanes_om', 'avg_slope_hm', 'region', 'Distance to Park Center', 
#    'employment_density_om', 'pct_female_hm', 
#  'cycleway_track_all_hm', 'Residential_Road_om', 'School_hm', 'avg_slope_om', 'cycleway_lane_all_hm', 
#    'footway_binary', 'Bike_Commuter_hm', 'min_dist_to_maj_uni', 'Water Area_hm', 
#    'population_density_om', 'Commercial Area_om', 'Footway_hm', 'Distance to Forest Center', 'HH_density_hm', 
#    'Distance to Industrial Center', 'Secondary_hm', 'Bike_Commuter_om', 'bridge_hm', 'Commercial Area_hm', 'Path_om', 
#    'Bicycle Parking_hm', 'Intersection_Density_om', 'Point Bridge_om', 'min_dist_to_school', 'Cycleway_hm', 
#    'Bus Stops_hm', 'Bicycle Parking_om', 'sep_bikeway_hm', 'Footway_om', 'Bus Stops_om', 
#    'Distance to Residential Area', 'Distance to Industrial Area', 'population_density_hm', 'Tertiary_hm', 
#    'Distance_to_Water_Body_mi', 'Student Access_om', 'Distance to Commercial Area', 
#    'Median_HH_income_om', 'Point Bridge_hm', 'Point Speed_hm', 'min_dist_to_university', 
#    'cycleway_lane_all_om', 'pct_at_least_college_education_om', 'cycleway_track_all_om', 'Number of jobs_om', 
#    'Distance to Water Center', 'University_om', 'HH_density_om', 'Distance to forest', 
#   'Distance to Retail Center', 'Water Area_om', 'BikeFac_onstreet_om', 'employment_density_hm', 'school_college_hm', 
#    'Number of jobs_hm', 'Point Speed_om', 'pct_at_least_college_education_hm', 
#    'Cycleway_om', 'Distance to Water Body', 'Secondary_om', 'lanes_hm', 'pct_white_hm', 'Distance to Retail Area', 
#    'Residential_Road_hm', 'site_id', 'Intersection_Density_hm'
#]

# 'aadb1', 'aadb', 'aadb2', 'AADBT', 
# 'stv_nc_adb', 'adb', 'log_stv_nc_adb', 'reg_num', 'stv_adb', 'log_stv_adb', 'stv_c_adb', 'log_stv_c_adb', 'valid_months',
# 'valid_days_year', 'valid_year', 
# 'Counts', 'stv_c_monthly', 'stv_monthly', 'valid_month', 'valid_dayofweek', 'valid_days', 
# 'month', 

# yearly
# site_id, site_name, year, valid_months, valid_days_year, adb, aadb1, valid_year, aadb2, aadb, reg_num, stv_adb, stv_c_adb


# monthly
# site_id, site_name, year, month, valid_days, valid_dayofweek, Counts, valid_month, madb, stv_monthly, stv_c_monthly,
# n_links

# madb target - 2019 - monthly and df1 - correlation + rf
#strava_features_2019 = [
#    'Counts', 'stv_c_monthly', 'stv_monthly', 'valid_month', 'valid_dayofweek', 'valid_days', 'valid_days_year', 
#     'month', 'site_id' 
#]

#  'n_links'


# madb target - 2022 - monthly and df1 - correlation + rf
#strava_static_features_2022 = [
#    'lanes_om', 'BikeFac_onstreet_hm', 'valid_month', 'employment_density_om', 
#    'cycleway_track_all_hm', 'School_hm', 'avg_slope_om', 'Residential_Area_hm', 
#    'Retail Area_om', 'footway_binary', 'Bike_Commuter_hm', 'valid_dayofweek', 
#    'maj_uni_count_om', 'min_dist_to_maj_uni', 'Water Area_hm', 'population_density_om', 'Commercial Area_om', 
#    'Footway_hm', 'Distance to Forest Center', 'pct_African_American_hm', 'Secondary_hm', 'Bike_Commuter_om', 
#    'Commercial Area_hm', 'Intersection_Density_om', 'Point Bridge_om', 'Cycleway_hm', 'Bus Stops_hm', 'Footway_om', 
#    'Bus Stops_om', 'Distance_to_Water_Body_mi', 'Grass Area_om', 'pct_African_American_om', 
#    'Student Access_om', 'point_slope_om', 'Point Bridge_hm', 'valid_days', 'stv_c_monthly', 'Counts', 'stv_monthly', 
#    'Primary_hm', '_osmId', 'University_om', 'HH_density_om', 'Distance to forest', 'Water Area_om', 
#    'BikeFac_onstreet_om', 'min_dist_to_park', 'Cycleway_om', 'Distance to Water Body', 'lanes_hm', 
#    'Distance to Retail Area', 'site_id', 'cycleway_binary', 'month', 'point_slope_hm', 
#    'min_dist_to_city_mi', 'uni_count_om', 'Intersection_Density_hm',
#    'aadb1', 'aadb', 'aadb2',  'AADBT', 
#    'stv_nc_adb', 'adb', 'stv_adb', 'log_stv_nc_adb', 'valid_months', 'log_stv_adb', 'log_stv_c_adb', 'stv_c_adb','valid_days_year',     
#]    



# madb target - 2022 - monthly and df1 - correlation + rf
#static_features_2022 = [
#    'lanes_om', 'BikeFac_onstreet_hm', 'employment_density_om', 
#    'cycleway_track_all_hm', 'School_hm', 'avg_slope_om', 'Residential_Area_hm', 
#    'Retail Area_om', 'footway_binary', 'Bike_Commuter_hm', 
#    'maj_uni_count_om', 'min_dist_to_maj_uni', 'Water Area_hm', 'population_density_om', 'Commercial Area_om', 
#    'Footway_hm', 'Distance to Forest Center', 'pct_African_American_hm', 'Secondary_hm', 'Bike_Commuter_om', 
#    'Commercial Area_hm', 'Intersection_Density_om', 'Point Bridge_om', 'Cycleway_hm', 'Bus Stops_hm', 'Footway_om', 
#    'Bus Stops_om', 'Distance_to_Water_Body_mi', 'Grass Area_om', 'pct_African_American_om', 
#    'Student Access_om', 'point_slope_om', 'Point Bridge_hm', 
#    'Primary_hm', '_osmId', 'University_om', 'HH_density_om', 'Distance to forest', 'Water Area_om', 
#    'BikeFac_onstreet_om', 'min_dist_to_park', 'Cycleway_om', 'Distance to Water Body', 'lanes_hm', 
#    'Distance to Retail Area', 'site_id', 'cycleway_binary', 'point_slope_hm', 
#    'min_dist_to_city_mi', 'uni_count_om', 'Intersection_Density_hm'
#]    
   

# 'aadb1', 'aadb', 'AADBT', 'aadb2', 
# 'stv_c_adb',  'stv_nc_adb', 'adb', 'log_stv_nc_adb', 'stv_adb', 'valid_days_year', 'log_stv_adb', 'log_stv_c_adb', 'valid_months', 
# 'valid_dayofweek', 'valid_days', 'stv_c_monthly', 'Counts', 'stv_monthly', 'month', 'valid_month', 

# yearly
# site_id, site_name, year, valid_months, valid_days_year, adb, aadb1, valid_year, aadb2, aadb, reg_num, stv_adb, stv_c_adb


# monthly
# site_id, site_name, year, month, valid_days, valid_dayofweek, Counts, valid_month, madb, stv_monthly, stv_c_monthly,
# n_links

# madb target - 2022 - monthly and df1 - correlation + rf
#strava_features_2022 = [
#    'valid_dayofweek', 'valid_days', 'stv_c_monthly', 'Counts', 'stv_monthly', 'month', 'valid_month', 
#     'site_id' 
#]
# valid_days_year', 'valid_year',

#-----------------------------------------------------------------------------------------------------------
# just correlation features

# (monthly + df) (madb target)
#strava_static_features_2019 = [
#    'Counts', 'stv_monthly', 'stv_c_monthly', 'valid_months', 'valid_days_year', 'adb', 'aadb1', 'valid_year', 'aadb2', 
#    'aadb', 'reg_num', 'stv_adb', 'stv_c_adb', 'AADBT', 'footway_binary', 'lanes_hm', 'Intersection_Density_hm', 
#    'Water Area_hm', 'Distance to Water Body', 'Bicycle Parking_hm', 'Bus Stops_hm', 'Secondary_hm', 'Cycleway_hm', 
#    'Footway_hm', 'cycleway_track_all_hm', 'Point Bridge_hm', 'pct_at_least_college_education_hm', 'HH_density_hm', 
#    'population_density_hm', 'employment_density_hm', 'Number of jobs_hm', 'avg_slope_hm', 'lanes_om', 
#    'Intersection_Density_om', 'Water Area_om', 'Bicycle Parking_om', 'Bus Stops_om', 'college_om', 'University_om', 
#    'Secondary_om', 'Residential_Road_om', 'Cycleway_om', 'Footway_om', 'cycleway_track_all_om', 'Point Bridge_om', 
#    'Student Access_om', 'pct_at_least_college_education_om', 'HH_density_om', 'population_density_om', 
#    'employment_density_om', 'Number of jobs_om', 'avg_slope_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 'stv_nc_adb', 
#    'BikeFac_onstreet_om', 'log_stv_adb', 'log_stv_c_adb', 'log_stv_nc_adb', 'Distance_to_Water_Body_mi', 'region'
#]
    

#static_features_2019 = [
#    'footway_binary', 'lanes_hm', 'Intersection_Density_hm', 
#    'Water Area_hm', 'Distance to Water Body', 'Bicycle Parking_hm', 'Bus Stops_hm', 'Secondary_hm', 'Cycleway_hm', 
#    'Footway_hm', 'cycleway_track_all_hm', 'Point Bridge_hm', 'pct_at_least_college_education_hm', 'HH_density_hm', 
#    'population_density_hm', 'employment_density_hm', 'Number of jobs_hm', 'avg_slope_hm', 'lanes_om', 
#    'Intersection_Density_om', 'Water Area_om', 'Bicycle Parking_om', 'Bus Stops_om', 'college_om', 'University_om', 
#    'Secondary_om', 'Residential_Road_om', 'Cycleway_om', 'Footway_om', 'cycleway_track_all_om', 'Point Bridge_om', 
#    'Student Access_om', 'pct_at_least_college_education_om', 'HH_density_om', 'population_density_om', 
#    'employment_density_om', 'Number of jobs_om', 'avg_slope_om', 'Bike_Commuter_hm', 'Bike_Commuter_om',
#    'BikeFac_onstreet_om', 'Distance_to_Water_Body_mi', 'region'
#]
    
# 'AADBT', 'aadb1', 'aadb',  'aadb2',
# 'valid_months', 'valid_days_year', 'adb', 'valid_year', 'reg_num', 'stv_adb', 'stv_c_adb',  'stv_nc_adb', 'log_stv_adb', 
# 'log_stv_c_adb', 'log_stv_nc_adb', 
# 'Counts', 'stv_monthly', 'stv_c_monthly', 

#strava_features_2019 = [
#    'Counts', 'stv_monthly', 'stv_c_monthly'
#]
    
    
    
    
#strava_static_features_2022 = [
#    'Counts', 'stv_monthly', 'stv_c_monthly', 'adb', 'aadb1', 'aadb2', 'aadb', 'stv_adb', 'stv_c_adb', 'AADBT', 
#    'footway_binary', 'Intersection_Density_hm', 'Water Area_hm', 'Bus Stops_hm', 'Secondary_hm', 'Cycleway_hm', 
#    'Footway_hm', 'cycleway_track_all_hm', 'Point Bridge_hm', 'Intersection_Density_om', 'Water Area_om', 'Bus Stops_om', 
#    'uni_count_om', 'University_om', 'Cycleway_om', 'Footway_om', 'Point Bridge_om', 'Student Access_om', 'HH_density_om', 
#    'population_density_om', 'employment_density_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 'stv_nc_adb', 
#    'BikeFac_onstreet_hm', 'BikeFac_onstreet_om', 'log_stv_adb', 'log_stv_c_adb', 'log_stv_nc_adb'
#]
    
#static_features_2022 = [    
#    'footway_binary', 'Intersection_Density_hm', 'Water Area_hm', 'Bus Stops_hm', 'Secondary_hm', 'Cycleway_hm', 
#    'Footway_hm', 'cycleway_track_all_hm', 'Point Bridge_hm', 'Intersection_Density_om', 'Water Area_om', 'Bus Stops_om', 
#    'uni_count_om', 'University_om', 'Cycleway_om', 'Footway_om', 'Point Bridge_om', 'Student Access_om', 'HH_density_om', 
#    'population_density_om', 'employment_density_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 
#    'BikeFac_onstreet_hm', 'BikeFac_onstreet_om'
#]

# 'aadb1', 'aadb2', 'aadb', 'AADBT', 
# 'adb', 'stv_adb', 'stv_c_adb', 'stv_nc_adb', 'log_stv_adb', 'log_stv_c_adb', 'log_stv_nc_adb'
# 'Counts', 'stv_monthly', 'stv_c_monthly', 

#strava_features_2022 = [    
#    'Counts', 'stv_monthly', 'stv_c_monthly'
#]

#-----------------------------------------------------------------------------------------------------------
# just random forest features

# (monthly + df) (madb target)
#strava_static_features_2019 = [
#    'Counts', 'stv_monthly', 'stv_c_monthly', 'adb', 'valid_days', 'month', 'Distance to Water Center', 'AADBT', 
#    'Median_HH_income_om', 'cycleway_lane_all_om', 'pct_at_least_college_education_hm', 'aadb', 'Distance to Water Body', 
#    'aadb2', 'Distance to Park Center', 'Point Speed_hm', 'Bike_Commuter_hm', 'Residential_Road_hm', 'Tertiary_hm', 
#    'Point Speed_om', 'HH_density_hm', 'min_dist_to_university', 'Commercial Area_hm', 'Distance to forest', 
#    'Distance to Industrial Center', 'pct_female_hm', 'Distance to Industrial Area', 'Distance to Retail Area', 
#    'Distance to Forest Center', 'pct_white_hm', 'School_hm', 'min_dist_to_maj_uni', 'sep_bikeway_hm', 'site_id', 
#    'Secondary_hm', 'bridge_hm', 'valid_month', 'Distance to Retail Center', 'Bus Stops_om', 'Path_om', 
#    'min_dist_to_school', 'Distance_to_Water_Body_mi', 'employment_density_om', 'Intersection_Density_hm', 
#    'Distance to Commercial Area', 'valid_dayofweek', 'Commercial Area_om', 'school_college_hm', 'cycleway_lane_all_hm', 
#    'Distance to Residential Area'
#]

#static_features_2019 = [
#    'Distance to Water Center', 
#    'Median_HH_income_om', 'cycleway_lane_all_om', 'pct_at_least_college_education_hm', 'Distance to Water Body', 
#    'aadb2', 'Distance to Park Center', 'Point Speed_hm', 'Bike_Commuter_hm', 'Residential_Road_hm', 'Tertiary_hm', 
#    'Point Speed_om', 'HH_density_hm', 'min_dist_to_university', 'Commercial Area_hm', 'Distance to forest', 
#    'Distance to Industrial Center', 'pct_female_hm', 'Distance to Industrial Area', 'Distance to Retail Area', 
#    'Distance to Forest Center', 'pct_white_hm', 'School_hm', 'min_dist_to_maj_uni', 'sep_bikeway_hm', 'site_id', 
#    'Secondary_hm', 'bridge_hm', 'Distance to Retail Center', 'Bus Stops_om', 'Path_om', 
#    'min_dist_to_school', 'Distance_to_Water_Body_mi', 'employment_density_om', 'Intersection_Density_hm', 
#    'Distance to Commercial Area', 'Commercial Area_om', 'school_college_hm', 'cycleway_lane_all_hm', 
#    'Distance to Residential Area'
#]

# 'AADBT', 'aadb',  
#  'adb', 
# 'Counts', 'stv_monthly', 'stv_c_monthly', 'valid_month', 'valid_dayofweek', 'valid_days', 'month'

#strava_features_2019 = [
#    'Counts', 'stv_monthly', 'stv_c_monthly', 'valid_month', 'valid_dayofweek', 'valid_days', 'month'
#]

# (monthly + df) (madb target)
#strava_static_features_2022 = [
    

#-----------------------------------------------------------------------------------------------------------
# just RPE features
# (monthly + df) (madb target)
#strava_static_features_2019 = [
#    'month', 'valid_days', 'valid_dayofweek', 'valid_month', 'n_links', 'valid_months', 'reg_num', 'stv_adb', 
#    'secondary_binary', 'tertiary_binary', 'residential_binary', 'path_binary', 'cycleway_binary', 'footway_binary', 
#    'lanes_hm', 'Bus Stops_hm', 'School_hm', 'college_hm', 'uni_count_hm', 'University_hm', 'maj_uni_count_hm', 
#    'Maj University_hm', 'bridge_hm', 'Point Bridge_hm', 'pct_white_hm', 'pct_African_American_hm', 'pct_male_hm', 
#    'point_slope_hm', 'avg_slope_hm', 'college_om', 'uni_count_om', 'University_om', 'maj_uni_count_om', 
#    'Maj University_om', 'Point Bridge_om', 'pct_white_om', 'pct_African_American_om', 'point_slope_om', 'avg_slope_om', 
#    'sep_onstreet_binary', 'BikeFac_binary', 'arterial_binary', 'arterial_no_bike_lane_binary', 
#    'secondary_no_bike_lane_binary', 'secondary_bike_lane_binary', 'school_college_hm', 'log_stv_adb', 'log_stv_c_adb', 
#    'log_stv_nc_adb', 'region'
#]

#static_features_2019 = [   
#    'secondary_binary', 'tertiary_binary', 'residential_binary', 'path_binary', 'cycleway_binary', 'footway_binary', 
#    'lanes_hm', 'Bus Stops_hm', 'School_hm', 'college_hm', 'uni_count_hm', 'University_hm', 'maj_uni_count_hm', 
#    'Maj University_hm', 'bridge_hm', 'Point Bridge_hm', 'pct_white_hm', 'pct_African_American_hm', 'pct_male_hm', 
#    'point_slope_hm', 'avg_slope_hm', 'college_om', 'uni_count_om', 'University_om', 'maj_uni_count_om', 
#    'Maj University_om', 'Point Bridge_om', 'pct_white_om', 'pct_African_American_om', 'point_slope_om', 'avg_slope_om', 
#    'sep_onstreet_binary', 'BikeFac_binary', 'arterial_binary', 'arterial_no_bike_lane_binary', 
#    'secondary_no_bike_lane_binary', 'secondary_bike_lane_binary', 'school_college_hm', 'region'
#]

# 
#  'reg_num', 'stv_adb', 'log_stv_adb', 'log_stv_c_adb', 'log_stv_nc_adb', 'valid_months'
# 'month', 'valid_days', 'valid_dayofweek', 'valid_month', 'n_links'

#strava_features_2019 = [
#    'month', 'valid_days', 'valid_dayofweek', 'valid_month', 'n_links'
#]

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

#2
# (yearly + df = df) (aadb target)

# aadb target - 2019 - yearly and df1 - correlation + rf
#strava_static_features_2019 = [
#    'valid_year', 'min_dist_to_maj_uni', 'Cycleway_om', 'stv_nc_adb', 'min_dist_to_school', 'Number of jobs_om', 'aadb1', 
#    'Residential_Road_hm', 'Distance to Grass', 'cycleway_lane_all_hm', 'School_hm', 'population_density_hm', 
#    'Distance to Water Body', 'cycleway_track_all_hm', 'Tertiary_om', 'Secondary_om', 'Path_om', 'Bicycle Parking_hm', 
#    'Secondary_hm', 'pct_female_om', 'aadb', 'Number of jobs_hm', 'stv_adb', 'Residential_Road_om', 'pct_female_hm', 
#    'lanes_hm', 'uni_count_hm', 'Bicycle Parking_om', 'Distance_to_Water_Body_mi', 'Commercial Area_hm', 'log_stv_nc_adb', 
#    'Commercial Area_om', 'sep_bikeway_hm', 'population_density_om', '_osmId', 'BikeFac_onstreet_om', 'valid_days_year', 
#    'log_stv_adb', 'pct_at_least_college_education_hm', 'avg_slope_om', 'Primary_om', 'Distance to Water Center', 
#    'Point Bridge_om', 'avg_slope_hm', 'Water Area_hm', 'University_om', 'Intersection_Density_hm', 
#    'Intersection_Density_om', 'Footway_hm', 'employment_density_hm', 'college_om', 'HH_density_om', 'Water Area_om', 
#    'lanes_om', 'University_hm', 'Bus Stops_om', 'footway_binary', 'pct_at_least_college_education_om', 'Bike_Commuter_hm', 
#    'adb', 'cycleway_track_all_om', 'pct_African_American_hm', 'Footway_om', 'employment_density_om', 'aadb2', 'stv_c_adb', 
#    'Point Bridge_hm', 'region', 'Bus Stops_hm', 'BikeFac_onstreet_hm', 'uni_count_om', 'Distance to Industrial Center', 
#    'Bike_Commuter_om', 'pct_African_American_om', 'Distance to Grass Center', 'Distance to Park', 'HH_density_hm', 
#    'Student Access_om', 'BikeFac_om', 'Cycleway_hm', 'valid_months', 'log_stv_c_adb', 'reg_num'
#]

    
# aadb target - 2019 - yearly and df1 - correlation + rf
#static_features_2019 = [
#    'min_dist_to_maj_uni', 'Cycleway_om', 'min_dist_to_school', 'Number of jobs_om', 
#    'Residential_Road_hm', 'Distance to Grass', 'cycleway_lane_all_hm', 'School_hm', 'population_density_hm', 
#    'Distance to Water Body', 'cycleway_track_all_hm', 'Tertiary_om', 'Secondary_om', 'Path_om', 'Bicycle Parking_hm', 
#    'Secondary_hm', 'pct_female_om', 'Number of jobs_hm', 'Residential_Road_om', 'pct_female_hm', 
#    'lanes_hm', 'uni_count_hm', 'Bicycle Parking_om', 'Distance_to_Water_Body_mi', 'Commercial Area_hm', 'log_stv_nc_adb', 
#    'Commercial Area_om', 'sep_bikeway_hm', 'population_density_om', '_osmId', 'BikeFac_onstreet_om', 'valid_days_year', 
#    'pct_at_least_college_education_hm', 'avg_slope_om', 'Primary_om', 'Distance to Water Center', 
#    'Point Bridge_om', 'avg_slope_hm', 'Water Area_hm', 'University_om', 'Intersection_Density_hm', 
#    'Intersection_Density_om', 'Footway_hm', 'employment_density_hm', 'college_om', 'HH_density_om', 'Water Area_om', 
#    'lanes_om', 'University_hm', 'Bus Stops_om', 'footway_binary', 'pct_at_least_college_education_om', 'Bike_Commuter_hm', 
#    'cycleway_track_all_om', 'pct_African_American_hm', 'Footway_om', 'employment_density_om',
#    'Point Bridge_hm', 'region', 'Bus Stops_hm', 'BikeFac_onstreet_hm', 'uni_count_om', 'Distance to Industrial Center', 
#    'Bike_Commuter_om', 'pct_African_American_om', 'Distance to Grass Center', 'Distance to Park', 'HH_density_hm', 
#    'Student Access_om', 'BikeFac_om', 'Cycleway_hm'
#]

# 'aadb1', 'aadb',  'aadb2', 
# 'valid_year', 'stv_nc_adb', 'stv_adb', 'log_stv_adb',  'stv_c_adb', 'adb',  'valid_months', 'log_stv_c_adb', 'reg_num'
# 
    
# aadb target - 2019 - yearly and df1 - correlation + rf
#strava_features_2019 = [    
#    'aadb1', 'aadb',  'aadb2', 
#    'valid_year', 'stv_nc_adb', 'stv_adb', 'log_stv_adb',  'stv_c_adb', 'adb',  'valid_months', 'log_stv_c_adb', 'reg_num'    
#]
    
    
# aadb target - 2022 - yearly and df1 - correlation + rf
#strava_static_features_2022 = [
#    'min_dist_to_college', 'Forest Area_om', 'BikeFac_hm', 'Intersection_Density_om', 'Path_hm', 'employment_density_om', 
#    'Distance to Water Body', 'Bicycle Parking_om', 'Intersection_Density_hm', 'Distance_to_Water_Body_mi', 
#    'Point Bridge_hm', 'Footway_hm', 'Industrial Area_om', 'HH_density_hm', 'Residential_Road_hm', 
#    'sep_bikeway_om', 'Distance to forest', 'edgeUID', 'Residential_Area_om', 'min_dist_to_park', 'University_hm', 
#    'Bus Stops_hm', 'Student Access_hm', 'pct_African_American_hm', 'Distance to Grass Center', 'Bike_Commuter_om', 
#    'Bike_Commuter_hm', 'Residential_Road_om', 'BikeFac_onstreet_om', 'Water Area_om', 'population_density_om', 
#    'population_density_hm', 'footway_binary', 'Point Bridge_om', 'Tertiary_om', 'lanes_om', 'Primary_hm', 
#    'Number of jobs_hm', 'University_om', 'pct_white_hm', 'cycleway_track_all_hm', 'avg_slope_hm', 'lanes_hm', 
#    'BikeFac_onstreet_hm', 'Bicycle Parking_hm', 'employment_density_hm', 'Bus Stops_om', 'min_dist_to_city_mi', 
#    'Secondary_hm', 'Footway_om', 'Secondary_om', 'Distance to Residential Area', 'Median_HH_income_hm', 
#    'Cycleway_om', 'pct_female_hm', 'uni_count_om', 'HH_density_om', 'adb', 'college_hm',
#    '_osmId', 'Median_HH_income_om', 'Water Area_hm', 'avg_slope_om', 'Student Access_om', 
#    'Cycleway_hm', 'Distance to Residential Center',
#     'AADBT', 'aadb2',  'aadb1', 
#    'log_stv_nc_adb', 'stv_adb', 'stv_c_adb',  'stv_nc_adb', 'valid_days_year', 'log_stv_adb', 'log_stv_c_adb' 
#]

    
# aadb target - 2022 - yearly and df1 - correlation + rf
#static_features_2022 = [
#    'min_dist_to_college', 'Forest Area_om', 'BikeFac_hm', 'Intersection_Density_om', 'Path_hm', 'employment_density_om', 
#    'Distance to Water Body', 'Bicycle Parking_om', 'Intersection_Density_hm', 'Distance_to_Water_Body_mi', 
#    'Point Bridge_hm', 'Footway_hm', 'Industrial Area_om', 'HH_density_hm', 'Residential_Road_hm', 
#    'sep_bikeway_om', 'Distance to forest', 'edgeUID', 'Residential_Area_om', 'min_dist_to_park', 'University_hm', 
#    'Bus Stops_hm', 'Student Access_hm', 'pct_African_American_hm', 'Distance to Grass Center', 'Bike_Commuter_om', 
#    'Bike_Commuter_hm', 'Residential_Road_om', 'BikeFac_onstreet_om', 'Water Area_om', 'population_density_om', 
#    'population_density_hm', 'footway_binary', 'Point Bridge_om', 'Tertiary_om', 'lanes_om', 'Primary_hm', 
#    'Number of jobs_hm', 'University_om', 'pct_white_hm', 'cycleway_track_all_hm', 'avg_slope_hm', 'lanes_hm', 
#    'BikeFac_onstreet_hm', 'Bicycle Parking_hm', 'employment_density_hm', 'Bus Stops_om', 'min_dist_to_city_mi', 
#    'Secondary_hm', 'Footway_om', 'Secondary_om', 'Distance to Residential Area', 'Median_HH_income_hm', 
#    'Cycleway_om', 'pct_female_hm', 'uni_count_om', 'HH_density_om', 'adb', 'college_hm',
#    '_osmId', 'Median_HH_income_om', 'Water Area_hm', 'avg_slope_om', 'Student Access_om', 
#    'Cycleway_hm', 'Distance to Residential Center'
#]

    
# aadb target - 2022 - yearly and df1 - correlation + rf
#strava_features_2022 = [ 
#        'AADBT', 'aadb2',  'aadb1', 
#    'log_stv_nc_adb', 'stv_adb', 'stv_c_adb',  'stv_nc_adb', 'valid_days_year', 'log_stv_adb', 'log_stv_c_adb'
#]
    
#-----------------------------------------------------------------------------------------------------------

#3
# (daily + df) (aadb target)

# aadb target - 2019 - daily and df1 - correlation + rf
#strava_static_features_2019 = [ 
#    'Median_HH_income_om', 'Tertiary_om', 'population_density_om', 'Residential_Area_hm', 
#    'cycleway_lane_all_om', 'Student Access_hm', 'Point Bridge_hm', 'Bike_Commuter_hm', 'Cycleway_hm', 
#    'cycleway_lane_binary', 'Intersection_Density_om', '_osmId', 'Water Area_om', 'pct_male_om', 
#    'maj_uni_count_om', 'min_dist_to_city', 'employment_density_hm', 'cycleway_track_all_om', 
#    'uni_count_om', 'min_dist_to_maj_uni', 'Number of jobs_hm', 'Footway_hm', 'cycleway_track_all_hm', 'BikeFac_om', 
#    'Residential_Area_om', 'Commercial Area_om', 'Primary_hm', 'Retail Area_om', 'Maj University_om', 'footway_binary', 
#    'Secondary_hm', 'Distance to Water Body', 'Primary_om', 'Secondary_om', 
#    'pct_at_least_college_education_om', 'Point Bridge_om', 'Bike_Commuter_om', 'avg_slope_hm', 'Residential_Road_om', 
#    'point_slope_hm', 'Footway_om', 'pct_at_least_college_education_hm', 'BikeFac_onstreet_om', 'Median Age_hm', 
#    'Median Age_om', 'Water Area_hm', 'pct_female_om', 'cycleway_lane_all_hm', 'Path_hm', 'School_om', 
#    'Park_acres_om', 'Tertiary_hm', 'Cycleway_om', 'site_id', 'Distance to Park', 'college_hm', 
#    'Distance to Industrial Center', 'avg_slope_om', 'Distance to Commercial Area', 
#    'Distance to Retail Area', 'School_hm', 'University_om', 'Bus Stops_om', 'min_dist_to_school', 
#    'Distance_to_Water_Body_mi', 'Bus Stops_hm', 'Retail Area_hm', 'Student Access_om', 'Path_om',
#    'Distance to Commercial Area Center', 'pct_female_hm', 'Median_HH_income_hm', 'BikeFac_hm', 
#    'Bicycle Parking_om', 'uni_count_hm', 'Commercial Area_hm', 'min_dist_to_city_mi', 'Residential_Road_hm', 
#    'Intersection_Density_hm', 'employment_density_om', 'Number of jobs_om', 'HH_density_om', 'BikeFac_onstreet_hm', 
#    'Distance to Grass Center', 'Forest Area_hm', 'University_hm', 'min_dist_to_university', 
#    'min_dist_to_college',
#    'n_links',  'Counts', 'stv_c_daily', 'stv_daily'
#]

#      'aadb2', 'aadb', 'aadb1', 
#    'stv_adb', 'log_stv_nc_adb', 'log_stv_adb', 'stv_c_adb', 'log_stv_c_adb', 'stv_nc_adb', 'adb', 
    
#static_features_2019 = [ 
#    'Median_HH_income_om', 'Tertiary_om', 'population_density_om', 'Residential_Area_hm', 
#    'cycleway_lane_all_om', 'Student Access_hm', 'Point Bridge_hm', 'Bike_Commuter_hm', 'Cycleway_hm', 
#    'cycleway_lane_binary', 'Intersection_Density_om', '_osmId', 'Water Area_om', 'pct_male_om', 
#    'maj_uni_count_om', 'min_dist_to_city', 'employment_density_hm', 'cycleway_track_all_om', 
#    'uni_count_om', 'min_dist_to_maj_uni', 'Number of jobs_hm', 'Footway_hm', 'cycleway_track_all_hm', 'BikeFac_om', 
#    'Residential_Area_om', 'Commercial Area_om', 'Primary_hm', 'Retail Area_om', 'Maj University_om', 'footway_binary', 
#    'Secondary_hm', 'Distance to Water Body', 'Primary_om', 'Secondary_om', 
#    'pct_at_least_college_education_om', 'Point Bridge_om', 'Bike_Commuter_om', 'avg_slope_hm', 'Residential_Road_om', 
#    'point_slope_hm', 'Footway_om', 'pct_at_least_college_education_hm', 'BikeFac_onstreet_om', 'Median Age_hm', 
#    'Median Age_om', 'Water Area_hm', 'pct_female_om', 'cycleway_lane_all_hm', 'Path_hm', 'School_om', 
#    'Park_acres_om', 'Tertiary_hm', 'Cycleway_om', 'site_id', 'Distance to Park', 'college_hm', 
#    'Distance to Industrial Center', 'avg_slope_om', 'Distance to Commercial Area', 
#    'Distance to Retail Area', 'School_hm', 'University_om', 'Bus Stops_om', 'min_dist_to_school', 
#    'Distance_to_Water_Body_mi', 'Bus Stops_hm', 'Retail Area_hm', 'Student Access_om', 'Path_om',
#    'Distance to Commercial Area Center', 'pct_female_hm', 'Median_HH_income_hm', 'BikeFac_hm', 
#    'Bicycle Parking_om', 'uni_count_hm', 'Commercial Area_hm', 'min_dist_to_city_mi', 'Residential_Road_hm', 
#    'Intersection_Density_hm', 'employment_density_om', 'Number of jobs_om', 'HH_density_om', 'BikeFac_onstreet_hm', 
#    'Distance to Grass Center', 'Forest Area_hm', 'University_hm', 'min_dist_to_university', 
#    'min_dist_to_college'
#]
    
#strava_features_2019 = [ 
#    'n_links',  'Counts', 'stv_c_daily', 'stv_daily',
#    'aadb1', 'aadb',  'aadb2',
#    'valid_year', 'stv_nc_adb', 'stv_adb', 'log_stv_adb',  'stv_c_adb', 'adb',  'valid_months', 'log_stv_c_adb', 'reg_num'
#]

# aadb target - 2022 - daily and df1 - correlation + rf
#strava_static_features_2022 = [ 
#    'min_dist_to_college', 'University_hm', 'pct_at_least_college_education_om', 'Commercial Area_om', 
#    'uni_count_hm', 'Bus Stops_om', 'sep_bikeway_hm', 'pct_male_om', 'Cycleway_hm', 'Path_hm', 
#    'BikeFac_onstreet_hm', 'Median_HH_income_hm', 'Point Bridge_om', 'bridge_hm', 'Median Age_hm', 
#    'Bus Stops_hm', 'School_om', 'Residential_Area_hm', 'Bicycle Parking_om', 'Distance to Residential Area', 'Path_om', 
#    'Student Access_hm', 'pct_African_American_hm', 'population_density_om', 
#    'footway_binary', 'Footway_hm', 'employment_density_om', 'Water Area_om', 'Residential_Road_om', 'region', 
#    'Tertiary_hm', 'Intersection_Density_om', 'Student Access_om', 'uni_count_om', 'lanes_om', 
#    'Distance to Water Center', 'sep_bikeway_om', 'Bike_Commuter_om', 'HH_density_hm', 'pct_at_least_college_education_hm', 
#    'cycleway_track_all_hm', 'Number of jobs_hm', 'min_dist_to_school', '_osmId', 
#    'site_id', 'Median_HH_income_om', 'population_density_hm', 'cycleway_track_all_om',  
#    'lanes_hm', 'BikeFac_hm', 'HH_density_om', 'University_om', 'Secondary_hm', 'Intersection_Density_hm', 
#    'pct_African_American_om', 'Primary_om', 'Distance to Retail Area', 'Cycleway_om',
#    'min_dist_to_maj_uni', 'BikeFac_onstreet_om', 'cycleway_lane_all_hm', 'Water Area_hm', 'Footway_om', 
#    'Bicycle Parking_hm', 'Retail Area_om', 'employment_density_hm', 'Point Bridge_hm', 'Secondary_om', 'Bike_Commuter_hm',
#    'aadb1', 'aadb2', 'aadb',  
#    'stv_daily',  'stv_c_daily', 'Counts', 'n_links'
#]

#     'stv_nc_adb', 'stv_c_adb',  'adb', 'log_stv_nc_adb', 'stv_adb', 'log_stv_c_adb', 'reg_num', 'log_stv_adb', 'valid_months',
#     'valid_days_year',

#static_features_2022 = [ 
#    'min_dist_to_college', 'University_hm', 'pct_at_least_college_education_om', 'Commercial Area_om', 
#    'uni_count_hm', 'Bus Stops_om', 'sep_bikeway_hm', 'pct_male_om', 'Cycleway_hm', 'Path_hm', 
#    'BikeFac_onstreet_hm', 'Median_HH_income_hm', 'Point Bridge_om', 'bridge_hm', 'Median Age_hm', 
#    'Bus Stops_hm', 'School_om', 'Residential_Area_hm', 'Bicycle Parking_om', 'Distance to Residential Area', 'Path_om', 
#    'Student Access_hm', 'pct_African_American_hm', 'population_density_om', 
#    'footway_binary', 'Footway_hm', 'employment_density_om', 'Water Area_om', 'Residential_Road_om', 'region', 
#    'Tertiary_hm', 'Intersection_Density_om', 'Student Access_om', 'uni_count_om', 'lanes_om', 
#    'Distance to Water Center', 'sep_bikeway_om', 'Bike_Commuter_om', 'HH_density_hm', 'pct_at_least_college_education_hm', 
#    'cycleway_track_all_hm', 'Number of jobs_hm', 'min_dist_to_school', '_osmId', 
#    'site_id', 'Median_HH_income_om', 'population_density_hm', 'cycleway_track_all_om',  
#    'lanes_hm', 'BikeFac_hm', 'HH_density_om', 'University_om', 'Secondary_hm', 'Intersection_Density_hm', 
#    'pct_African_American_om', 'Primary_om', 'Distance to Retail Area', 'Cycleway_om',
#    'min_dist_to_maj_uni', 'BikeFac_onstreet_om', 'cycleway_lane_all_hm', 'Water Area_hm', 'Footway_om', 
#    'Bicycle Parking_hm', 'Retail Area_om', 'employment_density_hm', 'Point Bridge_hm', 'Secondary_om', 'Bike_Commuter_hm'
#]

#strava_features_2022 = [ 
#    'stv_daily',  'stv_c_daily', 'Counts', 'n_links',
#    'aadb1', 'aadb',  'aadb2', 
#    'valid_year', 'stv_nc_adb', 'stv_adb', 'log_stv_adb',  'stv_c_adb', 'adb',  'valid_months', 'log_stv_c_adb', 'reg_num'
#]

#-----------------------------------------------------------------------------------------------------------
#4

#all-daily
strava_static_features_2019 = [
    'site_id', 'site_name.x', 
    'primary_binary', 'secondary_binary', 'tertiary_binary', 'residential_binary', 
    'path_binary', 'cycleway_binary', 'footway_binary', 'cycleway_lane_binary', 'cycleway_track_all_binary', 'site_name.y',
    'edgeUID', '_osmId', 'min_dist_to_city', 'min_dist_to_park', 'min_dist_to_polygon', 'min_dist_to_school', 'min_dist_to_college', 
    'min_dist_to_university', 'min_dist_to_maj_uni', 'lanes_hm,maxspeed_hm', 'Intersection_Density_hm', 'Commercial Area_hm',
   'Distance to Commercial Area', 'Distance to Commercial Area Center', 'Industrial Area_hm', 'Distance to Industrial Area', 
    'Distance to Industrial Center', 'Residential_Area_hm', 'Distance to Residential Area', 'Distance to Residential Center', 
    'Retail Area_hm', 'Distance to Retail Area', 'Distance to Retail Center', 'Grass Area_hm', 'Distance to Grass', 
    'Distance to Grass Center', 'Park Area_hm', 'Distance to Park', 'Distance to Park Center', 'Water Area_hm', 
    'Distance to Water Body', 'Distance to Water Center', 'Forest Area_hm', 'Distance to forest', 
    'Distance to Forest Center', 'Bicycle Parking_hm', 'Bus Stops_hm', 'School_hm', 'college_hm', 'uni_count_hm', 
    'University_hm', 'maj_uni_count_hm', 'Maj University_hm', 'Primary_hm', 'Secondary_hm', 'Tertiary_hm', 
    'Residential_Road_hm', 'Path_hm', 'Cycleway_hm', 'Footway_hm', 'cycleway_lane_all_hm', 'cycleway_track_all_hm', 
    'Point Speed_hm', 'bridge_hm', 'Point Bridge_hm', 'pct_white_hm', 'pct_African_American_hm', 'pct_male_hm', 
    'pct_female_hm', 'Student Access_hm', 'pct_at_least_college_education_hm', 'Median Age_hm', 'Median_HH_income_hm', 
    'HH_density_hm', 'population_density_hm', 'employment_density_hm', 'Number of jobs_hm', 'point_slope_hm', 'avg_slope_hm', 
    'lanes_om', 'maxspeed_om', 'Intersection_Density_om', 'Commercial Area_om', 'Industrial Area_om', 'Residential_Area_om', 
    'Retail Area_om', 'Grass Area_om', 'Park Area_om', 'Water Area_om', 'Forest Area_om', 'Bicycle Parking_om', 'Bus Stops_om', 
    'School_om', 'college_om', 'uni_count_om', 'University_om', 'maj_uni_count_om', 'Maj University_om', 'Primary_om',
    'Secondary_om', 'Tertiary_om', 'Residential_Road_om', 'Path_om', 'Cycleway_om', 'Footway_om', 'cycleway_lane_all_om', 
    'cycleway_track_all_om', 'Point Speed_om', 'bridge_om', 'Point Bridge_om', 'pct_white_om', 'pct_African_American_om', 
    'pct_male_om', 'pct_female_om', 'Student Access_om', 'pct_at_least_college_education_om', 'Median Age_om', 
    'Median_HH_income_om', 'HH_density_om', 'population_density_om', 'employment_density_om', 'Number of jobs_om', 
    'point_slope_om', 'avg_slope_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 'sep_bikeway_binary', 
    'sep_onstreet_binary', 'BikeFac_binary', 'sep_bikeway_hm', 'sep_bikeway_om', 'arterial_binary', 
    'arterial_no_bike_lane_binary', 'primary_no_bike_lane_binary', 'secondary_no_bike_lane_binary', 
    'tertiary_no_bike_lane_binary', 'primary_bike_lane_binary', 'secondary_bike_lane_binary', 'tertiary_bike_lane_binary', 
    'BikeFac_hm', 'BikeFac_om', 'BikeFac_onstreet_hm', 'BikeFac_onstreet_om', 'school_college_hm', 
    'Park_acres_om', 'Park_acres_hm', 'min_dist_to_city_mi', 
    'Distance_to_Water_Body_mi', 'region',
    'site_id', 'Date', 'year', 'month', 'dayofweek', 'weekday', 'hourly_flg', 'zero_flg', 'nonzero_flg', 'daily_flg', 
    'adb_flg1', 'adb_flg2', 'Hourly_Counts_N', 'Counts', 'valid_day', 'review_flg', 'stv_daily', 'stv_c_daily', 'n_links'
]

#all-daily
static_features_2019 = [
    'site_id', 'site_name.x', 
    'primary_binary', 'secondary_binary', 'tertiary_binary', 'residential_binary', 
    'path_binary', 'cycleway_binary', 'footway_binary', 'cycleway_lane_binary', 'cycleway_track_all_binary', 'site_name.y',
    'edgeUID', '_osmId', 'min_dist_to_city', 'min_dist_to_park', 'min_dist_to_polygon', 'min_dist_to_school', 'min_dist_to_college', 
    'min_dist_to_university', 'min_dist_to_maj_uni', 'lanes_hm,maxspeed_hm', 'Intersection_Density_hm', 'Commercial Area_hm',
   'Distance to Commercial Area', 'Distance to Commercial Area Center', 'Industrial Area_hm', 'Distance to Industrial Area', 
    'Distance to Industrial Center', 'Residential_Area_hm', 'Distance to Residential Area', 'Distance to Residential Center', 
    'Retail Area_hm', 'Distance to Retail Area', 'Distance to Retail Center', 'Grass Area_hm', 'Distance to Grass', 
    'Distance to Grass Center', 'Park Area_hm', 'Distance to Park', 'Distance to Park Center', 'Water Area_hm', 
    'Distance to Water Body', 'Distance to Water Center', 'Forest Area_hm', 'Distance to forest', 
    'Distance to Forest Center', 'Bicycle Parking_hm', 'Bus Stops_hm', 'School_hm', 'college_hm', 'uni_count_hm', 
    'University_hm', 'maj_uni_count_hm', 'Maj University_hm', 'Primary_hm', 'Secondary_hm', 'Tertiary_hm', 
    'Residential_Road_hm', 'Path_hm', 'Cycleway_hm', 'Footway_hm', 'cycleway_lane_all_hm', 'cycleway_track_all_hm', 
    'Point Speed_hm', 'bridge_hm', 'Point Bridge_hm', 'pct_white_hm', 'pct_African_American_hm', 'pct_male_hm', 
    'pct_female_hm', 'Student Access_hm', 'pct_at_least_college_education_hm', 'Median Age_hm', 'Median_HH_income_hm', 
    'HH_density_hm', 'population_density_hm', 'employment_density_hm', 'Number of jobs_hm', 'point_slope_hm', 'avg_slope_hm', 
    'lanes_om', 'maxspeed_om', 'Intersection_Density_om', 'Commercial Area_om', 'Industrial Area_om', 'Residential_Area_om', 
    'Retail Area_om', 'Grass Area_om', 'Park Area_om', 'Water Area_om', 'Forest Area_om', 'Bicycle Parking_om', 'Bus Stops_om', 
    'School_om', 'college_om', 'uni_count_om', 'University_om', 'maj_uni_count_om', 'Maj University_om', 'Primary_om',
    'Secondary_om', 'Tertiary_om', 'Residential_Road_om', 'Path_om', 'Cycleway_om', 'Footway_om', 'cycleway_lane_all_om', 
    'cycleway_track_all_om', 'Point Speed_om', 'bridge_om', 'Point Bridge_om', 'pct_white_om', 'pct_African_American_om', 
    'pct_male_om', 'pct_female_om', 'Student Access_om', 'pct_at_least_college_education_om', 'Median Age_om', 
    'Median_HH_income_om', 'HH_density_om', 'population_density_om', 'employment_density_om', 'Number of jobs_om', 
    'point_slope_om', 'avg_slope_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 'sep_bikeway_binary', 
    'sep_onstreet_binary', 'BikeFac_binary', 'sep_bikeway_hm', 'sep_bikeway_om', 'arterial_binary', 
    'arterial_no_bike_lane_binary', 'primary_no_bike_lane_binary', 'secondary_no_bike_lane_binary', 
    'tertiary_no_bike_lane_binary', 'primary_bike_lane_binary', 'secondary_bike_lane_binary', 'tertiary_bike_lane_binary', 
    'BikeFac_hm', 'BikeFac_om', 'BikeFac_onstreet_hm', 'BikeFac_onstreet_om', 'school_college_hm', 
    'Park_acres_om', 'Park_acres_hm', 'min_dist_to_city_mi', 
    'Distance_to_Water_Body_mi', 'region'
]

#all-daily
strava_features_2019 = [
    'site_id', 'Date', 'month', 'dayofweek', 'weekday', 'hourly_flg', 'zero_flg', 'nonzero_flg', 'daily_flg', 'adb_flg1',
    'adb_flg2', 'Hourly_Counts_N', 'Counts', 'valid_day', 'review_flg', 'stv_daily', 'stv_c_daily', 'n_links'
]

#all-daily
strava_static_features_2022 = [
    'site_id', 'site_name.x', 
    'primary_binary', 'secondary_binary', 'tertiary_binary', 'residential_binary', 
    'path_binary', 'cycleway_binary', 'footway_binary', 'cycleway_lane_binary', 'cycleway_track_all_binary', 'site_name.y',
    'edgeUID', '_osmId', 'min_dist_to_city', 'min_dist_to_park', 'min_dist_to_polygon', 'min_dist_to_school', 'min_dist_to_college', 
    'min_dist_to_university', 'min_dist_to_maj_uni', 'lanes_hm,maxspeed_hm', 'Intersection_Density_hm', 'Commercial Area_hm',
   'Distance to Commercial Area', 'Distance to Commercial Area Center', 'Industrial Area_hm', 'Distance to Industrial Area', 
    'Distance to Industrial Center', 'Residential_Area_hm', 'Distance to Residential Area', 'Distance to Residential Center', 
    'Retail Area_hm', 'Distance to Retail Area', 'Distance to Retail Center', 'Grass Area_hm', 'Distance to Grass', 
    'Distance to Grass Center', 'Park Area_hm', 'Distance to Park', 'Distance to Park Center', 'Water Area_hm', 
    'Distance to Water Body', 'Distance to Water Center', 'Forest Area_hm', 'Distance to forest', 
    'Distance to Forest Center', 'Bicycle Parking_hm', 'Bus Stops_hm', 'School_hm', 'college_hm', 'uni_count_hm', 
    'University_hm', 'maj_uni_count_hm', 'Maj University_hm', 'Primary_hm', 'Secondary_hm', 'Tertiary_hm', 
    'Residential_Road_hm', 'Path_hm', 'Cycleway_hm', 'Footway_hm', 'cycleway_lane_all_hm', 'cycleway_track_all_hm', 
    'Point Speed_hm', 'bridge_hm', 'Point Bridge_hm', 'pct_white_hm', 'pct_African_American_hm', 'pct_male_hm', 
    'pct_female_hm', 'Student Access_hm', 'pct_at_least_college_education_hm', 'Median Age_hm', 'Median_HH_income_hm', 
    'HH_density_hm', 'population_density_hm', 'employment_density_hm', 'Number of jobs_hm', 'point_slope_hm', 'avg_slope_hm', 
    'lanes_om', 'maxspeed_om', 'Intersection_Density_om', 'Commercial Area_om', 'Industrial Area_om', 'Residential_Area_om', 
    'Retail Area_om', 'Grass Area_om', 'Park Area_om', 'Water Area_om', 'Forest Area_om', 'Bicycle Parking_om', 'Bus Stops_om', 
    'School_om', 'college_om', 'uni_count_om', 'University_om', 'maj_uni_count_om', 'Maj University_om', 'Primary_om',
    'Secondary_om', 'Tertiary_om', 'Residential_Road_om', 'Path_om', 'Cycleway_om', 'Footway_om', 'cycleway_lane_all_om', 
    'cycleway_track_all_om', 'Point Speed_om', 'bridge_om', 'Point Bridge_om', 'pct_white_om', 'pct_African_American_om', 
    'pct_male_om', 'pct_female_om', 'Student Access_om', 'pct_at_least_college_education_om', 'Median Age_om', 
    'Median_HH_income_om', 'HH_density_om', 'population_density_om', 'employment_density_om', 'Number of jobs_om', 
    'point_slope_om', 'avg_slope_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 'sep_bikeway_binary', 
    'sep_onstreet_binary', 'BikeFac_binary', 'sep_bikeway_hm', 'sep_bikeway_om', 'arterial_binary', 
    'arterial_no_bike_lane_binary', 'primary_no_bike_lane_binary', 'secondary_no_bike_lane_binary', 
    'tertiary_no_bike_lane_binary', 'primary_bike_lane_binary', 'secondary_bike_lane_binary', 'tertiary_bike_lane_binary', 
    'BikeFac_hm', 'BikeFac_om', 'BikeFac_onstreet_hm', 'BikeFac_onstreet_om', 'school_college_hm', 
    'Park_acres_om', 'Park_acres_hm', 'min_dist_to_city_mi', 
    'Distance_to_Water_Body_mi', 'region',
    'site_id', 'Date', 'year', 'month', 'dayofweek', 'weekday', 'hourly_flg', 'zero_flg', 'nonzero_flg', 'daily_flg', 
    'adb_flg1', 'adb_flg2', 'Hourly_Counts_N', 'Counts', 'valid_day', 'review_flg', 'stv_daily', 'stv_c_daily', 'n_links'
]

# daily
#site_id,site_name,Date,year,month,dayofweek,weekday,hourly_flg,zero_flg,nonzero_flg,daily_flg,adb_flg1,adb_flg2,
# Hourly_Counts_N,Counts,valid_day,review_flg,stv_daily,stv_c_daily,n_links

#all-daily
static_features_2022 = [
    'site_id', 'site_name.x', 
    'primary_binary', 'secondary_binary', 'tertiary_binary', 'residential_binary', 
    'path_binary', 'cycleway_binary', 'footway_binary', 'cycleway_lane_binary', 'cycleway_track_all_binary', 'site_name.y',
    'edgeUID', '_osmId', 'min_dist_to_city', 'min_dist_to_park', 'min_dist_to_polygon', 'min_dist_to_school', 'min_dist_to_college', 
    'min_dist_to_university', 'min_dist_to_maj_uni', 'lanes_hm,maxspeed_hm', 'Intersection_Density_hm', 'Commercial Area_hm',
   'Distance to Commercial Area', 'Distance to Commercial Area Center', 'Industrial Area_hm', 'Distance to Industrial Area', 
    'Distance to Industrial Center', 'Residential_Area_hm', 'Distance to Residential Area', 'Distance to Residential Center', 
    'Retail Area_hm', 'Distance to Retail Area', 'Distance to Retail Center', 'Grass Area_hm', 'Distance to Grass', 
    'Distance to Grass Center', 'Park Area_hm', 'Distance to Park', 'Distance to Park Center', 'Water Area_hm', 
    'Distance to Water Body', 'Distance to Water Center', 'Forest Area_hm', 'Distance to forest', 
    'Distance to Forest Center', 'Bicycle Parking_hm', 'Bus Stops_hm', 'School_hm', 'college_hm', 'uni_count_hm', 
    'University_hm', 'maj_uni_count_hm', 'Maj University_hm', 'Primary_hm', 'Secondary_hm', 'Tertiary_hm', 
    'Residential_Road_hm', 'Path_hm', 'Cycleway_hm', 'Footway_hm', 'cycleway_lane_all_hm', 'cycleway_track_all_hm', 
    'Point Speed_hm', 'bridge_hm', 'Point Bridge_hm', 'pct_white_hm', 'pct_African_American_hm', 'pct_male_hm', 
    'pct_female_hm', 'Student Access_hm', 'pct_at_least_college_education_hm', 'Median Age_hm', 'Median_HH_income_hm', 
    'HH_density_hm', 'population_density_hm', 'employment_density_hm', 'Number of jobs_hm', 'point_slope_hm', 'avg_slope_hm', 
    'lanes_om', 'maxspeed_om', 'Intersection_Density_om', 'Commercial Area_om', 'Industrial Area_om', 'Residential_Area_om', 
    'Retail Area_om', 'Grass Area_om', 'Park Area_om', 'Water Area_om', 'Forest Area_om', 'Bicycle Parking_om', 'Bus Stops_om', 
    'School_om', 'college_om', 'uni_count_om', 'University_om', 'maj_uni_count_om', 'Maj University_om', 'Primary_om',
    'Secondary_om', 'Tertiary_om', 'Residential_Road_om', 'Path_om', 'Cycleway_om', 'Footway_om', 'cycleway_lane_all_om', 
    'cycleway_track_all_om', 'Point Speed_om', 'bridge_om', 'Point Bridge_om', 'pct_white_om', 'pct_African_American_om', 
    'pct_male_om', 'pct_female_om', 'Student Access_om', 'pct_at_least_college_education_om', 'Median Age_om', 
    'Median_HH_income_om', 'HH_density_om', 'population_density_om', 'employment_density_om', 'Number of jobs_om', 
    'point_slope_om', 'avg_slope_om', 'Bike_Commuter_hm', 'Bike_Commuter_om', 'sep_bikeway_binary', 
    'sep_onstreet_binary', 'BikeFac_binary', 'sep_bikeway_hm', 'sep_bikeway_om', 'arterial_binary', 
    'arterial_no_bike_lane_binary', 'primary_no_bike_lane_binary', 'secondary_no_bike_lane_binary', 
    'tertiary_no_bike_lane_binary', 'primary_bike_lane_binary', 'secondary_bike_lane_binary', 'tertiary_bike_lane_binary', 
    'BikeFac_hm', 'BikeFac_om', 'BikeFac_onstreet_hm', 'BikeFac_onstreet_om', 'school_college_hm', 
    'Park_acres_om', 'Park_acres_hm', 'min_dist_to_city_mi', 
    'Distance_to_Water_Body_mi', 'region'
]

#all-daily
strava_features_2022 = [
    'site_id', 'Date', 'month', 'dayofweek', 'weekday', 'hourly_flg', 'zero_flg', 'nonzero_flg', 'daily_flg', 'adb_flg1',
    'adb_flg2', 'Hourly_Counts_N', 'Counts', 'valid_day', 'review_flg', 'stv_daily', 'stv_c_daily', 'n_links'
]

# 'aadb1', 'aadb', 'aadb2', 'AADBT', 
# 'adb', 'stv_adb', 'stv_c_adb', 'stv_nc_adb', 'log_stv_adb', 'log_stv_c_adb', 'log_stv_nc_adb', 'site_name', 'year', 
# ' valid_months', 'valid_days_year', 'valid_year', 'reg_num', 

#    'site_name', 'year', 'month', 'valid_days', 'valid_dayofweek', 'Counts', 'valid_month', 'madb', 
#    'stv_monthly', 'stv_c_monthly', 'n_links' 

# daily
#site_id,site_name,Date,year,month,dayofweek,weekday,hourly_flg,zero_flg,nonzero_flg,daily_flg,adb_flg1,adb_flg2,
# Hourly_Counts_N,Counts,valid_day,review_flg,stv_daily,stv_c_daily,n_links
#-----------------------------------------------------------------------------------------------------------

# (monthly + df) (aadb target)

# aadb target - 2019 - monthly and df1 - correlation + rf
#strava_static_features_2019 = [
#    'Median Age_om', 'HH_density_hm', 'Number of jobs_hm', 'Distance to Grass', 'Counts', 
#    'Distance_to_Water_Body_mi', 'Cycleway_hm', 'BikeFac_hm', 'Commercial Area_om', 
#    'cycleway_track_all_hm', 'Student Access_hm', 'Point Bridge_hm', 'Bus Stops_om', 'cycleway_lane_all_om', 
#    'Secondary_hm', 'avg_slope_om', 'madb', 'School_om', 'Commercial Area_hm', 'Retail Area_hm', 'Median Age_hm', 
#    'uni_count_om', 'Intersection_Density_hm', 'cycleway_binary', 'Water Area_om', 'Retail Area_om', 
#    'Primary_om', 'population_density_om', 'min_dist_to_maj_uni', 'Path_om', 'Intersection_Density_om', 
#    'Bus Stops_hm', 'Residential_Area_hm', 'school_college_hm', 'BikeFac_onstreet_hm', 'population_density_hm', 
#    'Water Area_hm', 'Primary_hm', 'University_om', 'Residential_Road_hm', 'Number of jobs_om', 'avg_slope_hm', 
#    'stv_c_monthly', 'employment_density_hm', 'footway_binary',
#    'Tertiary_hm', 'Cycleway_om', 'stv_monthly', 'University_hm', 'cycleway_lane_binary', 'pct_male_om', 'Tertiary_om', 
#    'Bike_Commuter_hm', 'Bicycle Parking_om', 'pct_African_American_om', 'Distance to Commercial Area Center', 
#    'Footway_om', 'cycleway_track_all_om', '_osmId', 'BikeFac_onstreet_om', 'Student Access_om', 'Distance to Water Body', 
#    'employment_density_om', 'Distance to Commercial Area', 'maj_uni_count_om', 'Maj University_om', 'Median_HH_income_om', 
#    'Distance to Industrial Area', 'cycleway_lane_all_hm', 'Residential_Area_om', 'min_dist_to_college', 
#    'BikeFac_binary', 'Secondary_om', 'sep_bikeway_om', 'HH_density_om', 'BikeFac_om', 'min_dist_to_city', 'Footway_hm', 
#    'Point Bridge_om', 'pct_female_om', 'Forest Area_om', 'Bike_Commuter_om', 'min_dist_to_university', 'Path_hm', 
#    'uni_count_hm'
#]

# site_id

# 'aadb1', 'aadb2', 'AADBT', 
# 'log_stv_c_adb', 'stv_c_adb', 'log_stv_nc_adb', 'adb', 'stv_adb', 'log_stv_adb', 'stv_nc_adb',


# aadb target - 2019 - monthly and df1 - correlation + rf
#static_features_2019 = [
#    'Median Age_om', 'HH_density_hm', 'Number of jobs_hm', 'Distance to Grass', 
#    'Distance_to_Water_Body_mi', 'Cycleway_hm', 'BikeFac_hm', 'Commercial Area_om', 
#    'cycleway_track_all_hm', 'Student Access_hm', 'Point Bridge_hm', 'Bus Stops_om', 'cycleway_lane_all_om', 
#    'Secondary_hm', 'avg_slope_om', 'School_om', 'Commercial Area_hm', 'Retail Area_hm', 'Median Age_hm', 
#    'uni_count_om', 'Intersection_Density_hm', 'cycleway_binary', 'Water Area_om', 'Retail Area_om', 
#    'Primary_om', 'population_density_om', 'min_dist_to_maj_uni', 'Path_om', 'Intersection_Density_om', 
#    'Bus Stops_hm', 'Residential_Area_hm', 'school_college_hm', 'BikeFac_onstreet_hm', 'population_density_hm', 
#    'Water Area_hm', 'Primary_hm', 'University_om', 'Residential_Road_hm', 'Number of jobs_om', 'avg_slope_hm', 
#    'employment_density_hm', 'footway_binary', 
#    'Tertiary_hm', 'Cycleway_om', 'University_hm', 'cycleway_lane_binary', 'pct_male_om', 'Tertiary_om', 
#    'Bike_Commuter_hm', 'Bicycle Parking_om', 'pct_African_American_om', 'Distance to Commercial Area Center', 
#    'Footway_om', 'cycleway_track_all_om', '_osmId', 'BikeFac_onstreet_om', 'Student Access_om', 'Distance to Water Body', 
#    'employment_density_om', 'Distance to Commercial Area', 'maj_uni_count_om', 'Maj University_om', 'Median_HH_income_om', 
#    'Distance to Industrial Area', 'cycleway_lane_all_hm', 'Residential_Area_om', 'min_dist_to_college', 
#    'BikeFac_binary', 'Secondary_om', 'sep_bikeway_om', 'HH_density_om', 'BikeFac_om', 'min_dist_to_city', 'Footway_hm', 
#    'Point Bridge_om', 'pct_female_om', 'Forest Area_om', 'Bike_Commuter_om', 'min_dist_to_university', 'Path_hm', 
#    'uni_count_hm'
#]

# site_id

# 'aadb1', 'AADBT', 'aadb2', 
# 'adb', 'log_stv_c_adb', 'stv_c_adb', 'log_stv_nc_adb', 'stv_adb', 'stv_nc_adb', 'log_stv_adb', 
# 'Counts', 'stv_monthly', 'stv_c_monthly', 'madb', 


# yearly
# site_id, site_name, year, valid_months, valid_days_year, adb, aadb1, valid_year, aadb2, aadb, reg_num, stv_adb, stv_c_adb


# monthly
# site_id, site_name, year, month, valid_days, valid_dayofweek, Counts, valid_month, madb, stv_monthly, stv_c_monthly,
# n_links

# aadb target - 2019 - monthly and df1 - correlation + rf
#strava_features_2019 = [
#    'adb', 'log_stv_c_adb', 'stv_c_adb', 'log_stv_nc_adb', 'stv_adb', 'stv_nc_adb', 'log_stv_adb',
#    'reg_num', 'valid_days_year'
#]

#    'site_id'

# aadb target - 2022 - monthly and df1 - correlation + rf
#strava_static_features_2022 = [
#    'School_om', 'Bus Stops_om', 'avg_slope_hm', 'Bus Stops_hm', 'HH_density_hm', 'Path_om', 'Secondary_hm', 
#    'Water Area_hm', '_osmId', 'cycleway_lane_all_hm', 'Distance to Commercial Area Center', 
#    'Residential_Road_om', 'Distance to Water Center', 'Student Access_hm', 'Student Access_om',  
#    'employment_density_hm', 'HH_density_om', 'University_om', 'Forest Area_om', 
#    'Bicycle Parking_hm', 'employment_density_om', 'sep_bikeway_om', 'Point Bridge_hm', 
#    'population_density_hm', 'Footway_hm', 'region', 'BikeFac_onstreet_hm', 'pct_at_least_college_education_hm', 
#    'pct_female_hm', 'stv_c_monthly', 'Distance to Water Body', 'University_hm', 'Path_hm', 'Footway_om', 
#    'Water Area_om', 'min_dist_to_college', 'Median Age_hm', 'footway_binary', 'Cycleway_hm', 
#    'Counts', 'Number of jobs_hm', 'Bike_Commuter_om', 'min_dist_to_school', 'BikeFac_onstreet_om',  
#    'stv_monthly', 'lanes_om', 'Median_HH_income_hm', 'Bike_Commuter_hm', 'madb', 'Distance to Residential Area', 
#    'cycleway_track_all_om', 'Primary_om', 'Cycleway_om', 'Distance_to_Water_Body_mi', 'Distance to Residential Center', 
#    'population_density_om', 'Bicycle Parking_om', 'Median_HH_income_om', 'Secondary_om', 'cycleway_track_all_hm', 
#    'lanes_hm', 'Intersection_Density_om', 'min_dist_to_city_mi', 'Intersection_Density_hm', 'Residential_Area_om', 
#    'sep_bikeway_hm', 'Commercial Area_om', 'min_dist_to_polygon', 'Point Bridge_om', 'uni_count_om', 'uni_count_hm'
#    ]

# site_id

# 'AADBT', 'aadb1', 'aadb2', 
# 'log_stv_nc_adb', 'stv_nc_adb', 'adb', 'valid_days_year', 'log_stv_adb', 'log_stv_c_adb', 'stv_adb', 'stv_c_adb', 'reg_num', 


# aadb target - 2022 - monthly and df1 - correlation + rf
#static_features_2022 = [
#    'School_om', 'Bus Stops_om', 'avg_slope_hm', 'Bus Stops_hm', 'HH_density_hm', 'Path_om', 'Secondary_hm', 
#    'Water Area_hm', '_osmId', 'cycleway_lane_all_hm', 'Distance to Commercial Area Center', 
#    'Residential_Road_om', 'Distance to Water Center', 'Student Access_hm', 'Student Access_om', 
#    'employment_density_hm', 'HH_density_om', 'University_om', 'Forest Area_om',
#    'Bicycle Parking_hm', 'employment_density_om', 'sep_bikeway_om', 'Point Bridge_hm', 
#    'population_density_hm', 'Footway_hm', 'region', 'BikeFac_onstreet_hm', 'pct_at_least_college_education_hm', 
#    'pct_female_hm', 'Distance to Water Body', 'University_hm', 'Path_hm', 'Footway_om', 
#    'Water Area_om', 'min_dist_to_college', 'Median Age_hm', 'footway_binary', 'Cycleway_hm', 
#    'Number of jobs_hm', 'Bike_Commuter_om', 'min_dist_to_school', 'BikeFac_onstreet_om', 
#    'lanes_om', 'Median_HH_income_hm', 'Bike_Commuter_hm', 'Distance to Residential Area', 
#    'cycleway_track_all_om', 'Primary_om', 'Cycleway_om', 'Distance_to_Water_Body_mi', 'Distance to Residential Center', 
#    'population_density_om', 'Bicycle Parking_om', 'Median_HH_income_om', 'Secondary_om', 'cycleway_track_all_hm', 
#    'lanes_hm', 'Intersection_Density_om', 'min_dist_to_city_mi', 'Intersection_Density_hm', 'Residential_Area_om', 
#    'sep_bikeway_hm', 'Commercial Area_om', 'min_dist_to_polygon', 'Point Bridge_om', 'uni_count_om', 'uni_count_hm'
#    ]

#    'site_id'

# 'aadb2', 'AADBT',  'aadb1', 
# 'stv_adb', 'log_stv_c_adb', 'stv_nc_adb', 'log_stv_nc_adb', 'stv_c_adb', 'log_stv_adb', 'reg_num', 'adb', 'valid_days_year',
# 'stv_c_monthly', 'Counts', 'stv_monthly', 'madb', 

# yearly
# site_id, site_name, year, valid_months, valid_days_year, adb, aadb1, valid_year, aadb2, aadb, reg_num, stv_adb, stv_c_adb


# monthly
# site_id, site_name, year, month, valid_days, valid_dayofweek, Counts, valid_month, madb, stv_monthly, stv_c_monthly,
# n_links

# aadb target - 2022 - monthly and df1 - correlation + rf
#strava_features_2022 = [
#    'stv_adb', 'log_stv_c_adb', 'stv_nc_adb', 'log_stv_nc_adb', 'stv_c_adb', 'log_stv_adb', 'reg_num', 'adb', 'valid_days_year'
#    ]
# 'site_id'



# In[ ]:




