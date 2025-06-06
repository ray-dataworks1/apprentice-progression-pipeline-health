#  Statistical Justification for Apprentice Dataset

This document outlines the rationale for the statistical realism of the synthetic apprenticeship dataset used in the Apprentice Progression Pipeline Health Dashboard project. The distributions are grounded in UK apprenticeship data (2020–2025), Multiverse diversity reports, and government publications.

---

##  1. Ethnicity Distribution
- White: 44%
- Black: 15%
- Asian: 17%
- Mixed: 10%
- Other: 5%
- Prefer not to say: 9%

Justification:
- National apprenticeship participation: ~16% ethnic minority (DfE, 2023)
- Multiverse: 56% apprentices from ethnic minority backgrounds
- Reflects urban-focused, equity-driven intake

Sources:
- https://www.ethnicity-facts-figures.service.gov.uk/
- https://www.indexventures.com/perspectives/multiverse-raises-220m/

---

## 2. Gender Distribution
- Female: 52%
- Male: 45%
- Non-binary/Other: 3%

Justification:
- National average: ~49–52% female
- Tech apprenticeships: 17% female
- Multiverse: >50% female across programs

Sources:
- https://www.engineeringuk.com/
- https://www.fenews.co.uk/skills/it-s-official-multiverse-apprenticeships-are-outstanding/

---

## 3. Socioeconomic Status (SES)
- Weighted toward lower SES deciles (1–3 = 40%)

Justification:
- Multiverse: 34% from underserved communities
- Ada College: 50% from low-income backgrounds

Sources:
- https://www.fenews.co.uk/education/ada-the-national-college-for-digital-skills-recognised-with-the-kings-award-for-enterprise/
- https://www.suttontrust.com/

---

## 4. LDD / Neurodivergence Flag
- 15% prevalence of learning difficulty or disability (LDD)

**Justification**:
- 11–12% official self-reported (DfE)
- Cognitive assessments suggest up to 35% have learning needs

Sources:
- https://www.thehrdirector.com/business-news/apprenticeships/alarming-numbers-of-apprentices-with-hidden-learning-difficulties-new-study-reveals/

---

## 🧪 5. Quiz Scores
- Normally distributed around 70%, capped 30–100

Justification:
- Reflects typical educational performance distributions
- Allows for failure edge cases (<50%) in risk modeling

---

## 6. Attendance Rates
- Green: ~90%, Amber: ~75%, Red: ~55%

Justification:
- 85–95% attendance common for engaged learners
- <60% often precedes dropout

Sources:
- Ofsted reports (2020–2023)
- Sutton Trust and Multiverse internal analytics

---

##  7. Employer Count
- 100 employers for 500 apprentices (avg 5 per employer)

**Justification**:
- Mix of SME and enterprise clients
- Reflects Multiverse's blend of Google, NHS, startups, etc.

Sources:
- https://feweek.co.uk/
- https://youthfuturesfoundation.org/

---

##  8 Coach Count
- 20 coaches → ~25 apprentices per coach

Justification:
- Matches typical caseloads at Multiverse

Sources:
- https://www.fenews.co.uk/skills/it-s-official-multiverse-apprenticeships-are-outstanding/

---
