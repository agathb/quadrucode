This project uses four models to generate a plot of the lightcurve for specified parameers. The aim is to understand the dependencies of each model and compare them.

# Models
## BoxFit

Described in [Hendrik van Eerten, Alexander van der Horst, and Andrew MacFadyen. Gamma-ray burst afterglow broadband fitting based directly on hydrodynamics simulations. The Astrophysical Journal, 749(1):44, mar 2012.](https://arxiv.org/abs/1110.5089), and can be downloaded [here](https://cosmo.nyu.edu/afterglowlibrary/boxfit2011.html) as well as the box files. 
For the installation, it is recommended to follow the [user guide](https://cosmo.nyu.edu/afterglowlibrary/boxfitdatav2/boxfitguidev2.pdf) made by the author. 
Once it is installed and running, the outputdirectory (hereafter called 'boxfitoutput') should contain the following three files: 'boxfitsettings.txt' where the parameters are specified, 'lightcurve.txt' the output data of boxfit when it is asked to generate a lightcurve, 'spectrum.txt' the equivalent for a spectrum.

## Afterglowpy

Described in [Ryan, G., van Eerten, H., Piro, L. and Troja, E., 2020, Astrophysical Journal 896, 166 (2020)](https://arxiv.org/abs/1909.11691) and available on github [here](https://github.com/geoffryan/afterglowpy?tab=readme-ov-file).
The installation is straightforward by using pip as described in its github page. 

## JetFit

Described in [Yiyang Wu and Andrew MacFadyen. Constraining the outflow structure of the binary neutron star merger event gw170817/grb170817a with a markov chain monte carlo analysis. The Astrophysical Journal, 869(1):55, December 2018](https://arxiv.org/abs/1809.06843) and the github is [here](https://github.com/NYU-CAL/JetFit), which can be set up in a conda environment.

## JetSimpy

Described in [Hao Wang, Ranadeep G. Dastidar, Dimitrios Giannios, and Paul C. Duffell. jetsimpy:A highly efficient hydrodynamic code for gamma-ray burst afterglow, 2024](https://arxiv.org/html/2402.19359v1) and available on github [here](https://github.com/haowang-astro/jetsimpy).

## Input and units for each model

This table accounts for the input of each model and their units. The (.) account for the input variables with its unit next to it when there is one. 

| Input Parameter | BoxFit | Afterglowpy | JetFit | JetSimpy |
|:--------:|:--------:|:--------:| :--------:| :--------:|
|  $\theta_{obs}$   | . rad   | . rad  |   | . rad  |
|  $\theta_{j}$    | . rad   |  . rad  |   | . rad  |
|  $\theta_{wing}$    |    |  rad   |   |  |
|  $n$    | . $cm^{-3}$   | . $cm^{-3}$   | . $cm^{-3}$/1 $cm^{-3}$  | . $cm^{-3}$   |
|  $p$    |  .  |  .   | .   | .  |
|  $E$   |     |     | . erg / 10^50   |    |
|  $E_{iso}$   |  . erg   | . erg   |   | . erg   |
|  $\eta_0$   |     |    | .   |    |
|  $\gamma_B$    |     |    | .   |    |
|  $\Gamma$    |     |    |    | .  |
|  $\epsilon_B$   |  .  |  .   | .   | .  |
|  $\epsilon_E$   |  .   |  .  | .  | .  |
|  $\xi_N$   |  .  |  .   | .   |   |
|  $d_L$   |  cm   |  cm   | cm  | Mpc   |
|  $z$   |  .  |  .   | .   | .  |
|  $b$   |    |  .   |   | .  |

# Generating lightcurves

The parameter file from BoxFit called 'boxfitsettings.txt' has all the parameters 

Once all the models are installed, and the relevant files for each model are all in the same directory, the Jupyter notebook can run  and generate a single plot with evey model. A table of the input parameters 
