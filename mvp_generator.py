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

######################## START OF DEBUGGING SPACE #####################################
pd.set_option('display.max_columns', None)
print(mvp_ranking_df.head(20))
########################## END OF DEBUGGING SPACE #####################################



# caculate avg PAR for the season
# calculate total PAR for the season


# calculate player win/loss bonus for each game
# calculate player total win bonus

# calculate mvp score for each player

# remove duplicates
# rank
# choose desired columns

# save 





