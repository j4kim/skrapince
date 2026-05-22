# Skrapince

Simple Scraping of any website and send a notification if a section changes.

## Set up

Create and activate a virtual environmnent, then install the dependencies:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Config

Create `.env` file from example:

    cp .env.example .env

Fill variables:

- `URL`: The URL to scrape
- `SELECTOR`: The selector of the element to check, example "body > p:nth-child(2)"
- `SMTP_SERVER`, `SMTP_LOGIN`, `SMTP_PASSWORD`: SMTP host, login and password
- `MAIL_FROM`: Example "Skrapince <skrapince@3sdl.ch>"
- `MAIL_TO`: Can be a list of emails in the form "Person1 <person1@gmail.com>, Person2 <person2@gmail.com>"
- `MAIL_SUBJECT`: Well, the subject of the email notification

## Run

    python run.py

## Cron

Update crontab:

    crontab -e

Add something like:

    */5 * * * * cd /path/to/skrapince && ./venv/bin/python run.py >> logs.log 2>&1
