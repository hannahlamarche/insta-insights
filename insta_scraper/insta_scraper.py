import requests
import json
import time


def fetch_report_details(username, password):
    followers = []
    followings = []
    dont_follow_me_back = []
    i_dont_follow_back = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        print("Process started! Give it a couple of seconds")

        login_url = 'https://www.instagram.com/accounts/login/'
        login_data = {
            'username': username,
            'password': password,
        }
        login_res = session.post(login_url, data=login_data)
        login_res.raise_for_status()

        user_query_res = session.get(f"https://www.instagram.com/web/search/topsearch/?query={username}")
        user_query_res.raise_for_status()
        user_query_json = user_query_res.json()

        user_id = user_query_json['users'][0]['user']['pk']

        after = None
        has_next = True

        while has_next:
            variables = json.dumps({
                "id": user_id,
                "include_reel": True,
                "fetch_mutual": True,
                "first": 50,
                "after": after
            })

            url = f"https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={variables}"
            res = session.get(url)
            res.raise_for_status()
            res_json = res.json()

            has_next = res_json['data']['user']['edge_followed_by']['page_info']['has_next_page']
            after = res_json['data']['user']['edge_followed_by']['page_info']['end_cursor']
            followers += [
                {
                    "username": node['node']['username'],
                    "full_name": node['node']['full_name']
                }
                for node in res_json['data']['user']['edge_followed_by']['edges']
            ]

            time.sleep(1)

        print("Followers:", followers)

        after = None
        has_next = True

        while has_next:
            variables = json.dumps({
                "id": user_id,
                "include_reel": True,
                "fetch_mutual": True,
                "first": 50,
                "after": after
            })

            url = f"https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={variables}"
            res = session.get(url)
            res.raise_for_status()
            res_json = res.json()

            has_next = res_json['data']['user']['edge_follow']['page_info']['has_next_page']
            after = res_json['data']['user']['edge_follow']['page_info']['end_cursor']
            followings += [
                {
                    "username": node['node']['username'],
                    "full_name": node['node']['full_name']
                }
                for node in res_json['data']['user']['edge_follow']['edges']
            ]

            time.sleep(1)

        print("Followings:", followings)

        dont_follow_me_back = [
            following for following in followings
            if not any(follower['username'] == following['username'] for follower in followers)
        ]

        print("Don't Follow Me Back:", dont_follow_me_back)

        i_dont_follow_back = [
            follower for follower in followers
            if not any(following['username'] == follower['username'] for following in followings)
        ]

        print("I Don't Follow Back:", i_dont_follow_back)

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Error: {e}")
    except Exception as err:
        print(f"Error: {err}")
