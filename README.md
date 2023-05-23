# A simulation-optimization model for groundwater remediation:
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

# Methodology: **
	FLOPY is used to generate the MODFLOW and MT3DMS input files. https://flopy.readthedocs.io/en/3.3.2/
	Particle swarm optimization is used as an optimization model.





