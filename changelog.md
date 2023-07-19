# Changelog

### July 3, 2023

- Initialized GitHub repo
- Added description and credits
- Added code to initialize DataFrame
- Large files cannot be uploaded to GitHub without Large File Storage (LSF)
- Added code to generate plots from Figure 1
- Generated plots moved to own folders

### July 5, 2023

- Added code to generate plots from Figure 2
- Slight but noticeable differences in distribution of air pollution levels
  with ethnicity, but not with HOLC grade

### July 6, 2023

- Fixed discrepancy in plots from Figures 1 and 2; these plots are only
  meant to display air pollution levels in HOLC-mapped areas, was not
  explicitly checking for this before

### July 7, 2023

- Factored PHOLC into plots from Figures 1 and 2
- Inefficient code may result in slower runtime

### July 10, 2023

- Added code to generate plots from Figure S3
- Added comments to code to generate plots from Figures 1, 2, and S3
- Edited README to include todo
- Added code to generate modified version of plot from Figure S4

### July 12, 2023

- Added code to generate six additional plots from Figure S5
- Made note of major number discrepancy in city size from Figure S5

### July 19, 2023

- Reformatted README, todo
- Abstracted Figure 1 script functions into utils, could go a step further
  and combine all four into one script, but that would take something like ten
  minutes to run to completion
- Abstracted Figure 2 script functions into utils
