import pandas as pd
from jobspy import scrape_jobs
import os

try:
    # Search sources
    sources = [
        "linkedin", "indeed",
    ]

    def get_jobs(location):
        # First search: 'intern'
        intern_jobs = scrape_jobs(
            site_name=sources,
            search_term="intern",     # <---- Edit this search term ---->
            location=location,
            results_wanted=200,
            hours_old=2,              # <---- Edit the hours old for the job listing ---->
        )

        # Second search: 'co-op'
        coop_jobs = scrape_jobs(
            site_name=sources,
            search_term="co-op",     # <---- Edit this search term ---->
            location=location,
            results_wanted=200,
            hours_old=2,             # <---- Edit the hours old for the job listing ---->
        )

        # Combine results and drop duplicates (based on job URL)
        combined = pd.concat([intern_jobs, coop_jobs]).drop_duplicates(subset="job_url")
        return combined

    print("Getting jobs...")
    jobs = get_jobs("United States")

    # Filter to your search related roles
    print("Filtering jobs...")
    filtered = jobs[    # <---- For this line below, replace the key words for filtering jobs. Use as many as you can and make sure they are relevant. Separate each with | ---->
            jobs["title"].str.contains("software|developer|development|backend|frontend|swe|devops|cloud|ml|ai|data|platform|web|application", case=False, na=False)
    ]
    '''
    # Remove unrelated/spam
    filtered = filtered[
        ~filtered["company"].str.contains(
            "Lensa",
            case=False,
            na=False
        )
    ]
    '''
    print("Filtering job data...")
    columns_to_keep = ["id", "site", "job_url", "job_url_direct", "title", "company", "location", "date_posted", "job_type"]
    filtered = filtered[columns_to_keep]

    filtered = filtered.sort_values(by=["site", "date_posted"], ascending=[True, False])

    current_path = os.getcwd()
    check_path = os.path.join(current_path, "jobs.csv")

    if os.path.exists(check_path):
        print("jobs.csv already exists, removing...")
        os.remove(check_path)

    print(f"Found {len(filtered)} internships!")
    filtered.to_csv("jobs.csv", index=False)
    print(f"Saved to: {check_path}")

except KeyboardInterrupt:
    print("\nExecution terminated.")
            
            
