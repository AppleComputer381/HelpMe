import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix="!", description="HelpME")


@client.event
async def on_ready():
    print("Ready !")


@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount):
    member_name =ctx.author.name
    print (amount+" messages ont été supprimé par "+member_name)
    await ctx.channel.purge(limit=int(amount) + 1)


@client.command()
async def serverInfo(ctx, info):
    await ctx.channel.purge(limit=int(1))
    print(info.strip().lower())
    if info.strip().lower()=="name":
        await ctx.send(f"Nom du serveur : {ctx.guild.name}")
    elif info.strip().lower()=="description":
        await ctx.send(f"Description du serveur : {ctx.guild.description}")
    elif info.strip().lower()=="member":
        await ctx.send(f"Nombres de membres : {ctx.guild.member_count}")
    elif info.strip().lower()=="text_chan":
        await ctx.send(f"Nombres de channel textuels : {len(ctx.guild.text_channels)}")
    elif info.strip().lower()=="voice_chan":
        await ctx.send(f"Nombres de channel vocaux : {len(ctx.guild.voice_channels)}")
    elif info.strip().lower()=="all":
        await ctx.send(f"Le serveur {ctx.guild.name} contient {ctx.guild.member_count} personnes. \n -La description du serveur {ctx.guild.description}. \n -Ce server possède {len(ctx.guild.text_channels)} salons écrit ainsi que {len(ctx.guild.voice_channels)} vocaux")




@client.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, user : discord.User, *reason):
    await ctx.channel.purge(limit=int(1))
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")
    print(f"{user} à été ban pour la raison suivante : {reason}")

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@client.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, user: discord.User, *reason):
    await ctx.channel.purge(limit=int(1))
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick pour la raison suivante : {reason}.")
    print(f"{user} à été kick pour la raison suivante : {reason}")

@client.command()
async def bansID(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send("La liste des utilisateurs bannis sur ce serveur est la suivante :")
    await ctx.send("\n".join(ids))




@client.command()
async def innactif(ctx):
    await ctx.send("Mon Maitre bien aimé m'eteind je serai de nouveau actif dans les plus bref delais 😘")

@client.event
async def on_member_join(member):
    channel = member.guild.get_channel(723325946786218097)
    await channel.send(f"Acceuillons a bras ouvert {member.mention} ! Bienvenue sur le serveur :)")
    print(f"{member.mention} vient d'arriver !")


client.run("NzIwNzI1NzA4ODQ2MTM3Mzc5.XuQRsA.izOVHG7IjJG9DKwVHh72j4XxXOc")