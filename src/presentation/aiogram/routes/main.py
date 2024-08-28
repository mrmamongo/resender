from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dishka import FromDishka

from src.infra.postgres.gateways import ChatsGateway
from src.presentation.aiogram.formatters import format_chat_pair_schema

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer('Halo!')


@router.message(Command('chats'))
async def set_settings(message: Message, chats_gateway: FromDishka[ChatsGateway]) -> None:
    await message.answer(
        "\n".join(
            [format_chat_pair_schema(pair) for pair in await chats_gateway.get_all_pairs()]
        )
    )

