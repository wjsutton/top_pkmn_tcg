
# Download Top 25 Valuable
library(dplyr)

prices <- read.csv('data/pkmn_card_prices.csv',stringsAsFactors = F)
top_25 <- filter(prices,market_price_rank<=25)
top_25 <- arrange(top_25,market_price_rank)

# Missing art cards
missing <- 'https://shop.tcgplayer.com/pokemon/xy-promos/champions-festival-2016-staff'
replacement <- 'https://www.magicmadhouse.co.uk/images/x-y-promo-xy176-champions-festival-staff-p238914-309000_medium.jpg'

#top_25 <- filter(top_25,card_url != missing)

images <- gsub('_25w','_200w',top_25$img_url)

images <- if_else(images == 'https://tcgplayer-cdn.tcgplayer.com/product/199329_200w.jpg',replacement,images)

for(i in 1:length(images)){
  num <- if_else(i<10,paste0('0',i),paste0(i))
  
  download.file(images[i],paste0('images/',num,'.jpg'), mode = 'wb')
}


#download.file(images[2],'test.jpg', mode = 'wb')