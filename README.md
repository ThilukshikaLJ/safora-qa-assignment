# Safora QA Automation — Contact Form Testing

## ⚠️ Important Note
The code is in the **master** branch.
If you are viewing the main branch, please switch to **master** to see all files.

👉 Direct link: https://github.com/ThilukshikaLJ/safora-qa-assignment/tree/master

## Project Overview
This project automates the Contact Us form testing on [Safora](https://safora.se/en/contact.html) using Selenium WebDriver with Python, following the Page Object Model (POM) design pattern.

## Project Structure
```
safora_automation/
├── pages/
│   └── contact_page.py       # Page Object — Contact Us page elements and actions
├── tests/
│   └── test_contact_form.py  # Test scenarios
├── screenshots/              # Auto-generated test screenshots
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Test Scenarios
| Test | Description | Status |
|------|-------------|--------|
| Test 1 | Valid form submission with all fields filled | ✅ Pass |
| Test 2 | Empty form submission — validation error check | ✅ Pass |

## Note on reCAPTCHA
The Contact Us form includes Google reCAPTCHA for security.
Automated form submission is blocked by reCAPTCHA — which is **expected security behavior.**
The script successfully verifies all form fields are fillable and the submit button is clickable.

## Requirements
- Python 3.x
- Google Chrome browser
- Internet connection

## Installation

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd safora_automation
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python tests/test_contact_form.py
```

## Screenshots
Screenshots are automatically saved in the `screenshots/` folder after each test run.
