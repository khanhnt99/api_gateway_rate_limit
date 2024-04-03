#!usr/bin/env python3
import random
import datetime
from datetime import timedelta

def init_data(num_request):
  # timestamps = [
  #   "2024-01-01T00:13:05Z",
  #   "2024-01-01T00:27:31Z",
  #   "2024-01-01T00:45:27Z",
  #   "2024-01-01T01:00:49Z",
  #   "2024-01-01T01:00:49Z",
  #   "2024-01-01T01:15:45Z",
  #   "2024-01-01T01:20:01Z",
  #   "2024-01-01T01:52:15Z",
  #   "2024-01-01T01:54:00Z",
  #   "2024-01-01T02:00:00Z",
  # ]

  # Generate a random year between 2020 and 2024
  year = random.randint(2020, 2024)

  # Generate a random month
  month = random.randint(1, 12)

  # Generate a random day within the selected month
  if month in [4, 6, 9, 11]:
    day = 30
  elif month == 2:
    day = 28
  else: 
    day = 31

  timestamps = []

  for i in range(0, num_request):
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)

    random_datetime = datetime.datetime(year, month, day, hours, minutes, seconds)
    iso_timestamp = random_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    timestamps.append(iso_timestamp)
  
  return timestamps

def rate_limit_request(num_request, rate_limit):

  result = None
  return result

def main():
  timestamps = [
    "2024-01-01T00:13:05Z",
    "2024-01-01T00:27:31Z",
    "2024-01-01T00:45:27Z",
    "2024-01-01T01:00:49Z",
    "2024-01-01T01:00:49Z",
    "2024-01-01T01:15:45Z",
    "2024-01-01T01:20:01Z",
    "2024-01-01T01:52:15Z",
    "2024-01-01T01:54:00Z",
    "2024-01-01T02:00:00Z",
  ]

  print(init_data(10))

  # print(rate_limit_request(3, 10))

if __name__ == '__main__':
  main()