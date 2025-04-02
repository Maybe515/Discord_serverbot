# Import Libralies
import subprocess
import discord

# Discordとbotの情報
## Access Token
token = "Botのアクセストークン"

## Channel ID (int)
chan_mc = ""    # Minecraft
chan_ck = ""    # CoreKeeper
chan_tr = ""    # Terraria
chan_cmd = ""   # Commmand

## GameID (str)
MC_gameID = ""    # Minecraft
CK_gameID = ""    # CoreKeeper
TR_gameID = ""    # Terraria

# サーバープロセスの情報
mc_finm = "サーバー実行ファイル名.jar"        # Minecraft
maxMem = "8G"  # 任意の最大メモリ割り当てサイズ
minMem = "8G"  # 任意の最小メモリ割り当てサイズ
ck_finm = "Launch.bat"    # Core Keeper
tr_finm = "Launch.bat"    # Terraria

# 接続に必要なオブジェクトを生成
client = discord.Client()

# test, debug
player = "Maybe515"

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

# リプライ
async def mc_rep(message):
    reply = f"{message.author.mention} " + MC_gameID
    await chan_cmd.send(reply)

async def ck_rep(message):
    reply = f"{message.author.mention} " + CK_gameID
    await chan_cmd.send(reply)

async def tr_rep(message):
    reply = f"{message.author.mention} " + TR_gameID
    await chan_cmd.send(reply)


# Embedメッセージ
## Minecraft
async def mc_join(message):    
    embed = discord.embed(title="Player Joined", description="Player：" + player, color=0x57F287)
    await chan_mc.send(embed=embed)
async def mc_left(message):    
    embed = discord.embed(title="Player Left", description="Player：" + player, color=0xED4245)
    await chan_mc.send(embed=embed)

## CoreKeeper
async def ck_join(message): 
    embed = discord.embed(title="Player Joined", description="Player：" + player, color=0x57F287)
    await chan_ck.send(embed=embed)
async def ck_left(message):     
    embed = discord.embed(title="Player Left", description="Player：" + player, color=0xED4245)
    await chan_ck.send(embed=embed)

## Terraria
async def tr_join(message):
    embed = discord.embed(title="Player Joined", description="Player：" + player, color=0x57F287)
    await chan_tr.send(embed=embed)
async def tr_left(message):
    embed = discord.embed(title="Player Left", description="Player：" + player, color=0xED4245)
    await chan_tr.send(embed=embed)

# ヘルプテキスト
help_str = """
/mcstart   【Minecraft】サーバープロセスを実行
/mcstop    【Minecraft】サーバープロセスを停止
/ckstart   【CoreKeeper】サーバープロセスを実行
/ckstop    【CoreKeeper】サーバープロセスを停止
/trstart   【Terraria】サーバープロセスを実行
/trstop    【Terraria】サーバープロセスを停止
/mcid      【Minecraft】GameIDを表示
/ckid      【CoreKeeper】GameIDを表示
/trid      【Terraria】GameIDを表示
/help      コマンド一覧を表示
"""

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("ログインしました")
    print(client.user.name)      # Bot Name
    print(client.user.id)        # Bot ID
    print(discord.__version__)   # discord.py Version
    print("------")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # Minecraftサーバー
    if message.content == "/mcstart":
        await chan_cmd.send("【Minecraft】サーバープロセスを実行します")
        MCserver.start()
    elif message.content == "/mcstop":
        await chan_cmd.send("【Minecraft】サーバープロセスを停止します")
        MCserver.stop()

    # CoreKeeperサーバー
    if message.content == "/ckstart":
        await chan_cmd.send("【CoreKeeper】サーバープロセスを実行します")
        CKserver.start()
    elif message.content == "/ckstop":
        await chan_cmd.send("【CoreKeeper】サーバープロセスを停止します")
        CKserver.stop()

    # Terrariaサーバー
    if message.content == "/trstart":
        await chan_cmd.send("【Terraria】サーバープロセスを実行します")
        TRserver.start()
    elif message.content == "/trstop":
        await chan_cmd.send("【Terraria】サーバープロセスを停止します")
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
        await chan_cmd.send(help_str)

# 入退室を表示
@client.event
    # Minecraft
    if status == "mc_join":
        await mc_join(message)
    elif status == "mc_left":
        await mc_left(message)

    # CoreKeeper
    if status == "ck_join":
        await ck_join(message)
    elif status == "ck_left":
        await ck_left(message)

    # Terraria
    if status == "tr_join":
        await tr_join(message)
    elif status == "tr_left":
        await tr_left(message)
        
# Botの起動とDiscordサーバーへの接続
client.run(token)
