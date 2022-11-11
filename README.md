# Inflam
![Continuous Integration build in GitHub Actions](https://github.com/<wk9874>/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)
Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main Features
Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) or JSON format
- Generate plots of trial data
- View a list of inflammation numbers for each Patient
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture
  
## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation
- Create and activate a virtual environment using venv
- Install prerequisites using pip

## Basic usage
### Adding data
Data can be entered using either CSV or JSON files. The following information should be present:
- Patient Name (string)
- Patient Observations:
  - Day of observation (integer, >=0)
  - Value: (float, >= 0)
### Running the program
- Run the program with the command `python inflammation-analysis.py`. Use the `--help` argument to get more information about usage.

## Contributing
- Support for additional file types
- A GUI interface for entering / retrieving data
- More advanced analysis / graphing tools

## Contact
For help, contact `matthew.field@ukaea.uk`

## Credits
With thanks to Carpentries and the UKAEA RSE team

## License
MIT License

Copyright (c) 2022, Matthew Field

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


