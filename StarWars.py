import requests 
import json     
import sys

#-Exercise 1: Find all ships that appeared in "Return of the Jedi"
def ships_return_of_the_jedi(results):
    for starship in results:
        if 'http://swapi.dev/api/films/3/' in starship['films']:
            yield starship['name']
            
#-Exercise 2: Find all ships that have a hyperdrive rating >=1.0 in
def ships_hyperdrive_rating(results):
    for startship in results:
        if startship['hyperdrive_rating'] != 'unknown' and float(startship['hyperdrive_rating']) >= 1.0 :
            yield startship['name']

#-Exercise 3: Find all ships that have crews between 3 and 100
def ships_crew(results):
    for starship in results:
        #print(starship['crew'])
        if starship['crew'] != 'unknown':
            if '-' in starship['crew']:
                crew_range = starship['crew'].split('-')
                if int(crew_range[0]) >3 and 100> int(crew_range[1]):
                    yield starship['name']
            else: 
                number_coma = int(starship['crew'].replace(',',''))
                if 3< number_coma and number_coma <100:
                    yield starship['name']
                    
def crawl(link,exercise):
    response = requests.get(link)
    api_results = json.loads(response.content)
    if exercise == '1':
        yield from ships_return_of_the_jedi(api_results['results'])
    elif exercise == '2':
        yield from ships_hyperdrive_rating(api_results['results'])
    elif exercise == '3':
        yield from ships_crew(api_results['results'])
        
    if 'next' in api_results and api_results['next'] is not None:
        next_page = crawl(api_results['next'],exercise)
        for page in next_page:
            yield page

def print_results(link,exercise):
    if exercise in ['1','2','3']:
        star_wars_exercises = crawl(link,exercise)
        print(star_wars_exercises)
        for result in star_wars_exercises:
            print(result)
        else:
            sys.exit(0)
    else:
        print("Invalid exercise")
        sys.exit(1)

    
if __name__ == "__main__":
   print_results('http://swapi.dev/api/starships',sys.argv[1])


#                       .-.
#                      |_:_|
#                     /(_Y_)\
#.                   ( \/M\/ )
# '.               _.'-/'-'\-'._
#   ':           _/.--'[[[[]'--.\_
#     ':        /_'  : |::"| :  '.\
#       ':     //   ./ |UUU| \.'  :\
#         ':  _:'..' \_|___|_/ :   :|
#           ':.  .'  |_[___]_|  :.':\
#            [::\ |  :  | |  :   ; : \
#             '-'   \/'.| |.' \  .;.' |
#             |\_    \  '-'   :       |
#             |  \    \ .:    :   |   |
#             |   \    | '.   :    \  |
#             /       \   :. .;       |
#            /     |   |  :__/     :  \\
#           |  |   |    \:   | \   |   ||
#          /    \  : :  |:   /  |__|   /|
#          |     : : :_/_|  /'._\  '--|_\
#          /___.-/_|-'   \  \
#                         '-'
#
#        ---  May the force be with you ---