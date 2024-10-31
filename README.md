# DRB-OSeMOSYS-model
[![DOI](https://zenodo.org/badge/636122125.svg)](https://zenodo.org/badge/latestdoi/636122125)

# Paper supporting files
This repository contains the data, model and solver needed to replicate the modelling efforts conducted for the paper titled: "**Aligning the Western Balkans power sectors with the European Green Deal**", DOI 10.1088/2515-7620/ad8ca4.

### Scenarios
------------------

Scenario data files included in this repository:

* Reference scenario (**REF**)
* Emission Limit scenario (**EL**)
* Wind on Agricultural land scenario (**AG**)

### Model
------------------
The **OSeMOSYS** model file used to run all the scenarios:
Open Source energy MOdeling SYStem

Modified by Francesco Gardumi, Constantinos Taliotis, Igor Tatarewicz, Adrian Levfert
Main changes to previous version **OSeMOSYS_2016_08_01**

Bugs fixed in equations:
* Objective function
* E5, E8, E9
* SV1, SV2        
* SC2 (both lower and upper)
* RE4

The code used for this paper is based on the above mentioned OSeMOSYS_2017_11_08 version, with changes made by Taco Neit in 2016 and Youssef Almulla in 2020.  

The OSeMOSYS model file can be accessed through this repository. Other versions are available at the [OSeMOSYS Website](http://www.osemosys.org/get-started.html)

### Solver
------------------
The solver used to obtain the results shown in the paper:
**Gurobi Optimizer version 10.0.0 build v10.0.0rc2 (win64)**
Copyright (c) 2022, Gurobi Optimization, LLC
Available at the [Gurobi Website](https://www.gurobi.com/downloads/)
# Licence
The code in the DRB-OSeMOSYS-model is released as free software under the [MIT License](https://opensource.org/license/mit/), see LICENSE.txt. However, different licenses and terms of use may apply to the various input data.
