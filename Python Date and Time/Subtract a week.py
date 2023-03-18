from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)

past_date = given_date - timedelta(days=7)

print(past_date)