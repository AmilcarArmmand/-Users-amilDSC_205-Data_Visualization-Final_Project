import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

# Set up the page layout to use the full width of the web page
st.set_page_config(layout="wide")

# Function to load data from a given file path, caching the data to avoid reloading
def load_data(file_path):
    return pd.read_csv(file_path)

# Define the paths to the population and GDP data CSV files
population_file_path = os.path.join('data', 'population_percentage.csv')
gdp_file_path = os.path.join('data', 'gdp_percentage.csv')

# Load population and GDP data using the function defined above
population_df = load_data(population_file_path)
gdp_df = load_data(gdp_file_path)

st.title('Modernization of China: GDP and Population Growth Comparison')

# Get the list of countries from the population DataFrame for the dropdown
country_options = population_df['Country Name'].unique().tolist()

# Dropdown for selecting a country to compare with China
selected_country = st.selectbox(
    'Select a country to compare with China:',
    country_options, 
    index=country_options.index('United States')
)

# Slider for selecting the range of years to display
years = [col for col in population_df if col.isdigit()]
selected_years = st.slider(
    'Select a range of years:',
    int(min(years)), int(max(years)), 
    (int(min(years)), int(max(years)))
)

# Determine which years to display based on the slider selection
years_to_show = [year for year in years if int(year) >= selected_years[0] and int(year) <= selected_years[1]]

# Set up columns for side-by-side charts
col1, col2 = st.columns(2)

# Plot the population growth comparison in the first column
with col1:
    fig_population, ax_population = plt.subplots(figsize=(9, 4.5))
    # Plot China's population data
    china_data = population_df[population_df['Country Name'] == 'China'].loc[:, years_to_show].values.flatten()
    ax_population.plot(years_to_show, china_data, marker='o', label='China', linewidth=2)

    # Plot the selected country's population data if different from China
    if selected_country != 'China':
        country_data = population_df[population_df['Country Name'] == selected_country].loc[:, years_to_show].values.flatten()
        ax_population.plot(years_to_show, country_data, marker='o', label=selected_country, linewidth=2)

    # Configure the population plot
    ax_population.set_title('Population Growth (annual %) Comparison', fontsize=20, fontweight='bold')
    ax_population.set_xlabel('Year', fontsize=18)
    ax_population.set_ylabel('Population Growth (annual %)', fontsize=18)
    ax_population.legend()
    plt.xticks(years_to_show, rotation=45, ha="right", fontsize=14)
    ax_population.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax_population.axhline(0, color='grey', linewidth=1, linestyle='--')
    ax_population.tick_params(axis='y', labelsize=10)
    ax_population.grid(True, which='both', linestyle='--', linewidth=0.5)
    st.pyplot(fig_population)

# Plot the GDP growth comparison in the second column
with col2:
    fig_gdp, ax_gdp = plt.subplots(figsize=(9, 4.5))
    # Plot China's GDP data
    china_data = gdp_df[gdp_df['Country Name'] == 'China'].loc[:, years_to_show].values.flatten()
    ax_gdp.plot(years_to_show, china_data, marker='o', label='China', linewidth=2)

    # Plot the selected country's GDP data if different from China
    if selected_country != 'China':
        country_data = gdp_df[gdp_df['Country Name'] == selected_country].loc[:, years_to_show].values.flatten()
        ax_gdp.plot(years_to_show, country_data, marker='o', label=selected_country, linewidth=2)

    # Configure the GDP plot
    ax_gdp.set_title('GDP Growth (annual %) Comparison', fontsize=20, fontweight='bold')
    ax_gdp.set_xlabel('Year', fontsize=18)
    ax_gdp.set_ylabel('GDP Growth (annual %)', fontsize=18)
    ax_gdp.legend()
    plt.xticks(years_to_show, rotation=45, ha="right", fontsize=14)
    ax_gdp.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax_gdp.axhline(0, color='grey', linewidth=1, linestyle='--')
    ax_gdp.tick_params(axis='y', labelsize=10)
    ax_gdp.grid(True, which='both', linestyle='--', linewidth=0.5)
    st.pyplot(fig_gdp)
