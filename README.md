# Twitter-bot-python
Twitter bot written in python which takes a random string from a file which contains, in my case, song lyrics.

`would you like to make a bot? here's the step by step guide (for windows):`

Read the whole thing before doing anything!

## 1. Set up the bot's account
Create an X (formerly Twitter) account to tag it as automatized and apply for APIs.

Go to https://developer.twitter.com/ and select `free`.

You will need to apply for the neccesary APIs, so explain briefly what your bot will do, ex:

_The purpose of this bot is to investigate programming languages and automatization, ..._

_This bot will tweet (strings from a .txt file) every (hour) from a (python) script, available at..._

_I am requesting your APIs for academic purposes, since I would like to create..._

Full example:

```
The purpose of this bot is for academic research.
I am interested in programming languages and would like to try automation with python.
I request your APIs to create a bot which will (post select music lyrics randomly chosen from a previously written .txt file) every (hour).
(optional) This python script will be available at (github.com/your username/ your repo/etc...).
**This bot will not actively engage with other users, by liking, reposting, sending direct messages, adding users to lists, quoting or following them.**
If it does, it's done by the owner of the account, manually.
```

You might have to give it a day or two until you get Twitter's approval for their APIs. Check your email!

## 2. Check all the criteria and settings in your bot's account

Now that you have access to Twitter APIs, go to https://developer.twitter.com/en/portal/projects-and-apps and create a new `project`.

Give it any name you like, and inside it, create the bot's `app`, where we will adjust some settings. Go to the `settings` tab.

| Setting | Value |
| --- | --- |
| App permissions | Read and write |
| Type of App | Web App, Automated App or Bot |
| Callback URI | `Redirect URL & Website URL` |

Paste any link in the website URL, even x.com, google.com or the link to your Github repository even.

Click `save`.

Now, you will need 5 codes which will be important: the `api key`, `api secret key`, `bearer token`, `consumer key`, and `consumer secret key`. Click on `generate`.

They will be shown to you _only once_, you should treat them as passwords, so copy and paste them somewhere safe on your pc, and save them. Only _you_ must have them.

**Remember to add the `automated` label to the bot account, since it is now a requirement in Twitter's terms and conditions.**

## 3. Set up your bot

Write a bot that does what you want it to. You can use my `main.py` file, or do whatever is good for you.

I guess you can do all of this online on Github, but it must be uncomfortable and not practical.
I recommend you do the following:

also, just to test that it runs locally:

Copy my `main.py` file and paste it, to edit it locally on your pc, or download it and open it. You can use Notepad or, if you have it, VSCode (recommended). I made mine with VSCode. You will need:

https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy

https://marketplace.visualstudio.com/items?itemName=ms-python.python

https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

Create a folder for the bot, and name it something like `bot for twitter`, where you will keep the `.txt` file (in my case, with the lyrics to tweet), and the `main.py` file.

In the `main.py` file, replace the 5 keys' values from the previous step, with your own. Put all of them in between " ", except the `bearer token`, which will look like r" " (at least in my case). Save the changes.

`Note: if you're uploading it to Github at some point, make sure to delete the 5 key values before you upload it!`
`Write anything else, like API_KEY = my_api_key instead of the actual values. Only you should have access to them!`

Download my `requirements.txt` file, or copy and paste the following contents into a new local `.txt` file. Save it in the same folder, `bot for twitter`, as `requirements.txt`.

```
requests==2.31.0
tweepy==4.14.0
random
time
```

Next, **create your `tweets.txt` file with your tweets, separated by line.** Take your time. Choose something you like, anything.

Where it says File_path, change its value to whichever the file path to your `tweets.txt` file is, for example:
file_path = 'C:/Users/Sfn02/Downloads/bot for twitter/tweets.txt'. Save these changes.

And now, open a Terminal (`cmd.exe`) in the folder you're working on. If you need to know [how](https://www.wikihow.com/Open-a-Folder-in-Cmd)
Or `Terminal` on [macos](https://www.youtube.com/watch?v=aj9QWELAv9o)/linux from the `bot for twitter` folder.

Now paste this in the `cmd`:

```
pip install -r requirements.txt
```

This will install the necessary requirements to make the bot work. Let it think and process the request.

And then, if it's all set, in a Terminal, `cmd.exe`, opened in the `bot for python` folder, type:

```
python main.py
```

which will make the bot start working. If everything's good, you should see something like:

```
Attempting to tweet...
Tweeted: (any string from your tweets.txt file)
Tweet ID: (some number)
```

If you keep the terminal open while using your computer, every hour you will see it tweets.

If it worked, congratulations!

## 3. Create a new repository on Github
