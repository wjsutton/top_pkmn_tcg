# Two sites
# https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards
# https://shop.tcgplayer.com/price-guide/pokemon
# https://www.pokegoldfish.com/prices/paper/standard

# dev portal http://developer.tcgplayer.com/

library(rvest)
library(dplyr)
library(stringr)

site_maps <- read.csv("data/pkmn_tcg_urls.csv", stringsAsFactors = F)
meta <- read.csv("data/pokemon.csv", stringsAsFactors = F)

meta <- meta[,c('name','generation','is_legendary','type1','type2')] 

for(i in 1:nrow(site_maps)){
  url <- site_maps$url[i]
  pkmn_html <- read_html(url)
  print(url)
  df <- pkmn_html %>% 
    html_node("table") %>% 
    html_table()
  
  df$card_url <- as.character(pkmn_html %>% html_nodes(".thumbnail a") %>% html_attr('href'))
  df$img_url <- as.character(pkmn_html %>% html_nodes(".thumbnail a img") %>% html_attr('src'))
  df$page_url <- site_maps$url[i]
  df$pack <- site_maps$pack[i]
  #head(df)
  
  if(i == 1){
    pkmn_df <- df
  }
  if(i > 1){
    pkmn_df <- rbind(pkmn_df,df)
  }
}
pkmn_df$fullsize_img_url <- gsub('_25w','',pkmn_df$img_url)
pkmn_df$market_price_in_dollars <- as.numeric(gsub('\\$|,', '', pkmn_df$`Market Price`)) 
pkmn_df$listed_median_in_dollars <- as.numeric(gsub('\\$|,', '', pkmn_df$`Listed Median`))
pkmn_df$market_price_rank <- rank(desc(if_else(is.na(pkmn_df$market_price_in_dollars),0,pkmn_df$market_price_in_dollars)),ties.method = "first")

pkmn_df <- pkmn_df[ , !(names(pkmn_df) %in% c("","Market Price","Listed Median"))]

pkmn_df <- sapply(pkmn_df, as.character) # since your values are `factor`
pkmn_df[is.na(pkmn_df)] <- ""


write.csv(pkmn_df,'data/pkmn_card_prices.csv',row.names = F)


