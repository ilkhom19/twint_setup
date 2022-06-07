## To setup Twint:


1. Clone the project from: https://github.com/twintproject/twint.git.
2. Install dependencies using commands shown in the [github page](https://github.com/twintproject/twint.git). 
3. Once it is installed and works, fix language problem as shown below:
	
	Type "pip show twint" into the command line, follow the path shown at "Location", then open the folder named "twint" and change these lines:
   ```
		101    if conif.Lang:
		102        q += f" lang:{config.Lang}"
		
		110    if config.Search:
		111        q += f" {config.Search}"
   ```
4. Now if you run "ex.py", the scraping will start. 
5. Scraping results for each day will be saved separately in json files in folder ./json-files
6. Scraping logs for each day will be saved in folder ./logs

### ex.py will create folders "./logs" and "./json-files" itself
