
"""command: .netflix"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "netflix":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Netflix Server...`",
            "`Cracking accounts.`",
            "`cracking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`cracking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`cracking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`cracking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`cracking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`cracking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`cracking... 69%\n█████████████████████▒▒▒▒ `",
            "`cracking... 100%\n█████████HACKED███████████ `",
            "`Account cracked...\n\nPay 2000 Rupees To Stiff to get id and password.. And Enjoy 4screen hd `"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])

