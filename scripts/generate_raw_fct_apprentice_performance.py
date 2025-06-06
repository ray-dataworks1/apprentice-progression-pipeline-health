import numpy as np
import pandas as pd
import random

# Set seed for reproducibility
np.random.seed(42)

# Constants
NUM_APPRENTICES = 500
WEEKLY_SNAPSHOTS = 10

# Demos
ethnicity_dist = {
    'White': 0.44,
    'Black': 0.15,
    'Asian': 0.17,
    'Mixed': 0.10,
    'Other': 0.05,
    'Prefer not to say': 0.09
}

gender_dist = {
    'Female': 0.52,
    'Male': 0.45,
    'Non-binary/Other': 0.02,
    'Prefer not to say': 0.01
}

ses_deciles = list(range(1, 11))  # 1 = most deprived, 10 = most affluent
ses_probs = [0.15, 0.13, 0.12, 0.10, 0.10, 0.10, 0.08, 0.07, 0.08, 0.07]  # Skewed toward lower SES

ldd_prob = 0.15  # Learning difficulty/disability prevalence

# Helper Functions
def generate_quiz_scores():
    score = np.random.normal(70, 10)
    return min(max(round(score, 1), 30), 100)

def generate_attendance(risk_status):
    if risk_status == 'Red':
        return round(np.random.normal(55, 10), 1)
    elif risk_status == 'Amber':
        return round(np.random.normal(75, 8), 1)
    else:
        return round(np.random.normal(90, 5), 1)

def assign_risk(score, attendance, feedback_gap):
    if attendance < 65 or score < 50 or feedback_gap > 21:
        return 'Red'
    elif attendance < 80 or score < 65 or feedback_gap > 14:
        return 'Amber'
    else:
        return 'Green'

# Generate dim_apprentice 
dim_apprentice = pd.DataFrame({
    'apprentice_id': range(1, NUM_APPRENTICES + 1),
    'gender': np.random.choice(list(gender_dist.keys()), size=NUM_APPRENTICES, p=list(gender_dist.values())),
    'ethnicity': np.random.choice(list(ethnicity_dist.keys()), size=NUM_APPRENTICES, p=list(ethnicity_dist.values())),
    'SES_decile': np.random.choice(ses_deciles, size=NUM_APPRENTICES, p=ses_probs),
    'LDD_flag': np.random.choice([True, False], size=NUM_APPRENTICES, p=[ldd_prob, 1 - ldd_prob]),
    'coach_id': np.random.randint(1, 21, size=NUM_APPRENTICES),
    'employer_id': np.random.randint(1, 31, size=NUM_APPRENTICES),
    'apprenticeship_type': np.random.choice(['Data', 'Software', 'Project Mgmt'], size=NUM_APPRENTICES, p=[0.5, 0.3, 0.2]),
    'start_date': pd.to_datetime('2024-09-01'),
    'end_date': pd.to_datetime('2025-09-01')
})

#  Generate fct_apprentice_progression snapshots 
records = []
for apprentice in dim_apprentice['apprentice_id']:
    for week in range(WEEKLY_SNAPSHOTS):
        snapshot_date = pd.to_datetime('2025-01-01') + pd.Timedelta(weeks=week)
        quiz = generate_quiz_scores()
        feedback_gap = np.random.randint(0, 30)
        attendance = generate_attendance('Red' if quiz < 50 else 'Amber' if quiz < 65 else 'Green')
        risk = assign_risk(quiz, attendance, feedback_gap)
        promoted_flag = random.choices([True, False], weights=[0.05, 0.95])[0]
        records.append([
            apprentice, snapshot_date, quiz, attendance, feedback_gap, 
            risk, promoted_flag
        ])

fct_apprentice_progression = pd.DataFrame(records, columns=[
    'apprentice_id', 'snapshot_date', 'quiz_score', 'attendance_rate', 
    'feedback_gap_days', 'risk_status', 'promoted_flag'
])

import ace_tools as tools; tools.display_dataframe_to_user(name="Apprentice Progression Dataset", dataframe=fct_apprentice_progression)
Result
   apprentice_id snapshot_date  quiz_score  attendance_rate  \
0              1    2025-01-01        75.4             84.8   
1              1    2025-01-08        78.1             92.7   
2              1    2025-01-15        66.7             86.9   
3              1    2025-01-22        69.0             93.9   
4              1    2025-01-29        48.6             60.3   

   feedback_gap_days risk_status  promoted_flag  
0                  6       Green          False  
1                 18       Amber          False  
2                  3       Green          False  
3                  9       Green          False  
4                 25         Red           True  