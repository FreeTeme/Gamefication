from telethon.sync import TelegramClient
from telethon import functions, types

api_id = "21451938"
api_hash = "02e804da78ecfda445b8ce657e9020bc"
phone = "+88802424137"

client = TelegramClient(phone, api_id, api_hash)

async def reaction():
    async with client:
        messages = await client.get_messages('@luxcrypto123', limit=5)

        if messages:
            msg_id = messages[1].id
            print(f"Используемый msg_id: {msg_id}")

            # Отправка реакции
            await client(functions.messages.SendReactionRequest(
                peer='@luxcrypto123',
                msg_id=msg_id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon='👍')]
            ))

            # Получение списка реакций
            result = await client(functions.messages.GetMessagesReactionsRequest(
                peer='@luxcrypto123',
                id=[msg_id]
            ))

            # Подсчет общего количества реакций
            total_reactions = 0
            for update in result.updates:
                if isinstance(update, types.UpdateMessageReactions):
                    total_reactions += sum(reaction.count for reaction in update.reactions.results)
            print(f"Общее количество реакций: {total_reactions}")

            return total_reactions

with client:
    client.loop.run_until_complete(reaction())
