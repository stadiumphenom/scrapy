import streamlit as st
import requests
from lxml import html, etree
import pandas as pd

st.set_page_config(page_title="Web Scraper", page_icon="🕷️", layout="wide")

st.title("🕷️ SOULSCRAPER")

# --- Inputs ---
url = st.text_input("Enter a URL to scrape:", "http://quotes.toscrape.com")
method = st.radio("Choose extraction method:", ["CSS Selector", "XPath"])
query = st.text_input("Enter your selector (e.g., span.text or //span[@class='text']):")

# --- Run scraper ---
if st.button("Scrape"):
    st.write(f"Scraping: {url}")

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
    except Exception as e:
        st.error(f"Error fetching page: {e}")
    else:
        results = []

        try:
            tree = html.fromstring(response.content)

            if method == "CSS Selector":
                try:
                    elements = tree.cssselect(query)
                    results = [el.text_content().strip() for el in elements]
                except cssselect.SelectorSyntaxError as e:
                    st.error(f"Invalid CSS selector: {e}")

            elif method == "XPath":
                try:
                    elements = tree.xpath(query)
                    results = [el if isinstance(el, str) else el.text_content().strip() for el in elements]
                except etree.XPathEvalError as e:
                    st.error(f"Invalid XPath expression: {e}")

        except Exception as e:
            st.error(f"Error parsing HTML: {e}")

        if results:
            df = pd.DataFrame({"Result": results})
            st.success(f"Extracted {len(results)} elements!")
            st.dataframe(df, use_container_width=True)

            # Downloads
            st.download_button("⬇️ Download CSV", df.to_csv(index=False), "results.csv")
            st.download_button("⬇️ Download JSON", df.to_json(orient="records"), "results.json")
        else:
            if not st.session_state.get("st_error_displayed", False):  # prevent duplicate warnings
                st.warning("No results found. Try adjusting your selector.")
                st.session_state["st_error_displayed"] = True
