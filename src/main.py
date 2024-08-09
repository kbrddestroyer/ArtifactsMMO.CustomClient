import config
import asyncio
from API.ArtifactsMMO import ActifactsAPI
from API.Character import Character

if __name__ == '__main__':
    # Do main
    api = ActifactsAPI()
    api.start('KbrdDstr', config.TOKEN)

    character = Character('KbrdDstr', api)
    asyncio.run(character.move(0, 1))
    # asyncio.run(character.fight())
    asyncio.run(character.move(0, 0))
    asyncio.run(character.move(2, -1))
    asyncio.run(character.fight())
    asyncio.run(character.move(0, 0))
