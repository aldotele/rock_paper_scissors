import random


class FunnyNameGenerator:
    adjectives = ["Bad", "Crazy", "Baby", "Big", "Lazy", "Friendly", "Shy"]
    animals = ["Unicorn", "Bird", "Shark", "Leopard", "Dog", "Cat", "Whale", "Hippo"]

    @staticmethod
    def compose_name():
        adj = random.choice(FunnyNameGenerator.adjectives)
        anim = random.choice(FunnyNameGenerator.animals)
        return adj + anim
