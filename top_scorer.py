import pandas as pd

# read csv 
player_game_data_df = pd.read_csv("NBA Data/Player Game Data.csv")

# make a copy of player_game_data_df
top_scorer_df = player_game_data_df.copy()


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
top_scorer_df["avg_ppg"] = top_scorer_df.groupby(
    ["PLAYER_ID"])["PTS"].transform("mean")


# rank players on each team by avg_ppg
top_scorer_df["team_avg_ppg_ranking"] = top_scorer_df.groupby(
    ["TEAM_ID"])["avg_ppg"].rank(ascending=False)


# filter dataframe to include only the top player for each team



# sort players by avg_ppg



# save the dataframe
top_scorer_df.to_csv("NBA Data/Generated/Top Scorers Per Team.csv", index = False)
 
######################## START OF DEBUGGING SPACE #####################################
pd.set_option('display.max_columns', None)
print(top_scorer_df.head(5))
########################## END OF DEBUGGING SPACE #####################################