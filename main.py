import pandas as pd
from jobspy import scrape_jobs
import os

try:
    sources = [
        "linkedin", "indeed",
    ]

    def get_jobs(location):
        # First search: 'intern'
        intern_jobs = scrape_jobs(
            site_name=sources,
            search_term="intern",
            location=location,
            results_wanted=200,
            hours_old=6,
        )

        # Second search: 'co-op'
        coop_jobs = scrape_jobs(
            site_name=sources,
            search_term="co-op",
            location=location,
            results_wanted=200,
            hours_old=6,
        )

        # Combine results and drop duplicates (based on job URL)
        combined = pd.concat([intern_jobs, coop_jobs]).drop_duplicates(subset="job_url")
        return combined

    print("Getting jobs...")
    jobs = get_jobs("United States")

    # Filter to software-related roles
    print("Filtering jobs...")
    filtered = jobs[
            jobs["title"].str.contains("software|developer|development|backend|frontend|full[- ]?stack|swe|devops|cloud|ml|ai|data|platform|web|application", case=False, na=False)
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
    check_path = os.path.join(current_path, "internships.csv")

    if os.path.exists(check_path):
        print("internships.csv already exists, removing...")
        os.remove(check_path)

    print(f"Found {len(filtered)} internships!")
    filtered.to_csv("internships.csv", index=False)
    print(f"Saved to: {check_path}")

except KeyboardInterrupt:
    print("\nExecution terminated.")
            
            
