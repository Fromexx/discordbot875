# imports
import os
import discord
from discord import Member
from discord.ext import commands
# this library allows you to make a frame to the left of the message
# for color you can use HEX colors with the addition of a prefix "0x"
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.utils import get

Bot = commands.Bot(command_prefix = "!")
client = discord.Client()


class MyClient(discord.Client):
    # displays the message "Bot connection!" when the bot is online
    async def on_ready(self):
        # bot connection
        print('Bot connection!')

    @Bot.event
    @client.event
    async def on_message(self, message):


        if int(message.channel.id) != 846795263866568744:
            return

        # displays server rules
        if message.content == '!правила':
            embed = discord.Embed(title='''Правила:
    1) не писать говнокод
    2) не делать говномодельки
    3) не придумывать говноидеи
    4) работать и развиваться
    5) работать, если не работаешь, выгоняем!
            ''', color=0xFF0000)
            await message.channel.send(embed=embed)

        # outputs server commands
        if message.content == '!команды':
            embed = discord.Embed(title='''Команды:
    1) !правила - выводит правила сервера 
    2) Дай роль: "название роли" - дает роль автору сообщения 
    3) Удали роль: "название роли" - удаляет роль у автора сообщения
    Имеющиеся роли: Программист, Художник, Геймдизайнер
                    ''', color=0xfcf403)
            await message.channel.send(embed=embed)


        # adds a role to the author of the message.
        # If the author of the post already has this role, then the bot warns about this
        if message.content == f'Дай роль: Программист':

            if get(message.author.roles, id=846807803154661447):
                embed = discord.Embed(title="У вас уже есть такая роль!", color=0x0000FF)
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"Дана роль: Программист.", color=0x00ff40)
                await message.channel.send(embed=embed)
                await message.author.add_roles(discord.utils.get(message.guild.roles, id=846807803154661447))


        elif message.content == 'Дай роль: Художник':

            if get(message.author.roles, id=846808154792788019):
                embed = discord.Embed(title="У вас уже есть такая роль!", color=0x0000FF)
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"Дана роль: Художник", color=0x00ff40)
                await message.channel.send(embed=embed)
                await message.author.add_roles(discord.utils.get(message.guild.roles, id=846808154792788019))


        elif message.content == 'Дай роль: Геймдизайнер':

            if get(message.author.roles, id=847056513746731008):
                embed = discord.Embed(title="У вас уже есть такая роль!", color=0x0000FF)
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"Дана роль: Геймдизайнер", color=0x00ff40)
                await message.channel.send(embed=embed)
                await message.author.add_roles(discord.utils.get(message.guild.roles, id=847056513746731008))


        # removes the role from the author of the post.
        # If he does not have this role, then the bot warns about this.
        if message.content == 'Удали роль: Программист':

            if get(message.author.roles, id=846807803154661447):
                role = get(message.author.guild.roles, id=846807803154661447)
                embed = discord.Embed(title=f"Удаленна роль: Программист.", color=0x20B2AA)
                await message.channel.send(embed=embed)
                await message.author.remove_roles(role, reason=None)

            else:
                embed = discord.Embed(title="У вас нету данной роли!", color=0x0000FF)
                await message.channel.send(embed=embed)

        if message.content == 'Удали роль: Художник':

            if get(message.author.roles, id=846808154792788019):
                role = get(message.author.guild.roles, id=846808154792788019)
                embed = discord.Embed(title=f"Удаленна роль: Художник.", color=0x20B2AA)
                await message.channel.send(embed=embed)
                await message.author.remove_roles(role, reason=None)

            else:
                embed = discord.Embed(title="У вас нету данной роли!", color=0x0000FF)
                await message.channel.send(embed=embed)


        if message.content == 'Удали роль: Геймдизайнер':

            if get(message.author.roles, id=847056513746731008):
                role = get(message.author.guild.roles, id=847056513746731008)
                embed = discord.Embed(title=f"Удаленна роль: Геймдизайнер.", color=0x20B2AA)
                await message.channel.send(embed=embed)
                await message.author.remove_roles(role, reason=None)

            else:
                embed = discord.Embed(title="У вас нету данной роли!", color=0x0000FF)
                await message.channel.send(embed=embed)
                

# bot launch
token1 = os.environ.get('BOT_TOKEN')
client = MyClient()
client.run(str(token1))
