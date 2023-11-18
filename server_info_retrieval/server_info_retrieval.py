import json
import requests

def get_server_info(server):
    try:
        response = requests.get(server['url'])
        if response.status_code == 200:
            server_info = {
                "name": server['name'],
                "url": server['url'],
                "software_version": response.headers.get("Server", "N/A")
            }
            return server_info
        else:
            return None
    except Exception as e:
        return None

def main():
    input_file = 'servers.json'
    output_file = 'server_info.txt'

    with open(input_file, 'r') as json_file:
        servers = json.load(json_file)

    server_info_list = []

    for server in servers:
        server_info = get_server_info(server)
        if server_info:
            server_info_list.append(server_info)

    with open(output_file, 'w') as txt_file:
        for server_info in server_info_list:
            txt_file.write(f"Server: {server_info['name']}\n")
            txt_file.write(f"URL: {server_info['url']}\n")
            txt_file.write(f"Software Version: {server_info['software_version']}\n\n")

if __name__ == "__main__":
    main()
