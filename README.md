# apprentice-progression-pipeline-health
This project aims to create a dashboard that empowers coaches and program managers at EdTech firms to identify apprentices at risk of stagnation, dropout, or underperformance. By surfacing engagement and progression signals in real time, this tool will help optimize coaching interventions, boost completion rates, and strengthen employer outcomes.

## Project Structure
Apprentice-Progression-Pipeline-Health-Dashboard/
│
├── data/
│   ├── raw/             # Raw data files (e.g., CSVs, JSONs)
│   ├── processed/       # Processed data ready for loading into BigQuery
│
├── models/              # dbt models for transformation
│   ├── staging/         # Staging models (raw data to clean format)
│   ├── marts/           # Star schema (fact and dimension tables)
│
├── scripts/             # Python scripts for mock data generation, etc.
│   ├── mock_data.py     # Script for generating mock data (Postgres or Python)
│   ├── data_check.py    # Source freshness and tests
│
├── venv/                # Virtual environment directory
│
├── dbt_project.yml      # dbt configuration file
├── looker/              # Looker project files
│   ├── dashboards/      # Looker dashboard files
│   ├── models/          # Looker LookML models
│
├── .gitignore           # Git ignore file 
├── README.md            # Project documentation
