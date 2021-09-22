import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ":", case_insensitive = True)

intents = discord.Intents.default()

intents.members = True

@client.event
async def on_ready():
 await client.change_presence(activity=discord.Game(name="Feito Pelo Melhor L4X#3855"))
 print('ligado')

  
@client.command()
async def teste(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Isso só teste!')

@client.command(aliases=['avs'])
async def aviso(ctx, *, avs=None):
 if avs is None:
   Avs = discord.Embed(title=f"Comando Está Faltando Mais Coisa",timestamp=ctx.message.created_at, description=f"Precisa colocar uma mensagem para eu fazer o aviso",  color=discord.Color.blue())
   await ctx.send(embed=Avs)
 else:
   embed = discord.Embed(title=f"", timestamp=ctx.message.created_at, description=f"{avs} \nBy: {ctx.author.mention}",  color=discord.Color.blue())
   await ctx.send(embed=embed)
   await ctx.message.delete()

@client.command(aliases=['falar'])
async def say(ctx, *, mensagem=None):
  if mensagem is None:
    mensagemm = discord.Embed(title=f"Comando Está Faltando Mais Coisa",timestamp=ctx.message.created_at, description=f"Precisa colocar uma mensagem que deseja que eu repita", color=discord.Color.blue())
    await ctx.send(embed=mensagemm)
  else:
    await ctx.message.delete()
    await ctx.send(f'{mensagem} \nBy: {ctx.author.mention}')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  Ban = discord.Embed(title=f"Membro Teve Seu Ban Com Sucesso",timestamp=ctx.message.created_at, description=f'Membro Ganhou Ban. Bem Feito \nBy: {ctx.author.mention}', color=discord.Color.blue())
  
  await member.ban(reason = reason)
  await ctx.send(embed=Ban)

#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Membro Perdeu Ban {user.mention} \nBy: {ctx.author.mention}')
            return
@client.command()
async def ajuda(ctx):
  embed = discord.Embed(title=f"Sou bot para criação de aviso e moderação. Para mais dúvidas fala :comandos", description=f"", color=discord.Color.blue())
  await ctx.send(embed=embed)

@client.command()
async def comandos(ctx):
      guild = ctx.guild
      embed = discord.Embed(title=f'COMANDOS', description="", timestamp=ctx.message.created_at, color=discord.Color.blue())
      embed.set_thumbnail(url=guild.icon_url)
      embed.add_field(name="kick:", value=f'Kicka uma pessoa')
      embed.add_field(name="ban:", value=f'Bane um player')
      embed.add_field(name="unban:", value=f'Tira ban da pessoa')
      embed.add_field(name="aviso:", value=f'Faz um aviso em embed')
      embed.add_field(name="say:", value=f'Copia uma mensagem sua')
      embed.add_field(name="avatar:", value=f'Baixa uma foto de player ou sua')
      embed.add_field(name="serveinfo:", value=f'Informação do servidor atual')
      embed.add_field(name="canal:", value=f'Cria canal no servidor')
      embed.add_field(name="votacao:", value=f'Faz uma votação')
      embed.set_footer(text=f"{guild} | Todos direitos reservados", icon_url=ctx.author.avatar_url)

      await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True) 
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"Foi kickado com sucesso membro {user.name}!",timestamp=ctx.message.created_at, description=f"Motivo de: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@commands.has_permissions(kick_members=True) 
@client.command(aliases=['Cn'])
async def canal(ctx, *, Cn=None):
  if Cn is None:
    canall = discord.Embed(title=f"Comando Está Faltando Mais Coisa",timestamp=ctx.message.created_at,description=f"Você precisa colocar nome do canal que deseja", color=discord.Color.blue())
    await ctx.send(embed=canall)
  else:
    embed = discord.Embed(title=f"Chat Criado Com Sucesso",
    timestamp=ctx.message.created_at, description=f"", color=discord.Color.blue())
    await ctx.guild.create_text_channel(f'{Cn}')
    await ctx.send(embed=embed)
    await ctx.message.delete()
 
@client.command(aliases=['Vt'])
async def votacao(ctx, *, Vt=None):
 if Vt is None:
    votaa = discord.Embed(title=f"Comando Está Faltando Mais Coisa",timestamp=ctx.message.created_at,description=f"Precisa por uma descrição ou objeto da votação", color=discord.Color.blue())
    await ctx.send(embed=votaa)
 else:
   embed = discord.Embed(title=f"Votação Iniciada",
   timestamp=ctx.message.created_at, description=f"{Vt}", icon_url=ctx.author.avatar_url, color=discord.Color.blue())
   msg = await ctx.send(embed=embed)
   await ctx.message.delete()
   await msg.add_reaction('✅')
   await msg.add_reaction('❌')


@client.command()
async def avatar(ctx, member:discord.Member):
    await ctx.send(member.avatar_url)

@commands.has_permissions(kick_members=True)  
@client.command()
async def clear(ctx):
   embed = discord.Embed(title=f"Chat Limpinho",
   timestamp=ctx.message.created_at,  
   description=f"Limpo igual você", color=discord.Color.blue())
   await ctx.message.delete()
   await ctx.channel.purge()                         
   await ctx.send(embed=embed)  

@client.command()
async def serverinfo(ctx):
      guild = ctx.guild
      embed = discord.Embed(title=f'iNFORMÇÃO DO SERVER {guild}', description="Informação Do Server", timestamp=ctx.message.created_at, color=discord.Color.blue())
      embed.set_thumbnail(url=guild.icon_url)
      embed.add_field(name="Canais:", value=len(guild.channels))
      embed.add_field(name="Funções:", value=len(guild.roles))
      embed.add_field(name="Booster:", value=guild.premium_subscription_count)
      embed.add_field(name="Membros :", value=guild.member_count)
      embed.add_field(name="Criado:", value=guild.created_at)
      embed.set_footer(text=f"{guild} | Todos direitos reservados", icon_url=ctx.author.avatar_url)

      await ctx.send(embed=embed)
client.run('ODg0ODY3ODM2NzAxNDQ2MjQ0.YTevZA.eoGjSTEiJHTqmrpfoqmVCrt0zBg')