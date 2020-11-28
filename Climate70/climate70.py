import matplotlib.pyplot as plt # Import Matplotlib 
import numpy as np # Import numpy
import csv # Import the csv python package

station = [] # Initialize Station List
latitude = [] # Initialize Latitude List
longitude = [] # Initialize Longitude List
dx70_1948 = [] # Initialize dx70 1948 List
dx70_2018 = [] # Initialize dx70 2018 List
dx90_1948 = [] # Initialize dx90 1948 List
dx90_2018 =  [] # Initialize dx90 2018 List

infile = 'climate70.csv' # Define name of input file

with open(infile, 'r', newline = "") as datafile: # Open the file
    reader = csv.DictReader(datafile) #Create a CSV Dictionary Reader
    for row in reader: # Loop over each row in the CSV file
        station.append(row['station']) # Append a string to the Station List
        latitude.append(float(row['latitude'])) # Append a float to the Latitude List
        longitude.append(float(row['longitude'])) # Append a float to the Longitude List 
        dx70_1948.append(float(row['dx70_1948'])) # Append a float to the dx70 1948 List
        dx70_2018.append(float(row['dx70_2018'])) # Append a float to the dx70 2018 List
        dx90_1948.append(float(row['dx90_1948'])) # Append a float to the dx90 1948 List
        dx90_2018.append(float(row['dx90_2018'])) # Append a float to the dx90 2018 List
        
fig1, ax1 = plt.subplots(1, 1) # Define the first figures and axes

ax1.scatter(longitude, latitude, label = "Station GPS coordinates") # Define scatter plot
ax1.set_title("GPS Coordinates of Temperature Stations") # Set title
ax1.set_xlabel("Longtitude") # Set x axis title
ax1.set_ylabel("Latitude") # Set y axis title
ax1.set_xlim(-180,180) # Set x axis limit
ax1.set_ylim(-90,90) # Set y axis limit

my_lat = [42.338356] # Latitude Comerica Park, Detroit, MI
my_long = [-83.048134] # Longitude Comerica Park, Detroit, MI

#my_lat = [42.338356] # CVIF Jagna
#my_long = [-83.048134] # CVIF Jagna

ax1.scatter(my_long, my_lat, label = "My GPS coordinates") # Create scatter plot with my coordinates
ax1.legend() # Draw legend

plt.savefig('gps.png') # Save your plot as a png named "gps"

fig2, ax2 = plt.subplots(1, 1) # Define the second figures and axes

nbins = 10 # Number of bins in the histogram

ax2.hist(dx70_1948, nbins, label = "1948", alpha = 0.5) # Define histogram
ax2.hist(dx70_2018, nbins, label = "2018", alpha = 0.5) # Define histogram
ax2.set_title("Comparing the Number of Days where Temp > 70 F Between 1948 and 2018") # Set title
ax2.set_xlabel("Number of Days Temp > 70 F") # Set x axis title
ax2.set_ylabel("Number of Occurences") # Set y axis title
ax2.legend() # Draw legend

plt.savefig('dx70.png') # Save your plot as a png named "dx70"

fig3, ax3 = plt.subplots(1, 1) # Define the third figures and axes

ax3.hist(dx90_1948, nbins, label = "1948", alpha = 0.5) # Define histogram
ax3.hist(dx90_2018, nbins, label = "2018", alpha = 0.5) # Define histogram
ax3.set_title("Comparing Temp > 90 F Between 1948 and 2018") # Set title
ax3.set_xlabel("Number of Days Temp > 90 F") # Set x axis title
ax3.set_ylabel("Number of Occurences") # Set y axis title
ax3.legend() # Draw legend

plt.savefig('dx90.png') # Save your plot as a png named "dx90"

fig4, ax4 = plt.subplots(1, 1) # Define the fourth figures and axes 

nlist = 5 # Number of elements in the list
station_trunc = station[0 : nlist] # Truncate the station list
dx70_1948_trunc = dx70_1948[0 : nlist] # Truncate the dx70 1948 list
dx70_2018_trunc = dx70_2018[0 : nlist] # Truncate the dx70 2018 list

ax4.bar(station_trunc, dx70_1948_trunc, label = "1948", alpha = 0.5) # Define bar graph
ax4.bar(station_trunc, dx70_2018_trunc, label = "2018", alpha = 0.5) # Define bar graph
ax4.set_title("Comparing Temp > 70 F Between 1948 and 2018") # Set title
ax4.set_xlabel("Station") # Set x axis title
ax4.set_ylabel("Number of Days with Temp > 70 F") # Set y axis title
ax4.legend() # Draw legend

plt.savefig('dx70bar.png') # Save your plot as a png named "dx70bar"

fig5, ax5 = plt.subplots(1, 1) # Define the fifth figures and axes

ax5.bar(station, dx90_1948, label = "1948", alpha = 0.5) # Define bar graph
ax5.bar(station, dx90_2018, label = "2018", alpha = 0.5) # Define bar graph
ax4.set_title("Comparing Temp > 90 F Between 1948 and 2018") # Set title
ax5.set_xlabel("Station") # Set x axis title
ax5.set_ylabel("Number of Days with Temp > 90 F") # Set y axis title
ax5.legend() # Draw legend

#fig.show() # Show the plot, you should see 4 different plots 
plt.savefig('dx90bar.png') # Save your plot as a png named "dx90bar"

print(sum(dx70_1948)/len(dx70_1948)) # Print mean dx70 1948
print(sum(dx70_2018)/len(dx70_2018)) # Print mean dx70 2018
print(sum(dx90_1948)/len(dx90_1948)) # Print mean dx90 1948
print(sum(dx90_2018)/len(dx90_2018)) # Print mean dx90 2018
