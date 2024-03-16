![Logo](https://user-images.githubusercontent.com/94779840/220741614-2ea1ace7-4bd7-411a-80e8-21ec40b75b4e.jpg)
# IGFI 🤖

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9864f7f507804c81975576919a4a684a?logo=codacy&style=for-the-badge)](https://app.codacy.com/gh/new92/IGFI/dashboard?logo=codacy&style=for-the-badge) [![Number of files](https://img.shields.io/github/directory-file-count/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/directory-file-count/new92/IGFI) [![Code size](https://img.shields.io/github/languages/code-size/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/languages/code-size/new92/IGFI) [![Followers](https://img.shields.io/github/followers/new92?style=for-the-badge)](https://img.shields.io/github/followers/new92) [![Forks](https://img.shields.io/github/forks/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/forks/new92/IGFI) [![Stars](https://img.shields.io/github/stars/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/stars/new92/IGFI) [![Open issues](https://img.shields.io/github/issues-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-raw/new92/IGFI) [![Closed Issues](https://img.shields.io/github/issues-closed-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-closed-raw/new92/IGFI) [![Open pull requests](https://img.shields.io/github/issues-pr-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-pr-raw/new92/IGFI) [![Closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/issues-pr-closed-raw/new92/IGFI) [![Discussions](https://img.shields.io/github/discussions/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/discussions/new92/IGFI) [![Contributors](https://img.shields.io/github/contributors/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/contributors/new92/IGFI) [![Language](https://img.shields.io/github/languages/top/new92/IGFI?style=for-the-badge)](https://img.shields.io/github/languages/top/new92/IGFI?style=for-the-badge)

With IGFI, you can effortlessly increase their followers by simply logging in. **It works seamlessly for both private and public accounts**. Upon the initial use, you can gain up to **50 followers**! Subsequent uses typically result in an addition of 25-30 followers. To maintain account safety, it is recommended to use the script every two (2) days to prevent potential blocking. The script also provides valuable information, including the number and the usernames of the followers added.

> If you find this repository helpful, please consider giving it a star and/or forking it. Your support encourages me to keep sharing similar repositories. If you encounter any issues, have suggestions, or simply didn't like the script, feel free to contact me anytime at <a href='mailto:new92github@gmail.com'>this email address</a>, or start a <a href="https://github.com/new92/IGFI/discussions">discussion</a>, or open an <a href="https://github.com/new92/IGFI/issues">issue</a>. Any form of feedback is welcome and appreciated (please refrain from using vulgar language).

[![github-stats-card](https://kasroudra-stats-card.onrender.com/repo?user=new92&repo=IGFI&layout=compact&theme=vue)](https://github.com/KasRoudra/github-stats-card)

# <a href="https://github.com/new92/IGFI/discussions/56">Potential feature 🚀</a>

## Urls 🔗

 - [License](https://github.com/new92/IGFI/blob/main/LICENSE.md)
 - [Contributing](https://github.com/new92/IGFI/blob/main/CONTRIBUTING.md)
 - [Code of conduct](https://github.com/new92/IGFI/blob/main/CODE_OF_CONDUCT.md)
 - [You may also find interesting](https://github.com/new92?tab=repositories)


## Author ✍️

- [@new92](https://www.github.com/new92)

## Installation 📥

- **Make sure you're logged in to your Instagram account from Firefox before executing IGFI.**

### Linux 🐧

```bash
sudo su
git clone https://github.com/new92/IGFI
cd IGFI
sudo pip install -r ./files/requirements.txt
python3 ./cookies.py
python3 ./igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### Windows 🪟

```bash
git clone https://github.com/new92/IGFI
cd IGFI
pip install -r ./files/requirements.txt
python3 cookies.py
python3 igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### MacOS 🍎

```bash
git clone https://github.com/new92/IGFI
cd IGFI
python -m pip install -r ./files/requirements.txt
python3 ./cookies.py
python3 ./igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### Docker 🐋

```bash
git clone https://github.com/new92/IGFI
cd IGFI
docker build -t igfi .
docker run -e DOCKER_CONTAINER=true -e USERNAME=<username> -e PASSWORD=<password> -e SESSION=<path_to_session_file> -p 4000:4000 -it igfi
```

## Virtual environment setup 💻

### Windows 🪟

```bash
git clone https://github.com/new92/IGFI
cd IGFI
python -m venv igfi
.\igfi\scripts\activate
pip install -r ./files/requirements.txt
python3 cookies.py
python3 igfi.py -u <username> -p <password> --session <path_to_session_file>
```

### Linux 🐧 / MacOS 🍎

```bash
git clone https://github.com/new92/IGFI
cd IGFI
python -m venv igfi
source venv/bin/activate
pip install -r ./files/requirements.txt
python3 ./cookies.py
python3 ./igfi.py -u <username> -p <password> --session <path_to_session_file>
```

##### Virtual environment deactivation 📭

##### Windows 🪟

`.\venv\Scripts\deactivate`

##### Linux 🐧 / MacOS 🍎

`deactivate`

## Update 🔄️

```bash
cd <path_to_script>/IGFI
git pull
```

## Features 🚀

- [ ] **Add followers from specific categories (ex. fitness, education, food, entertainment etc.)**
- [ ] Script which doesn't depend on third-party modules.
- [ ] GUI
- [ ] Docker support
- [x] ~~Virtual environment setup~~
- [x] ~~Execute the script directly from terminal (using argparse)~~
- [ ] V4 (this version will include the features as shown above and some extra)
- [x] ~~Display the usernames of the followers added~~ **<a href="https://github.com/new92/IGFI/scripts/tree/main/igfi.py">URL</a>**
- [x] ~~V3 script~~ **<a href='https://github.com/new92/IGFI/tree/main/scripts/igfi.py'>URL</a>**

## Tested on 🔎

| OS | Linux | Windows | MacOS
| :---: | :---: | :---: | :---: |
| -> | Kali |
| -> | | 10 |
| -> | | 11 |

## Screenshots 📸

**Photos of the script can be found at <a href="https://github.com/new92/IGFI/tree/main/photos">this url</a>**

## Contributing 🤝

Contributions are always welcome !

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
For more info please check the `CODE_OF_CONDUCT.md` file

## Feedback 💭

If you have any feedback, please reach out to us at <a href="mailto:new92github@gmail.com">this email address</a>.

**Feel free to contact us anytime ! You'll get a reply within a day. Please avoid abusive or offensive language.
If you are reporting a bug or making a suggestion please make sure your make it as detailed as possible.**

## FAQ 🤔

#### Question 1

- Error while logging in ?

Answer ➡️ This error can be resolved by simply executing the `cookies.py` script and running the script again.

#### Question 2

- Where can I report a bug ?

Answer ➡️ You can report a bug by creating an issue or by emailing us at <a href="mailto:new92github@gmail.com">this</a> email address. Please feel free to include screenshots, the error which is being displayed, the OS you are using, your default browser etc. Any other additional info will be appreciated and will help to resolve the bug faster

### Question 3

- Is illegal to increase followers using script(s) ?

Answer ➡️ No, not at all! It's similar to asking if following and unfollowing an account is illegal, even though Instagram doesn't recommend using this technique to increase your followers.


### Question 4

- Can my account get blocked by using this script ?

Answer ➡️ Only if you're using a very old version of Instagram. But the script has been tested in several accounts and none of them got blocked.

## License 📜

[![License](https://img.shields.io/github/license/new92/IGFI?style=for-the-badge)](https://github.com/new92/IGFI/blob/main/LICENSE.md)
