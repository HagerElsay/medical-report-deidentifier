# Medical Report De-identifier

A Python prototype for removing identifying information from medical reports.

## What it does

The tool detects and redacts identifiers such as:

- Patient names
- Dates
- Phone numbers
- Email addresses
- Patient IDs / MRNs
- National IDs
- Addresses
- Doctor names
- Passport numbers
- Insurance numbers
- Sex/gender

It preserves clinical information such as diagnoses and treatments.

## Disclaimer

This is a prototype for educational and research purposes. It is **not production-ready** and should not be used with real patient data.

## How to Run

1. Download `deidentifier.py`
2. Run it with Python 3
3. Paste a medical report
4. Type `END` when finished
5. The de-identified report will be displayed and saved as `deidentified_output.txt`
## Example

### Input

Patient Name: Omar Hassan
Date of Birth: 1998-07-15
Phone: +20 1012345678
Email: omar@example.com
Patient ID: P-889922
Diagnosis: Diabetes mellitus type 2.

### Output

Patient Name: [NAME REDACTED]
Date of Birth: [DATE REDACTED]
Phone: [PHONE REDACTED]
Email: [EMAIL REDACTED]
Patient ID: [PATIENT ID REDACTED]
Diagnosis: Diabetes mellitus type 2.
