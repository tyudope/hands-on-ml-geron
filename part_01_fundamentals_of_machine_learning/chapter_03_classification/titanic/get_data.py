import urllib.request
import tarfile
from pathlib import Path
url = 'https://homl.info/titanic.tgz'
tarball_path = Path('titanic.tgz')

if not tarball_path.is_file():
    urllib.request.urlretrieve(url, tarball_path)
    with tarfile.open(tarball_path) as titanic_tarball:
        titanic_tarball.extractall(path="datasets")