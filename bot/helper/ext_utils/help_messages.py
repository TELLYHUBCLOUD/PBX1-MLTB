#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands

YT_HELP_MESSAGE = ["""
🎬 <b>YT-DLP Mirror/Leech Guide</b>

<i>Send links along with command or reply to download from YouTube and 1000+ supported sites via yt-dlp engine</i>

<blockquote expandable>
📋 <b>Available Arguments</b>

1️⃣  <b>-n or -name</b> ➜ Rename file
2️⃣  <b>-z or -zip</b> ➜ Zip files or links
3️⃣  <b>-up or -upload</b> ➜ Upload to Drive/RClone/DDL
4️⃣  <b>-b or -bulk</b> ➜ Download bulk links
5️⃣  <b>-i</b> ➜ Download multi links by reply
6️⃣  <b>-m or -sd or -samedir</b> ➜ Multi links in same directory
7️⃣  <b>-opt or -options</b> ➜ Custom yt-dlp options
8️⃣  <b>-s or -select</b> ➜ Select quality from yt-dlp links
9️⃣  <b>-rcf</b> ➜ RClone additional flags
🔟  <b>-id</b> ➜ GDrive folder ID or link
1️⃣1️⃣ <b>-index</b> ➜ Index URL for gdrive
1️⃣2️⃣ <b>-c or -category</b> ➜ GDrive category to upload
1️⃣3️⃣ <b>-ud or -dump</b> ➜ Dump category to upload
1️⃣4️⃣ <b>-ss or -screenshots</b> ➜ Generate screenshots
1️⃣5️⃣ <b>-t or -thumb</b> ➜ Custom thumbnail
</blockquote>
""", """
<blockquote expandable>
📝 <b>Usage Examples</b>

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Send Link Along With Command</b>
<code>/cmd</code> link -s -n new name -opt x:y|x1:y1

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>By Replying To Link</b>
<code>/cmd</code> -n new name -z password -opt x:y|x1:y1

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Rename File</b> (-n or -name)
<code>/cmd</code> link -n new name
📌 <b>Note:</b> Don't add file extension

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Screenshot Generation</b> (-ss or -screenshots)
<code>/cmd</code> link -ss number
📌 Screenshots for each video file

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Custom Thumbnail</b> (-t or -thumb)
<code>/cmd</code> link -t tglink|dl_link
📌 <b>Direct Link:</b> Image URL
📌 <b>Tg Link:</b> Public/Private/Super link to download image

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Quality Selection</b> (-s or -select)
<code>/cmd</code> link -s
📌 Use when default quality is set but you need to select for specific link

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Zip Files</b> (-z or -zip)
<code>/cmd</code> link -z
<code>/cmd</code> link -z password
📌 With or without password protection

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>YT-DLP Options</b> (-opt or -options)
<code>/cmd</code> link -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{"ffmpeg": ["-threads", "4"]}|wait_for_video:(5, 100)

📌 <b>Note:</b> Add ^ before integer or float values
📌 Some values must be numeric, some string
📌 playlist_items:10 works with string (no ^ needed)
📌 playlistend works only with integer (add ^)
📌 You can add tuple and dict also
📌 Use double quotes inside dict

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Multi Links</b> (-i)
<code>/cmd</code> -i 10
📌 Reply to first link only

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Same Upload Directory</b> (-m or -sd or -samedir)
<code>/cmd</code> -i 10 -m folder name
📌 Reply to first link only

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Custom Drive Upload</b> (-id and -index)
<code>/cmd</code> -id drive_folder_link -index https://example.com/0:
<code>/cmd</code> -id drive_id -index https://example.com/0:
📌 drive_id must be folder id or folder link
📌 index must be a valid URL

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Category Select</b> (-c or -category)
<code>/cmd</code> -c category_name
📌 Works for Bot Categories and UserTDs
📌 Case insensitive
📌 Can also select from buttons if not specified

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Dump Select</b> (-ud or -dump)
<code>/cmd</code> -ud dump_name
<code>/cmd</code> -ud @username
<code>/cmd</code> -ud -100xxxxxx
<code>/cmd</code> -ud all
📌 Use -ud all for uploading to all dump chats
📌 Bot must be admin in dump chat

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Upload Destination</b> (-up or -upload)
<code>/cmd</code> link -up rcl
<code>/cmd</code> link -up ddl
<code>/cmd</code> link -up remote:dir/subdir

📌 <b>rcl:</b> Select rclone config, remote and path
📌 <b>ddl:</b> Upload to DDL server
📌 If DEFAULT_UPLOAD is rc ➜ pass up: gd for gdrive
📌 If DEFAULT_UPLOAD is gd ➜ pass up: rc for rclone
📌 If DEFAULT_UPLOAD is ddl ➜ pass up: rc or gd

📌 <b>For manual config path:</b>
<code>/cmd</code> link -up mrcc:main:dump
📌 Add mrcc: before path without space

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>RClone Flags</b> (-rcf)
<code>/cmd</code> link -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
📌 This will override all other flags except --exclude
📌 Check all <a href='https://rclone.org/flags/'>RcloneFlags</a>

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Bulk Download</b> (-b or -bulk)
📌 Use by text message or reply to text file
📌 Links separated by new line
📌 All options should be along with link

<b>Example:</b>
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -z -n new name -opt ytdlpoptions

📌 <b>Note:</b> Can't add -m arg for some links only
📌 Do it for all links or use multi without bulk

📌 <b>Set start and end:</b>
<code>/cmd</code> -b start:end
<code>/cmd</code> -b :end
<code>/cmd</code> -b start
📌 Default start is 0 (first link) to inf

━━━━━━━━━━━━━━━━━━━━━━

📚 <b>Reference</b>
Check all yt-dlp API options from this <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a>
</blockquote>
"""]


MIRROR_HELP_MESSAGE = ["""
🔰 <b>Mirror/Leech Guide</b>

<i>Send links/files along with command to mirror or leech on Telegram, GDrive or DDLs with different engines like RClone, Aria2 or qBittorrent</i>

<blockquote expandable>
📋 <b>Available Arguments</b>

1️⃣  <b>-n or -name</b> ➜ Rename file
2️⃣  <b>-z or -zip</b> ➜ Zip files or links
3️⃣  <b>-e or -extract or -uz or -unzip</b> ➜ Extract/Unzip files
4️⃣  <b>-up or -upload</b> ➜ Upload to Drive/RClone/DDL
5️⃣  <b>-b or -bulk</b> ➜ Download bulk links
6️⃣  <b>-i</b> ➜ Download multi links by reply
7️⃣  <b>-m or -sd or -samedir</b> ➜ Multi links in same directory
8️⃣  <b>-d or -seed</b> ➜ Seed torrent via BitTorrent
9️⃣  <b>-s or -select</b> ➜ Select files from torrent
🔟  <b>-u or -user</b> ➜ Username for auth
1️⃣1️⃣ <b>-p or -pass</b> ➜ Password for auth
1️⃣2️⃣ <b>-j or -join</b> ➜ Join multiple files
1️⃣3️⃣ <b>-rcf</b> ➜ RClone additional flags
1️⃣4️⃣ <b>-id</b> ➜ GDrive folder ID or link
1️⃣5️⃣ <b>-index</b> ➜ Index URL for gdrive
1️⃣6️⃣ <b>-c or -category</b> ➜ GDrive category to upload
1️⃣7️⃣ <b>-ud or -dump</b> ➜ Dump category to upload
1️⃣8️⃣ <b>-ss or -screenshots</b> ➜ Generate screenshots
1️⃣9️⃣ <b>-t or -thumb</b> ➜ Custom thumbnail
</blockquote>
""", """
<blockquote expandable>
📝 <b>Usage Examples</b>

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Send Link Along With Command</b>
<code>/cmd</code> link -n new name

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>By Replying To Link/File</b>
<code>/cmd</code> -n new name -z -e -up upload_destination

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Rename File</b> (-n or -name)
<code>/cmd</code> link -n new name
📌 <b>Note:</b> Doesn't work with torrents

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Direct Link Authorization</b> (-u -p or -user -pass)
<code>/cmd</code> link -u username -p password

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Direct Link Custom Headers</b> (-h or -headers)
<code>/cmd</code> link -h key: value key1: value1

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Screenshot Generation</b> (-ss or -screenshots)
<code>/cmd</code> link -ss number
📌 Screenshots for each video file

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Custom Thumbnail</b> (-t or -thumb)
<code>/cmd</code> link -t tglink|dl_link
📌 <b>Direct Link:</b> Image URL
📌 <b>Tg Link:</b> Public/Private/Super link to download image

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Extract/Zip</b> (-uz -z or -zip -unzip or -e -extract)
<code>/cmd</code> link -e password
📌 Extract password protected

<code>/cmd</code> link -z password
📌 Zip password protected

<code>/cmd</code> link -z password -e
📌 Extract and zip password protected

<code>/cmd</code> link -e password -z password
📌 Extract password protected and zip password protected

📌 <b>Note:</b> When both extract and zip added, it will extract first then zip

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>qBittorrent Selection</b> (-s or -select)
<code>/cmd</code> link -s
📌 Or by replying to file/link

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>qBittorrent/Aria2 Seed</b> (-d or -seed)
<code>/cmd</code> link -d ratio:seed_time
📌 Or by replying to file/link

<b>Examples:</b>
<code>/cmd</code> link -d 0.7:10
📌 ratio and time (time in minutes)

<code>/cmd</code> link -d 0.7
📌 only ratio

<code>/cmd</code> link -d :10
📌 only time

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Multi Links</b> (-i)
<code>/cmd</code> -i 10
📌 Reply to first link/file only

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Same Upload Directory</b> (-m or -sd or -samedir)
<code>/cmd</code> -i 10 -m folder name
📌 Multi message - reply to first link/file

<code>/cmd</code> -b -m folder name
📌 Bulk message/file

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Custom Drive Upload</b> (-id and -index)
<code>/cmd</code> -id drive_folder_link -index https://example.com/0:
<code>/cmd</code> -id drive_id -index https://example.com/0:
📌 drive_id must be folder id or folder link
📌 index must be a valid URL

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Category Select</b> (-c or -category)
<code>/cmd</code> -c category_name
📌 Works for Bot Categories and UserTDs
📌 Case insensitive
📌 Can also select from buttons if not specified

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Dump Select</b> (-ud or -dump)
<code>/cmd</code> -ud dump_name
<code>/cmd</code> -ud @username
<code>/cmd</code> -ud -100xxxxxx
<code>/cmd</code> -ud all
📌 Use -ud all for uploading to all dump chats
📌 Bot must be admin in dump chat

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Upload Destination</b> (-up or -upload)
<code>/cmd</code> link -up rcl
<code>/cmd</code> link -up ddl
<code>/cmd</code> link -up remote:dir/subdir

📌 <b>rcl:</b> Select rclone config, remote and path
📌 <b>ddl:</b> Upload to DDL server
📌 If DEFAULT_UPLOAD is rc ➜ pass up: gd for gdrive
📌 If DEFAULT_UPLOAD is gd ➜ pass up: rc for rclone
📌 If DEFAULT_UPLOAD is ddl ➜ pass up: rc or gd

📌 <b>For manual config path:</b>
<code>/cmd</code> link -up mrcc:main:dump
📌 Add mrcc: before path without space

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>RClone Flags</b> (-rcf)
<code>/cmd</code> link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
📌 This will override all other flags except --exclude
📌 Check all <a href='https://rclone.org/flags/'>RcloneFlags</a>
</blockquote>

<blockquote expandable>
🔹 <b>Bulk Download</b> (-b or -bulk)
📌 Use by text message or reply to text file
📌 Links separated by new line
📌 All options should be along with link

<b>Example:</b>
link1 -n new name -up remote1:path1 -rcf |key:value|key:value
link2 -z -n new name -up remote2:path2
link3 -uz -n new name -up remote2:path2

📌 <b>Note:</b> Can't add -m arg for some links only
📌 Do it for all links or use multi without bulk

📌 <b>Set start and end:</b>
<code>/cmd</code> -b start:end
<code>/cmd</code> -b :end
<code>/cmd</code> -b start
📌 Default start is 0 (first link) to inf

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Join Splitted Files</b> (-j or -join)
📌 Works before extract and zip
📌 Mostly used with -m argument (samedir)
📌 Not for merging two links/files

<b>By Reply:</b>
<code>/cmd</code> -i 3 -j -m folder name
<code>/cmd</code> -b -j -m folder name

<b>For link with splitted files:</b>
<code>/cmd</code> link -j

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>RClone Download</b>
📌 Treat rclone paths exactly like links
<code>/cmd</code> main:dump/ubuntu.iso
<code>/cmd</code> rcl
📌 rcl to select config, remote and path

📌 <b>For manual config path:</b>
<code>/cmd</code> mrcc:main:dump/ubuntu.iso
📌 Add mrcc: before path without space

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Telegram Links</b>
📌 Treat tg links like any direct link
📌 Some links need USER_SESSION_STRING

<b>Types of Links:</b>
🔸 <b>Public:</b> https://t.me/channel_name/message_id
🔸 <b>Private:</b> tg://openmessage?user_id=xxxxxx&message_id=xxxxx
🔸 <b>Super:</b> https://t.me/c/channel_id/message_id

━━━━━━━━━━━━━━━━━━━━━━

📌 <b>Important Notes:</b>
1️⃣ Commands starting with <b>qb</b> are ONLY for torrents
</blockquote>
"""]


RSS_HELP_MESSAGE = """
📡 <b>RSS Feed Guide</b>

<blockquote expandable>
🔹 <b>Format for Adding Feed URLs</b>

Title1 link (required)
Title2 link -c cmd -inf xx -exf xx
Title3 link -c cmd -d ratio:time -z password

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Argument Details</b>

📌 <b>-c</b> ➜ Command + any arg
📌 <b>-inf</b> ➜ Included words filter
📌 <b>-exf</b> ➜ Excluded words filter

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Example</b>

Title https://www.rss-url.com inf: 1080 or 720 or 144p|mkv or mp4|hevc exf: flv or web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value

📌 This filter will parse links that titles contains:
   (1080 or 720 or 144p) AND (mkv or mp4) AND hevc
📌 And doesn't contain:
   (flv or web) AND xxx

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Another Example</b>

inf: 1080 or 720p|.web. or .webrip.|hvec or x264

📌 This will parse titles containing:
   (1080 or 720p) AND (.web. or .webrip.) AND (hvec or x264)
📌 Space added before/after 1080 to avoid wrong matching
📌 10805695 won't match if using " 1080 " with spaces

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Filter Notes</b>

1️⃣ <b>|</b> means AND
2️⃣ Add <b>or</b> between similar keys
   ✅ Correct: 1080 or 720|mkv or mp4
   ❌ Wrong: 1080|mp4 or 720|web
3️⃣ You can add <b>or</b> and <b>|</b> as much as needed
4️⃣ Use static special characters in titles for accurate matching
</blockquote>

⏱️ <b>Timeout:</b> 60 seconds
"""


CLONE_HELP_MESSAGE = ["""
📂 <b>Clone Guide</b>

<i>Send GDrive, Gdtot, Filepress, Filebee, Appdrive, Gdflix link or RClone path along with command or by replying</i>

<blockquote expandable>
📋 <b>Available Arguments</b>

1️⃣ <b>-up or -upload</b> ➜ Upload to Drive/RClone/DDL
2️⃣ <b>-i</b> ➜ Download multi links by reply
3️⃣ <b>-rcf</b> ➜ RClone additional flags
4️⃣ <b>-id</b> ➜ GDrive folder ID or link
5️⃣ <b>-index</b> ➜ Index URL for gdrive
6️⃣ <b>-c or -category</b> ➜ GDrive category to upload
</blockquote>
""",
"""
<blockquote expandable>
📝 <b>Usage Examples</b>

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Supported Links</b>
📌 GDrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix | RClone path

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Multi Links</b> (-i)
<code>/cmd</code> -i 10
📌 Reply to first gdlink or rclone_path only

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>GDrive Link</b>
<code>/cmd</code> gdrive_link

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>RClone Path with Flags</b> (-rcf)
<code>/cmd</code> (rcl or rclone_path) -up (rcl or rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Custom Drive Upload</b> (-id and -index)
<code>/cmd</code> -id drive_folder_link -index https://example.com/0:
<code>/cmd</code> -id drive_id -index https://example.com/0:

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Category Select</b> (-c or -category)
<code>/cmd</code> -c category_name

━━━━━━━━━━━━━━━━━━━━━━

📌 <b>Important Notes:</b>
1️⃣ If -up not specified, rclone destination will be RCLONE_PATH from config.env
2️⃣ If UserTD enabled, it will upload to UserTD by direct arg or category buttons
3️⃣ For multi custom upload, use arg in respective msgs then reply with /cmd -i 10
</blockquote>
"""]


CATEGORY_HELP_MESSAGE = """
📁 <b>Category Change Guide</b>

Reply to an active /{cmd} which was used to start the download or add gid along with {cmd}

📌 This command is mainly for changing category of already added download
📌 You can always use -c or -category to select category before download starts

<blockquote expandable>
🔹 <b>Upload Custom Drive</b>

<code>/{cmd}</code> -id drive_folder_link -index https://example.com/0: gid

📌 Or by replying to active download

━━━━━━━━━━━━━━━━━━━━━━

📌 <b>Note:</b>
🔸 drive_id must be folder id or folder link
🔸 index must be a valid URL
</blockquote>
"""


help_string = [f'''
🤖 <b>Basic Commands</b>

<blockquote expandable>
━━━━━━━━━━━━━━━━━━━━━━
📥 <b>Mirror Commands</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}
│  ➜ Download via file/url/media to upload to Cloud Drive
│
└ /{BotCommands.CategorySelect}
   ➜ Select custom category to upload to Cloud Drive

━━━━━━━━━━━━━━━━━━━━━━
🧲 <b>qBittorrent Commands</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.QbMirrorCommand[0]} or /{BotCommands.QbMirrorCommand[1]}
│  ➜ Download using qBittorrent and upload to Cloud Drive
│
└ /{BotCommands.BtSelectCommand}
   ➜ Select files from torrents by btsel_gid or reply

━━━━━━━━━━━━━━━━━━━━━━
🎬 <b>YT-DLP Commands</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.YtdlCommand[0]} or /{BotCommands.YtdlCommand[1]}
   ➜ Mirror yt-dlp supported link

━━━━━━━━━━━━━━━━━━━━━━
📤 <b>Leech Commands</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.LeechCommand[0]} or /{BotCommands.LeechCommand[1]}
│  ➜ Upload to Telegram
│
├ /{BotCommands.QbLeechCommand[0]} or /{BotCommands.QbLeechCommand[1]}
│  ➜ Download using qBittorrent and upload to Telegram
│
└ /{BotCommands.YtdlLeechCommand[0]} or /{BotCommands.YtdlLeechCommand[1]}
   ➜ Download using yt-dlp and upload to Telegram

━━━━━━━━━━━━━━━━━━━━━━
☁️ <b>GDrive Commands</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.CloneCommand[0]}
│  ➜ Copy file/folder to Cloud Drive
│
├ /{BotCommands.CountCommand} [drive_url]
│  ➜ Count file/folder of Google Drive
│
└ /{BotCommands.DeleteCommand} [drive_url]
   ➜ Delete file/folder from Google Drive
   📌 Only Owner and Sudo

━━━━━━━━━━━━━━━━━━━━━━
❌ <b>Cancel Tasks</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.CancelMirror}
   ➜ Cancel task by cancel_gid or reply
</blockquote>
''',

f'''
👤 <b>User Commands</b>

<blockquote expandable>
━━━━━━━━━━━━━━━━━━━━━━
⚙️ <b>Bot Settings</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]} [query]
   ➜ Open user settings
   📌 Works in PM also

━━━━━━━━━━━━━━━━━━━━━━
🔐 <b>Authentication</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /login
   ➜ Login to bot to access without temp pass system
   📌 Private only

━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Bot Stats</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.StatusCommand[0]} or /{BotCommands.StatusCommand[1]}
│  ➜ Shows status page of all active tasks
│
├ /{BotCommands.StatsCommand[0]} or /{BotCommands.StatsCommand[1]}
│  ➜ Show server detailed stats
│
└ /{BotCommands.PingCommand[0]} or /{BotCommands.PingCommand[1]}
   ➜ Check how long it takes to ping the bot

━━━━━━━━━━━━━━━━━━━━━━
📡 <b>RSS Feed</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.RssCommand}
   ➜ Open RSS menu (Sub/Unsub/Start/Pause)
</blockquote>
''',

f'''
👑 <b>Owner/Sudo Commands</b>

<blockquote expandable>
━━━━━━━━━━━━━━━━━━━━━━
⚙️ <b>Bot Settings</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.BotSetCommand[0]} or /{BotCommands.BotSetCommand[1]} [query]
│  ➜ Open bot settings
│  📌 Only Owner and Sudo
│
└ /{BotCommands.UsersCommand}
   ➜ Show user stats info
   📌 Only Owner and Sudo

━━━━━━━━━━━━━━━━━━━━━━
🔐 <b>Authentication</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.AuthorizeCommand[0]} or /{BotCommands.AuthorizeCommand[1]}
│  ➜ Authorize chat or user to use the bot
│  📌 Only Owner and Sudo
│
├ /{BotCommands.UnAuthorizeCommand[0]} or /{BotCommands.UnAuthorizeCommand[1]}
│  ➜ Unauthorize chat or user
│  📌 Only Owner and Sudo
│
├ /{BotCommands.AddSudoCommand}
│  ➜ Add sudo user
│  📌 Only Owner
│
├ /{BotCommands.RmSudoCommand}
│  ➜ Remove sudo user
│  📌 Only Owner
│
├ /{BotCommands.AddBlackListCommand[0]} or /{BotCommands.AddBlackListCommand[1]}
│  ➜ Add user to blacklist
│  📌 User can't use the bot anymore
│
└ /{BotCommands.RmBlackListCommand[0]} or /{BotCommands.RmBlackListCommand[1]}
   ➜ Remove user from blacklist

━━━━━━━━━━━━━━━━━━━━━━
📢 <b>Broadcast</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.BroadcastCommand[0]} or /{BotCommands.BroadcastCommand[1]} [reply_msg]
   ➜ Broadcast to PM users who have started the bot

━━━━━━━━━━━━━━━━━━━━━━
☁️ <b>GDrive Commands</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.GDCleanCommand[0]} or /{BotCommands.GDCleanCommand[1]} [drive_id]
   ➜ Delete all files from specific folder in Google Drive

━━━━━━━━━━━━━━━━━━━━━━
❌ <b>Cancel Tasks</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.CancelAllCommand[0]}
   ➜ Cancel all tasks
   📌 Use /{BotCommands.CancelAllCommand[1]} for multiple bots

━━━━━━━━━━━━━━━━━━━━━━
🔧 <b>Maintenance</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.RestartCommand[0]} or /{BotCommands.RestartCommand[1]}
│  ➜ Restart and update the bot
│  📌 Only Owner and Sudo
│
├ /{BotCommands.RestartCommand[2]}
│  ➜ Restart and update all bots
│  📌 Only Owner and Sudo
│
└ /{BotCommands.LogCommand}
   ➜ Get log file of the bot
   📌 Handy for crash reports
   📌 Only Owner and Sudo

━━━━━━━━━━━━━━━━━━━━━━
💻 <b>Executors</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.ShellCommand}
│  ➜ Run shell commands
│  📌 Only Owner
│
├ /{BotCommands.EvalCommand}
│  ➜ Run Python code line/lines
│  📌 Only Owner
│
├ /{BotCommands.ExecCommand}
│  ➜ Run commands in exec
│  📌 Only Owner
│
├ /{BotCommands.ClearLocalsCommand}
│  ➜ Clear {BotCommands.EvalCommand} or {BotCommands.ExecCommand} locals
│  📌 Only Owner
│
└ /exportsession
   ➜ Generate user string session
   📌 Same Pyrogram version
   📌 Only Owner

━━━━━━━━━━━━━━━━━━━━━━
📡 <b>RSS Feed</b>
━━━━━━━━━━━━━━━━━━━━━━

└ /{BotCommands.RssCommand}
   ➜ Open RSS menu (Sub/Unsub/Start/Pause)

━━━━━━━━━━━━━━━━━━━━━━
🖼️ <b>Extras</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.AddImageCommand} [url/photo]
│  ➜ Add images to bot
│
└ /{BotCommands.ImagesCommand}
   ➜ Generate grid of stored images
</blockquote>
''',

f'''
🛠️ <b>Miscellaneous Commands</b>

<blockquote expandable>
━━━━━━━━━━━━━━━━━━━━━━
🔧 <b>Extras</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.SpeedCommand[0]} or /{BotCommands.SpeedCommand[1]}
│  ➜ Check speed in VPS/Server
│
└ /{BotCommands.MediaInfoCommand[0]} or /{BotCommands.MediaInfoCommand[1]} [url/media]
   ➜ Generate MediaInfo of media or download URLs

━━━━━━━━━━━━━━━━━━━━━━
🔍 <b>Torrent/Drive Search</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.ListCommand} [query]
│  ➜ Search in Google Drive(s)
│
└ /{BotCommands.SearchCommand} [query]
   ➜ Search for torrents with API

━━━━━━━━━━━━━━━━━━━━━━
🎬 <b>Movie/TV/Drama Search</b>
━━━━━━━━━━━━━━━━━━━━━━

├ /{BotCommands.IMDBCommand}
│  ➜ Search in IMDB
│
├ /{BotCommands.AniListCommand}
│  ➜ Search for anime in AniList
│
├ /{BotCommands.AnimeHelpCommand}
│  ➜ Anime help guide
│
└ /{BotCommands.MyDramaListCommand}
   ➜ Search in MyDramaList
</blockquote>
''']


PASSWORD_ERROR_MESSAGE = """
🔒 <b>Password Required!</b>

<blockquote expandable>
This link requires a password to access

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>How to Add Password</b>

Insert <b>::</b> after the link and write the password

━━━━━━━━━━━━━━━━━━━━━━

🔹 <b>Example</b>

{}::love you

━━━━━━━━━━━━━━━━━━━━━━

📌 <b>Notes:</b>
🔸 No spaces between the <b>::</b> signs
🔸 Password can contain spaces
</blockquote>
"""


default_desp = {
    'AS_DOCUMENT': '📄 Default type of Telegram file upload. Default is False mean as media',
    'ANIME_TEMPLATE': '🎌 Set template for AniList Template. HTML Tags supported',
    'AUTHORIZED_CHATS': '✅ Fill user_id and chat_id of groups/users you want to authorize. Separate them by space',
    'AUTO_DELETE_MESSAGE_DURATION': '⏱️ Interval of time (in seconds), after which the bot deletes its message and command message which is expected to be viewed instantly. Set to -1 to disable auto message deletion',
    'BASE_URL': '🌐 Valid BASE URL where the bot is deployed to use torrent web files selection. Format: http://myip or http://myip:port (http not https)',
    'BASE_URL_PORT': '🔌 BASE_URL Port. Default is 80',
    'BLACKLIST_USERS': '🚫 Restrict users from using the bot. It will display a blacklisted message. USER_ID separated by space',
    'BOT_MAX_TASKS': '📊 Maximum number of tasks bot will run in parallel (Queue tasks included)',
    'STORAGE_THRESHOLD': '💾 To leave specific storage free. Any download leading to less free storage than this value will be cancelled. Default unit is GB',
    'LEECH_LIMIT': '📦 To limit the torrent/direct/ytdlp leech size. Default unit is GB',
    'CLONE_LIMIT': '📂 To limit the size of Google Drive folder/file which you can clone. Default unit is GB',
    'MEGA_LIMIT': '🔷 To limit the size of Mega download. Default unit is GB',
    'TORRENT_LIMIT': '🧲 To limit the size of torrent download. Default unit is GB',
    'DIRECT_LIMIT': '🔗 To limit the size of direct link download. Default unit is GB',
    'YTDLP_LIMIT': '🎬 To limit the size of ytdlp download. Default unit is GB',
    'PLAYLIST_LIMIT': '📝 To limit maximum playlist number',
    'IMAGES': '🖼️ Add multiple telegraph (graph.org) image links that are separated by spaces',
    'IMG_SEARCH': '🔍 Put keyword to download images. Separate each name by comma like anime, iron man, god of war',
    'IMG_PAGE': '📄 Set the page value for downloading an image. Each page has approx 70 images. Default is 1',
    'IMDB_TEMPLATE': '🎬 Set bot default IMDB template. HTML Tags, Emojis supported',
    'AUTHOR_NAME': '✍️ Author name for Telegraph pages, shown in Telegraph page as by AUTHOR_NAME',
    'AUTHOR_URL': '🔗 Author URL for Telegraph page. Put channel URL to show Join Channel',
    'COVER_IMAGE': '🖼️ Cover image for Telegraph page. Put Telegraph photo link',
    'TITLE_NAME': '📌 Title name for Telegraph pages (while using /list command)',
    'GD_INFO': '📝 Description of file uploaded to GDrive using bot',
    'DELETE_LINKS': '🗑️ Delete TgLink/Magnet/File on start of task to auto clean group. Default is False',
    'EXCEP_CHATS': '🚫 Exception chats which will not use logging. chat_id separated by space',
    'SAFE_MODE': '🔒 Hide task name, source link and indexing of leech link for safety precautions. Default is False',
    'SOURCE_LINK': '🔗 Add an extra button of source link whether it is magnet link or file link or DL link. Default is False',
    'SHOW_EXTRA_CMDS': '➕ Add extra commands beside arg format for -z or -e. Commands: /unzipxxx or /zipxxx or /uzx or /zx',
    'BOT_THEME': '🎨 Theme of the bot to switch. Default theme available is minimal. You can make your own theme and add in BSet',
    'USER_MAX_TASKS': '👤 Limit the maximum task for users of group at a time',
    'DAILY_TASK_LIMIT': '📅 Maximum task a user can do in one day',
    'DISABLE_DRIVE_LINK': '🚫 Disable drive link button. Default is False',
    'DAILY_MIRROR_LIMIT': '📊 Total size upto which user can mirror in one day. Default unit is GB',
    'GDRIVE_LIMIT': '☁️ To limit the size of Google Drive folder/file link for leech, zip, unzip. Default unit is GB',
    'DAILY_LEECH_LIMIT': '📤 Total size upto which user can leech in one day. Default unit is GB',
    'USER_TASKS_LIMIT': '📊 The maximum limit on every user for all tasks',
    'FSUB_IDS': '📢 Fill chat_id (-100xxxxxx) of groups/channel you want to force subscribe. Separate by space. Note: Bot should be added as admin',
    'BOT_PM': '📬 File/links send to the bot PM also. Default is False',
    'BOT_TOKEN': '🤖 The Telegram Bot Token that you got from @BotFather',
    'CMD_SUFFIX': '🔢 Telegram bot command index number or custom text. Added at the end of all commands except global commands',
    'DATABASE_URL': '🗄️ Your Mongo Database URL (Connection string). Data saved: auth and sudo users, user settings including thumbnails, RSS data and incomplete tasks',
    'DEFAULT_UPLOAD': '☁️ Whether rc to upload to RCLONE_PATH or gd to upload to GDRIVE_ID or ddl to upload to DDLserver. Default is gd',
    'DOWNLOAD_DIR': '📁 The path to the local folder where the downloads should be downloaded to',
    'MDL_TEMPLATE': '📺 Set bot custom default MyDramaList template. HTML Tags, Emojis supported',
    'CLEAN_LOG_MSG': '🧹 Clean leech log and bot PM task start message. Default is False',
    'LEECH_LOG_ID': '📤 Chat ID to where leeched files would be uploaded. Note: Only for superGroup/channel. Add -100 before channel/superGroup id',
    'MIRROR_LOG_ID': '📥 Chat ID to where mirror files would be sent. Note: Only for superGroup/channel. Add -100 before id. For multiple ids separate by space',
    'EQUAL_SPLITS': '✂️ Split files larger than LEECH_SPLIT_SIZE into equal parts size (Not working with zip cmd). Default is False',
    'EXTENSION_FILTER': '🚫 File extensions that wont upload/clone. Separate them by space',
    'GDRIVE_ID': '☁️ This is the Folder/TeamDrive ID of the Google Drive OR root to which you want to upload all the mirrors',
    'INCOMPLETE_TASK_NOTIFIER': '🔔 Get incomplete task messages after restart. Require database and superGroup. Default is False',
    'INDEX_URL': '🔗 Refer to https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index',
    'IS_TEAM_DRIVE': '👥 Set True if uploading to TeamDrive using google-api-python-client. Default is False',
    'SHOW_MEDIAINFO': '📊 Add button to show MediaInfo in leeched file',
    'SCREENSHOTS_MODE': '📸 Enable or disable generating screenshots via -ss arg. Default is False',
    'CAP_FONT': '🔤 Add custom caption font to leeched files. Available values: b, i, u, s, code, spoiler. Reset var to use regular (no format)',
    'LEECH_FILENAME_PREFIX': '🏷️ Add custom word prefix to leeched file name',
    'LEECH_FILENAME_SUFFIX': '🏷️ Add custom word suffix to leeched file name',
    'LEECH_FILENAME_CAPTION': '📝 Add custom word caption to leeched file/videos',
    'LEECH_FILENAME_REMNAME': '🗑️ Remove custom word from the leeched file name',
    'LOGIN_PASS': '🔑 Permanent pass for user to skip the token system',
    'TOKEN_TIMEOUT': '⏱️ Token timeout for each group member in seconds',
    'DEBRID_LINK_API': '🔗 Set debrid-link.com API for 172 supported hosters leeching support',
    'REAL_DEBRID_API': '🔗 Set real-debrid.com API for torrent cache and few supported hosters (VPN maybe)',
    'LEECH_SPLIT_SIZE': '✂️ Size of split in bytes. Default is 2GB. Default is 4GB if your account is premium',
    'MEDIA_GROUP': '📦 View uploaded splitted file parts in media group. Default is False',
    'MEGA_EMAIL': '📧 E-Mail used to sign-in on mega.nz for using premium account',
    'MEGA_PASSWORD': '🔑 Password for mega.nz account',
    'OWNER_ID': '👑 The Telegram User ID (not username) of the owner of the bot',
    'QUEUE_ALL': '📊 Number of parallel tasks of downloads and uploads. For example if 20 tasks added and QUEUE_ALL is 8, then summation of uploading and downloading tasks are 8 and rest in queue',
    'QUEUE_DOWNLOAD': '📥 Number of all parallel downloading tasks',
    'QUEUE_UPLOAD': '📤 Number of all parallel uploading tasks',
    'RCLONE_FLAGS': '🚩 key:value|key|key|key:value. Check here all RcloneFlags',
    'RCLONE_PATH': '📂 Default rclone path to which you want to upload all the mirrors using rclone',
    'RCLONE_SERVE_URL': '🌐 Valid URL where the bot is deployed to use rclone serve. Format: http://myip or http://myip:port (http not https)',
    'RCLONE_SERVE_USER': '👤 Username for rclone serve authentication',
    'RCLONE_SERVE_PASS': '🔑 Password for rclone serve authentication',
    'RCLONE_SERVE_PORT': '🔌 RCLONE_SERVE_URL Port. Default is 8080',
    'RSS_CHAT_ID': '📡 Chat ID where RSS links will be sent. If you want message to be sent to channel then add channel id with -100 before it',
    'RSS_DELAY': '⏱️ Time in seconds for RSS refresh interval. Recommended 900 seconds at least. Default is 900',
    'SEARCH_API_LINK': '🔍 Search API app link. Supported sites: 1337x, Piratebay, Nyaasi, Torlock, Torrent Galaxy, Zooqle, Kickass, Bitsearch, MagnetDL, Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject and YourBittorrent',
    'SEARCH_LIMIT': '🔢 Search limit for search API, limit for each site and not overall result limit. Default is zero (default API limit for each site)',
    'SEARCH_PLUGINS': '🔌 List of qBittorrent search plugins (github raw links). You can remove/add plugins as you want',
    'STATUS_LIMIT': '📊 Limit the number of tasks shown in status message with buttons. Default is 10. Recommended limit is 4 tasks',
    'STATUS_UPDATE_INTERVAL': '⏱️ Time in seconds after which the progress/status message will be updated. Recommended 10 seconds at least',
    'STOP_DUPLICATE': '🚫 Bot will check file/folder name in Drive incase uploading to GDRIVE_ID. If present in Drive then downloading or cloning will be stopped. Note: Item checked using name not hash, so feature is not perfect yet. Default is False',
    'SUDO_USERS': '👤 Fill user_id of users whom you want to give sudo permission. Separate them by space',
    'TELEGRAM_API': '🔑 This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org',
    'TELEGRAM_HASH': '🔑 This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org',
    'TIMEZONE': '🕐 Set your preferred timezone for restart message. Get yours at http://www.timezoneconverter.com/cgi-bin/findzone.tzc',
    'TORRENT_TIMEOUT': '⏱️ Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds',
    'UPSTREAM_REPO': '📦 Your github repository link. If your repo is private add https://username:{githubtoken}@github.com/{username}/{reponame} format. Get token from Github settings. You can update your bot from filled repository on each restart',
    'UPSTREAM_BRANCH': '🌿 Upstream branch for update. Default is master',
    'UPGRADE_PACKAGES': '📦 Install new requirements file without thinking of crash',
    'SAVE_MSG': '💾 Add button of save message',
    'SET_COMMANDS': '⚙️ Set bot command automatically',
    'JIODRIVE_TOKEN': '🔑 Set token for the jiodrive.xyz to download the files',
    'USER_TD_MODE': '👤 Enable user GDrive TD to use. Default is False',
    'USER_TD_SA': '📧 Add global SA mail for user to give permissions to bot for UserTD upload. Like wzmlx@googlegroups.com',
    'USER_SESSION_STRING': '🔐 To download/upload from your telegram account and to send RSS. To generate session string use python3 generate_string_session.py after mounting repo folder. Note: You cant use bot with private message. Use it with superGroup',
    'USE_SERVICE_ACCOUNTS': '🔑 Whether to use Service Accounts or not with google-api-python-client. Default is False',
    'WEB_PINCODE': '🔢 Whether to ask for pincode before selecting files from torrent in web or not. Default is False',
    'YT_DLP_OPTIONS': '🎬 Default yt-dlp options. Check all possible options or use script to convert cli arguments to api options. Format: key:value|key:value|key:value. Add ^ before integer or float, some numbers must be numeric and some string. Example: format:bv*+mergeall[vcodec=none]|nocheckcertificate:True'
}
