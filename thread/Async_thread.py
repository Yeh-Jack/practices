import asyncio

SKIP_ONE_LINE = "\n\n"


async def job(seq):
    print(f"Task {seq} working, wait {seq*2} seconds ...")
    await asyncio.sleep(seq * 2)
    print(f"Thread {seq} completed.")


async def main():
    child1 = asyncio.create_task(job(1))
    child2 = asyncio.create_task(job(2))
    child3 = asyncio.create_task(job(3))

    # 主執行緒繼續執行自己的工作
    await asyncio.sleep(0.5)
    print("Main thread: wait for doughter threads ending ...", end=SKIP_ONE_LINE)

    # Wait for all children threads finish.
    results = await asyncio.gather(
        child1,
        child2,
        child3,
    )
    print("Main Done.")


asyncio.run(main())
