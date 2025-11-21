import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

# Prvo create_task raspoređuje sva tri timera u event loop
# Nakon toga asyncio.gather pauzira main() i event loop započinje izvršavati sve timere po redu
# Onda svaki timer ispisuje stanje, pa se pauzira s await asyncio.sleep(1)
# Te nakon svake sekunde event loop koristi sve aktivne timere i oni nastavljaju sa  odbrojavanjem.
# Timer 1 završava prvi nakon 3 sekunde te zatim Timer 2 za 5 sekundi i Timer 3 za 7 sekundi
# Kada sve korutine završe, gather završava i main() završava, event loop se završi.
