# Final-Project
This repository is dedicated to the data analysis for my Final Project on Machine Learning course. For this project, I analyzed the data from THEMIS mission measurements and developed subroutines for mathematical models to further proceed with the data.  The project consists of the models that is written both in Python and MATLAB.

Here is the short description on files in this repository:

- 'downloading data.py' is Python script to automise the process of downloading the data from url address (it shows how it is implimented to download data for THEMIS measurements)
- 'FFT_plots.py' is Python script to convert data measurements for magnetic field, ion velocity, and Electric field into spectogram to observe teh events of high activity
 - 'FFT_analysis_matlab.mlx' is MATLAB script for precisely converting magnetic and electric field data into FFT spectrum using hanning windowing method. It also includes specific parameters for sampling rate of the data.
- 'stfto.py' is Python script for the function that builds FFT spectrum from data using hanning windowing method
- 'Plasma_injection_model.py' is Python script for processing and entering libraries of '.cdf' data files, entering time period where the plasma injection is (once identified), interpolating data for different measurement instruments (they have different sampling rate), implying governing equations for the calculations and visualise the data in terms of time-dependent plots. This model shows the processing of plasma injection event that happened in Jan 3, 2016 <6.40 - 7.40>
- 'magnetic_field_Jan_03_2016.mlx' is MATLAB script to draw magnetic lines for the chosen event using pre-processed data from 'Plasma_injection_model.py' and implying governing equations to solve ODE. The script also includes the routine and function to accurately perform solving ODE and discretizing the coordinates of magnetic field lines in -x and -z axis
- 'magnetic_field_lines.py' is python analogue for ODE function to discretize the coordinates of magnetic field lines 
