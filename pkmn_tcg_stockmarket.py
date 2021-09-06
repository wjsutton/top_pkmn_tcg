import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from pathlib import Path

today = date.today()

packs = ['swsh07-evolving-skies',
'swsh06-chilling-reign',
'swsh05-battle-styles',
'first-partner-pack',
'shining-fates',
'shining-fates-shiny-vault',
'mcdonalds-25th-anniversary-promos',
'swsh04-vivid-voltage',
'champions-path',
'swsh03-darkness-ablaze',
'battle-academy',
'swsh02-rebel-clash',
'swsh01-sword-and-shield-base-set',
'swsh-sword-and-shield-promo-cards',
'sm-cosmic-eclipse',
'mcdonalds-promos-2019',
'hidden-fates',
'hidden-fates-shiny-vault',
'sm-unified-minds',
'sm-unbroken-bonds',
'detective-pikachu',
'sm-team-up',
'mcdonalds-promos-2018',
'sm-lost-thunder',
'miscellaneous-cards-and-products',
'dragon-majesty',
'sm-celestial-storm',
'sm-forbidden-light',
'sm-trainer-kit-alolan-sandslash-and-alolan-ninetales',
'sm-ultra-prism',
'mcdonalds-promos-2017',
'sm-crimson-invasion',
'shining-legends',
'sm-burning-shadows',
'alternate-art-promos',
'sm-guardians-rising',
'sm-trainer-kit-lycanroc-and-alolan-raichu',
'sm-base-set',
'sm-promos',
'xy-evolutions',
'deck-exclusives',
'xy-steam-siege',
'league-and-championship-cards',
'xy-fates-collide',
'xy-trainer-kit-pikachu-libre-and-suicune',
'generations',
'generations-radiant-collection',
'xy-breakpoint',
'mcdonalds-promos-2015',
'xy-breakthrough',
'xy-ancient-origins',
'xy-roaring-skies',
'xy-trainer-kit-latias-and-latios',
'jumbo-cards',
'double-crisis',
'xy-primal-clash',
'xy-trainer-kit-bisharp-and-wigglytuff',
'xy-phantom-forces',
'xy-furious-fists',
'mcdonalds-promos-2014',
'xy-flashfire',
'xy-trainer-kit-sylveon-and-noivern',
'xy-base-set',
'xy-promos',
'legendary-treasures',
'legendary-treasures-radiant-collection',
'plasma-blast',
'plasma-freeze',
'plasma-storm',
'boundaries-crossed',
'dragons-exalted',
'dark-explorers',
'noble-victories',
'bw-trainer-kit-excadrill-and-zoroark',
'emerging-powers',
'black-and-white',
'call-of-legends',
'professor-program-promos',
'triumphant',
'undaunted',
'pikachu-world-collection-promos',
'unleashed',
'hgss-promos',
'arceus',
'supreme-victors',
'burger-king-promos',
'countdown-calendar-promos',
'legends-awakened',
'great-encounters',
'dp-trainer-kit-manaphy-and-lucario',
'diamond-and-pearl',
'diamond-and-pearl-promos',
'dragon-frontiers',
'crystal-guardians',
'delta-species',
'unseen-forces',
'emerald',
'deoxys',
'ex-battle-stadium',
'kids-wb-promos',
'team-magma-vs-team-aqua',
'dragon',
'aquapolis',
'best-of-promos',
'team-rocket',
'fossil',
'wotc-promo',
'blister-exclusives',
'base-set',
'base-set-shadowless',
'base-set-2',
'black-and-white-promos',
'dp-training-kit-1-blue',
'dp-training-kit-1-gold',
'dragon-vault',
'ex-trainer-kit-1-latias-and-latios',
'ex-trainer-kit-2-plusle-and-minun',
'expedition',
'firered-and-leafgreen',
'gym-challenge',
'gym-heroes',
'heartgold-soulsilver',
'hgss-trainer-kit-gyarados-and-raichu',
'hidden-legends',
'holon-phantoms',
'jungle',
'kalos-starter-set',
'legend-maker',
'legendary-collection',
'majestic-dawn',
'mcdonalds-promos-2011',
'mcdonalds-promos-2012',
'mysterious-treasures',
'neo-destiny',
'neo-discovery',
'neo-genesis',
'neo-revelation',
'next-destinies',
'nintendo-promos',
'platinum',
'pop-series-1',
'pop-series-2',
'pop-series-3',
'pop-series-4',
'pop-series-5',
'pop-series-6',
'pop-series-7',
'pop-series-8',
'pop-series-9',
'power-keepers',
'rising-rivals',
'ruby-and-sapphire',
'rumble',
'sandstorm',
'secret-wonders',
'skyridge',
'southern-islands',
'stormfront',
'team-rocket-returns']

for i in range(len(packs)):

    pack = packs[i]
    print(pack)

    url = "https://shop.tcgplayer.com/price-guide/pokemon/" + pack
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    tbl = soup.find("table")
    data_frame = pd.read_html(str(tbl))[0]
    urls = soup.find_all("div",{"class":"thumbnail"},"a")   

    card_urls = []
    img_urls = []

    for a in urls:
        card = a.select('a')
        card_urls = card_urls + [card[0]['href']]
        image = a.select('img')
        img_urls = img_urls + [image[0]['src']]

    data_frame['date'] = today
    data_frame['pack'] = pack
    data_frame['card_urls'] = card_urls
    data_frame['img_urls'] = img_urls
    data_frame['img_urls'] = data_frame['img_urls'].str.replace('_25w','')
    data_frame['img_urls'] = 'https://product-images.tcgplayer.com/' + data_frame['img_urls'].str.extract('(\d+)') + '.jpg'

    data_frame['Market Price'] = data_frame['Market Price'].str.replace('$','',regex=False)
    data_frame['Market Price'] = data_frame['Market Price'].str.replace('—','',regex=False)
    data_frame['Market Price'] = data_frame['Market Price'].str.replace(',','',regex=False)
    data_frame['Market Price'] = pd.to_numeric(data_frame['Market Price']) 
    data_frame = data_frame.rename(columns={'Market Price':'market_price_in_dollars'})

    del data_frame['Unnamed: 5']
    del data_frame['Listed Median']
    del data_frame['Number']

    if i == 0:
        output_df = data_frame
    else:
        output_df = output_df.append(data_frame)

print('Done!')
print(len(output_df))

my_file = Path("data\\pkmn_tcg_stockmarket.csv")
if my_file.is_file():
    previous_data = pd.read_csv('data\\pkmn_tcg_stockmarket.csv')
    output_df = output_df.append(previous_data, ignore_index=True)

output_df.to_csv('data\\pkmn_tcg_stockmarket.csv', index=False)

# upload to googlesheets
