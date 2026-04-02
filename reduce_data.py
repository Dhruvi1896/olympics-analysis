import pandas as pd

# load original dataset
df = pd.read_csv("athlete_events.csv")

# reduce size (keep random 5000 rows)
df_small = df.sample(5000, random_state=42)

# save new file
df_small.to_csv("athlete_events_small.csv", index=False)

print("Done! Small file created")