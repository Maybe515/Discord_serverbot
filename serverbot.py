# Access Token
TOKEN = ""

# Game ID (str)
ID_MC = ""    # Minecraft
ID_CK = ""    # Core Keeper
ID_TR = ""    # Terraria

# バッチコマンド用
JAR_FILE = "xxx.jar"  # Minecraftサーバー実行ファイル名
SERVER_PATH = "minecraft/java/paper"  # Minecraftサーバー実行ファイルのあるフォルダパス
SCREEN_NAME = ""
MAX_RAM = "8"      # 任意の最大メモリ割り当てサイズ（デフォルト：5）
MIN_RAM = "4"      # 任意の最小メモリ割り当てサイズ（デフォルト：2）
IP_ADDRESS = ""
PORT_NUMBER = ""

# コマンドリスト
LIST_STR = """
/mcstart   【Minecraft】サーバープロセスを実行
/mcstop    【Minecraft】サーバープロセスを停止
/ckstart   【Core Keeper】サーバープロセスを実行
/ckstop    【Core Keeper】サーバープロセスを停止
/trstart   【Terraria】サーバープロセスを実行
/trstop    【Terraria】サーバープロセスを停止
/mcid      【Minecraft】GameIDを表示
/ckid      【Core Keeper】GameIDを表示
/trid      【Terraria】GameIDを表示
/list      コマンドリストを表示
"""

# Import Libralies
from discord import Intents, Client, Interaction, Game
from discord.app_commands import CommandTree
from subprocess import Popen, PIPE

class MyClient(Client):
  def __init__(self, intents: Intents) -> None:
    super().__init__(intents=intents)
    self.tree = CommandTree(self)
  async def setup_hook(self) -> None:
    await self.tree.sync()
  async def on_ready(self):
    await client.change_presence(activity=Game(name="サーバー監視中"))    # ステータス表示
    # 起動したらターミナルにログイン通知が表示される  
    print(f"login: {self.user.name} [ID:{self.user.id}]")    # Bot Name, [Bot ID]
    print(f"discord.py Version: {discord.__version__}")     # discord.py Version
    print("------")

class Port_Forward:
  def open(self):    # ポート開放
    Popen(f"telnet {IP_ADDRESS} {self}")
  def close(self):    # ポートクローズ
    PID = Popen(f"netstat -nao | find {self}")
    Popen(f"taskkill /pid {PID}")

def port_select(target):
  if target == "mc":
    p_num = "7777"    # Minecraft
  elif target == "tr":
    p_num = "7878"    # Terraria
  return p_num

class mcserver_Process:
  def __init__(self):
    self.cmd = [f"java -server -Xmx{MAX_RAM}G -Xms{MIN_RAM}G -jar {JAR_FILE} nogui"]
  def is_running(self):    # MCサーバーが動作しているか確認する
    process = Popen(self.cmd, stdout=PIPE, shell=True)
    output, _ = process.communicate()
    return SCREEN_NAME in output.decode()
  def start(self):    # MCサーバーを起動するコマンド
    Popen(self.cmd, shell=True)
  def stop(self):    # MCサーバーを停止するコマンド
    cmd_stop = "stop"
    process = Popen(self.cmd, stdout=PIPE, shell=True)
    process.communicate(cmd_stop.encode())    

class ckserver_Process:
  def __init__(self):
    self.cmd = [f"nogui"]
  def is_running(self):    # CKサーバーが動作しているか確認する
    process = Popen(self.cmd, stdout=PIPE, shell=True)
    output, _ = process.communicate()
    return SCREEN_NAME in output.decode()
  def start(self):    # CKサーバーを起動するコマンド
    Popen(self.cmd, shell=True)
  def stop(self):    # CKサーバーを停止するコマンド
    cmd_stop = "q"
    process = Popen(self.cmd, stdout=PIPE, shell=True)
    process.communicate(cmd_stop.encode())    

# オブジェクト生成
intents = Intents.default()
client = MyClient(intents=intents)
mcserver = mcserver_Process()
ckserver = ckserver_Process()

@client.tree.command(name="hello", description="Hello, world!")    # /hello
async def hello(interaction: Interaction):
  await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

# Minecraft サーバー操作
@client.tree.command(name="mcstart", description="Minecraftサーバーを起動する")    # /mcstart
async def mcstart(interaction: Interaction):
  target = "mc"
  if mcserver.is_running():
    await interaction.response.send_message("Minecraftサーバーは既に起動しています")
  else:
    mcserver.start()
    await interaction.response.send_message("Minecraftサーバーを起動します")
    PORT_NUMBER = port_select(target)
    Port_Forward.open(PORT_NUMBER)
    await interaction.response.send_message(f"ポート番号：{PORT_NUMBER}　開放中")

@client.tree.command(name="mcstop", description="Minecraftサーバーを停止する")    # /mcstop
async def mcstop(interaction: Interaction):
  target = "mc"
  if mcserver.is_running():
    mcserver.stop()
    await interaction.response.send_message("Minecraftサーバーを停止します")
    PORT_NUMBER = port_select(target)
    Port_Forward.close(PORT_NUMBER)
  else:
    await interaction.response.send_message("Minecraftサーバーは既に停止されています")

# Core Keeper サーバー操作
@client.tree.command(name="ckstart", description="Core Keeperサーバーを起動する")    # /ckstart
async def ckstart(interaction: Interaction):
  if ckserver.is_running():
    await interaction.response.send_message("Core Kepperサーバーは既に起動しています")
  else:
    ckserver.start()
    await interaction.response.send_message("Core Keeperサーバーを起動します")

@client.tree.command(name="ckstop", description="Core Keeperサーバーを停止する")    # /ckstop
async def ckstop(interaction: Interaction):
  if ckserver.is_running():
    ckserver.stop()
    await interaction.response.send_message("Core Keeperサーバーを停止します")
  else:
    await interaction.response.send_message("Core Keeperサーバーは既に停止されています")

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

# コマンドリスト表示
@client.tree.command(name="list", description="コマンドリストを表示する")    # /list
async def list(interaction: Interaction):
  await interaction.response.send_message(f"{interaction.user.mention} {LIST_STR}")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
