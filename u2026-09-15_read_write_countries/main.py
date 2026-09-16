from pathlib import Path

#                   ,_   .  ._. _.  .
#               , _-\','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-
#      /~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_
#      /              ,/'-/~ '\ ,' _  , '|,'|~                   ._/-, /~
#      ~/-'~\_,       '-,| '|. '   ~  ,\ /'~                /    /_  /~
#    .-~      '|        '',\~|\       _\~     ,_  ,               /|
#              '\        /'~          |_/~\\,-,~  \ "         ,_,/ |
#               |       /            ._-~'\_ _~|              \ ) /
#                \   __-\           '/      ~ |\  \_          /  ~
#      .,         '\ |,  ~-_      - |          \\_' ~|  /\  \~ ,
#                   ~-_'  _;       '\           '-,   \,' /\/  |
#                     '\_,~'\_       \_ _,       /'    '  |, /|'
#                       /     \_       ~ |      /         \  ~'; -,_.
#                       |       ~\        |    |  ,        '-_, ,; ~ ~\
#                        \,      /        \    / /|            ,-, ,   -,
#                         |    ,/          |  |' |/          ,-   ~ \   '.
#                        ,|   ,/           \ ,/              \       |
#                        /    |             ~                 -~~-, /   _
#                        |  ,-'                                    ~    /
#                        / ,'                                      ~
#                        ',|  ~
#                          ~'

def write_countries(filename="countries.txt"):
    
    # Get current python directory and create file there
    script_directory = Path(__file__).resolve().parent
    output_countries = script_directory / filename

    msg = "Enter country names to add to the file. Type 'exit' or '0' to finish. 'help' for help!"
    print(msg)
    countries = []

    while True:
        country = input("> ")
        if country.lower() == 'exit' or country == '0':
            break
        elif country.lower() == 'help':
            print(msg)
            continue

        countries.append(country)
        with output_countries.open("a", encoding="utf-8") as file:
            file.write(country + "\n")

    print(f"Countries have been written to {output_countries.name}.")

    msg = "for each country, enter the capital city. Type 'exit' or '0' to finish. 'help' for help!"
    print(msg)

    filename_capitals = filename.split(".")[0] + "_capitals.txt"
    output_capitals = script_directory / filename_capitals

    for c in countries:
        capital = input(f"{c}: ")
        with output_capitals.open("a", encoding="utf-8") as file:
            file.write(f"{country}: {capital}\n")

    print("\n\n")


if __name__ == "__main__":
    write_countries()