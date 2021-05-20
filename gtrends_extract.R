library(gtrendsR)

search_terms <- c("pokemon cards")
results <- gtrends(keyword = search_terms,geo="", time = paste0("2004-01-01 ",Sys.Date()))
time_series <- results$interest_over_time

write.csv(time_series,"data/gtrends_pokemon_cards.csv",row.names = FALSE)