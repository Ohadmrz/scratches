goods = [['apple', 'pear', 'peach', 'chery' ],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
    'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]
for place, team in enumerate(goods):
    for place_team, word in enumerate(team):
     print(place,place_team)
     print(team,word)
     print(len(word))
