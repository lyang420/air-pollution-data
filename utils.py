# `utils.py` contains utility functions that may be used by different scripts
# several times. There is quite a lot of repetition in how some of these plots
# are generated, so many functions were abstracted here to improve readability.

# Necessary imports
import csv
import pandas as pd

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
