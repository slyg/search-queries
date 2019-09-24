from csv import DictWriter

from requests import get

API_CODE_SEARCH_BASE = "https://api.github.com/search/code"
API_REPO_SEARCH_BASE = "https://api.github.com/search/repositories"


def get_repos_for_repo_search(query):
    url = "{}?q={}".format(API_REPO_SEARCH_BASE, query)
    data = get(url).json()
    def lens(item): return {'name': item['name'],
                            'archived': item['archived']}
    return map(lens, data['items'])


def get_repos_for_code_search(query):
    url = "{}?q={}".format(API_CODE_SEARCH_BASE, query)
    data = get(url).json()
    def lens(item): return {'name': item['repository']['name']}
    return map(lens, data['items'])


def save_csv(output_file, fieldnames, rows):
    with open(output_file, 'w', newline='') as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("Report saved: {}".format(output_file))
