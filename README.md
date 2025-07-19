# Job Scraper
Welcome! This job scraper will make your job hunt easier and more efficient with just a couple of commands!

## Instructions (Linux)
1. Make sure Python is installed `python3 --version`. If correctly installed it will return the python version you are running. Otherwise, you can install it with this command: `sudo apt install python3`
2. In your desired directory, create a Python virtual environment `python3 -m venv venv`
3. Once the Python virtual environment is created, we want to activate it: `source venv/bin/activate`
4. Now we can download the dependencies: `pip3 install pandas` and `pip3 install -U python-jobspy`
5. Now download `main.py` from this repository and place it in the same directory as the virtual environment for ease of use.
6. Edit the file, note for simplicity; comments which include <---- instruction ----> are where the file needs to be edited. In the get_jobs function there are 2 searches placed. You may change the search_term for the type of job you are looking for and you may also change how old the job listing should be. Ex: 2 = 2 hours old. The next and last thing is to filter these searches. You want to use as many key words that may be relevant to the job field you are looking for. Separate them with pipes. Ex: "software|developer|web" and so on.
7. Once this is done, you can save the file and run it! `python3 main.py`
8. Once this happens, it will run. Depending on your search settings set previously and your machine time will vary, but expect anywhere between 10-60 seconds to finish executing.
9. Once the program finishes executing, it will create a csv file `jobs.csv` which has all the jobs found. Each job includes the job source, link, company, and location.

## Notes
- If you wish to re-run the script, it will delete the previous `jobs.csv` file and replace it with a new one!
- If you wish to exit the virtual environment just type `deactivate`
- If you wish to use the script again, you only have to follow instructions 3 and 7

