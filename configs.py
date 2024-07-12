# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("25062134")
    API_HASH = os.environ.get("1c2c6d7244d4576b2baab88337b1233a")
    BOT_TOKEN = os.environ.get("7098978512:AAHMV8j-r5YBSCryvWHIkMrE8vtNbbo7bxw")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("-1002208942976")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 6302921275))

    START_TEXT = """
Hi 👋, I am a Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.
"""
    CAPTION = "Video Merged by @{}\n\nMade by @Astra_botz"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
