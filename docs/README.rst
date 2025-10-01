🕷️ General Purpose Web Scraping App
===================================

This app allows you to extract content from any webpage using either CSS Selectors or XPath.
It's built with Streamlit and supports downloading scraped data as CSV or JSON.

Features
--------

- 🧭 Enter any URL to scrape
- 🧪 Choose extraction method: **CSS Selector** or **XPath**
- 📊 View results in a table
- 📥 Download as CSV or JSON
- 🌐 Deployable to Hugging Face Spaces or run locally

Quickstart
----------

1. **Run Locally:**

.. code-block:: bash

    pip install -r requirements.txt
    streamlit run app.py

2. **Deploy to Hugging Face Spaces:**

- Choose **Gradio** SDK
- Select **Blank** template
- Use **CPU Basic**
- Upload:
  - `app.py`
  - `requirements.txt`
  - `README.rst`

Dependencies
------------

- `streamlit`
- `requests`
- `beautifulsoup4`
- `lxml`
- `pandas`

Example
-------

.. image:: https://your-screenshot-link.png
   :width: 600px
   :alt: Scraping Example Screenshot

License
-------

Apache-2.0
