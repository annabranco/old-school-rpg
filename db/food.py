from core.elements import Food

# DEFINES DATABASE FOR ALL FOOD ITEMS
'''
    constructor = Food(name: str, description: str, weight: int, quantity: int = 0)
    All descriptions must complete the sentence: "The {food} looks..."
    Initial quantity is normally always 0 when the instance is created.
'''


apple = Food('apple', 'red and juicy', 0.2, 0)

dry_meat = Food('dry meat', 'dry and untasty', 0.5, 0)
leather_meat = Food('dry meat', 'dry like leather and very untasty', 0.5, 0)

smelly_meat = Food('smelly meat', 'dark and smells really bad', 0.5, 0)
