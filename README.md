# air-pollution-data

## Overview

### Introduction

The code in this repository aims to recreate plots displayed in a study from
2022 that shows an association between historical redlining and present-day
air pollution disparities in U.S. cities. The link to the publication (Lane,
Morello-Frosch, Marshall, & Apte, 2022) can be found here:

https://pubs.acs.org/doi/10.1021/acs.estlett.1c01012?fig=tgr1&ref=pdf

`createdf.py` generates and formats a pandas DataFrame to be used to create
plots.

`no2-unadjusted.py`, `no2-adjusted.py`, `pm25-unadjusted.py`, and
`pm25-adjusted.py` generates plots that display the following, respectively:

* Unadjusted NO2 levels by HOLC grade and Race/Ethnicity
* Adjusted NO2 levels (intraurban differences) by HOLC grade and Race/Ethnicity
* Unadjusted PM2.5 levels by HOLC grade and Race/Ethnicity
* Adjusted PM2.5 levels (intraurban differences) by HOLC grade and
  Race/Ethnicity

They correspond to Figure 1 in the study.

`no2-diff.py` and `pm25-diff.py` generates plots that display intraurban
differences between residents by both race/ethnicity and HOLC grade, as per
Figure 2.

`demographics.py` generates plots that display the distribution of the
population by HOLC grade, as well as their respective demographics, as seen in
Figure S3 from the study's supporting information.

### Sources

The raw data used to generate the plots can be found here:

https://figshare.com/articles/dataset/Historical_redlining_is_associated_with_present-day_air_pollution_disparities_in_U_S_cities_Associated_datasets/19193243?file=34300682.

It is too large for me to upload it to GitHub, either manually or via a commit.
I may look into Large File Storage (LSF); users may also download the `.csv`
file directly from the link above.

### Goal

Once the code is able to accurately generate plots from the study, it can be
used to process data from other sources, specifically, local data from the
Baltimore area (see Baltimore Buildings Data energy efficiency project). The
results from there may be integrated into an online dashboard.

## To Do

Questions, comments, and suggestions are welcome and encouraged.

- [ ] Write further comments in the `.py` files, some of them are hard to read.
- [ ] Can some of the code used to generate plots be made more efficient?
- [ ] Additional plots are present in the study's supporting information file,
      add code to generate those.
- [ ] Customize appearance and dimensions of plots from default.
