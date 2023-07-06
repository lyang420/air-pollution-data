# On my machine, Python3 seems to have issues with some of these imports,
# "could not be resolved from source." Installing packages manually on the
# command line and changing Python interpreters in the editor do not fix the
# problem, thus, debugging can be cumbersome.
#
# However, the code still runs fine.
import csv
import pandas as pd

# `init()` reads the raw data on air pollution from the provided link, sorts
# them into lists, and creates and returns a pandas DataFrame from which we can
# generate plots similar to the one in the study.
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

   # Never mind the first entry in the list we just populated, that's just the
   # names of all the fields.
   data.pop(0)

   # Notice how we didn't make space for the first field, `num`. That's because
   # all `num` does is keep track of the index of each entry, which will
   # automatically be done once we create the DataFrame later.
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

   # Populate lists to create dataframe.
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

   # Quick explanation of what each field means, abbreviated from the link:
   # 'CUA'      = Census Urbanized Area
   # 'City'     = HOLC-mapped city name
   # 'GEOID'    = Census block code
   # 'Grade'    = HOLC map grade (A, B, C, or D)
   # 'PHOLC'    = Portion of census block pop. attributed to a given grade
   # 'Asian'    = Num. Asian residents
   # 'Black'    = Num. Black residents
   # 'Hispanic' = Num. Hispanic residents
   # 'White'    = Num. White residents
   # 'Other'    = Num. residents not classified as above ethnicities
   # 'Total'    = Total num. residents
   # 'NO2'      = NO2 concentration
   # 'PM25'     = PM25 concentration
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

   # Format the entries of the dataframe that are numeric so we can make direct
   # comparisons when working with them to generate plots.
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
