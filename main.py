from playwright.sync_api import sync_playwright
import pandas as pd
import time
from datetime import datetime
import os

def scrape_pricesmart_from_file(file_path):
    os.makedirs("output", exist_ok=True)

    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M")
    hora_file = now.strftime("%H-%M")

    with open(file_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for url in urls:
            try:
                print(f"\n Abriendo: {url}")
                page.goto(url)
                page.wait_for_selector("h2.sf-heading__title", timeout=15000)

                title = page.query_selector("h2.sf-heading__title").inner_text().strip()
                price = page.query_selector("span.sf-price__regular").inner_text().strip()

                print(f"Producto: {title}")
                print(f"Precio: {price}")

                data.append({
                    "Fecha": fecha,
                    "Hora": hora,
                    "URL": url,
                    "Producto": title,
                    "Precio": price
                })

                time.sleep(1)

            except Exception as e:
                print(f"Error en {url}: {e}")
                data.append({
                    "Fecha": fecha,
                    "Hora": hora,
                    "URL": url,
                    "Producto": "Error",
                    "Precio": "Error"
                })

        browser.close()

    base_name = f"precios_pricesmart_{fecha}_{hora_file}"
    csv_path = os.path.join("output", f"{base_name}.csv")
    xlsx_path = os.path.join("output", f"{base_name}.xlsx")

    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    df.to_excel(xlsx_path, index=False)

    print("\n Archivos guardados:")
    print(f"CSV:  {csv_path}")
    print(f"Excel: {xlsx_path}")


scrape_pricesmart_from_file("links.txt")
