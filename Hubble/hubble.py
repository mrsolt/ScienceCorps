#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:27:34 2020

@author: matthewsolt
"""

import matplotlib.pyplot as plt # Import Matplotlib 
from scipy.optimize import curve_fit # Import Curve Fits
import numpy as np # Import numpy
import csv # Import the csv python package

Object_hub = [] # Initialize Object List
ms_hub = [] # Initialize ms_hub List
r_hub = [] # Initialize r_hub List
v_hub = [] # Initialize v_hub List
mt_hub = [] # Initialize mt_hub List
MT_hub = [] # Initialize MT_hub List

infile = 'hubble.csv' # Define name of input file

with open(infile, 'r', newline = "") as datafile: # Open the file
    reader = csv.DictReader(datafile) #Create a CSV Dictionary Reader
    for row in reader: # Loop over each row in the CSV file
        Object_hub.append(row['Object']) # Append a string to the Object List
        ms_hub.append(float(row['ms'])) # Append a float to the ms_hub List
        r_hub.append(float(row['r'])) # Append a float to the r_hub List 
        v_hub.append(float(row['v'])) # Append a float to the v_hub List
        mt_hub.append(float(row['mt'])) # Append a float to the mt_hub List
        MT_hub.append(float(row['MT'])) # Append a float to the MT_hub List
        
fig1, ax1 = plt.subplots(1, 1) # Define the first figures and axes

ax1.scatter(r_hub, v_hub, label = "Hubble's Original Data") # Define scatter plot
ax1.set_title("Hubble's Original Data") # Set title
ax1.set_xlabel("Distance (Mpc)") # Set x axis title
ax1.set_ylabel("Velocity (km/s)") # Set y axis title
ax1.set_xlim(0,2.5) # Set x axis limit
ax1.set_ylim(-500,1500) # Set y axis limit

def hublaw(x, h): #Simple Hubble Law Function
    return h*x

x_hub = np.linspace(0,2.5,100) # Create a simple list
popt_hub, pcov_hub = curve_fit(hublaw, r_hub, v_hub) # Fit the data to Hubble's Law
print ("H0 is {0:0.2f} +/- {1:0.2f} km/s/Mpc according to Hubble".format(popt_hub[0], np.sqrt(pcov_hub[0][0]))) # Print the fit results
print ("The age of the universe is {0:0.2f} billion years according to Hubble".format(980 / popt_hub[0])) # Print the age of the universe
ax1.plot(x_hub, hublaw(x_hub, *popt_hub), label = "Hubble Fit") # Plot the fit function
ax1.legend() # Draw legend

plt.savefig('hubble.png') # Save your plot as a png named "hubble.png"


Galaxy_cep = [] # Initialize Object List
r_cep = [] # Initialize r_neb List
v_cep = [] # Initialize v_neb List

infile2 = 'cepheids.csv' # Define name of input file

with open(infile2, 'r', newline = "") as datafile: # Open the file
    reader = csv.DictReader(datafile) #Create a CSV Dictionary Reader
    for row in reader: # Loop over each row in the CSV file
        Galaxy_cep.append(row['Galaxy']) # Append a string to the Galaxy List
        r_cep.append(float(row['r'])) # Append a float to the r_cep List 
        v_cep.append(float(row['v'])) # Append a float to the v_cep List
        
fig2, ax2 = plt.subplots(1, 1) # Define the first figures and axes

ax2.scatter(r_hub, v_hub, label = "Hubble's Original Data") # Define scatter plot
ax2.scatter(r_cep, v_cep, label = "Cepheid Data") # Define scatter plot 2
ax2.set_title("Hubble's Law") # Set title
ax2.set_xlabel("Distance (Mpc)") # Set x axis title
ax2.set_ylabel("Velocity (km/s)") # Set y axis title
ax2.set_xlim(0,25) # Set x axis limit
ax2.set_ylim(-1000,2000) # Set y axis limit

x_cep = np.linspace(0,25,100) # Create a simple list
popt_cep, pcov_cep = curve_fit(hublaw, r_cep, v_cep) # Fit the data to Hubble's Law
print ("H0 is {0:0.2f} +/- {1:0.2f} km/s/Mpc according to Cepheids".format(popt_cep[0], np.sqrt(pcov_cep[0][0]))) # Print the fit results
print ("The age of the universe is {0:0.2f} billion years according to Cepheids".format(980 / popt_cep[0])) # Print the age of the universe
ax2.plot(x_hub, hublaw(x_hub, *popt_hub), label = "Hubble Fit") # Plot the Hubble fit function
ax2.plot(x_cep, hublaw(x_cep, *popt_cep), label = "Cepheid Fit") # Plot the Cepheid fit function

r_hub_7331 = [14.52] # Distance for Galaxy 7331 using Hubble
v_hub_7331 = [816] # Velocity for Galaxy 7331 using Hubble

r_cep_7331 = [1.1] # Distance for Galaxy 7331 using Cepheids
v_cep_7331 = [500] # Velocity for Galaxy 7331 using Cepheids

ax2.scatter(r_hub_7331, v_hub_7331, label = "7331 Hubble") # Create scatter plot for 7331 with Hubble
ax2.scatter(r_cep_7331, v_cep_7331, label = "7331 Cepheids") # Create scatter plot for 7331 with Cepheids
ax2.legend() # Draw legend

plt.savefig('cepheids.png') # Save your plot as a png named "cepheids.png"