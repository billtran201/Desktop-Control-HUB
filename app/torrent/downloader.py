import requests

def add_torrent(url, download_path):
    data = {
        "method": "torrent-add",
        "arguments": {
            "filename": url,
            "download-dir": download_path
        }
    }
    response = requests.post('http://localhost:9091/transmission/rpc', json=data)
    print(response.json())

if __name__ == "__main__":
    torrent_url = "https://yts.mx/torrent/download/D0AC46748C23BA28E4AF5B8C99E79DC96C2D6B8C"
    download_path = "E:\Media"
    add_torrent(torrent_url, download_path)
