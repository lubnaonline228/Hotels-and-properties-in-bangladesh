# hotels_and_properties_in_bd
This repository has been created as a part of the Capstone Project work submission for the Dokkho Career Data Science Course, Cohort-3. It summarizes data collected about hotels and properties of Bangladesh as listed in the Booking.com website

## Problem Statement
The goal of this project is to gather information about hotels and properties of Bangladesh listed in the [Booking.com website](https://www.booking.com/searchresults.html?ss=Bangladesh&ssne=Bangladesh&ssne_untouched=Bangladesh&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=18&dest_type=country&ltfd=5%3A1%3A11-2023_12-2023_1-2024%3A1%3A&group_adults=2&no_rooms=1&group_children=0)

At the end of the scraping process I ended up with data for 551 hotels and properties. These were the fields that I extracted: 
1. Name of property
2. City
3. Price
4. Number of starts (for example 5-star, 4-star, etc.)
5. Rating text given by Booking.com for the hotel (for example 'Good', 'Very Good', 'Excellent')
6. Number of reviews from guests
7. Total rating given by guests (out of 10)
8. Individual ratings given by guests. This included ratings for:
     Staff (out of 10)
     Facilities (out of 10)
     Cleanliness (out of 10)
     Comfort (out of 10)
     Value for money (out of 10)
     Location (out of 10)

The code for the scraper is in [this link](https://github.com/lubnaonline228/hotels_and_properties_in_bd/blob/main/scraper_for_properties_in_bangladesh.py).

After scraping the relevant data, I used a separate code to process, transform, and clean the dataset, so it can be used for further analysis.  

The code for the data cleaning is in [this link](https://colab.research.google.com/drive/1WAU2Eawi-YsQIHe4wdhNEL6kKDSIVp_C?usp=sharing).

After running this code, you should get a file named `cleaned_dataset_properties_and_hotels.csv`. Alternatively you can get this dataset from [here](https://github.com/lubnaonline228/hotels_and_properties_in_bd/blob/main/cleaned_dataset_properties_and_hotels.csv).

Finally, I used the scraped and cleaned dataset to understand and analyze the data using the Tableau Dashboard. Here are the questions that I considered:
1. Which 3 cities have the most hotels and properties listed on Booking.com?
2. Is there a correlation between rating and the average price of hotels?
3. Which city has the most expensive 4-star hotels?
4. Are there any 5-star hotels in Rajshahi? What is the average price of a 4-star hotel in Rajshahi?
5. Which 3 cities have the highest rating on Booking.com?
6. In which cities can I find 4-star hotels in the price range of BDT 3,000 to 5,000?

You can view the public dashboards in the following 2 links: <br>
https://public.tableau.com/app/profile/nahid.akhtar/viz/HotelandPropertyDatafromBooking_com/Dashboard2?publish=yes
https://public.tableau.com/app/profile/nahid.akhtar/viz/HotelandPropertyDatafromBooking_com/Dashboard1?publish=yes

Here, the first dashboard displays a data summary by City. All the records are linked to the first bar chart, so you can easily filter the entire dashboard by city, by selecting the required cities from the 'Number of hotels by city' bar chart.

![2023-12-17_14-21-12](https://github.com/lubnaonline228/hotels_and_properties_in_bd/assets/46602183/dfa76241-8a26-42a4-a2f8-b0483c738ec9)

The second dashboard displays other relevant analytics, like 'average price by city and star rating', as well as 'highest rating by city'.

![2023-12-17_16-35-50](https://github.com/lubnaonline228/hotels_and_properties_in_bd/assets/46602183/a8e4940b-e86f-4e58-b2f0-90ee0840903c)

## Findings and Observations from the Dashboards
1. Dhaka, Sylhet, and Cox's Bazar have the most hotels and properties listed on Booking.com
![2023-12-17_16-36-39](https://github.com/lubnaonline228/hotels_and_properties_in_bd/assets/46602183/9f1c8ef9-ec55-48fb-91c0-e462421ae819)

2. There is fairly good correlation between rating and average price, even though there are some cases where average price of a high-rated hotel is less. This could probably be due to discounts provided by certain hotels.
![2023-12-17_16-39-17](https://github.com/lubnaonline228/hotels_and_properties_in_bd/assets/46602183/94d8c8a6-becd-4e36-bc5b-e25ac84826f7)

3. Dhaka has the most expensive 4-star hotels, since the average price of 4-star hotels in Dhaka are the highest. Second and third most expensive are Jessore and Chittagong respectively.
![2023-12-17_16-41-05](https://github.com/lubnaonline228/hotels_and_properties_in_bd/assets/46602183/27a01627-b69d-4e34-9271-2a1ec23b43c8)

4. There are no 5-star hotels in Rajshahi. The average price of a 4-star hotel in Rajshahi is BDT 4,233.

5. Sylhet, Dhaka, and Khulna have the highest rating on Booking.com (all have an average rating above 9 out of 10)
6. You can find a 4-star hotel in the price range of BDT 3,000 to 5,000 in Khulna, Rajshahi, and Sylhet.
7. The only Bangladeshi Hotel that got an 'Exceptional' rating on Booking.com is in Sylhet, and it has an average price of BDT 4,493.
8. Hotels of Bandarban have the lowest public rating.

## Build from Sources and Run the Selenium Scraper
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
