from app.models.item import Item
import random

def randomise(min, max):
    return random.randint(min, max)

def create_sample_items() -> list[Item]:
    items_data = [
        ("Wireless Mouse", "Ergonomic 2.4GHz wireless mouse with adjustable DPI"),
        ("Mechanical Keyboard", "RGB backlit keyboard with hot-swappable switches"),
        ("Noise-Cancelling Headphones", "Over-ear headphones with 30-hour battery life"),
        ("USB-C Charging Cable", "Braided 2m cable, supports fast charging"),
        ("Portable Power Bank", "20000mAh battery pack with dual USB output"),
        ("Laptop Stand", "Adjustable aluminum stand for laptops up to 17 inches"),
        ("Webcam 1080p", "Full HD webcam with built-in privacy shutter"),
        ("Bluetooth Speaker", "Waterproof speaker with 12-hour playtime"),
        ("Desk Lamp", "LED lamp with touch dimmer and USB charging port"),
        ("Phone Tripod", "Flexible tripod stand compatible with most smartphones"),
    ]
    return [
        Item(id=i, name=name, description=description)
        for i, (name, description) in enumerate(items_data, start=1)
    ]