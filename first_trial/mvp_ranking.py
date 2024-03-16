import pandas as ps

"""

Goal is to create an MVP algorithm. The algorithm will be based on the following:
pct of team points + pct of team assists + pct of team rebounds +- 0.25 wins and losses 

"""
# read CSV and save data frame as variable
player_game_data_df = ps.read_csv("NBA Data/Player Game Data.csv")

# make a copy of the source, save as variable
mvp_rankings_df = player_game_data_df.copy()

# calculate total team points, assists, and rebounds in each game
mvp_rankings_df["team_PTS"] = mvp_rankings_df.groupby(
    ["TEAM_ID", "GAME_ID"])["PTS"].transform("sum")

mvp_rankings_df["team_AST"] = mvp_rankings_df.groupby(
    ["TEAM_ID", "GAME_ID"])["AST"].transform("sum")

mvp_rankings_df["team_REB"] = mvp_rankings_df.groupby(
    ["TEAM_ID", "GAME_ID"])["REB"].transform("sum")

# calculate player share of team points, assists, and rebounds in each game
mvp_rankings_df["share_of_team_PTS"] = mvp_rankings_df["PTS"]/mvp_rankings_df["team_PTS"]

mvp_rankings_df["share_of_team_AST"] = mvp_rankings_df["AST"]/mvp_rankings_df["team_AST"]

mvp_rankings_df["share_of_team_REB"] = mvp_rankings_df["REB"]/mvp_rankings_df["team_REB"]


