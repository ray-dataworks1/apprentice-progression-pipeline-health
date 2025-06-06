import pandas as pd
import numpy as np
import random
from faker import Faker

# Initializing random seeds and faker instance
fake = Faker()
np.random.seed(42)
random.seed(42)

# Parameters
n_apprentices = 500
genders = ['Male', 'Female', 'Non-Binary', 'Prefer not to say']
ethnicities = ['White', 'Black', 'Asian', 'Mixed', 'Other']
tracks = ['Data Fellowship', 'Project Management', 'Software Engineering', 'Digital Marketing']
ses_deciles = list(range(1, 11))
ldd_flags = [True, False]
coach_ids = list(range(1, 21))
employer_ids = list(range(1, 101))

# Apprentice data generation function
def generate_dim_apprentice(n=500):
    data = []
    for apprentice_id in range(1, n + 1):
        gender = random.choices(genders, weights=[0.45, 0.45, 0.05, 0.05])[0]
        ethnicity = random.choices(ethnicities, weights=[0.6, 0.15, 0.1, 0.1, 0.05])[0]
        ses_decile = random.choices(ses_deciles, weights=[0.15]*2 + [0.1]*6 + [0.05]*2)[0]
        ldd_flag = random.choices(ldd_flags, weights=[0.2, 0.8])[0]
        coach_id = random.choice(coach_ids)
        employer_id = random.choice(employer_ids)
        track = random.choice(tracks)
        start_date = pd.Timestamp('2024-09-01') + pd.to_timedelta(random.randint(0, 30), unit='d')
        end_date = start_date + pd.DateOffset(months=12)
        name = fake.name()
        apprentice_record = {
            'apprentice_id': apprentice_id,
            'full_name': name,
            'gender': gender,
            'ethnicity': ethnicity,
            'ses_decile': ses_decile,
            'ldd_flag': ldd_flag,
            'coach_id': coach_id,
            'employer_id': employer_id,
            'track': track,
            'start_date': start_date,
            'expected_end_date': end_date
        }
        data.append(apprentice_record)
    return pd.DataFrame(data)

# Generate and export to CSV
dim_apprentice = generate_dim_apprentice(n_apprentices)
dim_apprentice_path = '/mnt/data/dim_apprentice.csv'
dim_apprentice.to_csv(dim_apprentice_path, index=False)

dim_apprentice_path