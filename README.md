# A simulation-optimization model for groundwater remediation (Ex4):

# Short note on groundwater remediation:
Pump and treat is a widely used groundwater remediation technique aimed at removing contaminants from subsurface environments. It involves pumping groundwater from wells, treating it to remove or degrade the contaminants, and then either reinjecting the treated water back into the ground or discharging it safely. However, designing an optimal pump and treat system can be challenging due to the complex nature of groundwater flow and contaminant transport. To address this challenge, a simulation optimization approach can be employed to optimize the design and operation of the pump and treat system. The simulation optimization approach combines numerical simulation models of groundwater flow and contaminant transport with optimization algorithms to find the best solution for the pump and treat system. The process involves iteratively evaluating different pumping and treatment strategies through simulations and optimizing the system based on specified objectives, such as maximizing contaminant removal or minimizing remediation costs. Initially, a conceptual model of the subsurface system is developed based on available site information, including hydrogeological data and contaminant distribution. This model serves as the basis for building a numerical simulation model that represents the groundwater flow and contaminant transport processes. The simulation model incorporates mathematical equations and boundary conditions to simulate the movement of groundwater and contaminants over time. Parameters such as hydraulic conductivity, porosity, and contaminant properties are included in the model based on site-specific data. The model is calibrated and validated using field measurements to ensure its accuracy in representing the real-world system. Once the simulation model is validated, optimization algorithms are employed to search for the optimal pumping and treatment strategies. These algorithms explore different combinations of pumping rates, well locations, and treatment options to find the solution that best achieves the desired objectives.

Optimization algorithms commonly used in simulation optimization include genetic algorithms, particle swarm optimization, and simulated annealing. These algorithms employ various techniques, such as mutation, crossover, and local search, to iteratively refine the solution and converge towards the optimal design and operation of the pump and treat system. During the optimization process, the simulation model is repeatedly run with different pumping and treatment scenarios. The model evaluates the performance of each scenario by considering factors such as contaminant removal efficiency, system costs, and other predefined objectives. Based on these evaluations, the optimization algorithm adjusts the parameters of the pump and treat system to improve its performance iteratively. The simulation optimization approach allows for a comprehensive assessment of different pump and treat strategies, enabling decision-makers to compare and select the most effective and cost-efficient options. It also provides insights into the trade-offs between different objectives, such as the balance between contaminant removal and operational costs. In conclusion, the pump and treat method for groundwater remediation can benefit greatly from a simulation optimization approach. By integrating numerical simulation models with optimization algorithms, the design and operation of pump and treat systems can be optimized to achieve desired objectives, such as maximizing contaminant removal and minimizing costs. This approach provides decision-makers with valuable insights and helps in making informed decisions for effective and efficient groundwater remediation

# Description of the problem:
This problem illustrates the containment and cleanup of groundwater contaminated by two different contaminant species in a two-layer river-aquifer system. The purposes are to minimize contaminant remaining in the aquifer while achieving cleanup to minimum concentration level (MCL) within one year and while preventing contamination from reaching water supply wells or rivers.
This study employs MODFLOW to simulate groundwater flow processes, while MT3DMS is utilized to simulate the transport of multiple species of solutes for one year.
The study area is characterized by a grid system with a coarse cell discretization, where each cell measures 80 by 80 meters. The grid consists of eight rows and six columns. The total size of the study area is 75.88 acres. The first aquifer layer is unconfined and has a thickness of 20 meters, while the second layer is confined and has a thickness of 10 meters.
The area is surrounded by constant head cells to the North and South, while impervious no-flow boundaries are present to the East and West. The top aquifer receives vertical recharge from rainfall, and recharge also enters the area horizontally through constant head cells and constant flux cells. In Layer 1, a river flows through the study area, specifically through cells (2,1), (2,2), (2,3), (2,4), (2,5), and (2,6).
There are two identified zones: Zone 1, which serves as an exclusion area for containment purposes, and Zone 2, designated as the cleanup area. Both zones encompass the same area in both Layer 1 and Layer 2. This particular example focuses on two distinct non-reactive contaminants, with a predefined initial distribution of contaminant 1 in Layer 1 and contaminant 2 in Layer 2. It is assumed that there is instantaneous mixing of the contaminants with groundwater in any contaminated cell.
The pumping system in the study consists of two unmanaged drinking water wells. The first well has a pumping rate of 316.98 gallons per minute (1728 cubic meters per day), while the second well has a pumping rate of 184.96 gallons per minute (1008.29 cubic meters per day). Both wells fully penetrate Layers 1 and 2 of the aquifer. The study area has six candidate extraction wells and seven candidate injection wells. The S/O model defines the wells using 13 distinct blocks. Typically, each block corresponds to a single well, which may be screened in multiple layers. However, for the two injection wells, the blocks are designed to allow for an optimal strategy that may involve neither, either, or both layers.

# Objective:
The goal is to minimize the remaining mass while simultaneously achieving containment and cleanup levels within the threshold of 5 parts per billion (ppb).
More details of the optimization problem can be found in (Peralta, 2012).

# Methodology: 
	FLOPY is used to generate the MODFLOW and MT3DMS input files. https://flopy.readthedocs.io/en/3.3.2/
	Particle swarm optimization is used as an optimization model.


# License
Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg





