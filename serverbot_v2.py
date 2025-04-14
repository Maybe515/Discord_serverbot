# Access Token
TOKEN = ""

# Channel ID (int)
CHA_MC = ""    # Minecraft
CHA_CK = ""    # Core Keeper
CHA_TR = ""    # Terraria
CHA_CMD = ""   # Command

# Game ID (str)
ID_MC = ""    # Minecraft
ID_CK = ""    # Core Keeper
ID_TR = ""    # Terraria

# バッチコマンド用
JAR_FILE = "xxx.jar"  # Minecraftサーバー実行ファイル名
SERVER_PATH = "minecraft/java/paper"  # Minecraftサーバー実行ファイルのあるフォルダパス
SCREEN_NAME = "papermc"  # 使用するscreenセッション名
MAX_RAM = "8"      # 任意の最大メモリ割り当てサイズ（デフォルト：5）
MIN_RAM = "4"      # 任意の最小メモリ割り当てサイズ（デフォルト：2）
BAT_CK = "Launch.bat"    # Core Keeper
BAT_TR = "Launch.bat"    # Terraria

# ヘルプテキスト
HELP_STR = """
/mcstart   【Minecraft】サーバープロセスを実行
/mcstop    【Minecraft】サーバープロセスを停止
/ckstart   【Core Keeper】サーバープロセスを実行
/ckstop    【Core Keeper】サーバープロセスを停止
/trstart   【Terraria】サーバープロセスを実行
/trstop    【Terraria】サーバープロセスを停止
/mcid      【Minecraft】GameIDを表示
/ckid      【CoreKeeper】GameIDを表示
/trid      【Terraria】GameIDを表示
/help      コマンド一覧を表示
"""

# test, debug
PLAYER = "Maybe515"
STATUS = "mc_join"

# Import Libralies
from discord import Intents, Client, Interaction, Game
from discord.app_commands import CommandTree
import subprocess

class MyClient(Client):
  def __init__(self, intents: Intents) -> None:
    super().__init__(intents=intents)
    self.tree = CommandTree(self)

  async def setup_hook(self) -> None:
      await self.tree.sync()

  async def on_ready(self):
      await client.change_presence(activity=Game(name="/helpでヘルプを表示"))  #「○○をプレイ中」と表示するところ
    # 起動したらターミナルにログイン通知が表示される  
    print(f"login: {self.user.name} [{self.user.id}]")    # Bot Name, [Bot ID]
      print(discord.__version__)   # discord.py Version
      print("------")

# 接続に必要なオブジェクトを生成
intents = Intents.default()
client = MyClient(intents=intents)

@client.tree.command(name="hello", description="Hello, world!")    # /hello
async def hello(interaction: Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}!')

@client.tree.command(name="mcstart", description="Minecraftサーバーを起動する")    # /mcstart
async def mcstart(interaction: Interaction):
    if is_server_running():
        await interaction.response.send_message('Minecraftサーバーは既に起動しています')
    else:
        start_server()
        await interaction.response.send_message('Minecraftサーバーを起動します')

def is_server_running():  # サーバーが動作しているか確認する関数
    process = subprocess.Popen(f"screen -ls {SCREEN_NAME}", stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return SCREEN_NAME in output.decode()

def start_server():  # screenを利用してサーバーを起動するコマンド
    subprocess.Popen(f"screen -dmS {SCREEN_NAME} java -Xmx{MAX_RAM}G -Xms{MIN_RAM}G -jar {JAR_FILE} nogui", shell=True)


@client.tree.command(name="ckstart", description="Core Keeperサーバーを起動する")    # /ckstart
async def ckstart(interaction: Interaction):

@client.tree.command(name="ckstop", description="Core Keeperサーバーを停止する")    # /ckstop
async def ckstop(interaction: Interaction):

@client.tree.command(name="trstart", description="Terrariaサーバーを起動する")    # /trstart
async def trstart(interaction: Interaction):

@client.tree.command(name="trstop", description="Terrarriaサーバーを停止する")    # /trstop
async def trstop(interaction: Interaction):

@client.tree.command(name="mcid", description="【Minecraft】GameIDを表示する")    # /mcid
async def mcid(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {ID_MC}")

@client.tree.command(name="ckid", description="【Core Kepper】GameIDを表示する")    # /ckid
async def ckid(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {ID_CK}")

@client.tree.command(name="trid", description="【Terraria】GameIDを表示する")    # /trid
async def trid(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {ID_TR}")

@client.tree.command(name="help", description="ヘルプテキストを表示する")    # /help
async def help(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {HELP_STR}")

# Botの起動とDiscordサーバーへの接続
client.run(token)
