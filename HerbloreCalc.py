# Herblore calculator for most efficient leveling
# Fast, balanced, cheapest

# pull data from api for each id
# organize everything into a Dataframe
# calculators for..

# imports
import requests
import pandas as pd
import json

# Grand Exchange API 
api = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="

# lists for each potion and their id's
#TODO put potion lists in another list 
attack = [121, 91, 221]
poison = [175, 93, 235]
 
# create dataframe and append potion rows to it
def df_func(pot_id, base_id, ingr_id):
    # request from GE API
    response1 = requests.get(api + str(pot_id))
    response2 = requests.get(api + str(base_id))
    response3 = requests.get(api + str(ingr_id))

    # get data from response
    pot_data = response1.json()
    base_data = response2.json()
    ingr_data = response3.json()

    # pulling price and name from data
    pot_price = pot_data['item']['current']['price']
    base_price = base_data['item']['current']['price']
    ingr_price = ingr_data['item']['current']['price']

    # remove comma
    pot_price = str(pot_price).replace(',', '')
    base_price = str(base_price).replace(',', '')
    ingr_price = str(ingr_price).replace(',', '')

    pot_name = pot_data['item']['name']
    base_name = base_data['item']['name']
    ingr_name = ingr_data['item']['name']

    # Dataframe
    df = pd.DataFrame()
    
    # making lists for dataframe
    pot_list = [pot_name]
    # base_list = [base_name]
    # ingr_list = [ingr_name]
    p_price_list = [pot_price]
    b_price_list = [base_price]
    i_price_list = [ingr_price]

    # Assigning lists to named columns
    df['Potion'] = pot_list
    df['Pot price'] = p_price_list
    df['Base price'] = b_price_list
    df['Ingr Price'] = i_price_list

    #TODO append to existing table
    #TODO add column for profit

    df

# Test
df_func(*attack)

#TODO while loop using list of lists
#TODO table data based on user entry for # of potions