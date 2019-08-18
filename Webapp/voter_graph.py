import pandas as pd

def graph_stats():
    df = pd.read_csv("graphs.csv")
    constituency = df['Name of the Parliamentary Constituency'].tolist()
    registered_voters = df['Men Electors'].tolist()
    actual_vote_count = df['Men Voters'].tolist()

    constituency = constituency[0:8]
    registered_voters = registered_voters[0:8]
    actual_vote_count = actual_vote_count[0:8]
    return(constituency,registered_voters,actual_vote_count)