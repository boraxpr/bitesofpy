import csv

import pandas as pd
import math
XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    data = pd.read_csv(XYZ)
    data['Dollar Flux'] = data['12/31/20']-data['12/31/19']
    data['Percentage Flux'] = data['Dollar Flux']/data['12/31/19']
    return list(zip(data['Account'],data['12/31/20'],data['12/31/19'],data['Dollar Flux'],data['Percentage Flux']))


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []
    for key, value in enumerate(xyz):
        account,year1,year2,dollar_flux,percentage_flux = value
        if abs(dollar_flux)>THRESHOLDS[0] and abs(percentage_flux)>THRESHOLDS[1]:
            flagged_lines.append(xyz[key])
    return flagged_lines