import asyncio
import random

async def provjeri_parnost(broj: int):
    print(f"Provjera parnosti za {broj}...")
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    return f"Broj {broj} je neparan."

async def main():
    brojevi = [random.randint(1, 100) for _ in range(10)]
    print("Generirani brojevi:", brojevi)

    zadaci = [asyncio.create_task(provjeri_parnost(b)) for b in brojevi]
    rezultati = await asyncio.gather(*zadaci)

    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
