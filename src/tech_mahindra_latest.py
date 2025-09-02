from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Tech Mahindra careers page
url = "https://careers.techmahindra.com/CurrentOpportunity.aspx#Advance"
driver.get(url)

time.sleep(5)  # wait for page to load (adjust if needed)

# Collect job cards
job_cards = driver.find_elements(By.CSS_SELECTOR, "div.title2.field")

jobs_data = []

for job in job_cards:
    try:
        # Job Role
        role = job.find_element(By.CSS_SELECTOR, "div[style*='font-size: 16px']").text.strip()
    except:
        role = ""

    try:
        # Extract details
        details = job.find_element(By.CSS_SELECTOR, "p").text.split("\n")
        skills = details[0].replace('"', '').replace("Skill Set :", "").strip()
        experience = details[1].replace('"', '').replace("Experience :", "").strip()
        location = details[2].replace('"', '').replace("Location :", "").strip()
    except:
        skills, experience, location = "", "", ""

    jobs_data.append({
        "Job Role": role,
        "Skills": skills,
        "Experience": experience,
        "Location": location
    })

# Save to CSV
df = pd.DataFrame(jobs_data)
df.to_csv("data/TechMahindra.csv", index=False, encoding="utf-8-sig")

print("✅ Data saved to TechMahindra.csv")

driver.quit()
