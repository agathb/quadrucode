This project uses four models to generate a plot of the afterglow lightcurve for specified parameers. The aim is to understand the dependencies of each model and compare them.

# Models
## BoxFit

Described in [Hendrik van Eerten, Alexander van der Horst, and Andrew MacFadyen. Gamma-ray burst afterglow broadband fitting based directly on hydrodynamics simulations. The Astrophysical Journal, 749(1):44, mar 2012.](https://arxiv.org/abs/1110.5089), and can be downloaded [here](https://cosmo.nyu.edu/afterglowlibrary/boxfit2011.html) as well as the box files. 
For the installation, it is recommended to follow the [user guide](https://cosmo.nyu.edu/afterglowlibrary/boxfitdatav2/boxfitguidev2.pdf) made by the author. 
Once it is installed and has ran once, the code can readily run without moving any files. Indeed, the three necessary files are in the 'boxficode' directory, namely: 'boxfitsettings.txt' where the parameters are specified, `lightcurve.txt` the output data of boxfit when it is asked to generate a lightcurve and 'boxfit' containing the code. 

## Afterglowpy

Described in [Ryan, G., van Eerten, H., Piro, L. and Troja, E., 2020, Astrophysical Journal 896, 166 (2020)](https://arxiv.org/abs/1909.11691) and available on github [here](https://github.com/geoffryan/afterglowpy?tab=readme-ov-file).
The installation is straightforward by using pip as described in its github page, and needs no specific folder.

## JetFit

Described in [Yiyang Wu and Andrew MacFadyen. Constraining the outflow structure of the binary neutron star merger event gw170817/grb170817a with a markov chain monte carlo analysis. The Astrophysical Journal, 869(1):55, December 2018](https://arxiv.org/abs/1809.06843) and the github is [here](https://github.com/NYU-CAL/JetFit), which can be set up in a conda environment. The corresponding folder 'jetfitcode' has: three .py files namely `FitterClass.py, InterpolatorClass.py, FluxGeneratorClass.py' with classes and one table 'Table.h5' of precomputed fluxes for interpolation. 

## JetSimpy

Described in [Hao Wang, Ranadeep G. Dastidar, Dimitrios Giannios, and Paul C. Duffell. jetsimpy:A highly efficient hydrodynamic code for gamma-ray burst afterglow, 2024](https://arxiv.org/html/2402.19359v1) and available on github [here](https://github.com/haowang-astro/jetsimpy).

## Files

Once all the models are installed, the relevant files for each model will already be in each folder and the code should run smoothly.

## Input and units for each model

This table accounts for the input of each model and their units. 
(.) accounts for the input variables with its unit and a blank space indicates that it's not taken as an input. 

| Input Parameter | **BoxFit** | **Afterglowpy** | **JetFit** | **JetSimpy** |
|-----------------|------------|-----------------|------------|--------------|
| $\theta_{obs}$  | . rad      | . rad           |            | . rad        |
| $\theta_{j}$    | . rad      | . rad           |            | . rad        |
| $\theta_{wing}$ |            | . rad           |            |              |
| $n$             | . $cm^{-3}$| . $cm^{-3}$     | . $cm^{-3}$/1 $cm^{-3}$ | . $cm^{-3}$ |
| $p$             | .          | .               | .          | .            |
| $E$             |            |                 | . erg / 10^50|             |
| $E_{iso}$       | . erg      | . erg           |            | . erg        |
| $\eta_0$        |            |                 | .          |              |
| $\gamma_B$      |            |                 | .          |              |
| $\Gamma$        |            |                 |            | .            |
| $\epsilon_B$    | .          | .               | .          | .            |
| $\epsilon_E$    | .          | .               | .          | .            |
| $\xi_N$         | .          | .               | .          |              |
| $d_L$           | cm         | cm              | cm         | Mpc          |
| $z$             | .          | .               | .          | .            |
| $b$             |            | .               |            | .            |

*Table 1: Input Parameters for Models*


## Comparison of the models

|                              | **BoxFit**                                          | **Afterglowpy**                                                     | **JetFit**                                       | **JetSimpy**                                                        |
|------------------------------|-----------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------|
| **Jet Structure**            | TH                                                  | TH, G, PL, Spherical                                                | Boosted Fireball                                 | TH, G, PL                                                          |
| **Numerical Jet Simulations**| RAM parallel RHD code (Zhang 06)                    | None                                                                | JET Moving-Mesh RHD (Duffell 2013)              | None                                                               |                                                  |
| **Model Fitting**            | Deprecated                                          | Yes                                                                 | Yes                                             | Yes                                                                |
| **Synchrotron Self-Absorption** | Yes                                              | No                                                                  | No                                              | Self-Implement                                         |
| **Electron Cooling**         | Yes                                                 | Yes                                                                 | Yes                                             | Yes                                                                |
| **Inverse Compton**          | No                                                  | Experimental                                                        | No                                              | No                                                                 |
| **Wind Environment**         | Yes                                                 | No                                                                  | No                                              | Yes                                                                |
| **Reverse Shock**            | No                                                  | No                                                                  | No                                              | No                                                                 |
| **Energy Injection**         | No                                                  | Experimental                                                        | No                                              | No                                                                 |
| **Coasting Phase**           | No                                                  | No                                                                  | Yes                                             | Yes                                                                |
| **Counter-jet**              | Yes                                                 | Yes                                                                 | No                                              | Yes                                                                |

*Table 2: Comparison of the models*


# Generating lightcurves

The dictionary D must be specified with the desired values at the beginning of the code: it contains all the parameters and the code will ensure that the other models take the right input in its designated unit based on this dictionary. 
The code will require user input for BoxFit. Indeed, the user can either run the BoxFit code within the Jupyter notebook (1) or choose to read BoxFit's output file if the code already ran (2), in which case the user will have to put its own 'lightcurve.txt' file in the 'boxfitcode' folder. 

# Warnings

## JetFit

The specified time in the parameters can cause the scaled time $\tau$ from JetFit to be out of bounds and produce an array of Nans as the output Flux. To avoid this isue, the function `range_time_tau` calculates the time range allowed by the bounds of $\tau$ and throws a warning if the selected time frame is not suitable for JetFit.

The kernel must restart if the section JetFit has already run. Otherwise, the flux value turn into Nans. 
