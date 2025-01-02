# Stock Analyzer
All big US investors or fund managers are required to file form 13F. SEC has a defined XML schema which is used for the filing. This is a quarterly filing.

The goal of the tool is to provide necessary insight so that small investors can take a clue from the investment pattern of big investors and make an informed decision. Due to the daily changing market, a quarter might be too late.

## Requirements
* Compare two 13F files for a company and display an analysis of
    - New shares brought.
    - Shares offloaded.
    - Change in holdings.
    - Change in Market value.
* SEC publishes all the 13F in a zip. Write a method to list available dataset from https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets
* Evaluate 13F files for multiple companies and identify:
    - Common shares across the files.
