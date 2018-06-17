# KarmaGuardian
Reddit script that deletes your comments when they are downvoted below a threshold.

## Getting Started    

### Setting up Reddit application


### Setting up KarmaGuardian
1. Clone the repository or download the files.
2. Open the config.py file and replace XXXXXXXXX with relavent details.

```Python 
##REDDIT BASICS###
#More information here: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html 
username = 'XXXXXXXXX' #This is your reddit username, i.e. spez
password = 'XXXXXXXXX' #This is your reddit password, i.e hunter2
client_id = 'XXXXXXXXX' #This is the client ID received after creating an application.
client_secret = 'XXXXXXXXX' #Client secret received after creating an application
user_agent = "XXXXXXXXX"  #A descriptive user agent to help Reddit determine source of requests 

##KarmaGuardian Parameters###
threshold = -2 #Minimum comment score before it is deleted 
```
3. Run KarmaGuardian.py using the command line using "python KarmaGuardian.py". 
4. The script will delete comments with a score of below the threshold every 60 seconds. 
