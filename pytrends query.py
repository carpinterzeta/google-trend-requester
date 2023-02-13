from pytrends.request import TrendReq

# Create a pytrends object
pytrends = TrendReq()

# Define the search term and time frame
keyword = 'Python programming'
timeframe = 'today 3-m'

# Build the payload
pytrends.build_payload(kw_list=[keyword], timeframe=timeframe)

# Get the interest over time data
interest_over_time_df = pytrends.interest_over_time()

# Print the results
print(interest_over_time_df.head())
