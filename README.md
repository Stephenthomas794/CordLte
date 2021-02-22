# CordLte
### Web Scraper that searched the entire USA for foreclosed houses and organzied the information by zip code! :+1:

## How Connection is Made:
Client :smile: -> Elastic Load Balancer :weight_lifting: -> Nginx Reverse Proxy :arrows_counterclockwise: -> Application w/ SQL_Alchemy Database :apple: :convenience_store:

## How it works: 
1. Upon visiting webiste a Socket connection is made with the user 
2. The webpage shows when the program was last run using information pulled from a textFile
3. The webpage shows the top ten foreclosed houses by zip code from a Database query
4. Upon clicking run ---> :runner:
5. A function is run which looks at a textFile containing all the zipCodes in the USA
6. Makes a call to the website and counts the number of foreclosed houses for that particular zip code
7. This information is then updated in the Database 
8. This information is sent back to the user via socket connection
9. Repeat ---> :arrows_counterclockwise:

## Fun Facts:
1. This is a Python based Flask Application running in production within an Alpine Docker Container
2. There is a reverse proxy Nginx Container in front of the application on the same EC2 instance 
3. The webiste has an SSL Certificate to provide authentication and an encrypted connection 


- CordLte is a flask python application that executed web scraping to search the entire US for foreclosed houses based on zip code 

- SQL Alchemy database was created to store all information scrapped

- Focused on quality file structure for the project for scalability in accordance with the flask framework

- Python socketIo and AJAX were used to provide real time updates of the front end from the backend

- Migrated to production with an EC2 instance utilizing git and connected to Route53

- Containerized the application with docker, and put the nginx reverse proxy in front

- Placed the EC2 instance behind an elastic load balancer within an auto scaling group

- Added security with SSL Certificates.
