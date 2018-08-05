# Github data parser python script (ZoomRX challenge)

This repo contains a python script module which accepts set of inputs from stdin and processes a CSV file based on the given constraints.

## Contents

- [github_stats.py](github_stats.py): This script parses repository data from GitHub into CSV file.
- [sample_output](./sample_output): This directory contains the sample CSV output from local execution

## How to build and run Docker
docker build -t github_stats .\
docker run -it --env GITHUB_USERNAME="GitHub Username" --env GITHUB_PASSWORD="GitHub Password" github_stats

## Sample Execution
Please enter a list of public Github repositories and type 'quit' to proceed

pramodhayyappan92/zoomrx-challenge
quit

Please wait parsing...

Parsed to Github_stats.csv file in path :  /

CSV file output\
    Repository_Name                                          Clone_Url  \
0  zoomrx-challenge  https://github.com/pramodhayyappan92/zoomrx-ch...\

  Latest_Commit_Date Latest_Commited_Author\
0         2018-08-01      pramodhayyappan92\
