# Supermarket Price Scraper with Python and Playwright

This project aims to automate the collection of product prices from online supermarkets, starting with **PriceSmart Costa Rica**.

> This is a work-in-progress project. The goal is to expand it to at least two more supermarkets and eventually perform data analysis on the collected prices.

---

## Why this project?

Most supermarkets don't offer public APIs or structured data access for price comparison. This scraper was built to:

- Create a historical price record of key products.
- Analyze price trends over time.
- Compare prices across different supermarkets.

---

## Challenges encountered

Several technical issues were faced during development:

- **The product data was not in the initial HTML** - it was loaded dynamically via JavaScript.
- **Selenium didn't work as expected** - it couldn't reliably extract the product name and price.
- **The site uses a modern frontend framework (Vue)** - meaning elements load after the DOM is rendered.
- **The content was not inside iframes**, but loaded in layers dynamically.

---

## Why Playwright?

To solve these challenges, I used **Playwright**, a modern browser automation tool that:

- Automatically waits for dynamic content to load.
- Has better support for modern JavaScript frameworks like Vue, React, and Angular.
- Allows precise control over page loading and element rendering.

---

## Technologies used

- **Python 3.10+**
- **Playwright** – headless browser automation.
- **Pandas** – data transformation and export.
- **Openpyxl** – Excel export support.
- **dotenv** – environment configuration support (future use).
- **Git + GitHub** – version control and collaboration.

---

## Current functionality

- Reads a list of product URLs from `links.txt`.
- Visits each URL and extracts:
  - Product name
  - Price
  - Scraping date and time
- Saves the data into:
  - `output/prices_pricesmart_YYYY-MM-DD_HH-MM.csv`
  - `output/prices_pricesmart_YYYY-MM-DD_HH-MM.xlsx`

---

Future plans
 - Add support for more supermarkets (e.g., Walmart CR, AutoMercado).

 - Store results in a unified local or cloud database.

 - Compare similar products across stores.

 - Create dashboards to visualize price trends.

 - Implement automatic reports or price alerts.

