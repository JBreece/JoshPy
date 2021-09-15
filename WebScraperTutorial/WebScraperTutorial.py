# https://realpython.com/beautiful-soup-web-scraper-python/#scrape-the-fake-python-job-site

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)
# above prints page html without using beautifulsoup

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

results = soup.find(id="ResultsContainer")
print(results.prettify())

job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    print(job_element, end="\n"*2)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
print(len(python_jobs)) # prints number of results for python jobs, but printing the actual python_jobs is still unstructured here

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements: # notice this is similar to the above, but looks only for python jobs (see python_job_elements above)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# the above code already scrapes the site and filters the HTML for relevant job postings, however it does not include the link to apply to the job.  See below:

for job_element in python_job_elements: # notice this is similar to the above, but looks only for python jobs (see python_job_elements above)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

# final result of this one is using beautiful soup "soup.find(id="ResultsContainer")", then filtering on the h2 header elements that say the job is a python job, then going up to a higher level to have access to the other relevant elements in the same div, then finding all the relevant info using the .find() function, and then filtering for the relevant href to get the job link.