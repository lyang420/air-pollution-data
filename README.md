# Air Pollution Data Analysis

## About

The code in this repository aims to recreate plots displayed in a publication
that shows correlation between historical redlining across major cities in the
United States and present-day air pollution levels. The link to this study
(Lane, Morello-Frosch, Marshall, & Apte, 2022) can be found here:

https://pubs.acs.org/doi/10.1021/acs.estlett.1c01012?fig=tgr1&ref=pdf

Once the code is ascertained to be able to accurately analyze data from the
study, the goal then is to apply it to data on building projects in Baltimore
City, as part of a collaborative initiative by Morgan State University and
Georgetown University.

## Table of Contents

- [Repository Organization](#repo-organization)
- [Running the Code](#execution)
- [Contributing](#contributing)
- [Changelog](#roadmap)
- [To Do](#to-do)
- [Credits](#credits)

## Usage

### Repository Organization

Currently, the repository has seven folders. Five of them (`figure-1`,
`figure-2`, `figure-s3`, `figure-s4` and `figure-s5`) stores plots that
correspond to those seen in the study, as well as the Python scripts written to
generate them. The sixth folder (`baltimore-figures`) contains plots of the
same style as those seen in the study, but which display data relevant to
Baltimore City. The seventh folder (`notes`) contains a map of the HOLC grades
prescribed in the 1930s in Baltimore City, and several text files explaining
what an HOLC grade is, and how it was determined, as well as more in-depth
summaries of the plots in `baltimore-figures`.

Outside of the folders, there is a `README`, as well as a changelog tracking
progress made in the development of this repository. There is also a file
`utils.py`, where many heavy utility functions used by the aforementioned code
was abstracted to.

### Running the Code

Execute the code as you normally would by entering `python3 file-name` on the
command line, where `file-name` is the name of the script you want to run.

Be sure to have `utils.py` and the raw data file in the same directory. The raw
data can be found here:

https://figshare.com/articles/dataset/Historical_redlining_is_associated_with_present-day_air_pollution_disparities_in_U_S_cities_Associated_datasets/19193243?file=34300682

Depending on your machine and which script is being run, completion may take
a few minutes.

### Contributing

Suggestions are welcome and encouraged. If you have an idea to make this
better, please fork the repo and create a pull request.

## Changelog

### Version Control

See `changelog.md`.

### To Do

- [x] Abstract repetitive functions from individual scripts to `utils.py`
- [x] Adjust plot visual details (titles, axis labels, scales, colors, legends)
- [x] Standardize file naming convention
- [x] Modify code to process local (Baltimore) data
- [x] Adjust indentation in code and write comments

## Credits

Code written in Python3.

Study by Haley M. Lane, Rachel Morello-Frosch, Julian D. Marshall, and Joshua
S. Apte (https://pubs.acs.org/doi/10.1021/acs.estlett.1c01012?fig=tgr1&ref=pdf)

Morgan State University Faculty: Paul S. Wang
(https://www.morgan.edu/computer-science/faculty-and-staff/shuangbao-wang)

Contact me at
[lyang420@umd.edu](mailto:lyang420@umd.edu?subject=[GitHub]%20Air20%Pollution%20Data).
