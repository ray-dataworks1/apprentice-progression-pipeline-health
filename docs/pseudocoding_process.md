| Stakeholder Need |	Metric or Behavior | Entity |
|------------------|-----------------------|--------|
|Track apprentice outcomes weekly|	Engagement, risk score, progression	|Fact Table |
|View coach caseloads & actions| Apprentice feedback gap, outcome| dim_coach
|Flag equity issues (e.g. by race, SES)|	Gender, ethnicity, SES, LDD|	dim_apprentice
|Attribute apprentice journey to employer|	Completion & promotion rates by employer|	dim_employer|
|Use milestones (Promoted, Withdrawn)|	Promotion flag, dropout indicator |	Fact for promotion__flag as it is numerical metric defining a state or condition and a KPI, dropout indicator describes an apprentice so it belongs in dim_apprentice |
|Enable filters over time |	Weekly snapshot date|Snapshot dimension / date grain


## Pseudocode for Business Logic
### Fact Table: apprentice_progression
### Grain: One row per apprentice per snapshot period (weekly)

FACT apprentice_progression (
    apprentice_id           -- FK to dim_apprentice
    snapshot_date           -- Snapshot grain (weekly)
    quiz_score              -- Performance metric
    attendance_rate         -- Engagement metric
    feedback_gap_days       -- Time since coach last interacted
    risk_score              -- Composite risk score (0-100)
    risk_status             -- Derived label: Green/Amber/Red
    current_status          -- e.g., Active, At Risk, Withdrawn
    promoted_flag           -- Boolean promotion marker
    valid_from              -- SCD2 fields
    valid_to
    is_current
)

-- DIM apprentice
-- Stores apprentice metadata and demographics

DIM apprentice (
    apprentice_id
    full_name
    gender
    ethnicity
    SES_decile               -- Socioeconomic indicator
    LDD_flag                 -- Learning difficulty/disability
    apprenticeship_type
    employer_id              -- FK to dim_employer
    coach_id                 -- FK to dim_coach
    start_date
    end_date
)

-- DIM coach
-- Stores coach info for attribution

DIM coach (
    coach_id
    coach_name
    region
    team_lead_id
)

-- DIM employer
-- Stores employer org metadata

DIM employer (
    employer_id
    employer_name
    sector
    employer_size
    partner_status           -- Platinum, Gold, etc.
)
