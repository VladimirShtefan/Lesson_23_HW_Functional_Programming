from requests import request


def get_map():
    url = "http://127.0.0.1:5000/perform_query"

    payload = {
        'file_name': 'apache_logs.txt',
        'cmd1': 'filter',
        'value1': 'GET',
        'cmd2': 'map',
        'value2': '0',
        'cmd10': 'unique',
        'value10': '',
        'cmd8': 'sort',
        'value8': 'desc',
        'cmd6': 'limit',
        'value6': '15',
    }

    response = request("POST", url, data=payload)
    print(response.text)


def map_unique():
    url = "http://127.0.0.1:5000/perform_query"

    payload = {
        'file_name': 'apache_logs.txt',
        'cmd1': 'map',
        'value1': '0',
        'cmd2': 'unique',
        'value2': ''
    }

    response = request("POST", url, data=payload)
    print(response.text)


def regex():
    url = "http://127.0.0.1:5000/perform_query"
    payload = {
        'file_name': 'apache_logs.txt',
        'cmd1': 'regex',
        'value1': '/grok HTTP/1.1" \d{1,3} \d{5}',
        # 'cmd1': 'regex',
        # 'value1': 'images/\\w+\\.png',
        # 'cmd2': 'sort',
        # 'value2': 'asc'
    }
    response = request("POST", url, data=payload)
    print(response.text)


if __name__ == '__main__':
    get_map()
