# `utils.py` contains utility functions used by scripts to collect and organize
# data and subsequently generate plots of different variations. There is a lot
# of repetition in how some of these plots are generated, so many functions
# were abstracted here to improve readability.

# Necessary imports. My machine seems to have a problem with some of these
# (warnings visible in the editor), but the code runs fine when called from the
# command line.
import csv
import pandas as pd
import numpy as np

# `init()` takes the raw data file referenced in the study (see `README`) and
# generates and returns a pandas DataFrame for further analysis.
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
   
   # Discard the first field, `num`. All `num` is is an index marker (entry 1,
   # 2, 3, etc.), and this will be regenerated shortly when the DataFrame is
   # created.
   data.pop(0)

   # Initialize lists to store all other fields of interest...
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

   # ...and add the data to the appropriate ones.
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

   # -- `CUA` stands for "Census Urbanized Area," named from the 2010 census
   # -- `City` is the name of the city
   # -- `GEOID` is the FIPS code of the census block
   # -- `Grade` is the HOLC grade attributed to the census block
   # -- `PHOLC` is the percentage of the census block attributed to `Grade`
   # -- `Asian` is the number of Asian residents in the census block
   # -- `Black` is the number of black residents in the census block
   # -- `Hispanic` is the number of Hispanic residents in the census block
   # -- `White` is the number of white residents in the census block
   # -- `Other` is the number of residents not of the above ethnicities
   # -- `Total` is the total number of residents living in the census block
   # -- `NO2` is the NO₂ concentration in ppb at the census block level
   # -- 'PM25` is the PM₂.₅ concentration in μg/m³ at the census block level
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

   # Convert numerical field values to numbers so we can manipulate them as
   # needed later (they are stored as strings by default).
   df['PHOLC']    = pd.to_numeric(df['PHOLC'])
   df['Asian']    = pd.to_numeric(df['Asian'])
   df['Black']    = pd.to_numeric(df['Black'])
   df['Hispanic'] = pd.to_numeric(df['Hispanic'])
   df['White']    = pd.to_numeric(df['White'])
   df['Other']    = pd.to_numeric(df['Other'])
   df['Total']    = pd.to_numeric(df['Total'])
   df['NO2']      = pd.to_numeric(df['NO2'])
   df['PM25']     = pd.to_numeric(df['PM25'])

   # Return complete DataFrame.
   return df

# `calc_city_pwm` is a function that, given a `target_city`, calculates and
# returns the population-weighted mean level of the given datapoint (either NO₂
# or PM₂.₅ concentration) for that city. It is referenced by many scripts,
# especially the ones used in generating Figures 1, 2, and S5.
def calc_city_pwm(target_city, all_cities, datapoint, population):

   # We want to filter out the input lists to only include those pertaining to
   # our city of interest. It also helps to make sure that all the datapoints
   # that should be numbers, are numbers.
   condition = ((all_cities == target_city) & (~np.isnan(datapoint)) &
                (~np.isnan(population)))

   # Filter input lists according to the above condition.
   datapoint = datapoint[condition]
   population = population[condition]

   # Numpy has a handy function to calculate weighted means.
   return np.average(datapoint, weights = population)

# `collect_data` creates and returns a list containing NO₂ levels (measured in
# ppb) and PM₂.₅ levels (measured in (μg/m³)), organized by both HOLC grade (A,
# B, C, or D), as well as the demographics of residents in the census. Out of
# all the plots generated by the study, this is the most basic (i.e., involves
# the least number of auxiliary computations), and is the first one seen,
# present in Figure 1.
def collect_data(df, population_factor, target_data, calc_diff):
   HOLC_A_data = []
   HOLC_B_data = []
   HOLC_C_data = []
   HOLC_D_data = []
   white       = []
   other       = []
   black       = []
   asian       = []
   hispanic    = []

   # Sometimes, instead of just viewing the air pollution levels for residents
   # in a census block, we may want to see the difference between that number
   # and the population-weighted mean pollutant level of some area. In the
   # event of the former, `diff`, which is the amount to subtract, will be 0.
   # Otherwise, we need to collect population-weighted mean statistics to be
   # referenced later.
   diff = "0"

   # Collect population-weighted air pollution levels for each unique city in
   # the census.
   if calc_diff:
      cities = list(set(df['City']))
      pwms = {}
      for city in cities:
         pwms[city] = calc_city_pwm(city, df['City'], df[target_data], df['Total'])
      
      # `diff` is stored as a string and evaluated later. This is because we
      # don't know which mean pollutant level we want until we iterate through
      # the DataFrame, so we can't write it explicitly right now because the
      # index variable `i` doesn't exist yet.
      diff = "pwms[df['City'][i]]"

   # Air pollution levels added to the correct list. Since the data is
   # population-weighted, we need to make the following modifications before
   # adding them:
   #
   # The data to be added is the air pollution level, which may or may not
   # have the population-weighted air pollution concentration of a city
   # subtracted from it.
   #
   # This number is then added to the appropriate list `n` times, where `n` is
   # the number of residents listed in the census block, multiplied by
   # `population_factor`, or `PHOLC`, the portion of residents in that census
   # block attributed to its given HOLC grade.
   for i in df.index:
      datapoint = [(df[target_data][i]) - eval(diff)]
      if df['Grade'][i] == 'A':
         HOLC_A_data += (round(df[population_factor][i] * df['Total'][i]) * datapoint)
      if df['Grade'][i] == 'B':
         HOLC_B_data += (round(df[population_factor][i] * df['Total'][i]) * datapoint)
      if df['Grade'][i] == 'C':
         HOLC_C_data += (round(df[population_factor][i] * df['Total'][i]) * datapoint)
      if df['Grade'][i] == 'D':
         HOLC_D_data += (round(df[population_factor][i] * df['Total'][i]) * datapoint)
      if df['Grade'][i] != 'N':
         white += (round(df[population_factor][i] * df['White'][i]) * datapoint)
         other += (round(df[population_factor][i] * df['Other'][i]) * datapoint)
         black += (round(df[population_factor][i] * df['Black'][i]) * datapoint)
         asian += (round(df[population_factor][i] * df['Asian'][i]) * datapoint)
         hispanic += (round(df[population_factor][i] * df['Hispanic'][i]) * datapoint)
   
   return [HOLC_A_data, HOLC_B_data, HOLC_C_data, HOLC_D_data, white, other,
           black, asian, hispanic]

# `collect_data_intraurban_diff` creates and returns five lists of lists, each
# of which represents the intraurban difference in an air pollutant level for
# the listed demographics that live in a specified HOLC grade. This is a
# somewhat more specific measurement than `collect_data`, and is featured
# primarily in Figure 2; whereas `collect_data` filters air pollution levels
# first by HOLC grade, and then by ethnicity, this does so both ways at once.
def collect_data_intraurban_diff(df, population_factor, target_data):

   # `collect_demographic_data` returns a list containing air pollution data
   # across HOLC grades for a specified ethnicity. This is a helper function
   # called for each ethnicity listed in the study.
   def collect_demographic_data(df, population_factor, population, target_data, pwms):
      A_data = []
      B_data = []
      C_data = []
      D_data = []

      # If you think about it, this is in fact very similar to a function
      # previously defined in this file, `collect_data`. The difference is that
      # this function only classifies data by HOLC grade, and returns their
      # averages in a list; and that this function focuses only on one
      # population of interest, and is called by another function several
      # times.
      for i in df.index:
         datapoint = (round(df[population_factor][i] * df[population][i]) *
                      [df[target_data][i] - pwms[df['City'][i]]])
         if df['Grade'][i] == 'A':
            A_data += datapoint
         if df['Grade'][i] == 'B':
            B_data += datapoint
         if df['Grade'][i] == 'C':
            C_data += datapoint
         if df['Grade'][i] == 'D':
            D_data += datapoint
      return [np.average(A_data), np.average(B_data), np.average(C_data), np.average(D_data)]

   # Create a list containing all unique cities present in the data.
   cities = list(set(df['City']))

   # Create a dictionary containing all unique cities, and their corresponding
   # population-weighted mean concentration of air pollutant.
   pwms = {}
   for city in cities:
      pwms[city] = calc_city_pwm(city, df['City'], df[target_data], df['Total'])

   # Collect HOLC-grade specific, intraurban difference, data for each listed
   # ethnicity, and then return them for further analysis (Figure 2).
   hispanic = collect_demographic_data(df, population_factor, 'Hispanic', target_data, pwms)
   asian = collect_demographic_data(df, population_factor, 'Asian', target_data, pwms)
   black = collect_demographic_data(df, population_factor, 'Black', target_data, pwms)
   total = collect_demographic_data(df, population_factor, 'Total', target_data, pwms)
   white = collect_demographic_data(df, population_factor, 'White', target_data, pwms)
   return [hispanic, asian, black, total, white]

# `collect_data_residents` creates and returns two lists. The first displays
# the total number of residents living in each mapped HOLC grade, separated by
# their listed ethnicity. The second displays the percentages of the population
# living in each HOLC grade that are attributed to each ethnicity. This is used
# primarily in Figure S3 to showcase the association between race/ethnicity and
# HOLC grade, which bridges the link between race/ethnicity and air pollution
# levels as seen in Figures 1 and 2, among others.
def collect_data_residents(df, population_factor, divisor):

   # `collect_demographic_data` collects the total number of residents of each
   # ethnicity living in a specific census block.
   def collect_demographic_data(df, population_factor, residents, index, grade):
      residents[0][grade] += (round(df[population_factor][index] * df['White'][index]))
      residents[1][grade] += (round(df[population_factor][index] * df['Other'][index]))
      residents[2][grade] += (round(df[population_factor][index] * df['Black'][index]))
      residents[3][grade] += (round(df[population_factor][index] * df['Asian'][index]))
      residents[4][grade] += (round(df[population_factor][index] * df['Hispanic'][index]))

   # Python is hilarious
   # This function divides each element in a `lst` by `divisor`. I had to write
   # this manually because `lst` isn't just a one-dimensional list, it's a list
   # of more lists, and when I tried to perform this operation cleanly (i.e.,
   # without iteration), it created a new variable which was subsequently
   # discarded, and didn't modify the list in placee, which was the goal. So I
   # had to do this explicitly, like this.
   def adjust_numerical_data(lst, divisor):
      res = []
      for sublist in lst: res.append([x / divisor for x in sublist])
      return res

   # lol
   # Similar idea as `adjust_numerical_data` up above, this converts each
   # element in a list to be a percentage of their total sample.
   def compute_percentages(lst, totals):
      res = []
      for elem, total in zip(lst, totals): res.append((elem / total) * 100)
      return res

   # Population figures for each demographic. Each list has four spots to
   # account for each HOLC grade.
   white = [0] * 4
   other = [0] * 4
   black = [0] * 4
   asian = [0] * 4
   hispanic = [0] * 4
   residents = [white, other, black, asian, hispanic]

   for i in df.index:
      if df['Grade'][i] == 'A':
         collect_demographic_data(df, population_factor, residents, i, 0)
      if df['Grade'][i] == 'B':
         collect_demographic_data(df, population_factor, residents, i, 1)
      if df['Grade'][i] == 'C':
         collect_demographic_data(df, population_factor, residents, i, 2)
      if df['Grade'][i] == 'D':
         collect_demographic_data(df, population_factor, residents, i, 3)
   
   # Divide each population number by a specified divisor, because otherwise,
   # the plot is going to be crammed to the brim with numbers in the millions,
   # or the hundreds of thousands, at the very least.
   numerical_data = adjust_numerical_data(residents, divisor)

   # Collect the total number of people living in each HOLC grade so that we
   # can have a list representing the _percentage_ of residents that are of
   # some ethnicity in an HOLC grade.
   A_total = sum(lst[0] for lst in residents)
   B_total = sum(lst[1] for lst in residents)
   C_total = sum(lst[2] for lst in residents)
   D_total = sum(lst[3] for lst in residents)
   totals = [A_total, B_total, C_total, D_total]
   percentage_data = [compute_percentages(population, totals) for population in residents]

   return numerical_data, percentage_data

# `collect_data_percentile` creates and returns a list containing the overall
# cumulative distribution of the given air pollutant level referenced across
# the various HOLC grades, as well as in the overall census urbanized area,
# presented in percentile format. This is used primarily in the generation
# of a _variation_ of Figure S4.
def collect_data_percentile(df, population_factor, population, target_data):
   percentile_A = []
   percentile_B = []
   percentile_C = []
   percentile_D = []
   cumulative = []
   percentiles = range(0, 100)

   # This is also similar to `collect_data`, except that it only sorts air
   # pollutant statistics by HOLC grade, and subsequently transforms them into
   # percentile values before returning.
   for i in df.index:
      datapoint = (round(df[population_factor][i] * df[population][i]) * [df[target_data][i]])
      cumulative += datapoint
      if df['Grade'][i] == 'A':
         percentile_A += datapoint
      if df['Grade'][i] == 'B':
         percentile_B += datapoint
      if df['Grade'][i] == 'C':
         percentile_C += datapoint
      if df['Grade'][i] == 'D':
         percentile_D += datapoint

   return (np.percentile(percentile_A, percentiles), np.percentile(percentile_B, percentiles),
           np.percentile(percentile_C, percentiles), np.percentile(percentile_D, percentiles),
           np.percentile(cumulative, percentiles))

# `collect_data_city` creates and returns a list containing the distribution of
# a given air pollutant across HOLC grades, separated by city size. This
# function is used primarily in the generation of plots seen in Figure S5.
def collect_data_city(df, population_factor, population, target_data, calc_diff, calc_per):

   # `calc_city_pop` returns the total number of people living in an HOLC-mapped
   # block in `target_city`.
   def calc_city_pop(target_city, all_cities, grade, population_factor, population):
      condition = ((all_cities == target_city) & (~np.equal(grade, 'N')))
      population_factor = population_factor[condition]
      population = population[condition]
      return sum(round(population_factor * population))

   # `sort_city_pops` takes the list containing all unique cities from the
   # study and their corresponding populations, and divides them into "small,"
   # "medium," and "large" cities. Classification of city size was based on
   # population; according to the study, there were 162 "small" cities
   # containing roughly 16 million residents in total, 29 "medium" cities with
   # 11 million, and 11 "large" cities with 18 million. However, when I divided
   # the total population into 162 small cities, 29 medium, and 11 large, I
   # found the population numbers were different, skewing the resulting plots
   # marginally. I also found that by classifying cities into city sizes based
   # on _population_ (rather than 162 small, 29 medium, etc.), I'd achieve
   # results closer to those shown in the study.
   def sort_city_pops(city_pops, sorted_populations):
      small_cities = []
      medium_cities = []
      large_cities = []

      for i in range(0, 173):
         small_cities.append(list(city_pops.keys())[list(city_pops.values()).index(sorted_populations[i])])
      for i in range(173, 194):
         medium_cities.append(list(city_pops.keys())[list(city_pops.values()).index(sorted_populations[i])])
      for i in range(194, 202):
         large_cities.append(list(city_pops.keys())[list(city_pops.values()).index(sorted_populations[i])])
      
      return small_cities, medium_cities, large_cities

   # `collect_city_measurements` checks to see if the `target_city` is part of
   # the list of `cities`, and if so, adds the datapoint (the air pollutant
   # concentration) to the list representing the appropriate HOLC grade.
   def collect_city_measurements(target_city, target_grade, cities, lst, datapoint):
      if target_city in cities:
         if target_grade == 'A':
            lst[0] += datapoint
         if target_grade == 'B':
            lst[1] += datapoint
         if target_grade == 'C':
            lst[2] += datapoint
         if target_grade == 'D':
            lst[3] += datapoint

   # `adjust_percentages` multiplies each element in a list of lists by 100.
   def adjust_percentages(lst):
      res = []
      for sublist in lst: res.append([x * 100 for x in sublist])
      return res

   # Initialize a dictionary containing each unique city in the study, and the
   # number of people living in each of them.
   cities = set(df['City'])
   cities.remove('NA')
   city_pops = {}
   diff = "0"
   for city in cities:
      city_pops[city] = calc_city_pop(city, df['City'], df['Grade'],
                                      df[population_factor], df[population])
   
   # If the parameter specifies that we are to measure the intraurban
   # difference in air pollutant level as opposed to just the air pollutant
   # level by itself, then we also need to initialize a dictionary containing
   # the population-weighted mean concentration of the pollutant in each unique
   # city.
   if calc_diff:
      pwms = {}
      for city in cities:
         pwms[city] = calc_city_pwm(city, df['City'], df[target_data], df[population])
      diff = "pwms[df['City'][i]]"
   
   # Sort the list of cities by their population size so we may partition them
   # into small, medium, or large class.
   sorted_populations = list(city_pops.values())
   sorted_populations.sort()
   small_cities, medium_cities, large_cities = sort_city_pops(city_pops, sorted_populations)

   # Each list contains data for each HOLC grade in cities of some size.
   small_city_data  = [[], [], [], []]
   medium_city_data = [[], [], [], []]
   large_city_data  = [[], [], [], []]

   # If the parameter specifies that we are to measure the intraurban
   # difference in air pollutant level as a percentage, we must remember to
   # use this marker to convert that number to a percent after sorting.
   per = "1"
   if calc_per:
      per = "pwms[df['City'][i]]"

   # Collect data for each city. Adjust appropriately, if the above arguments
   # indicate to do so.
   for i in df.index:
      if df['City'][i] != 'NA':
         datapoint = (round(df[population_factor][i] * df[population][i]) *
                      [((df[target_data][i]) - eval(diff)) / eval(per)])
         collect_city_measurements(df['City'][i], df['Grade'][i], small_cities,
                                   small_city_data, datapoint)
         collect_city_measurements(df['City'][i], df['Grade'][i], medium_cities,
                                   medium_city_data, datapoint)
         collect_city_measurements(df['City'][i], df['Grade'][i], large_cities,
                                   large_city_data, datapoint)

   if calc_per:
      small_city_data = adjust_percentages(small_city_data)
      medium_city_data = adjust_percentages(medium_city_data)
      large_city_data = adjust_percentages(large_city_data)

   # Population-weighted mean concentration of air pollution, represented
   # either by themselves, as intraurban differences, or as a percentage of
   # their intraurban difference.
   small_city_data = [np.average(x) for x in small_city_data]
   medium_city_data = [np.average(x) for x in medium_city_data]
   large_city_data = [np.average(x) for x in large_city_data]

   return [small_city_data, medium_city_data, large_city_data]
