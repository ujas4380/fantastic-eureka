

from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq()

# Define keywords and timeframe
keywords = ["Data Science", "Machine Learning"]
pytrends.build_payload(keywords, timeframe='today 5-y')

# Fetch interest over time
data = pytrends.interest_over_time()
data.to_csv('google_trends_data.csv')
