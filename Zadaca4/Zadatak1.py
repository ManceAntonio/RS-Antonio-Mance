import asyncio

async def dohvat_podataka():
    print("Dohvaćam podatke...")
    await asyncio.sleep(3)
    podaci = [i for i in range(1, 11)]
    print("Podaci su dohvaćeni.")
    return podaci

async def main():
    podaci = await dohvat_podataka()
    print("Dobiveni podaci:", podaci)

if __name__ == "__main__":
    asyncio.run(main())
