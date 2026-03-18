import asyncio

async def tarea():
    print("Esperando 3 segundos...")
    await asyncio.sleep(3)
    print("Listo")
    
asyncio.run(tarea())