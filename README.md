This project uses four models to generate a plot of the afterglow lightcurve for specified parameers. The aim is to understand the dependencies of each model and compare them.

# Models
## BoxFit

Described in [Hendrik van Eerten, Alexander van der Horst, and Andrew MacFadyen. Gamma-ray burst afterglow broadband fitting based directly on hydrodynamics simulations. The Astrophysical Journal, 749(1):44, mar 2012.](https://arxiv.org/abs/1110.5089), and can be downloaded [here](https://cosmo.nyu.edu/afterglowlibrary/boxfit2011.html) as well as the box files. 
For the installation, it is recommended to follow the [user guide](https://cosmo.nyu.edu/afterglowlibrary/boxfitdatav2/boxfitguidev2.pdf) made by the author. 
Once it is installed and running, the outputdirectory (hereafter called 'boxfitoutput') should contain the following three files: 'boxfitsettings.txt' where the parameters are specified, `lightcurve.txt` the output data of boxfit when it is asked to generate a lightcurve, `spectrum.txt` the equivalent for a spectrum.

## Afterglowpy

Described in [Ryan, G., van Eerten, H., Piro, L. and Troja, E., 2020, Astrophysical Journal 896, 166 (2020)](https://arxiv.org/abs/1909.11691) and available on github [here](https://github.com/geoffryan/afterglowpy?tab=readme-ov-file).
The installation is straightforward by using pip as described in its github page. 

## JetFit

Described in [Yiyang Wu and Andrew MacFadyen. Constraining the outflow structure of the binary neutron star merger event gw170817/grb170817a with a markov chain monte carlo analysis. The Astrophysical Journal, 869(1):55, December 2018](https://arxiv.org/abs/1809.06843) and the github is [here](https://github.com/NYU-CAL/JetFit), which can be set up in a conda environment.
[//]: <> beware i think maybe this is the jetfit first paper https://arxiv.org/abs/1308.1731

## JetSimpy

Described in [Hao Wang, Ranadeep G. Dastidar, Dimitrios Giannios, and Paul C. Duffell. jetsimpy:A highly efficient hydrodynamic code for gamma-ray burst afterglow, 2024](https://arxiv.org/html/2402.19359v1) and available on github [here](https://github.com/haowang-astro/jetsimpy).

## Files

Once all the models are installed, the relevant files for each model must all be in the same directory, namely: `FitterClass.py, InterpolatorClass.py, FluxGeneratorClass.py` and `Table.h5` for JetFit and the event data for plotting. (see JetSimpy also)
The path for the output of the BoxFit must be specified at the beginning of the code to make sure the code can read `boxfitsettings.txt` `lightcurve.txt` and 'spectrum.txt'

## Input and units for each model

This table accounts for the input of each model and their units. 
(.) accounts for the input variables with its unit and a blank space indicates that it's not taken as an input. 

| Input Parameter | BoxFit | Afterglowpy | JetFit | JetSimpy |
|:--------:|:--------:|:--------:| :--------:| :--------:|
|  $\theta_{obs}$   | . rad   | . rad  |   | . rad  |
|  $\theta_{j}$    | . rad   |  . rad  |   | . rad  |
|  $\theta_{wing}$    |    | . rad   |   |  |
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

## Comparing the models

TH: Top-Hat \begin{equation} 
E($\theta$) = E_0 for $\theta$ < $\theta_j$
\end{equation}
G: Gaussian $E$($\theta$) = $E_0$ $\exp( - \frac{$\theta$**2}{2 $\theta_c$**2})$ $\label{eq2}$
PL: Power Law $E$($\theta$) = $E_0$ $( 1 + \frac{$\theta$**2}{b $\theta_c$**2} )**-b/2$ $\label{eq3}$

|  | BoxFit | Afterglowpy | JetFit | JetSimpy |
|:--------:|:--------:|:--------:| :--------:| :--------:|
| Jet Structure   |  $\ref{eq1}$  | TH, G, PL, Spherical  | Not specified  | Specify formula |
| Energy per solid angle |  TH  | TH, G, PL, Spherical  | Not specified  | Specify formula |
| Approximations |  conic section of the full spherical solution truncated at fixed opening angle  | thin blast shell  | Not specified  | 2D thin blast shell |
| Scaling relations|  TH  | thin blast shell  | Not specified  | 2D thin blast shell |
| Box entries|  TH  | thin blast shell  | Not specified  | 2D thin blast shell |
| Method|  numerical synchrotron radiation calculation: solving the linear radiative transfer equations including synch slef absorb  | thin blast shell  | Not specified  | 2D thin blast shell |
| ?|  linear interpolation of fluid profiles between different emisson times  | thin blast shell  | Not specified  | 2D thin blast shell |
| dominant radiaton mechanism|  synchrotron radiation  | thin blast shell  | Not specified  | 2D thin blast shell |
| Jet Spreading | Yes |  No  | No  | No  |
| Model Fitting  | Deprecated  |  Yes  | Yes  | Yes  |
| Synchrotron Self- Absorption | Yes  |  No  | No  | No  |
| Electron Cooling | Yes  |  No  | No  | No  |
| Inverse Compton | ? |  No  | No  | No  |
| $\theta_0$ range | [0.045, 0.5] rad |    | No  | No  |
| $\theta_obs$ range | [0, 1.57] rad |    | No  | No  |


# Generating lightcurves

The parameter file from BoxFit called 'boxfitsettings.txt' contains all the parameters and the code will ensure that the other models take the right input in its designated unit based of this boxfit file. However, the specific internal energy $\eta_0$ and the boost lorentz factor $\gamma_B$ from JetFit can be changed directly in the code in the JetFit section. It will affect JetSimpy as well because it relies on the lorentz factor $\Gamma \approx$ 2 $\eta_0 \gamma_B$

Once BoxFit is executed with the desired parameters, the Jupyter notebook can take over and plot all four lightcurves in one plot. 

# Caveats

## JetFit

The specified time in the BoxFit parameter file can cause the scaled time $\tau$ from JetFit to be out of bounds and produce an array of Nans as the output Flux. To avoid this isue, the function `range_time_tau` calculates the time range allowed by the bounds of $\tau$ and throws a warning if the selected time frame is not suitable for JetFit.

The kernel must restart if the section JetFit has already run. Otherwise, the flux value turn into Nans. 
