import webbrowser
import sys

# I noticed that all wiki pages start with this URL as a base
# and just change the last part for the item you're looking up.
# This is why I'm making it a global constant.
BASE_URL = 'https://minecraft.fandom.com/wiki/'
# Shortcut for typing 'sys.argv' over and over again.
CMD_ARGS = sys.argv

def check_for_tools(user_input_args: str) -> str:
    # I noticed that if you click on any type of tool,
    # (i.e. if you click on 'Diamond Pickaxe')
    # it redirects to the base tool page.
    # TODO: This introduces a potential bug when the user passes in
    # 'AxePick', it interprets as 'Axe.'
    # (i.e. it is looking too aggressively for these keywords)
    result = user_input_args
    if 'pickaxe' in user_input_args.lower():
        result = 'Pickaxe'
    elif 'axe' in user_input_args.lower():
        result = 'Axe'
    elif 'shovel' in user_input_args.lower():
        result = 'Shovel'
    elif 'hoe' in user_input_args.lower():
        result = 'Hoe'
    elif 'sword' in user_input_args.lower():
        result = 'Sword'
    return result


def main():
    if len(CMD_ARGS) < 2:
        # Guards against an IndexError that would occur otherwise.
        print('Usage: pymcwiki [Name_of_minecraft_item]')
        exit()

    # Combine the space separated arguments list into one string
    # to be used to construct the full URL.
    # The separator is the underscore character because
    # if there is more than one word in the search,
    # then the Minecraft Wiki uses an underscore in the URL of the page.
    user_input_args = '_'.join(CMD_ARGS[1:])
    result = check_for_tools(user_input_args)
    # TODO: Change the input to make in the format 'Firstword Secondword Thirdword' etc.
    # (with the first letter capitalized and the rest of the word lowercase)
    webbrowser.open(f'{BASE_URL}{result}')


if __name__ == '__main__':
    main()
