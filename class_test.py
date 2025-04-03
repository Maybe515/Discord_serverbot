# Channel ID (int)
chan_mc = ""    # Minecraft
chan_ck = ""    # CoreKeeper
chan_tr = ""    # Terraria
chan_cmd = ""   # Command

# GameID (str)
MC_gameID = ""    # Minecraft
CK_gameID = ""    # CoreKeeper
TR_gameID = ""    # Terraria

# test, debug
player = "Maybe515"
status = "mc_join"

# Embedメッセージ(class)
class mc(self):    # Minecraft
    def joined(self, player):
        self.embed = discord.embed(title="Player Joined", description="Player：" + player, color=0x57F287)
        await chan_mc.send(self.embed=self.embed)
    def left(self, player):
        self.embed = discord.embed(title="Player Left", description="Player：" + player, color=0xED4245)
        await chan_mc.send(self.embed=self.embed)

class ck(self):    # CoreKeeper
    def joined(self, player):
        self.embed = discord.embed(title="Player Joined", description="Player：" + player, color=0x57F287)
        await chan_ck.send(self.embed=self.embed)
    def left(self, player):
        self.embed = discord.embed(title="Player Left", description="Player：" + player, color=0xED4245)
        await chan_ck.send(self.embed=self.embed)

class tr(self):    # Terraria
    def joined(self, player):
        self.embed = discord.embed(title="Player Joined", description="Player：" + player, color=0x57F287)
        await chan_tr.send(self.embed=self.embed)
    def left(self, player):
        self.embed = discord.embed(title="Player Left", description="Player：" + player, color=0xED4245)
        await chan_tr.send(self.embed=self.embed)

# 入退室をEmbedメッセージで表示
if status == "mc_join":
    mc.joined()
elif status == "mc_left":
    mc.left()

if status == "ck_join":
    ck.joined()
elif status == "ck_left":
    ck.left()

if status == "tr_join":
    tr.joined()
elif status == "tr_left":
    tr.left()
