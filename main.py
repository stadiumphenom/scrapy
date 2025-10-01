import streamlit as st
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd

st.set_page_config(page_title="Web Scraper", page_icon="🕷️", layout="wide")

st.title("🕷️ General Purpose Web Scraping App")

# --- Inputs ---
url = st.text_input("Enter a URL to scrape:", "http://quotes.toscrape.com")
method = st.radio("Choose extraction method:", ["CSS Selector", "XPath"])
query = st.text_input("Enter your selector (e.g., span.text or //span[@class='text']):")

# --- Run scraper ---
if st.button("Scrape"):
    st.write(f"Scraping: {url}")

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except Exception as e:
        st.error(f"Error fetching page: {e}")
    else:
        results = []

        if method == "CSS Selector":
            soup = BeautifulSoup(response.text, "html.parser")
            elements = soup.select(query)
            results = [el.get_text(strip=True) for el in elements]

        elif method == "XPath":
            tree = html.fromstring(response.content)
            elements = tree.xpath(query)
            # XPath can return text or elements
            results = [el if isinstance(el, str) else el.text_content().strip() for el in elements]

        if results:
            df = pd.DataFrame({"Result": results})
            st.success(f"Extracted {len(results)} elements!")
            st.dataframe(df, use_container_width=True)

            # Downloads
            st.download_button("⬇️ Download CSV", df.to_csv(index=False), "results.csv")
            st.download_button("⬇️ Download JSON", df.to_json(orient="records"), "results.json")
        else:
            st.warning("No results found. Try adjusting your selector.")
