# Medical Diagnosis Assistant - Project Overview

## Architecture

### Class Hierarchy
```
Disease (Base Class)
    ├── Infectious
    │   ├── Flu
    │   ├── COVID-19
    │   └── Common Cold
    ├── Chronic
    │   ├── Diabetes
    │   ├── Hypertension
    │   └── Asthma
    └── Acute
        ├── Migraine
        ├── Food Poisoning
        └── Appendicitis
```

## How It Works

1. User enters symptoms
2. System compares against disease database
3. Calculates match percentage for each disease
4. Returns top matches ranked by likelihood
5. Provides treatment recommendations

## Key Components

### Disease Class (Parent)
- Stores disease information
- Calculates symptom matches
- Provides recommendations based on severity

### Category Classes (Infectious, Chronic, Acute)
- Extend Disease with category-specific attributes
- Add specialized methods

### DiagnosisSystem
- Manages disease database
- Performs diagnosis matching
- Displays results

### Validators
- Input validation
- Error handling
- User guidance

## Adding New Diseases

To add a new disease:
1. Create file in `models/diseases/`
2. Inherit from appropriate category class
3. Add to `diagnosis_system.py` in `load_diseases()`

## Future Enhancements
- Machine learning for better accuracy
- Patient history tracking
- Medical professional review integration
- Multi-language support