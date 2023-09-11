import requests


class SteamAPI:
    def __init__(self):
        self.base_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"

    def get_app_list(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            data = response.json()
            app_list = data["applist"]["apps"]
            return {str(app["appid"]): app["name"] for app in app_list}
        else:
            return None

    def get_game_info(self, app_id, game_name):
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
        response = requests.get(url)
        if response.status_code == 200:
            game_all_info = response.json()

            if str(app_id) in game_all_info:
                game_data = game_all_info[str(app_id)]["data"]

                game_categories = game_data.get("categories", [])
                game_genres = game_data.get("genres", [])

                game_info = {
                    "appid": app_id,
                    "name": game_name,
                    "categories": [category["id"] for category in game_categories],
                    "genres": [genre["id"] for genre in game_genres]
                }

                return game_info
            else:
                return None
        else:
            return None