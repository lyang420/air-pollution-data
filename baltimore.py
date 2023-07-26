from utils import init

import matplotlib.pyplot as plt
import numpy as np

# Compute the population-weighted mean level of an air pollutant for a list
def compute_pwm(grade, population_factor, population, target_data):
   condition = (~np.equal(grade, 'N'))
   population_factor = population_factor[condition]
   population = population[condition]
   target_data = target_data[condition]
   return np.average(target_data, weights = round(population_factor * population))

def create_figure_1(local_data, local_no2_pwm, local_pm25_pwm, national_no2_pwm, national_pm25_pwm):

   # Collect air pollutant levels by HOLC grade and by ethnicity
   def collect_data(df, population_factor, target_data, difference):
      HOLC_A_data = []
      HOLC_B_data = []
      HOLC_C_data = []
      HOLC_D_data = []
      white       = []
      other       = []
      black       = []
      asian       = []
      hispanic    = []

      for i in df.index:
         datapoint = (round(df[population_factor][i] * df['Total'][i]) * [(df[target_data][i]) - difference])
         if df['Grade'][i] == 'A':
            HOLC_A_data += datapoint
         if df['Grade'][i] == 'B':
            HOLC_B_data += datapoint
         if df['Grade'][i] == 'C':
            HOLC_C_data += datapoint
         if df['Grade'][i] == 'D':
            HOLC_D_data += datapoint
         if df['Grade'][i] != 'N':
            white += (round(df[population_factor][i] * df['White'][i]) * [(df[target_data][i]) - difference])
            other += (round(df[population_factor][i] * df['Other'][i]) * [(df[target_data][i]) - difference])
            black += (round(df[population_factor][i] * df['Black'][i]) * [(df[target_data][i]) - difference])
            asian += (round(df[population_factor][i] * df['Asian'][i]) * [(df[target_data][i]) - difference])
            hispanic += (round(df[population_factor][i] * df['Hispanic'][i]) * [(df[target_data][i]) - difference])
      
      return [HOLC_A_data, HOLC_B_data, HOLC_C_data, HOLC_D_data, white, other, black, asian, hispanic]

   def generate_fig_1(data, labels, title, x_label, y_label, min_y, max_y, colors, file_name):
      fig, ax = plt.subplots(nrows = 1, ncols = 1)
      plot = ax.boxplot(data, labels = labels, patch_artist = True,
                        showfliers = False, showmeans = True, vert = True, whis = 0,
                        meanprops = {"marker": "o", "markerfacecolor": "black", "markeredgecolor": "black"})
      ax.set_title(title)
      ax.set_xlabel(x_label)
      ax.set_ylabel(y_label)
      ax.set_ylim(min_y, max_y)
      ax.axhline(y = np.nanmean([elem for lst in data for elem in lst]),
               color = 'black', linestyle = '--', linewidth = 1, label = 'Overall Mean')
      ax.legend()
      for median in plot['medians']: median.set_color('black')
      for patch, color in zip(plot['boxes'], colors): patch.set_facecolor(color)
      plt.savefig(file_name, dpi = 300)

   local_no2_data_unadjusted = collect_data(local_data, 'PHOLC', 'NO2', 0)
   local_no2_data_adjusted = collect_data(local_data, 'PHOLC', 'NO2', local_no2_pwm)
   compare_no2_national = collect_data(local_data, 'PHOLC', 'NO2', national_no2_pwm)
   local_pm25_data_unadjusted = collect_data(local_data, 'PHOLC', 'PM25', 0)
   local_pm25_data_adjusted = collect_data(local_data, 'PHOLC', 'PM25', local_pm25_pwm)
   compare_pm25_national = collect_data(local_data, 'PHOLC', 'PM25', national_pm25_pwm)

   labels  = ['A', 'B', 'C', 'D', 'White', 'Other', 'Black', 'Asian', 'Hispanic']
   x_label = 'HOLC Grade and Race/Ethnicity'
   colors  = ['lightcoral', 'burlywood', 'lightgreen', 'lightskyblue',
            'firebrick', 'orchid', 'darkkhaki', 'darkseagreen', 'cornflowerblue']

   generate_fig_1(local_no2_data_unadjusted, labels, 'Baltimore NO₂ Levels: Unadjusted',
                  x_label, 'Population-Weighted NO₂ (ppb)', 5, 20, colors, 'figure-b1_1.png')
   generate_fig_1(local_no2_data_adjusted, labels, 'Baltimore NO₂ Levels: Intraurban Difference',
                  x_label, 'Population-Weighted NO₂ (ppb)', -7.5, 7.5, colors, 'figure-b1_2.png')
   generate_fig_1(compare_no2_national, labels, 'Baltimore NO₂ Levels: National Difference',
                  x_label, 'Population-Weighted NO₂ (ppb)', -7.5, 7.5, colors, 'figure-b1_3.png')
   
   generate_fig_1(local_pm25_data_unadjusted, labels, 'Baltimore PM₂.₅ Levels: Unadjusted',
                  x_label, 'Population-Weighted PM₂.₅ (μg/m³)', 10, 12, colors, 'figure-b1_4.png')
   generate_fig_1(local_pm25_data_adjusted, labels, 'Baltimore PM₂.₅ Levels: Intraurban Difference',
                  x_label, 'Population-Weighted PM₂.₅ (μg/m³)', -1, 1.2, colors, 'figure-b1_5.png')
   generate_fig_1(compare_pm25_national, labels, 'Baltimore PM₂.₅ Levels: National Difference',
                  x_label, 'Population-Weighted PM₂.₅ (μg/m³)', -1, 1.2, colors, 'figure-b1_6.png')

def create_figure_2(local_data, local_no2_pwm, local_pm25_pwm, national_no2_pwm, national_pm25_pwm):

   def collect_data(df, population_factor, target_data, pwm):

      def collect_demographic_data(df, population_factor, population, target_data, pwm):
         A_data = []
         B_data = []
         C_data = []
         D_data = []
         for i in df.index:
            datapoint = (round(df[population_factor][i] * df[population][i]) * [df[target_data][i] - pwm])
            if df['Grade'][i] == 'A':
               A_data += datapoint
            if df['Grade'][i] == 'B':
               B_data += datapoint
            if df['Grade'][i] == 'C':
               C_data += datapoint
            if df['Grade'][i] == 'D':
               D_data += datapoint
         return [np.average(A_data), np.average(B_data), np.average(C_data), np.average(D_data)]

      hispanic = collect_demographic_data(df, population_factor, 'Hispanic', target_data, pwm)
      asian = collect_demographic_data(df, population_factor, 'Asian', target_data, pwm)
      black = collect_demographic_data(df, population_factor, 'Black', target_data, pwm)
      total = collect_demographic_data(df, population_factor, 'Total', target_data, pwm)
      white = collect_demographic_data(df, population_factor, 'White', target_data, pwm)
      res = [hispanic, asian, black, total, white]
      return res

   def generate_fig_2(data, axes, x_label, y_label, min_y, max_y, file_name):
      fig, ax = plt.subplots()
      ax.plot(axes, data[0], 'g--', label = 'Hispanic')
      ax.plot(axes, data[1], 'b:', label = 'Asian')
      ax.plot(axes, data[2], 'm-', label = 'Black')
      ax.plot(axes, data[3], 'k-', label = 'Total')
      ax.plot(axes, data[4], 'm--', label = 'White')
      ax.axhline(y = 0, color = 'grey', linestyle = '-', linewidth = 1)
      ax.set_xlabel(x_label)
      ax.set_ylabel(y_label)
      ax.set_ylim(min_y, max_y)
      ax.legend()
      plt.savefig(file_name, dpi = 300)

   local_no2_diff = collect_data(local_data, 'PHOLC', 'NO2', local_no2_pwm)
   national_no2_diff = collect_data(local_data, 'PHOLC', 'NO2', national_no2_pwm)
   local_pm25_diff = collect_data(local_data, 'PHOLC', 'PM25', local_pm25_pwm)
   national_pm25_diff = collect_data(local_data, 'PHOLC', 'PM25', national_pm25_pwm)

   axes = ['A', 'B', 'C', 'D']
   x_label = 'HOLC Grade'

   generate_fig_2(local_no2_diff, axes, x_label, 'Intraurban NO₂ Difference (ppb)', -6, 6, 'figure-b2_1.png')
   generate_fig_2(national_no2_diff, axes, x_label, 'National NO₂ Difference (ppb)', -6, 6, 'figure-b2_2.png')
   generate_fig_2(local_pm25_diff, axes, x_label, 'Intraurban PM₂.₅ Difference (μg/m³)', -0.8, 0.8, 'figure-b2_3.png')
   generate_fig_2(national_pm25_diff, axes, x_label, 'National PM₂.₅ Difference (μg/m³)', -0.8, 0.8, 'figure-b2_4.png')




# Nationwide statistics
national_df = init()

# Baltimore statistics
baltimore_df = national_df[national_df['City'] == 'Baltimore, MD']

local_no2_pwm = compute_pwm(baltimore_df['Grade'], baltimore_df['PHOLC'], baltimore_df['Total'], baltimore_df['NO2'])
local_pm25_pwm = compute_pwm(baltimore_df['Grade'], baltimore_df['PHOLC'], baltimore_df['Total'], baltimore_df['PM25'])
national_no2_pwm = compute_pwm(national_df['Grade'], national_df['PHOLC'], national_df['Total'], national_df['NO2'])
national_pm25_pwm = compute_pwm(national_df['Grade'], national_df['PHOLC'], national_df['Total'], national_df['PM25'])

# Comment out whichever plots you don't want to generate so you don't have to
# wait half an hour for it to redo everything

# -- create_figure_1(baltimore_df, local_no2_pwm, local_pm25_pwm, national_no2_pwm, national_pm25_pwm)
create_figure_2(baltimore_df, local_no2_pwm, local_pm25_pwm, national_no2_pwm, national_pm25_pwm)