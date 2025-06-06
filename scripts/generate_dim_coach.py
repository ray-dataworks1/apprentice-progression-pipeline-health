# Generate dim_coach
NUM_COACHES = 20

# Example regions and optional team leads
regions = ['North', 'South', 'East', 'West', 'Midlands', 'London']
team_leads = [fake.name() for _ in range(5)]

dim_coach = pd.DataFrame({
    'coach_id': range(1, NUM_COACHES + 1),
    'coach_name': [fake.name() for _ in range(NUM_COACHES)],
    'region': np.random.choice(regions, size=NUM_COACHES),
    'team_lead_id': np.random.choice(range(1, 6), size=NUM_COACHES)  # Assume 5 team leads
})

tools.display_dataframe_to_user(name="Coach Dimension Table", dataframe=dim_coach)
 