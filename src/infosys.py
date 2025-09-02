import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://career.infosys.com/jobs?companyhiringtype=IL&countrycode=IN&searchJob=data%20analyst")
driver.maximize_window()


wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-titleTxt")))


titles = driver.find_elements(By.CLASS_NAME, "job-titleTxt")
locations = driver.find_elements(By.CLASS_NAME, "job-locationTxt")
descriptions = driver.find_elements(By.CLASS_NAME, "job_right_cont")
experiences = driver.find_elements(By.CLASS_NAME, "job-levelTxt")   
skills = driver.find_elements(By.CLASS_NAME, "skillTxt")            

jobs = []
count = max(len(titles), len(locations), len(descriptions), len(experiences), len(skills))
print(f"Found {count} job cards...")

for i in range(count):
    title = titles[i].get_attribute("innerText").strip() if i < len(titles) else "N/A"
    location = locations[i].get_attribute("innerText").strip() if i < len(locations) else "N/A"
    description = descriptions[i].get_attribute("innerText").strip() if i < len(descriptions) else "N/A"
    experience = experiences[i].get_attribute("innerText").strip() if i < len(experiences) else "N/A"
    skill = skills[i].get_attribute("innerText").strip() if i < len(skills) else "N/A"
    
    print(f"{title} | {location} | {experience} | {skill}")
    jobs.append([title, location, description, experience, skill])
    

with open("data/Infosys_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Location", "Description", "Experience", "Skills"])  
    writer.writerows(jobs)

print("Data Saved to Infosys_jobs.csv")

driver.quit()  
