# `utils.py` contains utility functions that may be used by different scripts
# several times. There is quite a lot of repetition in how some of these plots
# are generated, so many functions were abstracted here to improve readability.

# Necessary imports
import csv
import pandas as pd
import numpy as np

# `init()` creates and returns a pandas DataFrame from the specific .csv file
# used in the 2022 study on air pollution.
def init():
   data = []
   with open('HOLC.all.20220304.csv') as input:
      for line in csv.DictReader(input, fieldnames = ('num',
                                                      'CUA',
                                                      'City',
                                                      'GEOID',
                                                      'grade',
                                                      'PHOLC',
                                                      'asian',
                                                      'black',
                                                      'hispanic',
                                                      'white',
                                                      'other',
                                                      'total',
                                                      'no2',
                                                      'pm25')):
         data.append(line)
   data.pop(0)

   cua      = []
   city     = []
   geo_id   = []
   grade    = []
   pholc    = []
   asian    = []
   black    = []
   hispanic = []
   white    = []
   other    = []
   total    = []
   no2      = []
   pm25     = []

   for entry in data:
      cua.append(entry['CUA'])
      city.append(entry['City'])
      geo_id.append(entry['GEOID'])
      grade.append(entry['grade'])
      pholc.append(entry['PHOLC'])
      asian.append(entry['asian'])
      black.append(entry['black'])
      hispanic.append(entry['hispanic'])
      white.append(entry['white'])
      other.append(entry['other'])
      total.append(entry['total'])
      no2.append(entry['no2'])
      pm25.append(entry['pm25'])

   df = pd.DataFrame({
      "CUA"      : cua,
      "City"     : city,
      "GEOID"    : geo_id,
      "Grade"    : grade,
      "PHOLC"    : pholc,
      "Asian"    : asian,
      "Black"    : black,
      "Hispanic" : hispanic,
      "White"    : white,
      "Other"    : other,
      "Total"    : total,
      "NO2"      : no2,
      "PM25"     : pm25
   })

   df['PHOLC']    = pd.to_numeric(df['PHOLC'])
   df['Asian']    = pd.to_numeric(df['Asian'])
   df['Black']    = pd.to_numeric(df['Black'])
   df['Hispanic'] = pd.to_numeric(df['Hispanic'])
   df['White']    = pd.to_numeric(df['White'])
   df['Other']    = pd.to_numeric(df['Other'])
   df['Total']    = pd.to_numeric(df['Total'])
   df['NO2']      = pd.to_numeric(df['NO2'])
   df['PM25']     = pd.to_numeric(df['PM25'])

   return df

# `calc_city_pwm()` returns a dictionary of all unique cities and their
# population-weighted mean level of air pollution measurement of interest.
def calc_city_pwm(target_city, all_cities, datapoint, pop):
   condition = ((all_cities == target_city) & (~np.isnan(datapoint)) & (~np.isnan(pop)))
   datapoint = datapoint[condition]
   pop = pop[condition]
   return np.average(datapoint, weights = pop)

# `collect_data()` parses the DataFrame and returns a list of lists containing
# air pollution levels by HOLC grade and race/ethnicity.
def collect_data(df, target, calc_diff):
   HOLC_A_data = []
   HOLC_B_data = []
   HOLC_C_data = []
   HOLC_D_data = []
   white       = []
   other       = []
   black       = []
   asian       = []
   hispanic    = []

   diff = "0"
   if calc_diff:
      cities = list(set(df['City']))
      pwms = {}
      for city in cities:
         pwms[city] = calc_city_pwm(city, df['City'], df[target], df['Total'])
      diff = "pwms[df['City'][i]]"

   for i in df.index:
      if df['Grade'][i] == 'A':
         HOLC_A_data += (round(df['PHOLC'][i] * df['Total'][i]) * [(df[target][i]) - eval(diff)])
      if df['Grade'][i] == 'B':
         HOLC_B_data += (round(df['PHOLC'][i] * df['Total'][i]) * [(df[target][i]) - eval(diff)])
      if df['Grade'][i] == 'C':
         HOLC_C_data += (round(df['PHOLC'][i] * df['Total'][i]) * [(df[target][i]) - eval(diff)])
      if df['Grade'][i] == 'D':
         HOLC_D_data += (round(df['PHOLC'][i] * df['Total'][i]) * [(df[target][i]) - eval(diff)])
      if df['Grade'][i] != 'N':
         white += (round(df['PHOLC'][i] * df['White'][i]) * [(df[target][i]) - eval(diff)])
         other += (round(df['PHOLC'][i] * df['Other'][i]) * [(df[target][i]) - eval(diff)])
         black += (round(df['PHOLC'][i] * df['Black'][i]) * [(df[target][i]) - eval(diff)])
         asian += (round(df['PHOLC'][i] * df['Asian'][i]) * [(df[target][i]) - eval(diff)])
         hispanic += (round(df['PHOLC'][i] * df['Hispanic'][i]) * [(df[target][i]) - eval(diff)])
   
   return [HOLC_A_data, HOLC_B_data, HOLC_C_data, HOLC_D_data, white, other, black, asian, hispanic]

# `calc_pwm_diff()` parses the DataFrame and returns a list of the differences
# between population-weighted air pollution levels by both HOLC grade _and_
# ethnicity. This computation, used starting in Figure 2, differed sufficiently
# from Figure 1 that it had to be included as its own separate function.
def calc_pwm_diff(df, pop, target):
   spec_A_data = []
   spec_B_data = []
   spec_C_data = []
   spec_D_data = []

   cities = list(set(df['City']))
   pwms = {}
   for city in cities:
      pwms[city] = calc_city_pwm(city, df['City'], df[target], df['Total'])
   
   for i in df.index:
      if df['Grade'][i] == 'A':
         spec_A_data += (round(df['PHOLC'][i] * df[pop][i]) * [(df[target][i] - pwms[df['City'][i]])])
      if df['Grade'][i] == 'B':
         spec_B_data += (round(df['PHOLC'][i] * df[pop][i]) * [(df[target][i] - pwms[df['City'][i]])])
      if df['Grade'][i] == 'C':
         spec_C_data += (round(df['PHOLC'][i] * df[pop][i]) * [(df[target][i] - pwms[df['City'][i]])])
      if df['Grade'][i] == 'D':
         spec_D_data += (round(df['PHOLC'][i] * df[pop][i]) * [(df[target][i] - pwms[df['City'][i]])])
   
   return [np.average(spec_A_data), np.average(spec_B_data), np.average(spec_C_data), np.average(spec_D_data)]
