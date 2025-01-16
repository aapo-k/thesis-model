import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()

def fetch_articles(query, total_results=20, count_per_request=10):
    url = "https://api.elsevier.com/content/search/scopus"
    headers = {
        "X-ELS-APIKey": os.getenv("ELSEVIER_API_KEY"),
        "Accept": "application/json"
    }
    articles = []
    start = 0

    date_range = "PUBYEAR > 2019"

    while len(articles) < total_results:
        params = {
            "query": f"{query} AND {date_range}",
            "count": count_per_request,
            "start": start,
            "sort": "citedby-count",
            "sort-order": "desc",            
        }

        # Make the API request
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
            break

        data = response.json()
        entries = data.get("search-results", {}).get("entry", [])

        # If no entries returned, break the loop
        if not entries:
            break

        for item in entries:
            articles.append({
                "title": item.get('dc:title'),
                "authors": item.get('dc:creator'),
                "publication_name": item.get('prism:publicationName'),
                "citations": item.get('citedby-count', 0),
                "pub_year": item.get('prism:coverDate', '').split("-")[0]
            })

        start += count_per_request  # Move to the next page

    article_strings = []
    for article in articles:
        article_info = (
            f"Title: {article['title']}\n"
            f"Authors: {article['authors']}\n"
            f"Publication Name: {article['publication_name']}\n"
            f"Year: {article['pub_year']}\n"
            f"Citations: {article['citations']}\n"
        )
        article_strings.append(article_info)
    
    return "\n---\n".join(article_strings)

print(fetch_articles("generative AI"))