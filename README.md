# Google Suggest Keyword Extractor Tool

## Introduction

This tool is a Python Flask-based web application designed to help you extract keywords related to a seed keyword using Google's autocomplete (Google Suggest) feature. It is highly beneficial for SEO professionals, content marketers, and anyone looking to find popular and relevant keywords.

## Features

*   **Google Suggest Keyword Extraction:** Utilizes the Google Suggest API to retrieve related keywords.
*   **Search Depth Control:** Allows you to define the search depth to explore more relevant and extensive keywords.
*   **Alphabet and Number Expansion:** Option to append Persian alphabet letters and numbers to keywords to broaden results.
*   **Manual Prefix and Suffix Addition:** Capability to add custom prefixes and suffixes for personalized and refined results.
*   **Tabular Result Display:** Displays extracted keywords in categorized tables based on the seed keyword.
*   **Table Copy Functionality:** Enables copying each table as text for use elsewhere.
*   **Excel Download:** Feature to download all extracted keywords in CSV format (Excel-compatible).
*   **Persian UI and Right-to-Left Support:** Designed for Persian language and right-to-left users.
*   **Pause and Resume Search:** Ability to pause and resume the keyword extraction process.
*   **Job Reset:** Reset button to clear results and start a new search.

## How to Use

1.  **Prerequisites Installation:**
    *   Ensure Python and pip are installed on your system.
    *   Install the required libraries:

        ```bash
        pip install Flask requests
        ```

2.  **Running the Application:**
    *   Execute the `app.py` file using Python:

        ```bash
        python app.py
        ```

3.  **Accessing the Tool:**
    *   Navigate to `http://127.0.0.1:5000` or `http://localhost:5000` in your web browser.

4.  **Using the Tool:**
    *   **Keyword:** Enter your main seed keyword in the "کلمه کلیدی" (Keyword) field.
    *   **Additional Settings (Click "تنظیمات اضافی" - Additional Settings button):**
        *   **Search Depth:** Define the desired search depth. Higher depth yields broader results.
        *   **Add Prefix and Suffix:** Select desired prefixes and suffixes from the list or add new ones manually.
        *   **Use Alphabet:** Enable this option to append Persian alphabet letters to keywords.
        *   **Use Numbers:** Enable this option to append numbers to keywords.
    *   **"جستجو" (Search) Button:** Click the "جستجو" (Search) button to start the keyword extraction process.
    *   **Results:** Results are displayed in the "نتایج اینجا نمایش داده می‌شوند" (Results will be displayed here) section and also as tables below. Each table corresponds to a seed keyword.
    *   **"توقف/ادامه" (Pause/Resume) Button:** To pause or resume the extraction process during operation.
    *   **"ریست" (Reset) Button:** To clear all results and start a new search.
    *   **"دانلود اکسل" (Download Excel) Button:** To download the results as a CSV file.
    *   **"کپی جدول" (Copy Table) Button (in each table):** To copy the content of a specific table as text.

## File Structure

*   `app.py`: Main Python Flask application file.
*   `index.html`: HTML file for the web user interface.
*   `static/styles.css`: CSS file for styling the user interface.
*   `static/search-svgrepo-com.svg`: Search icon.
*   `templates/index.html`: Template HTML file (in this project, identical to the main `index.html`).

## Prerequisites

*   Python 3.6+
*   Flask
*   requests
*   jQuery
*   Select2
*   Modern web browser

## Development and Contribution

You are welcome to improve this project by providing suggestions and contributing to the codebase.

## License

[Specify MIT License or any other desired license here]

---

**Note:** This tool does not use the official Google API and relies on Google's autocomplete functionality. Excessive use may lead to temporary access restrictions from Google. Use this tool cautiously and reasonably.
