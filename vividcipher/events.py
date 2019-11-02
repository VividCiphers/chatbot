from vividcipher.client import bot
from vividcipher.config import channels

msg = "Welcome to {}, <@{}>! Have a look at server info & coc in <#{}> and <#{}>. If you need help with anything, start posting your questions in <#{}>."


@bot.event
async def on_member_join(member):
    guild = member.guild
    for c in guild.channels:
        if c.name == "welcome-🎊":
            await c.send(
                msg.format(
                    guild.name,
                    member.id,
                    channels["information"],
                    channels["netiquette"],
                    channels["general"],
                )
            )


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

