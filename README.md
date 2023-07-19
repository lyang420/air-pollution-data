# Air Pollution Data Analysis

## About

The code in this repository aims to recreate plots displayed in a publication
that shows correlation between historical redlining across major cities in the
United States and present-day air pollution levels. The link to this study
(Lane, Morello-Frosch, Marshall, & Apte, 2022) can be found here:

https://pubs.acs.org/doi/10.1021/acs.estlett.1c01012?fig=tgr1&ref=pdf

Once the code is ascertained to be able to accurately analyze data, the goal is
to apply it to data regarding building projects in a smaller area in Baltimore
City, as part of a project by Morgan State University and Georgetown
University.

## Table of Contents

- [How to Read this Repo](#repo-organization)
- [How to Run the Code](#execution)
- [How to Contribute](#contributing)
- [Changelog](#roadmap)
- [To Dos](#to-do)
- [Credits](#credits)

## Usage

### Repo Organization

The folders store each of the respective generated plots from the study. Each
folder (will) also contain a Jupyter Notebook write-up providing more
comprehensive overview of the code used to generate its graphs.

### Execution

The code files are stored in the main part of the repository. In order for them
to run correctly, be sure to have the `utils.py` and the raw data file in the
same folder. The raw data can be found here:

https://figshare.com/articles/dataset/Historical_redlining_is_associated_with_present-day_air_pollution_disparities_in_U_S_cities_Associated_datasets/19193243?file=34300682

Execute the code as you normally would in the terminal by entering
`python [file-name]`, where `file-name` is the name of the script you want to
run. Depending on your machine, runtime may be a few minutes.

### Contributing

Suggestions are welcome and encouraged. If you have an idea to make this
better, please fork the repo and create a pull request.

## Changelog

### Roadmap

See `changelog.md`.

### To Do

- [ ] Abstract repetitive functions from code into utility file
- [ ] Rename scripts and generated plot images
- [ ] Finish writing comments in code
- [ ] Adjust additional plot visual details (legend, dimensions, colors)
- [ ] Include Jupyter Notebook writeups in folders

## Credits

Code written in Python.

Study by Haley M. Lane, Rachel Morello-Frosch, Julian D. Marshall, and Joshua
S. Apte (https://pubs.acs.org/doi/10.1021/acs.estlett.1c01012?fig=tgr1&ref=pdf)

Morgan State University Faculty: Paul S. Wang
(https://www.morgan.edu/computer-science/faculty-and-staff/shuangbao-wang)

Contact me at
[lyang420@umd.edu](mailto:lyang420@umd.edu?subject=[GitHub]%20Air20%Pollution%20Data)
