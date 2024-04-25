import requests
import shutil
import os
import wget
import json
import requests
import shutil
import os
import wget
import json
token = "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"

home_directory = os.path.expanduser("~")
minecraft_mods_directory = os.path.join(home_directory,"AppData","Roaming", ".minecraft", "mods")
api_request = requests.get("https://ullerman.github.io/mod_list.json",auth=('ullerman', token))

mod_urls_json = api_request.text
mod_urls_dict = json.loads(mod_urls_json)

mod_urls = mod_urls_dict['mod_urls']

def download_mods():
  for url in mod_urls:
      filename = wget.detect_filename(url)
      r = requests.get(url, allow_redirects=True)
      open(filename, "wb").write(r.content)
      print(f"Downloaded {filename}")
      try:
        shutil.move(filename, minecraft_mods_directory)
        print(f"Moved {filename} to {minecraft_mods_directory}")
      except shutil.Error as e:
        print(e)
        pass
