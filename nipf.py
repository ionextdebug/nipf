from urllib.request import urlretrieve
import sys
import os
from zipfile import ZipFile 

path = os.getcwd()
org_repository = sys.argv[1]
facility = sys.argv[2]
facility_zip = facility+".zip"

nostr_facilities = os.path.join(path,"nostr_facilities")
exists_nostr_facilities = os.path.exists(nostr_facilities)
if not exists_nostr_facilities:
   os.makedirs(nostr_facilities)

url = f"https://raw.githubusercontent.com/{org_repository}/main/{facility_zip}"

filename_target_zip = os.path.join(path,"nostr_facilities",facility_zip)
filename_target = os.path.join(path,"nostr_facilities",facility)

urlretrieve(url, filename_target_zip)

with ZipFile(filename_target_zip, 'r') as zObject:
    zObject.extractall(path=filename_target)
    os.remove(filename_target_zip)

