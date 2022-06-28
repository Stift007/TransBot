import nextcord
import random
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.messages = True

client = commands.Bot(command_prefix="?", intents=intents)

@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong!\n> {round(client.latency*1000)}ms Latency")

sentences = [
    "I'm gonna hang out with [name] today, [subjective] wanted me to help with [possessive] Homework.",
    "What do you think about [name]? [subjective:U] has a nice style, I really like [possessive] Clothes",
    "[name] and I have a lot in common, we like the same music,the same food and the same clothes. We have known each other for like forever and I'm glad I'm friends with [objective].",
    "Your Computer isn't working? Ask [name], [subjective] knows a lot about computers.",
    "[name] and I have been friends since elementary. Next year I'll move together with [objective] in our own apartment!",
    "[name] is a great artist! [subjective] doesn't have much confidence in [reflexive], but I know [subjective] will see how wonderful [subjective] is someday"
]

@client.command(name="try")
async def _try(ctx, subjective, objective, possessive, reflexive, name=None):
    if not name:name=ctx.author.display_name
    name = name.capitalize()
    choices = random.choices(sentences, k=3)
    finalStr = f"Hey, {ctx.author.mention}, looks like you want to try out the {subjective}/{objective} Pronouns and the name {name}\nHere are some random sentences for you, {name}:\n"
    print(choices)
    for c in choices:
        c = c.replace("[subjective:U]", subjective.capitalize())
        c = c.replace("[name]", name)
        c = c.replace("[objective:U]",  objective.capitalize())
        c = c.replace("[possessive:U]", possessive.capitalize())
        c = c.replace("[reflexive:U]", reflexive.capitalize())
        c = c.replace("[subjective]", subjective)
        c = c.replace("[name]", name)
        c = c.replace("[objective]",  objective)
        c = c.replace("[possessive]", possessive)
        c = c.replace("[reflexive]", reflexive)
        print(c)
        finalStr += f"\n»{c}«"
    await ctx.send(finalStr)

@client.command()
async def pronouns(ctx):
    await ctx.send("""
> *All forms of some of the most common pronouns:*

He: `?try he him his himself`

She: `?try she her her herself`

They: `?try they them their themselves`

> *Pronoun forms explained*

Subjective pronoun: "Who is cool?" **He** is cool.

Objective pronoun: "Who do you love?" I love **him**

Possessive determiner: "Whose phone is this?" This is **his** phone.

Reflexive pronouns: "Who does he love?" He loves **himself**.
    """)

client.run(open("token.key").read())
