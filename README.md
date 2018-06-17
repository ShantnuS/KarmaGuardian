# KarmaGuardian
Reddit script that deletes your comments when they are downvoted below a threshold.

## Getting Started    

Before starting, [PRAW](https://praw.readthedocs.io/en/latest/) must be installed on the machine. On a Windows system, [the batch file can be used](install_libraries.bat). Alternatively, if pip is installed on the machine, the command below may be used.
``` 
pip install praw
```

### Setting up Reddit application

Instructions for setting up a Reddit application to use KarmaGuardian:

1. Log-on to Reddit and go to **preferences**. 
2. Go to the **apps** section.
3. At the bottom of the page, click **create another app...**.
4. Fill out relevant information, i.e. shown below:

<img src="readme_res\create_new_app.PNG" align="middle">

5. You will now be able to see your **client ID** and **client secret**!

<img src="readme_res\app_info.PNG" align="middle">

### Setting up KarmaGuardian

Instructions for setting up and running KarmaGuardian for your Reddit account:

1. Clone the repository or download the files.
2. Open the config.py file and replace XXXXXXXXX with relevant details.

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
