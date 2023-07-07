# air-pollution-data
https://pubs.acs.org/doi/10.1021/acs.estlett.1c01012?fig=tgr1&ref=pdf

The above publication (Lane, Morello-Frosch, Marshall, & Apte, 2022) presents
statistics on air pollution levels in cities across the United States, and
shows the long-term effects of historical redlining based on race/ethnicity
with present-day air quality decades later.

The Python scripts herein aim to use the raw data to generate plots from the
study. Once ascertained to be accurate, it may be modified and applied to data
surrounding the energy efficiency of buildings in Baltimore City.

The raw data referenced can be found at
https://figshare.com/articles/dataset/Historical_redlining_is_associated_with_present-day_air_pollution_disparities_in_U_S_cities_Associated_datasets/19193243?file=34300682.

File size makes it too large for traditional upload or commit; see GitHub
Large File Storage (LSF) for alternative options.

Questions, comments, and suggestions for code review welcome and encouraged.

## Notes

### Wednesday, July 5, 2023

When comparing air pollution levels against HOLC grade, numbers match up to
those present in study.

When comparing air pollution levels against race and ethnicity of residents,
numbers differ. Variances are mild in the NO2 plots, much more noticeable with
PM25.

In particular, intraurban differences broken down into both ethnicity and grade
yield _significantly_ different results, this will need to be looked at
further.

### Thursday, July 6, 2023

Fixed error from yesterday. Plots displayed in study are concentrated on
pollution levels in HOLC-mapped areas; raw data contains numbers from blocks
outside HOLC-mapped areas (denoted by 'N' grade). Omit these from plot
generation. Fixes to follow.

Need to factor in `PHOLC` into HOLC-grade numbers. Also lots and lots of
comments, a lot of this looks unintelligible.

### Friday, July 7, 2023

Factoring `PHOLC` into the population number calculations, differences are
marginal but present; I think it's relevant, the supporting information
mentioned it.

It is eating a huge bit of memory to run each script, maybe there are more
efficient ways of going about this, e.g., creating a new column in the
DataFrame so we only need to make the calculation once, right after creating
it. We'll see.

Need to make some of the plots prettier too (e.g., add titles, legends, modify
axes scales and sizes of bars)
