# Book.be Scraper

## About

Collects book titles from [book.be](https://book.be). See [this](https://gist.github.com/Addono/de7b0633d7faa1da3aeaf1f43985b163) example of a scrape getting the titles of all books released in 2019.

## Installation

Create a virtual Python 3 environment.
```bash
virtualenv venv
```

Enable the environment.
```bash
source venv/bin/activate
```

Install all requirements.
```bash
pip install -r requirements.txt
```

## Usage

Run the spider.

```bash
scrapy runspider spider.py
```

Or if you want to save the output gathered by the spider, e.g. as CSV:
```bash
scrapy runspider spider.py --output=res.csv -t csv
```

If you want to filter the collected titles, then change `URL` in `spider.py` to include the desired filters.

