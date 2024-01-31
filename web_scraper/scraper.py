import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Ottoman_Empire"

# function to get count of citations
def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all("sup", class_="noprint Inline-Template")

    return len(citations)

# function to generate report of passages where citations are needed
def get_citations_needed_report(url):
    response = requests.get(url) # makes a get request to URL
    soup = BeautifulSoup(response.content, 'html.parser') # parsing HTML content of page using BeautifulSoup
    citations = soup.find_all("sup", class_="noprint Inline-Template") # find instances of <sup> tags with specified class

    # check if no citations
    if not citations:
        return "No citations needed."
    
    # initialize empty string to store report
    report = ""
    for citation in citations: # iterate over each citation found
        passage_tag = citation.find_next("p") # find next <p> tag after current <sup> tag

        if passage_tag: # check if <p> tag exists
            passage = passage_tag.text # extract text content of <p> tag
            report += f"Citation needed for: \"{passage}\" \n" # append passage to report string

    return report # return final report

count = get_citations_needed_count(url) # call function to get count of citations
print(f"Number of Citations needed: {count}")

report = get_citations_needed_report(url) # calling function to get report of passages needing citations
print(report)
