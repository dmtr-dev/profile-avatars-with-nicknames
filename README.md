# Avatar parser with nicknames from X(Twitter)
### TG Channel - https://t.me/dmtrcrypto [![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/dmtrcrypto)

The program saves avatars and nicknames of users from the specified X(Twitter) profiles

## Installation
1. *Python 3.11*
2. *Downloads the program from Github or using the console on the computer:*
 
    ```
    git clone https://github.com/dmtr-dev/profile-avatars-with-nicknames
    ```
3. *Libraries:*

    ```
    pip install selenium requests
    ```
4. *Download [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/#stable). Also need Chromedriver to match your version of Google Chrome and the operating system. File `chromedriver.exe` must be located in the same folder as the program `main.py`.*

# Details
- The link to subscribers in the profile must be specified in the format https://x.com/.../followers in the file X_accounts.txt.
- Avatars are saved in the Avatars folder.
- Nicknames are saved in a file nicknames.txt in the format NICKNAME:NAME_AVATAR_FILE.
- When starting the program, you will need to enter the number of users to be paired from each specified profile.
- When a warning appears in the console that you need to log in to your X(Twitter) account, you will need to log in to your account and press ENTER in the console. This is required in order to view subscribers in profiles, since X(Twitter) does not allow you to do this without an account.

# Admin
### Questions - https://t.me/dmtrcrypto [![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/dmtrcrypto)
