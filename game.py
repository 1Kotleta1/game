import random

# **Классы и функции**

class Character:
    def __init__(self, name, personality, quest=None, reward=None):
        self.name = name
        self.personality = personality
        self.friendship_level = random.randint(1, 5)
        self.quest = quest
        self.reward = reward

    def interact(self):
        phrases = {
            "дружелюбный": [
                f"{self.name}: Привет! Как идет отдых? Может, сходим к костру?",
                f"{self.name}: Ты отлично выглядишь! Давай сыграем в карты позже.",
                f"{self.name}: Мне нравится проводить время вместе. Кажется, ты мне нравишься...",
            ],
            "серьезный": [
                f"{self.name}: Тишина и спокойствие - залог хорошего отдыха.",
                f"{self.name}: Ты когда-нибудь думал о смысле этих прогулок?",
                f"{self.name}: Иногда я думаю, что вокруг нас слишком много суеты. Хочется просто быть здесь с тобой.",
            ],
            "романтичный": [
                f"{self.name}: Под луной у костра как будто всё становится теплее. Рядом с тобой время замирает.",
                f"{self.name}: Знаешь, мне всегда было сложно открываться людям, но с тобой... как будто всё иначе.",
                f"{self.name}: Мне кажется, этот отдых стал для меня особенным, и это благодаря тебе.",
            ]
        }
        mood = "романтичный" if self.friendship_level >= 7 else self.personality
        return random.choice(phrases[mood])

    def give_quest(self):
        if self.quest:
            print(f"{self.name}: {self.quest}")
            return True
        else:
            print(f"{self.name}: У меня пока нет для тебя заданий.")
            return False

class Game:
    def __init__(self):
        self.locations = {
            'лагерь': 'Ты находишься в лагере. Здесь отдыхает твоя группа. (пойти на озеро/в беседку/в лес/к костру)',
            'озеро': 'Ты у озера. Можно рыбачить или купаться. (рыбачить/вернуться)',
            'беседка': 'Ты в беседке. Тут уютно, можно поиграть в карты. (играть в карты/вернуться)',
            'лес': 'Ты среди деревьев. Здесь можно встретить друзей или вернуться в лагерь. (поговорить/встретить/вернуться)',
            'костер': 'Вокруг костра сидят друзья. Здесь особая атмосфера для душевных разговоров. (поговорить/вернуться)'
        }
        self.current_location = 'лагерь'
        self.inventory = set()
        self.friendship_level = 0

        # Персонажи
        self.characters = [
            Character("Анна", "дружелюбный", quest="Можешь принести мне цветы из леса?", reward="цветы"),
            Character("Максим", "серьезный", quest="Поймай для меня рыбу у озера.", reward="рыба"),
            Character("Лена", "дружелюбный", quest="Найди старую карту в беседке.", reward="карта"),
            Character("Игорь", "серьезный")
        ]

    def display_location(self):
        print("\n" + self.locations[self.current_location])

    def move(self, direction):
        if self.current_location == 'лагерь':
            if direction == 'пойти на озеро':
                self.current_location = 'озеро'
            elif direction == 'в беседку':
                self.current_location = 'беседка'
            elif direction == 'в лес':
                self.current_location = 'лес'
            elif direction == 'к костру':
                self.current_location = 'костер'
            else:
                print('Неверное направление!')
        elif self.current_location == 'озеро' and direction == 'вернуться':
            self.current_location = 'лагерь'
        elif self.current_location == 'беседка' and direction == 'вернуться':
            self.current_location = 'лагерь'
        elif self.current_location == 'лес' and direction == 'вернуться':
            self.current_location = 'лагерь'
        elif self.current_location == 'костер' and direction == 'вернуться':
            self.current_location = 'лагерь'
        elif self.current_location == 'озеро' and direction == 'рыбачить':
            self.fish()
        elif self.current_location == 'беседка' and direction == 'играть в карты':
            self.play_cards()
        else:
            print('Неверное направление!')

    def fish(self):
        fish = ['щуку', 'окуня', 'карпа']
        caught_fish = random.choice(fish)
        print(f'Ты поймал {caught_fish}!')
        self.inventory.add('рыба')
        self.friendship_level += 1

    def play_cards(self):
        win = random.choice([True, False])
        if win:
            print('Ты выиграл в карты! Друзья довольны.')
            self.friendship_level += 2
        else:
            print('Ты проиграл, но ничего страшного!')

    def talk_to_friends(self):
        print("Ты общаешься с друзьями.")
        friend = random.choice(self.characters)
        print(friend.interact())
        self.friendship_level += 1
        print(f"Текущий уровень дружбы с {friend.name}: {friend.friendship_level}")

    def meet_character(self):
        friend = random.choice(self.characters)
        print(f"Ты встретил {friend.name}.")
        if friend.give_quest():
            self.complete_quest(friend)

    def complete_quest(self, friend):
        if friend.reward in self.inventory:
            print(f"{friend.name}: Спасибо, что выполнил мою просьбу! Это очень много для меня значит.")
            self.friendship_level += 3
            self.inventory.remove(friend.reward)
        else:
            print(f"{friend.name}: Ты еще не нашел то, о чем я просил.")

# **Основная часть игры**

def main():
    print('Добро пожаловать в "Летние приключения"! Исследуй лагерь и знакомься с друзьями.')
    game = Game()

    while True:
        game.display_location()
        print(f'Уровень дружбы: {game.friendship_level}')
        command = input('Что ты хочешь сделать? ').lower()

        if command in ['пойти на озеро', 'в беседку', 'в лес', 'к костру', 'вернуться', 'рыбачить', 'играть в карты']:
            game.move(command)
        elif command == 'поговорить':
            if game.current_location in ['костер', 'лес']:
                game.talk_to_friends()
            else:
                print("Здесь не с кем поговорить.")
        elif command == 'встретить':
            if game.current_location == 'лес':
                game.meet_character()
            else:
                print("Здесь никого нет.")
        elif command == 'инвентарь':
            print(f'Твой инвентарь: {", ".join(game.inventory) if game.inventory else "ничего нет"}')
        elif command == 'выход':
            print('Спасибо за игру! До встречи!')
            break
        else:
            print('Неверная команда!')

if __name__ == "__main__":
    main()
