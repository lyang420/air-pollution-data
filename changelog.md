# Changelog

### July 3, 2023

- Initialized GitHub repo
- Wrote first draft of `README`
- Added code to initialize pandas DataFrame
- Added code to generate plots from study's Figure 1
- Moved generated plot image files to their own folders

### July 5, 2023

- Added code to generate plots from study's Figure 2
- Discovered slight, but noticeable difference in numbers displayed in the
  plots that I generated from the plots in the study

### July 6, 2023

- Fixed discrepancy in numbers from July 5; some of the plots only model air
  pollution levels in HOLC-mapped areas, but the raw data contains blocks that
  do not have an HOLC grade attached -- these should not be included in the
  data fed to the plot generation function

### July 7, 2023

- Factored PHOLC into the script used to generate plots from Figures 1 and 2
- Inefficient code may result in slower runtime

### July 10, 2023

- Added code to generate plots from study's Figure S3
- Wrote comments in scripts generating plots from Figures 1, 2, and S3
- Edited `README` to include a to-do section
- Added code to generate modified version of plot from study's Figure S4

### July 12, 2023

- Added code to generate plots from study's Figure S5
- Noticed major discrepancy in determination of city size from study's Figure
  S5

### July 19, 2023

- Edited `README`, specifically to-do section to be more comprehensible
- Abstracted functions used to generate Figure 1 to `utils.py`
- Abstracted functions used to generate Figure 2 to `utils.py`

### July 20, 2023

- Abstracted functions used to generate Figure S3 to `utils.py`
- Abstracted functions used to generate Figure S4 to `utils.py`

### July 21, 2023

- Abstracted functions used to generate Figure S5 to `utils.py`
- Updated `changelog` to reflect this week's progress
- Updated to-dos with notes on how to improve code efficiency, other plots to
  generate, and how to improve repo presentation next week

### July 24, 2023

- Finished abstracting functions used to generate Figure 1 to `utils.py` and
  added comments
- Renamed script and image files relating to Figure 1
- Added details to Figure 1 plots, including new title, axis labels, scale,
  and overall mean and median

### July 25, 2023

- Finished abstracting functions used to generate Figure 2 to `utils.py` and
  added comments
- Renamed script and image files relating to Figure 2
- Added details to Figure 2 plots, including new title, axis labels, and scale
- Finished fine-tuning Figures S3, S4, and S5 in a similar manner

### July 26, 2023

- Adjusted existing scripts appropriately to generate plots displaying air
  pollution statistics for Baltimore, MD
- Baltimore, MD code files moved to their own folder in the repository

### July 27, 2023

- Rewrote `README` and changelog to reflect progress made in the last week, and
  what to accomplish in the coming weeks
- Began the process of editing code indentation and style to make them more
  readable to viewers

### July 28, 2023

- Added additional comments to `utils.py` and `baltimore.py` explaining
  reasoning behind data collection methodology

### July 31, 2023

- Made final edits to indentation, variable names, and code comments in scripts
- Initialized `notes` folder to store auxiliary information, including a visual
  map of the HOLC grades of Baltimore City, pulled from the same source of data
  the original study referenced
- Constructed a more in-depth explanation of each of the plots in
  `baltimore-figures` in the form of `.txt` files that will come in handy when
  summarizing findings in a ` .tex` document later.
