from discord.utils import get

from redbot.core import Config, checks, commands

from redbot.core.bot import Red
from typing import Any

Cog: Any = getattr(commands, "Cog", object)


class ForceMention(Cog):
    """
    Mention the unmentionables
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=9811198108111121, force_registration=True)
        default_global = {}
        default_guild = {}

        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command()
    async def forcemention(self, ctx: commands.Context, role: str, *, message=''):
        """
       Mentions that role, regardless if it's unmentionable
       """
        role_obj = get(ctx.guild.roles, name=role)
        if role_obj is None:
            await ctx.maybe_send_embed("Couldn't find role named {}".format(role))
            return

        if not role_obj.mentionable:
            await role_obj.edit(mentionable=True)
            await ctx.send("{}\n{}".format(role_obj.mention, message))
            await role_obj.edit(mentionable=False)
        else:
            await ctx.send("{}\n{}".format(role_obj.mention, message))
