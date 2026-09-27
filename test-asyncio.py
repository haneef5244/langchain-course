import asyncio


async def print_result(delay, id):
    await asyncio.sleep(delay)
    print(f"Id {id} completed")
    return {"id": id}

async def main():

    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(print_result(sleep_time, i))
            tasks.append(task)
    

asyncio.run(main())