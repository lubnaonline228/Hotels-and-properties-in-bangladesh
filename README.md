# hotels_and_properties_in_bd
This repository has been created as a part of the Capstone Project work submission for the Dokkho Career Data Science Course, Cohort-3. It summarizes data collected about hotels and properties of Bangladesh as listed in the Booking.com website

## Problem Statement
The goal of this project is to gather information about hotels and properties of Bangladesh listed in the [Booking.com website](https://www.booking.com/searchresults.html?ss=Bangladesh&ssne=Bangladesh&ssne_untouched=Bangladesh&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=18&dest_type=country&ltfd=5%3A1%3A11-2023_12-2023_1-2024%3A1%3A&group_adults=2&no_rooms=1&group_children=0)

The code for the scraper is in [this link](https://github.com/lubnaonline228/hotels_and_properties_in_bd/blob/main/scraper_for_properties_in_bangladesh.py).

After scraping the relevant data, I used a separate code to process, transform, and clean the dataset, so it can be used for further analysis. 

The code for the data cleaning is in [this link](https://colab.research.google.com/drive/1WAU2Eawi-YsQIHe4wdhNEL6kKDSIVp_C?usp=sharing).

After running this code, you should get a file named `cleaned_dataset_properties_and_hotels.csv`. Alternatively you can get this dataset from [here](https://github.com/lubnaonline228/hotels_and_properties_in_bd/blob/main/cleaned_dataset_properties_and_hotels.csv).

## Build from Sources
1. Clone the repo:
```bash
git clone https://github.com/lubnaonline228/hotels_and_properties_in_bd.git
   ```

2. Initialize and activate virtual environment:
```bash
virtualenv ---no-site-packages venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Download Chrome Webdriver from https://chromedriver.chromium.org/downloads
   
5. Run the scraper:
```bash
python scraper_for_properties_in_bangladesh.py
```
6. You will get a file named `properties_and_hotels_bd.csv` containing all the scraped fields
Alternatively check our scraped data here: https://github.com/lubnaonline228/hotels_and_properties_in_bd/blob/main/properties_and_hotels_bd.csv

## Analytics
Tableau public view: <br>
https://public.tableau.com/app/profile/nahid.akhtar/viz/HotelandPropertyDatafromBooking_com/Dashboard2?publish=yes
https://public.tableau.com/app/profile/nahid.akhtar/viz/HotelandPropertyDatafromBooking_com/Dashboard1?publish=yes
