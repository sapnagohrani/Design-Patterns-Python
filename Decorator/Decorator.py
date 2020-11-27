def make_text_pretty(func):
    print("Going to make your text pretty")
    func()
    print("Your Text looks pretty")


def make_me_pretty():
    print("Make me pretty")


make_text_pretty(make_me_pretty)