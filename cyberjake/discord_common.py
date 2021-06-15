"""Common code for discord bots"""
import random
import typing
import discord


async def error_embed(ctx, message: str, title: str = "Error:", **kwargs):
    """
    Error embed

    **Requires discord.py**

    **Asynchronous Function**

    Makes and send an error embed

    :param ctx: Command context
    :param message: Message description
    :type message: str
    :param title: Error message title
    :type title: str
    """
    await make_embed(ctx, color="FF0000", send=True, description=message, title=title, **kwargs)


async def make_embed(
    ctx, color: typing.Union[str, int] = None, send: typing.Union[bool, str] = True, **kwargs
) -> discord.Embed():
    """Make embed

    **Requires discord.py**

    **Asynchronous Function**

    Makes and can send a discord.Embed

    :param ctx: Discord context
    :type ctx: discord.ext.commands.Context
    :param color: Color of the embed
    :param send: Send the message instead of returning
    :param kwargs: Keyword arguments to pass along
    :return: The filled out embed
    """
    if not color:
        kwargs["color"] = int("0x%06x" % random.randint(0, 0xFFFFFF), 16)  # nosec
    elif isinstance(color, str):
        kwargs["color"] = discord.Color(int(color, 16))

    embed = discord.Embed(timestamp=ctx.message.created_at, **kwargs)

    if "footer" in kwargs:
        embed.set_footer(text=kwargs["footer"])
    if send:
        await ctx.send(embed=embed)
    else:
        return embed
