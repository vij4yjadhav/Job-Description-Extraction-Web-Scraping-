import requests
from bs4 import BeautifulSoup
import pandas as pd

class Jobs_data_ext:
    
    def __init__(self): 
        self.job_role = []
        self.company_names = []
        self.location = []
        self.experience= []
        self.headers = { 
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
            }
        
    def fetchAndSaveData(self, url, path):
        resp = requests.get(url, headers = self.headers)
        soup = BeautifulSoup(resp.text, "lxml")
        with open(path , "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        print(f"File Saved to {path}")

    def parse_html(self, path):
        with open(path, "r") as f:
            html = f.read()
            soup = BeautifulSoup(html, "lxml")
        return soup

    def extract_data(self ,soup):

        roles = soup.find_all("a", target="_self")
        for role in roles:
            role_d = role.get_text().strip()
            self.job_role.append(role_d)
        # print(job_role)
            
        comp_n = soup.find_all("span", class_="jobCardNova_bigCardTopTitleName__M_W_m jdTruncationCompany") 
        for cm in comp_n:
            cm_d = cm.get_text().strip()
            self.company_names.append(cm_d)
        # print(company_names)

        exp_needed = soup.find_all("span" , class_="jobCardNova_bigCardCenterListExp__KTSEc")
        for exp in exp_needed:
            exp_d = exp.get_text().strip()
            if "LPA" not in exp_d and "Remote" not in exp_d and "Contractual" not in exp_d: 
                self.experience.append(exp_d)
        # print(experience)

        loc = soup.find_all("div", class_="jobCardNova_bigCardCenterListLoc__usiPB jobCardNova_limits__G87pQ d-flex justify-content-start align-items-center")
        for locs in loc:
            loc_d = locs.find("span")
            self.location.append(loc_d.text.strip())
        # print(location)
        print("Extracted And saved to in list format")

    def Data_to_csv(self):
        jobs_d = {
            "job_role": self.job_role,
            "company_names" : self.company_names,
            "experience" : self.experience,
            "locations" : self.location
                }

        df = pd.DataFrame(jobs_d)
        df.to_csv("jobs.csv", index = False)
        print("Data saved")

jb = Jobs_data_ext()
# url = "https://www.shine.com/job-search/data-analyst-jobs?q=data-analyst&qActual=Data+Analyst"
# jb.fetchAndSaveData(url, "data/shine_jobs_up.html")
# path ="data/shine_jobs_up.html"
# soup = jb.parse_html(path)
# jb.extract_data(soup)
# jb.Data_to_csv()

    
    

    