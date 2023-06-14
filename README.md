TASK: 
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

HOW TO USE IT:
First run "docker-compose up" after project is build go to http://127.0.0.1:8080 page and see the result.

ADVANCE USE:
If you want different flats or completely different web (Different web url in file sreality spider (start url))
Need setup Postgresql database
Setup in this project: 
        hostname = 'localhost'
        port = '5432'
        username = 'postgres'
        password = '12345'
        database = 'sreality'
        
Run "scrapy crawl sreality" 
Run "docker-compose up" and your result are on http://127.0.0.1:8080.

This app is build for web scraping titles and images url - other things will need more editing.

