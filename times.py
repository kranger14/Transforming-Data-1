from dateutil.parser import parse
import read

times = read.load_data()

def extract_hour(timestamp):
    time = parse(timestamp)
    hour_time = time.hour
    return hour_time


times["hour_time"] = times['submission_time'].apply(extract_hour)
print(times["hour_time"].value_counts())