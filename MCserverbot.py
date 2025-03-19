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
class server_process:

    def __init__(self, fi_name, maxMem,minMem):
        self.server = None
        self.command = ["java", "-server",f'-Xms{minMem}', f'-Xmx{maxMem}', "-jar", fi_name, "nogui"]

    def start(self):
        self.server = subprocess.Popen(self.command, stdin=subprocess.PIPE)

    def stop(self):
        input_string = "stop"
        self.server.communicate(input_string.encode())

server = server_process(fi_name, maxMem, minMem)

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

    if message.content == '/mcstart':
        await message.channel.send('マイクラサーバーを起動します')
        server.start()

    elif message.content == '/mcstop':
        await message.channel.send('マイクラサーバーを終了します')
        server.stop()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)