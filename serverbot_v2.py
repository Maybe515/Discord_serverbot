# Access Token
TOKEN = ""

# Channel ID (int)
# CHA_MC = ""    # Minecraft
# CHA_CK = ""    # Core Keeper
# CHA_TR = ""    # Terraria
# CHA_CMD = ""   # Command

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
IP_ADDRESS = ""

# ヘルプテキスト
HELP_STR = """
/mcstart   【Minecraft】サーバープロセスを実行
/mcstop    【Minecraft】サーバープロセスを停止
/ckstart   【Core Keeper】サーバープロセスを実行
/ckstop    【Core Keeper】サーバープロセスを停止
/trstart   【Terraria】サーバープロセスを実行
/trstop    【Terraria】サーバープロセスを停止
/mcid      【Minecraft】GameIDを表示
/ckid      【Core Keeper】GameIDを表示
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
    await client.change_presence(activity=Game(name="Bot 動作中"))  #「○○をプレイ中」と表示するところ
    # 起動したらターミナルにログイン通知が表示される  
    print(f"login: {self.user.name} [ID:{self.user.id}]")    # Bot Name, [Bot ID]
    print(f"discord.py Version: {discord.__version__}")   # discord.py Version
    print("------")

class Port_Forward:    # ポート開放・クローズ
  def __init__(self, target):
    self.game = target
  def open(self):
    port_select(self.game)
    subprocess.popen(f"telnet {IP_ADDRESS} {PORT_NUMBER}")
  def close(self):
    port_select(self.game)
    PID = subprocess.popen(f"netstat -nao | find {PORT_NUMBER}")
    subprocess.popen(f"taskkill /pid {PID}")

def port_select(target):
  if target == "mc":
    PORT_NUMBER = "7777"    # Minecraft
  elif target == "tr":
    PORT_NUMBER = "7878"    # Terraria
  return PORT_NUMBER

# オブジェクト生成
intents = Intents.default()
client = MyClient(intents=intents)
port = Port_Forward(target)

@client.tree.command(name="hello", description="Hello, world!")    # /hello
async def hello(interaction: Interaction):
  await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

# Minecraft サーバー操作
@client.tree.command(name="mcstart", description="Minecraftサーバーを起動する")    # /mcstart
async def mcstart(interaction: Interaction):
  if is_mcserver_running():
    await interaction.response.send_message("Minecraftサーバーは既に起動しています")
  else:
    start_mcserver()
    await interaction.response.send_message("Minecraftサーバーを起動します")
    port.open("mc")
    await interaction.response.send_message("ポート番号：{PORT_NUMBER}　開放中")

@client.tree.command(name="mcstop", description="Minecraftサーバーを停止する")    # /mcstop
async def mcstop(interaction: Interaction):
  if is_mcserver_running():
    stop_mcserver()
    await interaction.response.send_message("Minecraftサーバーを停止します")
  else:
    await interaction.response.send_message("Minecraftサーバーは既に停止されています")

def is_mcserver_running():  # MCサーバーが動作しているか確認する関数
  process = subprocess.Popen(f"screen -ls {SCREEN_NAME}", stdout=subprocess.PIPE, shell=True)
  output, _ = process.communicate()
  return SCREEN_NAME in output.decode()

def start_mcserver():  # screenを利用してMCサーバーを起動するコマンド
  subprocess.Popen(f"screen -dmS {SCREEN_NAME} java -Xmx{MAX_RAM}G -Xms{MIN_RAM}G -jar {JAR_FILE} nogui", shell=True)

def stop_mcserver():  # MCサーバーを停止するコマンド
  cmd = "stop"
  process = subprocess.Popen(f"screen -ls {SCREEN_NAME}", stdout=subprocess.PIPE, shell=True)
  process.communicate(cmd.encode())

# Core Keeper サーバー操作
@client.tree.command(name="ckstart", description="Core Keeperサーバーを起動する")    # /ckstart
async def ckstart(interaction: Interaction):

@client.tree.command(name="ckstop", description="Core Keeperサーバーを停止する")    # /ckstop
async def ckstop(interaction: Interaction):

# Terraria サーバー操作
@client.tree.command(name="trstart", description="Terrariaサーバーを起動する")    # /trstart
async def trstart(interaction: Interaction):

@client.tree.command(name="trstop", description="Terrarriaサーバーを停止する")    # /trstop
async def trstop(interaction: Interaction):

# GameID 表示
@client.tree.command(name="mcid", description="【Minecraft】GameIDを表示する")    # /mcid
async def mcid(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {ID_MC}")

@client.tree.command(name="ckid", description="【Core Kepper】GameIDを表示する")    # /ckid
async def ckid(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {ID_CK}")

@client.tree.command(name="trid", description="【Terraria】GameIDを表示する")    # /trid
async def trid(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {ID_TR}")

# ヘルプテキスト表示
@client.tree.command(name="help", description="コマンド一覧を表示する")    # /help
async def help(interaction: Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} {HELP_STR}")

# Botの起動とDiscordサーバーへの接続
client.run(token)
