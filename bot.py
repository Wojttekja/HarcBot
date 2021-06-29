import discord
import json

with open ("odpowiedzi.json", "r") as file:
    data = json.load(file)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.content[0] != "!":
        return

    # message.content 
    # struktura:
    # !odp <numer zadania> <odpowiedż>
    # !pyt <numer>
    real_message = message.content[1:]
    real_message = real_message.split(" ")

    if real_message[0] == "pyt":
        print(data[real_message[1]]["pyt"])
        await message.channel.send(data[real_message[1]]["pyt"])

    elif real_message[0] == "odp":
        if real_message[2] == data[real_message[1]]["odp"]:
            print("Dobrze")
            await message.channel.send("dobrze")

            #próba wysłania kolejenego pytania
            try:
                print(data[str(int(real_message[1]) + 1)]["pyt"])
                await message.channel.send(data[str(int(real_message[1]) + 1)]["pyt"])
            except:
                print("To by było na tyle :)")
                await message.channel.send("To by było na tyle :)")
        else:
            print ("Nie tym razem, spróbuj ponownie")
            await message.channel.send("Nie tym razem, spróbuj ponownie")


client.run('ODU5MTI0MTA3MjE2MTU4NzIw.YNoHrA.c1D9ukjeZ5Rx15ASrw-sBVqG-Og')