import subprocess

# discord.py を読み込む
import discord

# Discordとbotの情報
## Access Token
token = "botのアクセストークン"

## Channel ID(int)
chan_mc = ""    # Minecraft
chan_ck = ""    # CoreKeeper
chan_tr = ""    # Terraria
chan_cmd = ""   # Commmand

# サーバープロセスの情報
## Minecraft
mc_finm = "サーバー実行ファイル名.jar"
maxMem = "8G"  # 任意の最大メモリ割り当てサイズ
minMem = "8G"  # 任意の最小メモリ割り当てサイズ

## Core Keeper
ck_finm = "Launch.bat"

## Terraria
tr_finm = "Launch.bat"

# 接続に必要なオブジェクトを生成
client = discord.Client()

# サーバー操作用
class MCserver_process:     # Minecraft
    def __init__(self, mc_finm, maxMem, minMem):
        self.server = None
        self.command = ["java", "-server",f"-Xms{minMem}", f"-Xmx{maxMem}", "-jar", mc_finm, "nogui"]
    def start(self):
        self.server = subprocess.Popen(self.command, stdin=subprocess.PIPE)
    def stop(self):
        input_str = "stop"
        self.server.communicate(input_str.encode())
MCserver = MCserver_process(mc_finm, maxMem, minMem)

class CKserver_process:     # CoreKeeper
    def __init__(self, ck_finm):
        self.server = None
        self.command = ["batコマンドの処理"]
    def start(self):
        self.server = subprocess.Popen(self.command, stdin=subprocess.PIPE)
    def stop(self):
        input_str = "q"
        self.server.communicate(input_str.encode())
CKserver = CKserver_process(ck_finm)

class TRserver_process:     # Terraria
    def __init__(self, tr_finm):
        self.server = None
        self.command = ["batコマンドの処理"]
    def start(self):
        self.server = subprocess.Popen(self.command, stdin=subprocess.PIPE)
    def stop(self):
        input_str = ""
        self.server.communicate(input_str.encode())
TRserver = TRserver_process(tr_finm)

# リプライ内容
async def mc_rep(message):
    reply = f"{message.author.mention} MC_gameID"
    await chan_cmd.send(reply)

async def ck_rep(message):
    reply = f"{message.author.mention} CK_gameID"
    await chan_cmd.send(reply)

async def tr_rep(message):
    reply = f"{message.author.mention} TR_gameID"
    await chan_cmd.send(reply)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("ログインしました")
    print("------")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # Minecraftサーバー
    if message.content == "/mcstart":
        await chan_mc.send("【Minecraft】サーバープロセスを実行します")
        MCserver.start()
    elif message.content == "/mcstop":
        await chan_mc.send("【Minecraft】サーバープロセスを停止します")
        MCserver.stop()

    # CoreKeeperサーバー
    if message.content == "/ckstart":
        await chan_ck.send("【oreKeeper】サーバープロセスを実行します")
        CKserver.start()
    elif message.content == "/ckstop":
        await chan_ck.send("【CoreKeeper】サーバープロセスを停止します")
        CKserver.stop()

    # Terrariaサーバー
    if message.content == "/trstart":
        await chan_tr.send("【Terraria】サーバープロセスを実行します")
        TRserver.start()
    elif message.content == "/trstop":
        await chan_tr.send("【Terraria】サーバープロセスを停止します")
        TRserver.stop()

    # GameID表示
    if message.content == "/mcid":   # Minecraft
        await mc_rep(message)
    elif message.content == "/ckid": # CoreKeeper
        await ck_rep(message)
    elif message.content == "/trid": # Terraria
        await tr_rep(message)        

    # ヘルプ
    if message.content == "/help":
        await chan_cmd.send("ヘルプを表示します")
        chan_cmd.send("")

# Botの起動とDiscordサーバーへの接続
client.run(token)
