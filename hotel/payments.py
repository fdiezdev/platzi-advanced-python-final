# Pagos: Procesamiento de pagos de las reservas de forma asincrónica.
import asyncio
import random

async def process_payment(guest_name, amount) -> bool:
    """Process the payment of a certain guest_name charging an amount. Returns a bool condition:
    - True: the payment was processed correctly
    - False: there was an error processing the payment"""

    print(f"Processing payment to {guest_name}: ${amount}...")

    await asyncio.sleep(random.randint(3,5)) # simulate the payment gateway time

    return random.choices([True, False], weights=[70, 30])

if __name__ == "__main__":

    result = asyncio.run(process_payment("Francisco", 230))

    if result:
        print("Payment processed correctly!")
    else:
        print("There was an error processing your payment!")
