# Apprentice Progression Pipeline Health Dashboard

## Project Summary
This project aims to create a dashboard that empowers coaches and program managers at Multiverse to identify apprentices at risk of stagnation, dropout, or underperformance. By surfacing engagement and progression signals in real time, this tool will help optimize coaching interventions, boost completion rates, and strengthen employer outcomes.

##  Business Goals
- Reduce dropout rates through early risk detection.
- Improve completion and promotion rates for underrepresented groups.
- Enable coaches to personalize support and manage caseloads more effectively.
- Provide equity lens filters (e.g., gender, ethnicity, SES, LDD) to detect systemic gaps.

## Stakeholders
- Coaches: Want to quickly identify apprentices who need intervention.
- Program Managers: Need macro-level views of progression trends and equity gaps.
- Employers: Indirectly benefit from stronger apprentice retention and performance.
- Data & Insights Team: Will maintain the underlying models and reporting pipelines.

## Solution Components
- A star-schema data model in BigQuery using `dbt`
- A snapshot table tracking week-by-week apprentice progression status (SCD Type 2)
- A dbt risk model flagging apprentices as Green, Amber, or Red
- A Looker dashboard with cohort filters and demographic slicing

## 🧪 Key Metrics
- `current_progression_status`: Active, Delayed, At Risk, Promoted, Withdrawn
- `days_since_last_feedback`
- `quiz_score_avg_last_30d`
- `attendance_rate_last_30d`
- `risk_score` → Red (≥80), Amber (50–79), Green (<50)

## Data Freshness
- Daily ingestion (simulated), weekly snapshots for progression status

## Tech Stack
- `dbt` + `BigQuery` (SQL modeling + SCD2 snapshotting)
- `Python` for mock data generation
- `Looker` for dashboarding (modeled on dbt sources)
- `Git` for version control
- `pipenv/venv` + `pip install dbt-bigquery` (project env)

## Long-Term Extensions
- NLP sentiment model on apprentice check-in logs
- Employer-level benchmark dashboards
- SMS/email alerts to coaches when apprentices cross risk thresholds
