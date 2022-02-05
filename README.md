# scrapy_crawler
A crawler with scrapy-selenium

The bot is scraping specified page and exporting the results to json file

# For the crawler to work
1. all dependencies must be installed
2. the chromedriver must match the google chrome version installed on the computer
    - the `chromedriver` coming with this project is version 97
    - If replacement is needed, download from here `https://chromedriver.chromium.org/downloads`
    - You can check your google chrome version by going in `Google Chrome -> Help -> About Google Chrome`



# How to use
To use the crawler navigate in the first `scrapyproject` directory
open cmd and type
```
scrapy crawl mangospider -O output.json
```
`output.json` file will be created in the `scrapyproject` directory


>Updated method without selenium here https://github.com/Xamaneone/scrapy_crawler_mango_updated
