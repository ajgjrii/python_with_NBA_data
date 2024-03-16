import pandas as pd

# read CSVs
player_game_data_df = pd.read_csv("NBA Data/Player Game Data.csv")
team_games_played_df = pd.read_csv("NBA Data/Team Games Played.csv")

# make a copy of dataframes
top_scorer_df = player_game_data_df.copy()
games_played_df = team_games_played_df.copy()

# merge top_scorer_df with games_played_df
top_scorer_df = pd.merge(
    top_scorer_df,
    games_played_df,
    how = "left",
    on = "TEAM_ID"
    )

# create a new column "player_game_count" to count games player for each player
top_scorer_df["player_game_count"] = top_scorer_df.groupby(
    ["PLAYER_ID"])["PLAYER_ID"].transform("count")

# create a new column "player_game_percentage" to calculate percent of games played
top_scorer_df["player_game_percentage"] = (
    top_scorer_df["player_game_count"] / top_scorer_df["team_game_count"]
    )

# filter out players with <50% games played
cut_off = .5
top_scorer_df = top_scorer_df[
    top_scorer_df["player_game_percentage"] >= cut_off
]

# calculate avg ppg for each player using groupby and transform
"""
THIS CODE IS PRESEVED TO SHOW PROGRESSION OF TRANSFORM METHOD
top_scorer_df.groupby(["PLAYER_ID"])["PTS"].mean()

This is a personal note on commented code works. First off, the groupby function is 
called to pull every instance of a unique player ID. Then, the points column is used
to identify the column an aggregation will be performed on. Finally, the mean() method
calculates the mean for each unique player ID. 

"""
# the transform method allows us to write new ["avg_ppg"] to dataframe
# the round method at the end will round the calculation to nearest tenth
top_scorer_df["avg_ppg"] = top_scorer_df.groupby(
    ["PLAYER_ID"])["PTS"].transform("mean").round(1)


# remove duplicate rows for each player so .rank() works correctly
top_scorer_df = top_scorer_df.drop_duplicates(subset = ["PLAYER_ID"])

# rank players on each team by avg_ppg
top_scorer_df["team_avg_ppg_ranking"] = top_scorer_df.groupby(
    ["TEAM_ID"])["avg_ppg"].rank(ascending=False)

# filter dataframe to include only the top player for each team
top_scorer_df = top_scorer_df[
    top_scorer_df["team_avg_ppg_ranking"] == 1
]

# sort players by avg_ppg
top_scorer_df = top_scorer_df.sort_values(by = ["avg_ppg"], ascending = False)

# call only relevant columns
top_scorer_columns = [
    "PLAYER_ID",
    "PLAYER_NAME",
    "TEAM_ID",
    "TEAM_ABBREVIATION",
    "TEAM_NAME",
    "avg_ppg",
    "player_game_count",
    "player_game_percentage"
]

top_scorer_df = top_scorer_df[top_scorer_columns]

# save the dataframe
top_scorer_df.to_csv("NBA Data/Generated/Top Scorers Per Team.csv", index = False)
 
######################## START OF DEBUGGING SPACE #####################################
pd.set_option('display.max_columns', None)
print(top_scorer_df.head(20))
########################## END OF DEBUGGING SPACE #####################################