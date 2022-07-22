<div align=center>
    <img src="images_readme/avatar.jpg" width="100">
    <h1>🇺🇦 AssBot (open-source Ebobot)</h1>
</div>

<div align=center>
    <h2>Description</h2>
    <p>This bot is like "Ebobot" @kraft28_bot but that's open-source was written on Python.</p>
</div><hr>

<div>
    <h2>Configuration</h2>
    <h3>Typical .env file</h3>
    <ul>
        <li>TOKEN=here is your telegram token</li>
        <li>OWNER=here is owner's telegram id</li>
    </ul>
    <h3>Example</h3>
</div>

```
TOKEN=1777031958:AAF4O-_GmkvFJvhP7cVlxa697Y48rUPC4Hc
OWNER=37592934
```

<div>
    <h3>Configuration in config.py</h3>
    <ul>
        <li>DB_NAME - database name</li>
        <li>TOKEN - token which gets in .env file</li>
        <li>SUPER_USERS - owners id which gets in .env file and you can add other to list</li>
    </ul>
</div>

<div>
    <div align=center>
        <h3>Recommended Python version: Python 3.10.5</h3>
    </div>
    <div>
        <h3><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.iconfinder.com%2Fdata%2Ficons%2Fprogramming-17%2F24%2Fprogramming-module-2-512.png&f=1&nofb=1" width="30"> Modules in use:</h3>
    </div>
    <ul>
        <li><b>random</b></li>
        <li><b>sqlite3</b></li>
        <li><b>os</b></li>
        <li><b>time</b></li>
        <li><b>aiogram</b></li>
    </ul>
</div><hr>

## Running the bot
Creating a virtual enviroment
```
python3 -m venv venv
```

Activate venv
```
source venv/bin/activate
```

Installing necessary modules
```
pip3 install -r requirements.txt
```

Run the bot
```
python3 app.py
```
Deativate venv
```
deactivate
```

<div>
    <div>
        <h3><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F1%2F12%2FUser_icon_2.svg%2F768px-User_icon_2.svg.png&f=1&nofb=1" width="30"> User commands:</h3>
    </div>
    <div>
        <ul>
            <li>
                <b>/start</b> — greet the bot
            </li>
            <li>
                <b>/ass</b> — start playing
            </li>
            <li>
                <b>/luck</b> — try your luck
            </li>
            <li>
                <b>/help</b> — show help message
            </li>
            <li>
                <b>/leave</b> — leave game and delete user's data
            </li>
            <li>
                <b>/r text</b> — send report to `reports` table
            </li>
            <li>
                <b>/statistic</b> — show top list of users
            </li>
            <li>
                <b>/about</b> — show info about the developer
            </li>
        </ul>
    </div><hr>
    <div>
        <h3><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpngimage.net%2Fwp-content%2Fuploads%2F2018%2F05%2Fadmin-logo-png-6.png&f=1&nofb=1" width="30"> Admin's commands:</h3>
    </div>
    <div>
        <ul>
            <li>
                <b>/admin</b> — show admin commands
            </li>            
            <li>
                <b>/bl group_id</b> — show banned users
            </li>
            <li>
                <b>/ban group_id user_id</b> — add user to blacklist
            </li>
            <li>
                <b>/groups</b> — show groups id and name where bot are using
            </li>
            <li>
                <b>/ub group_id user_id</b> — unban user
            </li>
            <li>
                <b>/reports</b> — show all reports from table `reports`
            </li>
            <li>
                <b>/dreports</b> — show all reports from table `reports` (detailed form)
            </li>            
            <li>
                <b>/clear</b> — delete all rows in table `reports`
            </li>
            <li>
                <b>/notify</b> — notify all groups by your message
            </li>
        </ul>
    </div>
</div>

## Screenshots

> Adding bot to the group (it needs for creating a group's table)
<img src="images_readme/bot_added.png" width=400>

> **/start**
<img src="images_readme/start.png" width=400>

> **/help**
<img src="images_readme/help.png" width=400>

> **/ass** (your ass can reduce and icrease by random or stay without changes)
<img src="images_readme/ass.png" width=400>

> **/luck** (allows after 100cm)
<img src="images_readme/luck.png" width=400>

> **/statistic**
<img src="images_readme/statistic.png" width=400>

> **/leave**
<img src="images_readme/leave.png" width=400>

> **/about**
<img src="images_readme/about.png" width=400>

