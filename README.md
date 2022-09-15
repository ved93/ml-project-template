# ml-project-template
An opinionated python ml project structure




cd into project Directory   
run   
`conda env create -f environment.yml`
`conda activate env_name`
`make`  


## Structure

    ├── README.md          <- The top-level README
    │
    ├── notebooks          <- Jupyter notebooks
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions for submissions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── utils  <- Scripts for utility functions
    │       └── config.py
    │
    ├── test               <- test scripts for testing the functions
    ├── requirements  <- The requirements file for reproducing the analysis environment, e.g.
    │   └── dev             <- dev environment requirements
    |   └── prod            <- prod requirements
    ├── environment.yml         <- create manage environment
    ├── Dockerfile         <- Dockerfile, alternative approach to manage environment
    │                          
    ├── Makefile           <- Makefile with commands that perform parts of the processing pipeline