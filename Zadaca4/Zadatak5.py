import asyncio

async def secure_data(osjetljivi_podaci: dict):
    print(f"Enkripcija podataka za {osjetljivi_podaci['prezime']}...")
    await asyncio.sleep(3)

    return {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': hash(osjetljivi_podaci['broj_kartice']),
        'CVV': hash(osjetljivi_podaci['CVV'])
    }

async def main():
    kartice = [
        {'prezime': 'Horvat', 'broj_kartice': '1234 5678 9012 3456', 'CVV': '123'},
        {'prezime': 'Marić', 'broj_kartice': '1111 2222 3333 4444', 'CVV': '456'},
        {'prezime': 'Kovač', 'broj_kartice': '9999 8888 7777 6666', 'CVV': '789'}
    ]

    zadaci = [asyncio.create_task(secure_data(k)) for k in kartice]
    rezultati = await asyncio.gather(*zadaci)

    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
