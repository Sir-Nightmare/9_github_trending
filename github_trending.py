import requests
from datetime import date, timedelta

GITHUB_REP_API = 'https://api.github.com/search/repositories'
NUMBER_OF_TOP_REPS = 20
NUMBER_OF_DAYS = 7


def date_number_of_days_ago(days_number):
    return str(date.today() - timedelta(days=days_number))


def get_trending_repositories(top_size, url_api, days_number):
    created_date = '{}{}'.format('created:>=', date_number_of_days_ago(days_number))
    params_for_request = {'q': created_date, 'sort': 'stars', 'order': 'desc'}
    repository_data = requests.get(url_api, params=params_for_request).json()
    top_trend_repositories = repository_data['items'][:top_size]
    return top_trend_repositories


def print_repo_list(repo_list):
    print('Top trending repositories created last {0} days:\n'.format(NUMBER_OF_DAYS))
    print('{0:40s}{4:5}{1:5s}{4:5}{2:11s}{4:5}{3:70s}{4:5}'.format('Repository name', 'Stars',
                                                                   'Open issues',
                                                                   'Repository URL', '  |  '))
    print('-' * 144)
    for repo in repo_list:
        print('{0:40s}{4:5}{1:5d}{4:5}{2:8d}   {4:5}{3:70s}{4:5}'.format(repo['name'],
                                                                         repo['stargazers_count'],
                                                                         repo['open_issues_count'],
                                                                         repo['html_url'], '  |  '))


if __name__ == '__main__':
    print_repo_list(get_trending_repositories(NUMBER_OF_TOP_REPS, GITHUB_REP_API, NUMBER_OF_DAYS))
