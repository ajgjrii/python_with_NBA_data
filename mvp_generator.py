import pandas as pd

"""
The algorithm to calculate the MVP of the 2019 regular season will be determined by:

percentage of team points
+ percentage of team assists
+ percentage of team rebounds
+ .25 for each win
- .25 for each loss
"""

# read CSVs
player_game_data_df = pd.read_csv("NBA Data/Player Game Data.csv")


# make copy of dataframes
mvp_ranking_df = player_game_data_df.copy()

# calculate player share of PAR (points, assist, rebounds) for the season
# calculate share of PAR each player is responsible for
# caculate avg PAR for the season
# calculate total PAR for the season


# calculate player win/loss bonus for each game
# calculate player total win bonus

# calculate mvp score for each player

# remove duplicates
# rank
# choose desired columns

# save 





