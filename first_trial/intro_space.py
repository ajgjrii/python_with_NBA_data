import pandas as pd

## read the dataframe and store it as a variable
player_game_data_df = pd.read_csv("NBA Data/Player Game Data.csv")

## Create a copy of player_game_data_df to preserve raw data
player_game_data_df_copy = player_game_data_df.copy()

## workspace


## create a new column named "PTS_AST_REB" which will sum the values 
## for each player in each game
player_game_data_df["PTS_AST_REB"] = (
    player_game_data_df["PTS"] 
    + player_game_data_df["AST"] 
    + player_game_data_df["REB"]
    )


# Save player_game_data_df as a csv. Running script again will overwrite 
# files with this same name, so no need to worry about duplicates.
player_game_data_df.to_csv("NBA Data/Copy of Player Game Data.csv", index = False)