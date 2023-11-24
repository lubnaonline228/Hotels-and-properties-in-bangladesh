from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import pandas as pd

columns=["name","city","price","stars", "rating_text", "num_reviews","total_rating", "staff","facilities","cleanliness","comfort","value_for_money","location_rating"]

def main():
    property_count=0
    
    #Loading the Chrome Webdriver
    service = Service(executable_path='chromedriver-win64/chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    #Going over each page of the Booking.com website
    for offset_val in range(0,550,25):
        property_data=[]
        url=f"https://www.booking.com/searchresults.html?ss=Bangladesh&ssne=Bangladesh&ssne_untouched=Bangladesh&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=18&dest_type=country&ltfd=5%3A1%3A11-2023_12-2023_1-2024%3A1%3A&group_adults=2&no_rooms=1&group_children=0&offset={offset_val}"
        driver.get(url)

        #Going over each property card of the current Booking.com page
        property_cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        for property in property_cards:
            time.sleep(2)
            contents={}
            contents["name"] = property.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').text
            contents["city"] = property.find_element(By.CSS_SELECTOR,'span[data-testid="address"]').text
            contents["price"] = property.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').text
            try:
                rating_block=property.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]').text
                rating=rating_block.split('\n')
                contents["total_rating"]=rating[0]
                contents["rating_text"]=rating[1]
                number_of_reviews=rating[2].split(' ')
                contents["num_reviews"]=number_of_reviews[0]
            except:
                contents["total_rating"]=0
                contents["rating_text"]="Review score"
                contents["num_reviews"]=0
            try:
                star_panel=property.find_element(By.CSS_SELECTOR,'div[data-testid="rating-stars"]')
                star_panel=star_panel.find_elements(By.TAG_NAME,'span')
                star_count=len(star_panel)
            except:
                star_count=0
            contents["stars"] = star_count

            # Now opening each hotel's page one at a time to obtain other details
            property.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').click()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)
            try:
                contents["staff"]=driver.find_element(By.CSS_SELECTOR,'div[id=":r22:-label"]').text
            except:
                contents["staff"]=-1
            try:
                contents["facilities"]=driver.find_element(By.CSS_SELECTOR,'div[id=":r23:-label"]').text
            except:
                contents["facilities"]=-1
            try:
                contents["cleanliness"]=driver.find_element(By.CSS_SELECTOR,'div[id=":r24:-label"]').text
            except:
                contents["cleanliness"]=-1
            try:
                contents["comfort"]=driver.find_element(By.CSS_SELECTOR,'div[id=":r25:-label"]').text
            except:
                contents["comfort"]=-1
            try:
                contents["value_for_money"]=driver.find_element(By.CSS_SELECTOR,'div[id=":r26:-label"]').text
            except:
                contents["value_for_money"]=-1
            try:
                contents["location_rating"]=driver.find_element(By.CSS_SELECTOR,'div[id=":r27:-label"]').text
            except:
                contents["location_rating"]=-1
            try:
                contents["sustainability"]=driver.find_element(By.XPATH,'//*[@class="sustainability-badge-mfe-wrapper"]/div/span/span/div/span[2]').text
            except:
                contents["sustainability"]="None"
            #Appending the collected data into the 'property_data' list
            property_data.append(contents) 
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            property_count=property_count+1
            print(property_count)
    #Storing all the collected data into a dataframe
    df=pd.DataFrame(data=property_data,columns=columns)
    #print(df)
    #Saving the dataframe in a CSV file
    df.to_csv("properties_and_hotels_bd.csv", index=False)
        
    driver.close()


if __name__=="__main__":
    main()