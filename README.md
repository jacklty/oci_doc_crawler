# oci_doc_crawler
- All pages can be found in https://docs.oracle.com/en-us/laas/toc.json
  - according to the [robots.txt](https://docs.oracle.com/robots.txt), all docs are allowed to be scraped
  - schema
    - .pages
      - p: path
      - t: title
      - s: source
    - .sourceBasepaths
    - .tree
      - i: str
      - c: list[{i:str, c:list}]

# How to do Scraping
- https://medium.com/@speaktoharisudhan/crawling-with-crawl4ai-the-open-source-scraping-beast-9d32e6946ad4

# Cheat Sheet: CSS Selector
- Element: Selects HTML elements directly.
  - Example: p (selects all &lt;p> paragraphs).
- Class: Selects elements with a specific class.
  - Example: .my-class (selects all elements with class="my-class").
- ID: Selects a single element with a specific ID.
  - Example: #my-id (selects the element with id="my-id").
- Descendant: Selects elements that are descendants of another element.
  - Example: div p (selects all &lt;p> elements inside &lt;div> elements).
- Child: Selects elements that are direct children of another element.
  - Example: div > p (selects all &lt;p> elements that are direct children of &lt;div> elements).
- Attribute: Selects elements based on their attributes.
  - Example: [type="text"] (selects all elements with type="text").
