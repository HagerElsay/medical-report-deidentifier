import re


def deidentify(text):

    # PHONE — Egyptian local format
    text = re.sub(
        r'\b01[0125]\d{8}\b',
        '[PHONE REDACTED]',
        text
    )

    # PHONE — +20 international format
    text = re.sub(
        r'\+20\s*1[0125]\s*\d{8}\b',
        '[PHONE REDACTED]',
        text
    )

    # EMAIL
    text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        '[EMAIL REDACTED]',
        text
    )

    # EGYPTIAN NATIONAL ID
    text = re.sub(
        r'\b\d{14}\b',
        '[ID REDACTED]',
        text
    )

    # PATIENT ID
    text = re.sub(
        r'(?i)\b(patient\s+ID|patient\s+number|patient\s+no\.?)'
        r'\s*(?:is|:|-)?\s*[A-Za-z0-9-]+',
        r'\1: [PATIENT ID REDACTED]',
        text
    )

    # RECORD NUMBER
    text = re.sub(
        r'(?i)\b(record\s+(?:number|no\.?|#))'
        r'\s*(?:is|:|-)?\s*[A-Za-z0-9-]+',
        r'\1: [RECORD ID REDACTED]',
        text
    )

    # MEDICAL RECORD NUMBER
    text = re.sub(
        r'(?i)\b(medical record number)'
        r'(\s*(?:is|:)\s*)'
        r'[A-Za-z0-9-]+',
        r'\1: [RECORD ID REDACTED]',
        text
    )

    # MRN
    text = re.sub(
        r'(?i)\bMRN\s*(?:is|:)?\s*[A-Za-z0-9-]+',
        'MRN: [RECORD ID REDACTED]',
        text
    )

    # ID NUMBER
    text = re.sub(
        r'(?i)\b(ID\s+(?:number|no\.?|#))'
        r'\s*(?:is|:|-)?\s*[A-Za-z0-9-]+',
        r'\1: [ID REDACTED]',
        text
    )

    # PATIENT NAME
    text = re.sub(
        r'(?i)(Patient\s*:\s*)'
        r'([A-Za-z]+(?:\s+[A-Za-z]+)?)',
        r'\1[NAME REDACTED]',
        text
    )

    # PATIENT NAME
    text = re.sub(
        r'(?i)(Patient\s+Name\s*[-:]\s*)'
        r'([A-Za-z]+(?:\s+[A-Za-z]+)?)',
        r'\1[NAME REDACTED]',
        text
    )

    # Pt: NAME
    text = re.sub(
        r'(?i)(\bPt\s*:\s*)'
        r'([A-Za-z]+(?:\s+[A-Za-z]+)?)',
        r'\1[NAME REDACTED]',
        text
    )

    # DATES
    text = re.sub(
        r'\b(?:'
        r'\d{1,2}[./-]\d{1,2}[./-]\d{4}'
        r'|'
        r'\d{4}[./-]\d{1,2}[./-]\d{1,2}'
        r')\b',
        '[DATE REDACTED]',
        text
    )

    # ADDRESS
    text = re.sub(
        r'(?i)(address\s*:?\s*|lives at\s+)'
        r'[^\n.]+',
        r'\1[ADDRESS REDACTED]',
        text
    )

    # DOCTOR / PHYSICIAN
    text = re.sub(
        r'(?i)(\b(?:Doctor|Physician)\s*:?\s*)'
        r'(?:Dr\.?\s+)?'
        r'[A-Za-z]+(?:\s+[A-Za-z]+)?',
        r'\1[NAME REDACTED]',
        text
    )

    # Standalone Dr. Name
    text = re.sub(
        r'(?i)\b(Dr\.?)\s+'
        r'[A-Za-z]+(?:\s+[A-Za-z]+)?',
        r'\1 [NAME REDACTED]',
        text
    )

    # SEX / GENDER
    text = re.sub(
        r'(?i)\b(male|female|man|woman)\b',
        '[SEX REDACTED]',
        text
    )

    # UNLABELED NAME
    text = re.sub(
        r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,2})'
        r'(?=\s+(?:came|was|visited|arrived|was admitted)\b)',
        '[NAME REDACTED]',
        text,
        flags=re.MULTILINE
    )

    # PASSPORT
    text = re.sub(
        r'(?i)\b(passport\s*(?:number|no\.?|#)?\s*'
        r'(?:is\s+|:\s*|-\s*)?)'
        r'[A-Z0-9]{6,12}\b',
        r'\1[PASSPORT REDACTED]',
        text
    )

    # INSURANCE
    text = re.sub(
        r'(?i)\b(insurance\s*(?:number|no\.?|#)?\s*'
        r'(?:is\s+|:\s*|-\s*)?)'
        r'[A-Z0-9-]{6,20}\b',
        r'\1[INSURANCE ID REDACTED]',
        text
    )

    return text


def main():

    print("==============================================")
    print("       MEDICAL REPORT DE-IDENTIFIER")
    print("==============================================")
    print()
    print("Paste your medical report below.")
    print("When finished, type END on a new line.")
    print()

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    report = "\n".join(lines)

    clean_report = deidentify(report)

    print()
    print("==============================================")
    print("          DE-IDENTIFIED REPORT")
    print("==============================================")
    print()
    print(clean_report)

    # Save result
    with open(
        "deidentified_output.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(clean_report)

    print()
    print("==============================================")
    print("Saved successfully!")
    print("File: deidentified_output.txt")
    print("==============================================")


if __name__ == "__main__":
    main()
