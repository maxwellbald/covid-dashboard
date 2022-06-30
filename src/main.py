#from data import read_data
from visualization import make_plot, show_plots
from datetime import date 
from os.path import getctime
import plotly.express as px
import pandas as pd


def main():
    # Import Data
    #If data outdated, redownload dataset
    # today = date.today
    # filedate = date.getmtime("../data/external/owid-covid-data.json")
    # datecheck = filedate == today
    # if datecheck == 0:
    #     data = read_data("../data/external/owid-covid-data.json")
    # else:
    #     data = read_data("https://covid.ourworldindata.org/data/owid-covid-data.json")

    #Import and Organize Data (comment out later when including if statement)
    data = pd.read_csv("data/external/owid-covid-data.csv",sep=',')
    
    countries = ['Germany', 'Sweden','United Kingdom']
   # datacountries = data[data['location']==countries]
   # datacountries=datacountries.reset_index(drop=True)

    data_de = data[data['location']=='Germany']
    data_de = data_de.reset_index(drop=True)

    data_se = data[data['location']=='Sweden']
    data_se = data[data_se.reset_index(drop=True)]

    data_uk = data[data['location']=='United Kingdom']
    data_uk = data[data_uk.reset_index(drop=True)]

    #Make Plot of Covid Cases (by pop.) over time of Germany, Sweden, UK
    df = px.data_de
    fig_cases = px.line(df,x="date",y="total_cases_per_million")
    fig_cases.show()

    #Make Plot of Vaccinations (Fully Vaccinated by pop.) of Germany Sweden, UK



if __name__ == "__main__":
    main()
    