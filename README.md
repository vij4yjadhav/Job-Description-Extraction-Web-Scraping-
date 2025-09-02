# Job Data Scraper (Infosys + Tech Mahindra)

This project scrapes job postings from Infosys and Tech Mahindra career portals, merges them into a single dataset, and saves the output as a CSV file.

## Features
- Scrapes real-time job data using `requests` and `BeautifulSoup`.
- Extracted details include job title, location, company name, and experience requirements.
- Merges data from both companies into one file for easier analysis.

## Project Structure
```
Job-Scraper/
├── infosys_scraper.py        # Extracts jobs from Infosys
├── tech_mahindra_scraper.py  # Extracts jobs from Tech Mahindra
├── merge_data.py             # Merges both datasets into one CSV
├── Infosys_Jobs.csv          # Infosys job data (generated)
├── TechMahindra_Jobs.csv     # Tech Mahindra job data (generated)
├── All_Jobs.csv              # Combined dataset (generated)
└── README.md                 # Project documentation
```

## Prerequisites
Install required libraries before running the scripts:
```bash
pip install requests beautifulsoup4 pandas
```

## How to Run

### Step 1. Run scrapers individually
```bash
python infosys_scraper.py
python tech_mahindra_scraper.py
```

### Step 2. Merge both CSV files
```bash
python merge_data.py
```

This will create a final file named:
```
All_Jobs.csv
```

## Output Format
The combined CSV file (`All_Jobs.csv`) will have the following columns:
- **Job Title**
- **Company**
- **Location**
- **Experience**

## License
This project is for **educational purposes only**. Please check the terms of use of the respective websites before scraping.
