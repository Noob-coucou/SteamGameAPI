from SteamAPI import SteamAPI

if __name__ == "__main__":
    steam_api = SteamAPI()
    app_list = steam_api.get_app_list()
    #测试获取10个游戏的信息
    if app_list is not None:
        max_games = 10
        games_count = 0

        for app_id, app_name in app_list.items():
            print(f"AppID: {app_id}, 游戏名称: {app_name}")

            game_info = steam_api.get_game_info(app_id, app_name)

            if game_info is not None:
                print(f"游戏信息: {game_info}")
                games_count += 1

                if games_count >= max_games:
                    break
            else:
                print(f"未找到游戏信息 for AppID: {app_id}")
    else:
        print("无法获取App列表")
