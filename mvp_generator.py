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

"""
#######################################################################################
This section is preserved as original code that was written. It works, but the code
that will be used is written in for loops. 
#######################################################################################
# calculate player share of PAR (points, assist, rebounds) for the season

# calculate team totals of PAR
mvp_ranking_df["team_PTS"] = mvp_ranking_df.groupby(
    ["TEAM_ID", "GAME_ID"])["PTS"].transform("sum")

mvp_ranking_df["team_AST"] = mvp_ranking_df.groupby(
    ["TEAM_ID", "GAME_ID"])["AST"].transform("sum")

mvp_ranking_df["team_REB"] = mvp_ranking_df.groupby(
    ["TEAM_ID", "GAME_ID"])["REB"].transform("sum")

# calculate share of PAR each player is responsible for
mvp_ranking_df["share_of_team_PTS"] = (
    mvp_ranking_df["PTS"] / mvp_ranking_df["team_PTS"])

mvp_ranking_df["share_of_team_AST"] = (
    mvp_ranking_df["AST"] / mvp_ranking_df["team_AST"])

mvp_ranking_df["share_of_team_REB"] = (
    mvp_ranking_df["REB"] / mvp_ranking_df["team_REB"])


# calculate each player's avg share of PAR for the season
mvp_ranking_df["season_avg_share_of_PTS"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["share_of_team_PTS"].transform("mean")

mvp_ranking_df["season_avg_share_of_AST"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["share_of_team_AST"].transform("mean")

mvp_ranking_df["season_avg_share_of_REB"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["share_of_team_REB"].transform("mean")


# calculate total PAR for the season
mvp_ranking_df["season_total_share_of_PTS"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["share_of_team_PTS"].transform("sum")

mvp_ranking_df["season_total_share_of_AST"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["share_of_team_AST"].transform("sum")

mvp_ranking_df["season_total_share_of_REB"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["share_of_team_REB"].transform("sum")

# calculate players average PAR for the season
mvp_ranking_df["season_avg_PTS"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["PTS"].transform("mean")

mvp_ranking_df["season_avg_AST"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["AST"].transform("mean")

mvp_ranking_df["season_avg_REB"] = mvp_ranking_df.groupby(
    ["PLAYER_ID"])["REB"].transform("mean")
"""

# define a list with the columns we wan to calculate for each player's share
share_columns = [
    "PTS",
    "AST",
    "REB"
]

# loop through each column in shared_columns
for column in share_columns: 
    # calculate the total team PAR in each game
    mvp_ranking_df["team_" + column] = mvp_ranking_df.groupby(
        ["TEAM_ID", "GAME_ID"])[column].transform("sum")
    
    # calculate the share of PAR each player is responsible for
    mvp_ranking_df["share_of_team_" + column] = (
        mvp_ranking_df[column] / mvp_ranking_df["team_" + column])
    
    # calculate each players average share of PAR for the season
    mvp_ranking_df["season_avg_share_of_" + column] = mvp_ranking_df.groupby(
        ["PLAYER_ID"])["share_of_team_" + column].transform("mean")
    
    # calculate each player's total share of PAR for the seasion
    mvp_ranking_df["season_total_share_of_" + column] = mvp_ranking_df.groupby(
        ["PLAYER_ID"])["share_of_team_" + column].transform("sum")
    
    # calculate each players average PAR for the seasion
    mvp_ranking_df["season_avg_" + column] = mvp_ranking_df.groupby(
        ["PLAYER_ID"])[column].transform("mean")


######################## START OF DEBUGGING SPACE #####################################
pd.set_option('display.max_columns', None)
print(mvp_ranking_df.head(20))
########################## END OF DEBUGGING SPACE #####################################






# calculate player win/loss bonus for each game
# calculate player total win bonus

# calculate mvp score for each player

# remove duplicates
# rank
# choose desired columns

# save 





