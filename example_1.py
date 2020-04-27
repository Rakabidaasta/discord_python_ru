import discord

TOKEN = 'Ваш токен'

client = discord.Client()            # создаем и инициализируем экземпляр класса discord.Client
game = discord.Game("Hello world!")  # статус игры

@client.event                        # применяем функцию-декоратора
async def on_ready():
    print('Вы зашли под ботом с никнеймом: ', client.user.name)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=game)

client.run(TOKEN)
