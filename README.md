<h1 style="font-weight:normal">
  Top Pokemon from the Trading Card Game
</h1>


[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/top_pkmn_tcg.svg)](https://github.com/wjsutton/top_pkmn_tcg/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/top_pkmn_tcg.svg)](https://github.com/wjsutton/top_pkmn_tcg/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

Finding the top pokemon cards from the pokemon trading card game for a dataviz project


[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:


<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

## :a: About

The Pokemon trading card game has received attention recently which sparked this project

- `gtrends_extract.R` updates the google trends data on "Pokemon card" searches worldwide
- `get_card_prices.R` build the data set of card prices from tcgplayer.com
- `download_top_25_images.R` will find the top 25 most expensive cards and download their images
- `map_card_to_pokedex.R` will attempt to join the card names to pokedex entries, not a 100% match due to trainer and energy cards
- `refresh_all_datasets.R` runs the four scripts above in order for a general refresh of the datasets used in the Tableau dashboard


### 📈 See the Dashboard 

URL: [https://public.tableau.com/profile/wjsutton#!/vizhome/PokemonTradingCardPrices/Dashboard1](https://public.tableau.com/profile/wjsutton#!/vizhome/PokemonTradingCardPrices/Dashboard1)

<div style="width: 400px; overflow: hidden;margin: 0 10px 0 0">
<a href="https://public.tableau.com/profile/wjsutton#!/vizhome/PokemonTradingCardPrices/Dashboard1">
<img src='https://github.com/wjsutton/top_pkmn_tcg/blob/master/dashboard_image.png?raw=true' style="width: 400px">
</a>
</div>

