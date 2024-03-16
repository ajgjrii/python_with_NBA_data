import pandas as ps

# read CSV for team games played
team_games_played_df = ps.read_csv("NBA Data/Team Games Played.csv")


# read CSV for player game data
player_game_data_df = ps.read_csv("NBA Data/Player Game Data.csv")

#copy CSV to calculate scorer
top_scorer_per_team_df = player_game_data_df.copy()

# merge data frames
top_scorer_per_team_df = ps.merge(
    top_scorer_per_team_df,
    team_games_played_df,
    how = "left",
    on = "TEAM_ID"
)

# create a column that counts the number of games each player played
# this will add a column called "player_game_count" to the data frame
top_scorer_per_team_df["player_game_count"] = (
    top_scorer_per_team_df.groupby(["PLAYER_ID"])["PLAYER_ID"].transform("count")
)

# calculate percentage of games played for each player
top_scorer_per_team_df["player_game_percentage"] = (
    top_scorer_per_team_df["player_game_count"]/top_scorer_per_team_df["team_game_count"]
    )

# filter out players who did not play at least half of the games
# do this by creating a variable to do so
games_played_cutoff = 0.5
top_scorer_per_team_df = top_scorer_per_team_df[
    top_scorer_per_team_df["player_game_percentage"] >= games_played_cutoff
    ]

# calculate avg_ppg for each player
# variable is named (header created as "avg_ppg"). transform() method 
# adds a column to the dataframe
top_scorer_per_team_df["avg_ppg"]= top_scorer_per_team_df.groupby(
    ["PLAYER_ID"]
    )["PTS"].transform("mean")

# round avg_ppg to one decimal place
top_scorer_per_team_df["avg_ppg"] = top_scorer_per_team_df["avg_ppg"].round(1)

# Need to remove duplicate rows in dataframe to have one row per player
top_scorer_per_team_df = top_scorer_per_team_df.drop_duplicates(subset = ["PLAYER_ID"])

# rank players on each team by avg_ppg
# creates a column to with a rank for each player based on avg_ppg
top_scorer_per_team_df["team_avg_ppg_ranking"] = top_scorer_per_team_df.groupby(
    ["TEAM_ID"]
    )["avg_ppg"].rank(ascending = False)

# filter dataframe to include only top players on each team
top_scorer_per_team_df = top_scorer_per_team_df[
    top_scorer_per_team_df["team_avg_ppg_ranking"] == 1
]

# sort players by avg_ppg
top_scorer_per_team_df = top_scorer_per_team_df.sort_values(
    by = ["avg_ppg"], ascending = False
)

# Specify columns wanted for the final data frame
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

top_scorer_per_team_df = top_scorer_per_team_df[top_scorer_columns]

# save dataframe
top_scorer_per_team_df.to_csv("NBA Data/Top Scorers Per Team.csv",index = False)