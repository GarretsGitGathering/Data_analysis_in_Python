import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 
import pandas as pd 
import numpy as np

### READS DATA ###
illit_data = pd.read_csv("src/illiteracy in NY data - illiteracy in NY data.csv")

### CLEANSES DATA ###
illit_data.dropna(inplace = True)

### makes each borough unique ###
boroughs = illit_data['BOROUGH / COMMUNITY'].unique()

### makes list for each borough ###
illit_count_list = []

### PLOTS GRAPH WITH ILLITERATE ADULTS DATA ###
    ### (horizontal bar graph) ###
for borough in boroughs:
    ### associates the illiteracy count as keys and the boroughs as illit_count_by_borough ###
    ### -- also appends data for use in the math later -- ##
    borough_df = illit_data[illit_data['BOROUGH / COMMUNITY']== borough].groupby('BOROUGH / COMMUNITY')['Census Tract']
    illit_count_by_borough = borough_df.sum()
    illit_count_list.append(borough_df.sum())

    ### plots the graph ###
    plt.barh(illit_count_by_borough.keys(), illit_count_by_borough, label = borough)
plt.title('Adults Enlisted in NDA Reading and Writing Aid Programs In New York \n (updated as of January 15, 2020)')
plt.show()

### prints illit value for each brough ###
### -- it prints borough and illit_count because it has the keys (just a useful tip, luv u UwU) -- ##
for v in range(len(boroughs)):
    print(boroughs[v])

print('TOTALS OF ILLITERACY COUNT IN EACH BOROUGH')
print(illit_count_list)


### CALCULATING PERCENTAGE OF ILLITERATE ADULTS IN NEW YORK ###
    ### this is for the algorythmic part of the assignment ###
NY_total_pop = 8399000

### just a function for counting digits of an int... nothing to see here... ###
def numDigits(n):
    n_str = str(n)
    return len(n_str)

### the function to calculate the total illiterate percentage of NYC ###
def total_illiterate_percentage_calc():
    global illit_total, NY_total_pop
    #-- the calculation --#
    Census = illit_data["Census Tract"]
    illit_total = Census.sum()
    print("the total amount of illiterate adults in New York " + str(illit_total))

    ### finding the percentage of illiterates in New York.... is saying it like that offensive? ###
    illit_percentage = illit_total / NY_total_pop

    ##round percentage##
    if numDigits(illit_percentage) > 5:
        rounded_illit_percentage = round(illit_percentage, 4)

    ### -- prints the final statement -- ###
    print(str(rounded_illit_percentage) + "%. of New York City's adults are undertaking illiteracy aid programs")
#--- call the function and call it a night baby!!! ---#
total_illiterate_percentage_calc()


### so after some thought provoking conversation with Mr. Elwer, I thought that poverty rates could ###
  ### have something to do with why it was higher in certian boroughs since the poverty could be ###
       ### responsible for either them being enrolled or not wealthy enough to get the aid... ###
       ### So I'm also going to look at poverty rates in NYC by borough ###


### --POVERTY IN NYC GRAPH-- ###
NYC_pov_data = pd.read_csv("src/NYCgov_Poverty_Measure_Data__2017_.csv")

### makes each boro unique ###
boros = NYC_pov_data['Boro'].unique()

### poverty count list ###
pov_count_list = []

### --ASSOCIATES BORO WITH POVERTY STATUS-- ###
for boro in boros:
    ### associates the pov count as keys and the boroughs as pov_count_by_borough ###
    ### -- also appends data for use in the math later... divides by two to find average of 1's and 2's (can't figure out how to cleanse) -- ##
    pov_boro_df = NYC_pov_data[NYC_pov_data['Boro']== boro].groupby('Boro')['NYCgov_Pov_Stat']
    pov_count_by_borough = pov_boro_df.sum() / 2
    pov_count_list.append(pov_boro_df.sum() / 2)

    ### creates boros for the legend ###
    brooklyn = mpatches.Patch(color='purple', label = 'Brooklyn')
    queens = mpatches.Patch(color='red', label = 'Queens')
    staten_island = mpatches.Patch(color='orange', label = 'Staten Island')
    bronx = mpatches.Patch(color='blue', label = 'Bronx')
    manhatten = mpatches.Patch(color='green', label = 'manhatten')

    ### plots the graph ###
    plt.barh(pov_count_by_borough.keys(), pov_count_by_borough, label = boro)
plt.title('Random Sample of Adults Considered To Be Living In OR Bordering Poverty \n By the Government (year of 2017) \n (generating less than $35k yealry)')
plt.legend(fontsize='small', handles =[manhatten, brooklyn, staten_island, bronx, queens])
plt.ylabel('Borough Num')
plt.xlabel('Individuals in OR Bordering Poverty in Random Sample')
plt.show()

##prints the pov count in each borough##
print('TOTAL OF POV RANDOM SAMPLE IN EACH BOROUGH')
print(pov_count_list)

## NEXT STEP IS TO COMPARE ILLITERACY TO IMMIGRATION (since that might affect the rate) ##
### READS DATA ###
immi_data = pd.read_csv('src/DYCD_after-school_programs__Immigrant_Services - DYCD_after-school_programs__Immigrant_Services.csv')

### CLEANSES DATA ###
immi_data.dropna(inplace = True)

### makes each borough unique ###
borohs = immi_data['BOROUGH / COMMUNITY'].unique()

### makes list for each borough ###
immi_count_list = []

### PLOTS GRAPH WITH IMMIGRATION DATA ###
    ### (horizontal bar graph) ###
for boroh in borohs:
    ### associates the imiigrant count as keys and the boroughs as immi_count_by_borough ###
    ### -- also appends data for use in the math later -- ##
    boroh_df = immi_data[immi_data['BOROUGH / COMMUNITY']== boroh].groupby('BOROUGH / COMMUNITY')['Census Tract']
    immi_count_by_boroh = boroh_df.sum()
    immi_count_list.append(boroh_df.sum())

    ### plots the graph ###
    plt.barh(immi_count_by_boroh.keys(), immi_count_by_boroh, label = boroh)
plt.title('After-School services provided for immigrants in the Boroughs \n of New York \n (updated as of January 15, 2020)')
plt.show()

##makes the immigrant total##
immi_census = immi_data["Census Tract"]
immi_total = immi_census.sum()


### --PERCENTAGE CALCULATION FOR ILLITERACY AND POVERTY (borough calculation)-- ###

## -- I wanna keep this short and painless so im finna skip -- ##
## -- the whole calling each borough out of a list -- ##

print('ILLITERATE ADULTS ENLISTED IN NDA AID PROGRAMS PERCENTAGES IN DIFFERENT BOROUGHS')

def illit_percent_calc():
    #brooklyn
    brooklyn_per = (illit_count_list[0] / illit_total)*100
    if numDigits(brooklyn_per) > 2:
        rounded_brooklyn_per = round(brooklyn_per, 2)
    print(rounded_brooklyn_per)
    #Staten Island
    staten_island_per = (illit_count_list[1] / illit_total)*100
    if numDigits(staten_island_per) > 2:
        rounded_staten_island_per = round(staten_island_per, 2)
    print(rounded_staten_island_per)
    #queens
    queens_per = (illit_count_list[2] / illit_total)*100
    if numDigits(queens_per) > 2:
        rounded_queens_per = round(queens_per, 2)
    print(rounded_queens_per)
    #bronx
    bronx_per = (illit_count_list[3] / illit_total)*100
    if numDigits(bronx_per) > 2:
        rounded_bronx_per = round(bronx_per, 2)
    print(rounded_bronx_per)
    #manhatten
    manhatten_per = (illit_count_list[4] / illit_total)*100
    if numDigits(manhatten_per) > 2:
        rounded_manhatten_per = round(manhatten_per, 2)
    print(rounded_manhatten_per)
illit_percent_calc()

print('IMMIGRANTS ENLISTED IN AFTER-SCHOOL AID PERCENTAGES IN DIFFERENT BOROUGHS')

def immi_percent_calc():
    #brooklyn
    brooklyn_per = (immi_count_list[0] / immi_total)*100
    if numDigits(brooklyn_per) > 2:
        rounded_brooklyn_per = round(brooklyn_per, 2)
    print(rounded_brooklyn_per)
    #Staten Island
    staten_island_per = (immi_count_list[1] / immi_total)*100
    if numDigits(staten_island_per) > 2:
        rounded_staten_island_per = round(staten_island_per, 2)
    print(rounded_staten_island_per)
    #queens
    queens_per = (immi_count_list[2] / immi_total)*100
    if numDigits(queens_per) > 2:
        rounded_queens_per = round(queens_per, 2)
    print(rounded_queens_per)
    #bronx
    bronx_per = (immi_count_list[3] / immi_total)*100
    if numDigits(bronx_per) > 2:
        rounded_bronx_per = round(bronx_per, 2)
    print(rounded_bronx_per)
    #manhatten
    manhatten_per = (immi_count_list[4] / immi_total)*100
    if numDigits(manhatten_per) > 2:
        rounded_manhatten_per = round(manhatten_per, 2)
    print(rounded_manhatten_per)
immi_percent_calc()