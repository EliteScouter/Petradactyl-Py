from api_stuff import APIStuff as api


def main():


    id = api.get_server_id(api,api.list_servers(api),"SG RLCraft")
    fileList = api.list_files(api,id)
    
    print(fileList)
    playerList = api.get_player_info(api,id,fileList)
    print(playerList)
























if __name__ == "__main__":
    main()
    
        
    

