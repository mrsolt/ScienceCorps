#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:36:38 2020

@author: matthewsolt
"""

import matplotlib.pyplot as plt # Import Matplotlib 
import csv # Import the csv python package

treatment = [] # Initialize Treatment List
outcome = [] # Initialize Outcome List

infile = 'malaria.csv' # Define name of input file

with open(infile, 'r', newline = "") as datafile: # Open the file
    reader = csv.DictReader(datafile) # Create a CSV Dictionary Reader
    for row in reader: # Loop over each row in the CSV file
        treatment.append(row['treatment']) # Append a string to the Treatment List
        outcome.append(row['outcome']) # Append a string to the Outcome List
   
print(treatment)
print(outcome)        
   
vac_inf = 0 # Initialize vac_inf counter
vac_noinf = 0 # Initialize vac_noinf counter
plac_inf = 0 # Initialize plac_inf counter
plac_noinf = 0 # Initialize plac_inf counter

for i in range(len(treatment)): # Loop over the entire list
    if(treatment[i] == "vaccine"): # This person is vaccinated
        if(outcome[i] == "infection"): # This person got infected
            vac_inf = vac_inf + 1 # Add +1 to the count
        else: # This person did not get infected
            vac_noinf = vac_noinf + 1 # Add +1 to the count
    else: # This person is unvaccinated   
        if(outcome[i] == "infection"): # This person got infected
            plac_inf = plac_inf + 1 # Add +1 to the count
        else: # This person did not get infected
            plac_noinf = plac_noinf + 1 # Add +1 to the count
        
print(vac_inf)
print(vac_noinf)
print(plac_inf)
print(plac_noinf)

labels = ["Vac Inf", "Vac No Inf", "Plac Inf", "Plac No Inf"] # Create List of Labels
patients = [vac_inf, vac_noinf, plac_inf, plac_noinf] # Create list of Categories

fig, ax = plt.subplots(1, 1) # Define the figures and axes 

ax.bar(labels, patients, label = "Vaccine Infection") # Define bar graph
ax.set_title("Malaria Vaccine Trial") # Set title
ax.set_xlabel("Category") # Set x axis title
ax.set_ylabel("Number of Patients") # Set y axis title

plt.savefig('malaria.png') # Save your plot as a png named "malaria"

vaccin = vac_inf + vac_noinf # Total Number of People Vaccinated
placebo = plac_inf + plac_noinf # Total Number of People Unvaccinated

attack_vac = vac_inf / vaccin # Attack level for vaccinated
attack_novac = plac_inf / placebo # Attack level for unvaccinated

eff = (attack_novac - attack_vac) / attack_novac # Calculate Vaccine Efficacy
print(eff) # Print Efficacy
