# Python Workflow

This is a demonstration workflow which intends to run the papermillConvert.py file to run and save a new copy of the Input-MonteCarloPi.ipynb notebook and save a copy of the results in the output folder.

The input and output files could be anything, for example importing a bunch of data, refitting a model, and pushing the updated model to some location where it can be further utilized downstream.

Using the Github Actions functionality, this should repeat on a schedule until 60 days after I stop updating this repository (per the documents). It does so using a cron job, which case is straightforward to set up on a linux system, and similar functionality exists on platforms like Databricks.

The general workflow is:
* Github Actions runs on a scheduler using Cron ever 12 hours, which can be any cadence that makes sense for a project
* The Github Action runs papermillConvert.py
* papermillConvert.py calls on some Bash commands that uses the papermill library to run the nput-MonteCarloPi.ipynb and save a copy
