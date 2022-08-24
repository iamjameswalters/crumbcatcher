import datetime, random, re

import requests
from bs4 import BeautifulSoup
from rich import print


def main():
    logo = r"""[yellow]
     ____             _______  _____  _    _ _   _ _____
    /    \_     .    /  ___  \|  _  \| |  | | | | |  _  \ 
   /  [blue]@   @[/blue]\_  *  .  | |   |_|| |_| || |  | |  V  | |_| /
  (          \       | |    _ |  _  /| |  | | \ / |  _ (
  ( [blue]@   @   @[/blue] )      | |___| || | | \| \__/ | |V| | |_| \
  (           ) _____\_______/|_|_|_|_\____/|_| |_|_____/_____
   \  [blue]@   @[/blue]  / /  ___  \ / _ \|_   _|/  ___ \ | | |  ___|  _  \
    \_______/  | |   |_|/ / \ \ | | | |   |_| |_| | |___| |_| |
               | |    _ | |_| | | | | |    _|  _  |  ___|  _  /
               | |___| ||  _  | | | | |___| | | | | |___| | | \
               \_______/|_| |_| |_| \_______/_| |_|_____|_| |_|
               
               [blue]~~[/blue]A web scraper for Crumbl Cookie's weekly flavors[blue]~~[/blue]
               [/yellow]
  """
    print(logo)

    today = datetime.date.today()

    # Don't run if today is Sunday
    if today.weekday() == 6:
        return print(
            """
Crumbl is [red bold]closed on Sundays[/red bold], but come back tomorrow to find out the [green]new flavors[/green]!
 \n 
    """
        )

    url = "https://crumblcookies.com/"

    try:
        crumbl = requests.get(url)
    except requests.ConnectionError:
        return print(
            f"[red bold]ERROR:[/red bold] It looks like there's a problem with your internet connection. Reconnect and try again!\n"
        )

    # Return error message if we receive a non-2xx HTTP status
    if str(crumbl.status_code)[0] != "2":
        return print(
            f"[red bold]ERROR:[/red bold] {url} returned HTTP status code {crumbl.status_code}\n"
        )

    soup = BeautifulSoup(crumbl.content, "html.parser")
    flavors = soup.select("#weekly-cookie-flavors")

    # If flavors is empty, the site's changed and the scraper's broken
    if not flavors:
        return print(
            """[red bold]Oh no![/red bold] The website appears to have changed. Do the developer a [green]favor[/green] and report this issue on Github at [link=https://github.com/iamjameswalters/crumbcatcher/issues]https://github.com/iamjameswalters/crumbcatcher/issues[/link].\n
    """
        )

    print("[yellow]Here are this week's flavors:[/yellow]\n")

    colors = ["red", "blue", "yellow", "cyan", "magenta", "green"]

    for flavor in flavors[0].contents:
        random_color = colors.pop(random.randint(0, len(colors) - 1))
        flavor_name = flavor.select("div>h3")
        print(
            f"[blue] - [/blue][{random_color}]"
            + flavor_name[0].text
            + f"[/{random_color}]\n"
        )

    print(
        "[yellow]Better [link=https://google.com/maps?q=Crumbl+Cookies]go get one![/link][/yellow]\n"
    )


if __name__ == "__main__":
    main()
