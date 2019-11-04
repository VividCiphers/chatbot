#!/usr/bin/python3

from discord import HTTPException
from vividcipher.client import bot
from vividcipher.config import channels, roles

msg = "Welcome to __{}__, <@{}>! Have a look at server info & coc in <#{}> and <#{}>. "
msg += "If you need help with anything, start posting your questions in <#{}>."

# ON_MEMBER_JOIN
@bot.event
async def on_member_join(member):
    guild = member.guild
    welcome_chl = guild.get_channel(int(channels["welcome"]))  # id casted into int type
    bot_chl = guild.get_channel(int(channels["bot"]))
    dev_role = guild.get_role(int(roles["developer"]))

    try:
        await member.add_roles(dev_role, reason="new member")
    except HTTPException:
        print("error: http, adding role failed")
        await bot_chl.send("failure: failed to set role for <@{}>".format(member.id))

    await welcome_chl.send(
        msg.format(
            guild.name,
            member.id,
            channels["information"],
            channels["netiquette"],
            channels["general"],
        )
    )


# ON_BOT_READY
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

