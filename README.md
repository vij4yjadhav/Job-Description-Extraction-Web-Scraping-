Job Data Scraper and Merger

This project extracts job data from Infosys and Tech Mahindra websites using Python, processes it, and saves the results into CSV files. Finally, it merges the collected data into a single file for further analysis.

Features

Scrapes job listings from multiple sources (Infosys, Tech Mahindra).

Saves each company's data into individual CSV files.

Merges all datasets into a single consolidated file (All_Jobs.csv).

Written in Python using requests, BeautifulSoup, and pandas.

Project Structure
├── infosys_scraper.py        # Script to scrape Infosys jobs  
├── techmahindra_scraper.py   # Script to scrape Tech Mahindra jobs  
├── merge_data.py             # Script to merge CSV files  
├── Infosys_jobs.csv          # Output from Infosys scraper  
├── TechMahindra.csv          # Output from Tech Mahindra scraper  
├── All_Jobs.csv              # Final merged CSV file  
└── README.md                 # Project documentation  

Requirements

Install the required libraries before running the scripts:

pip install requests beautifulsoup4 pandas

How to Run

Run the Infosys scraper:

python infosys_scraper.py


Run the Tech Mahindra scraper:

python techmahindra_scraper.py


Merge the CSV files:

python merge_data.py


The final merged dataset will be available as All_Jobs.csv.

Disclaimer

This project is for educational purposes only. The data belongs to their respective companies, and scraping should comply with the website's terms of use.
