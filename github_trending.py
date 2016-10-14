import requests
from datetime import date, timedelta

GITHUB_REP_API = 'https://api.github.com/search/repositories'
NUMBER_OF_TOP_REPS = 20


def data_week_ago():
    return str(date.today() - timedelta(days=7))


def get_trending_repositories(top_size):
    created_date = 'created:>=' + data_week_ago()
    params_for_request = {'q': created_date, 'sort': 'stars', 'order': 'desc'}
    repository_data = requests.get(GITHUB_REP_API, params=params_for_request).json()
    top_trend_repositories = repository_data['items'][:top_size]
    return top_trend_repositories


def print_repo_list(repo_list):
    print('Top trending repositories created last week:\n')
    print('{0:40s} {1:5s}  {2:4s}     {3:30s}'.format('Repository name',
                                                      'Stars', 'Open issues', 'Repository URL'))
    print('-' * 100)
    for repo in repo_list:
        print('{0:40s} {1:5d}    {2:4d}       {3:30s}'.format(repo['name'],
                                                              repo['stargazers_count'], repo['open_issues_count'],
                                                              repo['html_url']))


if __name__ == '__main__':
    print_repo_list(get_trending_repositories(NUMBER_OF_TOP_REPS))
