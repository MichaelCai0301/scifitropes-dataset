import os
# pip3 install pandas
#! `python3 scifi_filter.py` to run!
import pandas as pd

# Create all_scifi_genres.csv by concatenating all CSV files in the scifi_genres directory
# ! NOTE: only run ONCE! Ty :)
all_scifi_exists = False
if not all_scifi_exists:
    input_folder = os.path.join(os.path.dirname(__file__), 'scifi_genres')
    output_file = os.path.join(os.path.dirname(__file__), 'all_scifi_genres.csv')

    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    dfs = [pd.read_csv(os.path.join(input_folder, f)) for f in csv_files]

    concatenated_df = pd.concat(dfs, ignore_index=True)
    concatenated_df.to_csv(output_file, index=False)


# Filter out non-scifi genres based on all_scifi_genres.csv from a given csv
def filter_scifi_genres(input_csv, output_csv):
    input_test_file = os.path.join(os.path.dirname(__file__), input_csv)
    output_test_file = os.path.join(os.path.dirname(__file__), output_csv)
    all_scifi_file = os.path.join(os.path.dirname(__file__), 'all_scifi_genres.csv')
    all_scifi_df = pd.read_csv(all_scifi_file)
    all_scifi_genres = set(all_scifi_df['title'].str.lower().tolist())

    input_df = pd.read_csv(input_csv)
    filtered_df = input_df[input_df['title'].str.lower().isin(all_scifi_genres)]
    filtered_df.to_csv(output_csv, index=False)
    print("Filtered")

# Test: (it works!)
test_scifi_filter = False
if test_scifi_filter:
    filter_scifi_genres('test.csv', 'test_filtered.csv')
    print("Test filtering complete. Check 'test_filtered.csv'.")



