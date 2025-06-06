import faker

# Initialize faker for realistic company names
fake = faker.Faker()
NUM_EMPLOYERS = 100

# Employer sectors and size bands
sectors = ['Tech', 'Finance', 'Healthcare', 'Retail', 'Education', 'Media', 'Consulting']
partner_statuses = ['Platinum', 'Gold', 'Silver', 'New']
size_bands = ['Small (1-50)', 'Medium (51-250)', 'Large (251-1000)', 'Enterprise (1000+)']
sector_probs = [0.25, 0.20, 0.15, 0.15, 0.10, 0.10, 0.05]
size_probs = [0.3, 0.3, 0.25, 0.15]
partner_probs = [0.2, 0.4, 0.3, 0.1]

# Generate employer dataset
dim_employer = pd.DataFrame({
    'employer_id': range(1, NUM_EMPLOYERS + 1),
    'employer_name': [fake.company() for _ in range(NUM_EMPLOYERS)],
    'sector': np.random.choice(sectors, size=NUM_EMPLOYERS, p=sector_probs),
    'size_band': np.random.choice(size_bands, size=NUM_EMPLOYERS, p=size_probs),
    'partner_status': np.random.choice(partner_statuses, size=NUM_EMPLOYERS, p=partner_probs)
})

tools.display_dataframe_to_user(name="Employer Dimension Table", dataframe=dim_employer)