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

  # print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  # print total number of countries in dataframe by counting the number of columns 
  print("Total number of countries:", str(len(df.columns) - 2))

  # display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  # initializing dataframe for SEA region
  sea_region = df.iloc[348:, 0:9]

  # display selected region
  print("\n\n" + "Southeast Asia region was selected.")

  # displays number of countries in the region by counting the number of columns
  print("Total number of countries:", str(len(sea_region.columns) - 2))

  # displays countries and year range
  print("The countries in the region are shown below.")
  print("Year range: 2007 - 2017" + "\n")

  # displays dataframe of SEA region
  print(sea_region)
  
  # displays top 3 countries of the region
  print("\n" + "The top 3 countries of visitors to Singapore from the selected region over the span of 10 years:" + "\n")
  print(" Country         Visitors")
  # takes the specified year range, sums up all the values vertically, sorts the value in descending order and takes the largest 3 values of the dataframe
  top3 = df.iloc[348:, 2:9].sum(axis=0).sort_values(ascending=False).nlargest(3)
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
  print( "\n\n" + "Available regions:", available_Regions)
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
  if i >= 1: # 'i' acts as a token; if no token, program won't run this part of code
    # show available year range to user
    year_range = ['1978 - 1987', '1988 - 1997', '1998 - 2007', '2008 - 2017']
    while True:
      print("Year range:", year_range)
      year = input("Enter the starting year: ")
      try:
        year = int(year)
      except:
        print("Invalid format.")
        break
      else:
        # note to teacher: some values have 0 in the dataframe because they are unassigned (check the excel file and you will understand)
        # 1978
        if year == 1978 and region == 'Southeast Asia':
          SEA_region = df.iloc[:120,:9]
          print("Total number of countries:", str(len(SEA_region.columns) - 2) + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 1978 and region == 'Asia Pacific':
          years = df.iloc[:120,:2] # dataframe1
          AP_region = df.iloc[:120,9:14] #dataframe2
          # combines 2 dataframe into 1 using the .join function
          result = years.join(AP_region)
          # print total number of countries in the chosen region
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          # print out result of the combination of dataframes
          print(result)
          i += 1
          break
        # same process for the rest below
        elif year == 1978 and region == 'South Asia Pacific':
          years = df.iloc[:120,:2]
          SAP_region = df.iloc[:120,14:17]
          result = years.join(SAP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Middle East':
          years = df.iloc[:120,:2]
          ME_region = df.iloc[:120,17:20]
          result = years.join(ME_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Europe':
          years = df.iloc[:120,:2]
          EU_region = df.iloc[:120,20:31]
          result = years.join(EU_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'North America':
          years = df.iloc[:120,:2]
          NA_region = df.iloc[:120,31:33]
          result = years.join(NA_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Australia':
          years = df.iloc[:120,:2]
          AUS_region = df.iloc[:120,33:35]
          result = years.join(AUS_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1978 and region == 'Africa':
          years = df.iloc[:120,:2]
          AF_region = df.iloc[:120,35:36]
          result = years.join(AF_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        # 1988
        elif year == 1988 and region == 'Southeast Asia':
          SEA_region = df.iloc[120:240,:9]
          print("Total number of countries:", str(len(SEA_region.columns) - 2) + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 1988 and region == 'Asia Pacific':
          years = df.iloc[120:240,:2]
          AP_region = df.iloc[120:240,9:14]
          result = years.join(AP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'South Asia Pacific':
          years = df.iloc[120:240,:2]
          SAP_region = df.iloc[120:240,14:17]
          result = years.join(SAP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Middle East':
          years = df.iloc[120:240,:2]
          ME_region = df.iloc[120:240,17:20]
          result = years.join(ME_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Europe':
          years = df.iloc[120:240,:2]
          EU_region = df.iloc[120:240,20:31]
          result = years.join(EU_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'North America':
          years = df.iloc[120:240,:2]
          NA_region = df.iloc[120:240,31:33]
          result = years.join(NA_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Australia':
          years = df.iloc[120:240,:2]
          AUS_region = df.iloc[120:240,33:35]
          result = years.join(AUS_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1988 and region == 'Africa':
          years = df.iloc[120:240,:2]
          AF_region = df.iloc[120:240,35:36]
          result = years.join(AF_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        # 1998
        elif year == 1998 and region == 'Southeast Asia':
          SEA_region = df.iloc[240:360,:9]
          print("Total number of countries:", str(len(SEA_region.columns) - 2) + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 1998 and region == 'Asia Pacific':
          years = df.iloc[240:360,:2]
          AP_region = df.iloc[240:360,9:14]
          result = years.join(AP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'South Asia Pacific':
          years = df.iloc[240:360,:2]
          SAP_region = df.iloc[240:360,14:17]
          result = years.join(SAP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Middle East':
          years = df.iloc[240:360,:2]
          ME_region = df.iloc[240:360,17:20]
          result = years.join(ME_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Europe':
          years = df.iloc[240:360,:2]
          EU_region = df.iloc[240:360,20:31]
          result = years.join(EU_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'North America':
          years = df.iloc[240:360,:2]
          NA_region = df.iloc[240:360,31:33]
          result = years.join(NA_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Australia':
          years = df.iloc[240:360,:2]
          AUS_region = df.iloc[240:360,33:35]
          result = years.join(AUS_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 1998 and region == 'Africa':
          years = df.iloc[240:360,:2]
          AF_region = df.iloc[240:360,35:36]
          result = years.join(AF_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        # 2008
        elif year == 2008 and region == 'Southeast Asia':
          SEA_region = df.iloc[360:,:9]
          print("Total number of countries:", str(len(SEA_region.columns) - 2) + "\n")
          print(SEA_region)
          i += 1
          break
        elif year == 2008 and region == 'Asia Pacific':
          years = df.iloc[360:,:2]
          AP_region = df.iloc[360:,9:14]
          result = years.join(AP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'South Asia Pacific':
          years = df.iloc[360:,:2]
          SAP_region = df.iloc[360:,14:17]
          result = years.join(SAP_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Middle East':
          years = df.iloc[360:,:2]
          ME_region = df.iloc[360:,17:20]
          result = years.join(ME_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Europe':
          years = df.iloc[360:,:2]
          EU_region = df.iloc[360:,20:31]
          result = years.join(EU_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'North America':
          years = df.iloc[360:,:2]
          NA_region = df.iloc[360:,31:33]
          result = years.join(NA_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Australia':
          years = df.iloc[360:,:2]
          AUS_region = df.iloc[360:,33:35]
          result = years.join(AUS_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        elif year == 2008 and region == 'Africa':
          years = df.iloc[360:,:2]
          AF_region = df.iloc[360:,35:36]
          result = years.join(AF_region)
          print("Total number of countries:", str(len(result.columns) - 2) + "\n")
          print(result)
          i += 1
          break
        else:
          print("Error. Please ensure that you picked a valid year.")
          break

  #########################################################################
  # Pie Chart
  #########################################################################
  if i >= 2:
    # slices represents the number of visitors to SG in a span of 10 years from 2007 to 2017 according to their country
    slices = [27572424, 715883, 11337420, 1042608, 6548622, 3914607, 4945136]
    # labels represents the country
    labels = ['Indonesia', 'Brunei', 'Malaysia', 'Myanmar', 'Philippines', 'Vietnam', 'Thailand']
    # color customization
    colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f','#E29661', '#E261AF', '#9CE261']
    explode = [0, 0, 0.2, 0, 0, 0, 0]

    # configuration for pie chart 
    pit.pie(slices, labels=labels, colors=colors, explode=explode, startangle=90, shadow=True, autopct='%1.2f%%', pctdistance=0.8, wedgeprops={'edgecolor': 'black'})
    # show title
    pit.title("Southeast Asia (2007 - 2017)")
    # to make sure that the pie chart fits the screen
    pit.tight_layout()

    # give user the option to view the pie chart of SEA region
    while True:
      graph = str(input( "\n\n" + "View pie chart of Southeast Asia region? [Y/N]" + "\n"))
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
  
#########################################################################
# Main Branch: End of Code
#########################################################################