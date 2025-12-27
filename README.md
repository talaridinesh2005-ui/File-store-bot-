<h2 align="Center"><b><i>File-sharing-Bot</i></b></h2>
<center><img src="https://files.catbox.moe/ufzpkn.jpg" ></center>
<p align="center">
  <a href="https://www.python.org">
    <img width="10" height="10" src="https://ibb.co/CK3TrSsj" width ="250">
  </a> 
</p>


<b><i>Telegram Bot to store Posts and Documents and it can Access by Special Links.</i></b> 


### Features

- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku ,koyeb and render.
- Protect Content to Prevent Forwarding
- Auto-Delete Files After a Configurable Time
- 4 customisable force suscribe buttons
- To check Separate force subscribe channel 

<details><summary><b> Upcoming Features :</b></summary>
 ## What’s Next Going to add

These features are in the pipeline, and contributions from the community are welcome!


- [x] **Channel Join Request**
   [ Implement a feature that prompts users to join a specified Telegram channel before accessing the bot's functionalities.]

- [x]  **Database search**
   [ This feature is used to search file from database by the user and get the file, for security of bot the file should be delete in certain time]

- [x] **IN-Built fsub customize**
   [ This feature is used to change the force subscribe button by the Admin while bot was running ]
</details>

<details><summary><b> Deploy Details :</b></summary>
### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 


#### Deploy in your VPS or Commandline
````bash
git clone https://github.com/Techfreak555/TF-File-store-bot
cd TF-File-store-bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````
</details>

<details><summary><b> Command of Bot :</b></summary>
### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users

/stats - checking your bot uptime
```
</details>

<details><summary><b> Required Data :</b></summary>
### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/Techfreak555/TF-File-store-bot/blob/main/README.md#start_message'>fillings</a>
* `START_PIC` Optional: URL or file path of the image to be sent as the start message
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding
* `AUTO_DELETE_TIME `  Set the time in seconds for automatic file deletion. Default is False, which disables auto-deletion.

### Extra Variables

* `AUTO_DELETE_MSG` put your custom deletion text if you want Setup Custom deletion messaeg,
* `AUTO_DEL_SUCCESS_MSG` Set your custom success message for when the file is successfully deleted
* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/Techfreak555/TF-File-store-bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and <a href='https://github.com/Techfreak555/TF-File-store-bot/blob/main/README.md#custom_stats'>fillings</a>
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML
* `DATABASE_NAME` Your mongo db session name
</details>

<details><summary><b> Optional Data :</b></summary>
### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime

</details>

<details><summary><b> Credits :</b></summary>
### Credits

- Telegram channel 👉<a href="https://t.me/tech_freak_tamil">Click here</a>

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/Techfreak555/TF-File-store-bot) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

</details>

   **Star this Repo if you Liked it ⭐⭐⭐**

