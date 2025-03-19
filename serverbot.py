import subprocess
# インストールした discord.py を読み込む
import discord

# TOKENとサーバーの情報
TOKEN = 'ここに自分のbotのアクセストークンを入力'
fi_name = 'サーバー実行ファイル名.jar'
maxMem = '8G'  # 任意の最大メモリ割り当てサイズ
minMem = '8G'  # 任意の最小メモリ割り当てサイズ

# 接続に必要なオブジェクトを生成
client = discord.Client()

# サーバー操作用
class MCserver_process:     # Minecraft
    def __init__(self, fi_name, maxMem,minMem):
        self.server = None
        self.command = ["java", "-server",f'-Xms{minMem}', f'-Xmx{maxMem}', "-jar", fi_name, "nogui"]
    def start(self):
        self.server = subprocess.Popen(self.command, stdin=subprocess.PIPE)
    def stop(self):
        input_string = "stop"
        self.server.communicate(input_string.encode())

MCserver = MCserver_process(fi_name, maxMem, minMem)

class CKserver_process:     # CoreKeeper
    def __init__(self, fi_name, maxMem,minMem):
        self.server = None
        self.command = ["java", "-server",f'-Xms{minMem}', f'-Xmx{maxMem}', "-jar", fi_name, "nogui"]
    def start(self):
        self.server = subprocess.Popen(self.command, stdin=subprocess.PIPE)
    def stop(self):
        input_string = "Q"
        self.server.communicate(input_string.encode())

CKserver = CKserver_process(fi_name, maxMem, minMem)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # Minecraftサーバー
    if message.content == '/mcstart':
        await message.channel.send('Minecraftのサーバープロセスを実行します')
        MCserver.start()
    elif message.content == '/mcstop':
        await message.channel.send('Minecraftのサーバープロセスを停止します')
        MCserver.stop()

    # CoreKeeperサーバー
    if message.content == '/ckstart':
        await message.channel.send('CoreKeeperのサーバープロセスを実行します')
        CKserver.start()
    elif message.content == '/ckstop':
        await message.channel.send('CoreKeeperのサーバープロセスを停止します')
        CKserver.stop()

    # ヘルプ
    if message.content == '/help':
        await message.channel.send('ヘルプを表示します')
        print('')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)