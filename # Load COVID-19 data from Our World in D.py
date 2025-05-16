# Load COVID-19 data from Our World in Data
def fetch_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    response = requests.get(url)
    data = pd.read_csv(StringIO(response.text))
    return data

# Filter data for a specific country
def get_country_data(df, country):
    country_data = df[df['location'] == country]
    country_data = country_data[['date', 'total_cases', 'total_deaths', 'people_vaccinated']]
    country_data['date'] = pd.to_datetime(country_data['date'])
    return country_data

# Plot data
def plot_country_data(country_data, country):
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['date'], country_data['total_cases'], label='Total Cases')
    plt.plot(country_data['date'], country_data['total_deaths'], label='Total Deaths')
    plt.plot(country_data['date'], country_data['people_vaccinated'], label='Vaccinated', linestyle='--')
    plt.title(f'COVID-19 Stats for {country}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main function
def main():
    print("Fetching latest COVID-19 data...")
    data = fetch_data()
    
    country = input("Enter a country (e.g., United States, India, Brazil): ")
    if country not in data['location'].unique():
        print("Country not found in the dataset.")
        return
    
    country_data = get_country_data(data, country)
    plot_country_data(country_data, country)

if __name__ == "__main__":
    main()
