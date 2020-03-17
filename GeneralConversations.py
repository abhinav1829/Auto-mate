import random
from Speak import speak


def who_are_you(query, txt):
    messages = [
        "I am automate your loyal personal assistant.",
        "automate, didn't I tell you before?",
        "You ask that so many times! I am automate."
    ]
    speak(random.choice(messages), txt)


def toss_coin(query, txt):
    outcomes = ['heads', 'tails']
    speak('I just flipped a coin. It shows ' + random.choice(outcomes), txt)


def how_am_i(query, txt):
    replies = [
        'You are goddamn handsome!',
        'My knees go weak when I see you.',
        'You are sexy!',
        'You look like the kindest person that I have met.'
    ]
    speak(random.choice(replies), txt)


def who_am_i(query, txt):
    name = 'Abhinav'
    speak('You are ' + name + ', a brilliant person.', txt)


def where_born(query, txt):
    speak('I was created by BE project group number thirty six.', txt)


def how_are_you(query, txt):
    speak('I am fine, thank you.', txt)


def are_you_up(query, txt):
    speak('For you, always.', txt)


def love_you(query, txt):
    replies = [
        'I love you too.',
        'You are looking for love in the wrong place.'
    ]
    speak(random.choice(replies), txt)


def marry_me(query, txt):
    speak('I have been receiving a lot of marriage proposals recently.', txt)