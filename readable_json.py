# This python file is to help make the text from the api readable
def champ_stats_readable(data):
    """
    The function was created to help read the raw data from the API for champions
    
    Arguments:
    Data (str): raw string data of the champion's stats
    """
    champ_stats = data["stats"]
    print(data["stats"])