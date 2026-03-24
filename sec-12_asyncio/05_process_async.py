
# asyncio and multiprocessing

import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"🔐 {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        res = await loop.run_in_executor(pool, encrypt, "credit_card_9876")
        print("Result:",res)


if __name__ == "__main__":
    asyncio.run(main())