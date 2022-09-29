from requests import request


def get_map():
    url = "http://127.0.0.1:5000/perform_query"

    payload = {
        'file_name': 'apache_logs.txt',
        'cmd1': 'filter',
        'value1': 'GET',
        'cmd2': 'map',
        'value2': '0',
        'cmd3': 'unique',
        'value3': '',
        'cmd4': 'sort',
        'value4': 'desc',
        'cmd5': 'limit',
        'value5': '15',
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


if __name__ == '__main__':
    get_map()
