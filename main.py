#########################################################################
# Title: PYTHON Project Scenario - Data Analysis
# Description: This program allows user to analyse countries, regions and year
# Name: Muhammad Aimar Bin Kamaruzzaman
# Group Name: Attack on Python
# Class: PN2004J
# Date: 9 February 2021
# Version: 1
#########################################################################

#########################################################################
# import pandas for data analysis
import pandas as pd

# import matplotlib for graphics implementation
import matplotlib.pyplot as pit
#########################################################################

#########################################################################
# CLASS Branch - Data Analysis
# load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)

#########################################################################
# CLASS Branch: End of Code
#########################################################################

#########################################################################
# FUNCTION Branch - sortCountry
# parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  # initializing dataframe for SEA region
  sea_region = df.iloc[348:, 0:9]

  # display region assigned by teacher
  print("Region: Southeast Asia")

  # displays number of countries in the region by counting the number of columns
  print("Total number of countries:", str(len(sea_region.columns) - 2))

  # displays year range
  print("Period: 2007 - 2017" + "\n")

  # displays dataframe of SEA region
  print(sea_region)
  
  # displays top 3 countries of the region
  print("\n" + "The top 3 countries of visitors to Singapore over the span of 10 years:" + "\n")
  # takes the specified year range, sums up all the values vertically, sorts the value in descending order and takes the largest 3 values of the dataframe
  top3 = df.iloc[348:, 2:9].sum(axis=0).sort_values(ascending=False).nlargest(3).reset_index()
  # sort sum value output into columns based on country and visitors 
  top3.columns = ['Country', 'Visitors']
  # change index to represent top 3
  top3.index = ['1)', '2)', '3)']
  # print top 3
  print(top3)

  return
  
#########################################################################
# FUNCTION Branch: End of Code
#########################################################################

#########################################################################
# Main Branch
#########################################################################
if __name__ == '__main__':
  
  # Project Title
  print("")
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')
  print("")

  # perform data analysis on specific excel (CSV) file
  DataAnalysis()

  # load excel data (CSV format) to dataframe - 'df'
  df = pd.read_csv('MonthyVisitors.csv')

  # show available regions to user
  available_Regions = ['Southeast Asia', 'Asia Pacific', 'South Asia Pacific', 'Middle East', 'Europe', 'North America', 'Australia', 'Africa']
  print( "\n\n" + "Regions:", available_Regions)
  # prompt user to enter a region
  region = str(input("Enter a region: "))
  print("")

  # error checking for each region, if region isdigit, prompt error. Else (if no error), initialize each of the region's respective variable with their respective dataframe
  while True:
    # variable
    i = 0
    # if user enter empty string, loop input until valid
    if region == "":
      # prompt user an input
      region = str(input("Please enter a region: "))
    elif region.isdigit():
      print("Invalid format.")
      break
    else:
      if region == 'Southeast Asia':
        SEA_region = df.iloc[:,2:9]
        i += 1
        break
      elif region == 'Asia Pacific':
        AP_region = df.iloc[:,9:14]
        i += 1
        break
      elif region == 'South Asia Pacific':
        SAP_region = df.iloc[:,14:17]
        i += 1
        break
      elif region == 'Middle East':
        ME_region = df.iloc[:,17:20]
        i += 1
        break
      elif region == 'Europe':
        EU_region = df.iloc[:,20:31]
        i += 1
        break
      elif region == 'North America':
        NA_region = df.iloc[:,31:33]
        i += 1
        break
      elif region == 'Australia':
        AUS_region = df.iloc[:,33:35]
        i += 1
        break
      elif region == 'Africa':
        AF_region = df.iloc[:,35:36]
        i += 1
        break
      else:
        print("Error. Please check for spelling errors.")
        break

  # error checking for year, if year is not integer, prompt invalid format. Else (if no error), print user's chosen region and year as a dataframe
  if i >= 1: # 'i' acts as a token; if value is not equal or more, program won't run this part of code
    # show year range for user to refer
    year_range = ['1978 - 1987', '1988 - 1997', '1998 - 2007', '2008 - 2017']
    while True:
      print("Periods:", year_range)
      year = input("Enter the starting year: ")
      try:
        year = int(year)
      except:
        print("\nInvalid format.")
        break
      else:
        # 1978
        if year == 1978 and region == 'Southeast Asia':
          SEA_region = df.iloc[:120,:9]
          region_df = df.iloc[:120,2:9]
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(SEA_region.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 1978 and region == 'Asia Pacific':
          years = df.iloc[:120,:2] # dataframe1 (year, month)
          region_df = df.iloc[:120,9:14] #dataframe2 (countries of region)
          # combines 2 dataframe into 1 using the .join function
          result = years.join(region_df)
          # print region selected by user
          print("\n" + "Region:", region)
          # print total number of countries in the chosen region
          print("Total number of countries:", str(len(result.columns) - 2))
          # print period selected by user
          print("Period:", year_range[0] + "\n")
          # print out result of the combination of dataframes
          print(result)
          i += 1
          break
        # same process for the rest below
        elif year == 1978 and region == 'South Asia Pacific':
          years = df.iloc[:120,:2]
          region_df = df.iloc[:120,14:17]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Middle East':
          years = df.iloc[:120,:2]
          region_df = df.iloc[:120,17:20]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Europe':
          years = df.iloc[:120,:2]
          region_df = df.iloc[:120,20:31]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'North America':
          years = df.iloc[:120,:2]
          region_df = df.iloc[:120,31:33]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Australia':
          years = df.iloc[:120,:2]
          region_df = df.iloc[:120,33:35]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Africa':
          years = df.iloc[:120,:2]
          region_df = df.iloc[:120,35:36]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[0] + "\n")
          print(result)
          i += 1
          break
        # 1988
        elif year == 1988 and region == 'Southeast Asia':
          SEA_region = df.iloc[120:240,:9]
          region_df = df.iloc[120:240,2:9]
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(SEA_region.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 1988 and region == 'Asia Pacific':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,9:14]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'South Asia Pacific':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,14:17]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Middle East':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,17:20]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Europe':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,20:31]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'North America':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,31:33]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Australia':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,33:35]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Africa':
          years = df.iloc[120:240,:2]
          region_df = df.iloc[120:240,35:36]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[1] + "\n")
          print(result)
          i += 1
          break
        # 1998
        elif year == 1998 and region == 'Southeast Asia':
          SEA_region = df.iloc[240:360,:9]
          region_df = df.iloc[240:360,2:9]
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(SEA_region.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 1998 and region == 'Asia Pacific':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,9:14]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'South Asia Pacific':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,14:17]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Middle East':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,17:20]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Europe':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,20:31]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'North America':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,31:33]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Australia':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,33:35]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Africa':
          years = df.iloc[240:360,:2]
          region_df = df.iloc[240:360,35:36]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[2] + "\n")
          print(result)
          i += 1
          break
        # 2008
        elif year == 2008 and region == 'Southeast Asia':
          SEA_region = df.iloc[360:,:9]
          region_df = df.iloc[360:,2:9]
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(SEA_region.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 2008 and region == 'Asia Pacific':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,9:14]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'South Asia Pacific':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,14:17]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Middle East':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,17:20]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Europe':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,20:31]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'North America':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,31:33]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Australia':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,33:35]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Africa':
          years = df.iloc[360:,:2]
          region_df = df.iloc[360:,35:36]
          result = years.join(region_df)
          print("\n" + "Region:", region)
          print("Total number of countries:", str(len(result.columns) - 2))
          print("Period:", year_range[3] + "\n")
          print(result)
          i += 1
          break
        else:
          print("\nError. Please ensure that you picked a valid year.")
          break

  # top 3 countries of user's selected region
  if i >= 2:
    print("\n" + "The top 3 countries of visitors to Singapore over the span of 10 years:" + "\n")
    # sum up all values in descending order and take largest 3 values
    top_3 = region_df.sum(axis=0).sort_values(ascending=False).nlargest(3).reset_index()
    # sort sum value output into columns based on country and visitors
    top_3.columns = ['Country', 'Visitors']
    #change index to represent top 3
    if len(top_3.index) == 3:
      top_3.index = ['1)', '2)', '3)']
      i += 1
    elif len(top_3.index) == 2:
      # if only 2 countries, apply 2 index
      top_3.index = ['1)', '2)']
      i += 1
      # if only 1 country, apply 1 index
    elif len(top_3.index) == 1:
      top_3.index = ['1)']
      i += 1
    else:
      # if none, print error
      print("Error.")

    if i >= 3:
      # print top 3
      print(top_3)

      # for pie chart use (user's pie chart)
      data = region_df.sum(axis=0).sort_values(ascending=False).reset_index()
      # column labels
      data.columns = ['Country', 'Visitors']
      # initialize variables and list
      visitors = []
      countries = []
      # take values of Visitors and Country and put it in their respective list
      visitors = data['Visitors'].tolist()
      countries = data['Country'].tolist()
      i += 1

  #########################################################################
  # Pie Chart (2 pie charts shown)
  #########################################################################
  if i >= 4:
    ### user input's countries and total visitors shown in pie chart (any region)###
    # slice is taken from the countries' total nf vumber oisitors
    user_slice = visitors
    # label is the countries of user's chosen region
    label = countries
    # distance away from the centre of the pie chart
    distance = 0.1
    # initialize variable and list
    explodes = []
    # for loop to append distance according to amount of region in countries
    for i in range(0, len(countries)):
      explodes.append(distance)
    
    # pie chart 1
    pit.figure(1)
    # configuration for Figure 1 (user's pie chart)
    pit.pie(user_slice, labels=label, explode=explodes, startangle=90, pctdistance=0.8, shadow=True, autopct='%1.2f%%', wedgeprops={'edgecolor': 'black'})
    if year == 1978:
      pit.title(f"{region} ({year_range[0]})")
    elif year == 1988:
      pit.title(f"{region} ({year_range[1]})")
    elif year == 1998:
      pit.title(f"{region} ({year_range[2]})")
    elif year == 2008:
      pit.title(f"{region} ({year_range[3]})")

    ### region assigned by teacher shown in pie chart (S.E.A region) ###
    # slices represents the number of visitors to SG in a span of 10 years from 2007 to 2017 according to their country
    slices = [27572424, 715883, 11337420, 1042608, 6548622, 3914607, 4945136]
    # labels represents the country
    labels = ['Indonesia', 'Brunei', 'Malaysia', 'Myanmar', 'Philippines', 'Vietnam', 'Thailand']
    # color customization
    colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f','#E29661', '#E261AF', '#9CE261']
    explode = [0, 0, 0.2, 0, 0, 0, 0]

    # pie chart 2
    pit.figure(2)
    # configuration for Figure 2 (Southeast Asia pie chart)
    pit.pie(slices, labels=labels, colors=colors, explode=explode, startangle=90, shadow=True, autopct='%1.2f%%', pctdistance=0.8, wedgeprops={'edgecolor': 'black'})
    # show title
    pit.title("Southeast Asia (2007 - 2017)")
    # to make sure that the pie chart fits the screen
    pit.tight_layout()

    # give user the option to view the pie chart of SEA region
    while True:
      graph = str(input( "\n\n" + f"View pie chart of Southeast Asia region and {region} region? [Y/N]" + "\n"))
      if graph == 'N':
        # if input is equal to 'N', program ends
        break
      elif graph != 'Y':
        # if input is not equal to 'Y', print invalid input
        print("Invalid input.")
        break
      else:
        # if input is equal to Y, show pie chart to user
        pit.show()
        break
  
  # note: move Figure 2 to see Figure 1 in the console
  # note to teacher: some pie charts might not work for periods between 1978 to 1995 as their values are either 0 or na (as seen on the excel sheet) 
#########################################################################
# Main Branch: End of Code
#########################################################################