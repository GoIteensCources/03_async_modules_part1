import aiofiles
import asyncio


async def writen_to_file(filename, content: str):
    async with aiofiles.open(filename, mode="w") as file:
        await file.write(content)
        print(f"data written to {filename}")


async def read_from_file(filename):
    async with aiofiles.open(filename, mode="r") as file:
        content = await file.read()
        print(f"data: {content}")
    return content


async def main():
    filename_ = "./data/text.txt"
    content = """aiofiles is an Apache2 licensed library, written in Python, for handling local disk files in asyncio applications.
Ordinary local file IO is blocking, and cannot easily and portably be made asynchronous. This means doing file IO 
may interfere with asyncio applications, which shouldn't block the executing thread. aiofiles helps with this by 
introducing asynchronous versions of files that support delegating operations to a separate thread pool."
"""

    await writen_to_file(filename_, content)
    await read_from_file(filename_)


if __name__ == "__main__":
    asyncio.run(main())
