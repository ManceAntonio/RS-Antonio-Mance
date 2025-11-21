import asyncio
import time

async def dohvat_korisnika():
    print("Dohvaćam korisnike...", time.strftime("%X"))
    await asyncio.sleep(3)
    print("Korisnici su dohvaćeni.", time.strftime("%X"))
    return [{"id": 1}]

async def dohvat_proizvoda():
    print("Dohvaćam proizvode...", time.strftime("%X"))
    await asyncio.sleep(5)
    print("Proizvodi su dohvaćeni.", time.strftime("%X"))
    return [{"id": 101}]

async def main():
    t1 = time.perf_counter()
    k, p = await asyncio.gather(dohvat_korisnika(), dohvat_proizvoda())
    t2 = time.perf_counter()
    print("Korisnici:", k)
    print("Proizvodi:", p)
    print(f"Vrijeme izvođenja: {t2 - t1:.2f} sekundi")

if __name__ == "__main__":
    asyncio.run(main())
