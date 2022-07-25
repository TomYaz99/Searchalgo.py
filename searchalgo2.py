import doctest
#PRETTY SIMILAR SEARCH ALGO BUT WITH DICS
# purpose is to find the most common actors in a data base of movies and list them based off of score, appearnces ect...
# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10


def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]]):
    '''
    Populates and returns a tuple with the following 3 dictionaries
    with data from valid filename.
    
    3 dictionaries returned as a tuple:
    - dict[show title: date added to Netflix]
    - dict[show title: list of actor names]
    - dict[category: list of show titles]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show title: list of actor names]
    
    Precondition: filename is csv with data in expected columns 
        and contains a header row with column titles.
        NOTE: csv = comma separated values where commas delineate columns
        Show titles are considered unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {})
    
    >>> read_file('11lines_data.csv')
    ({'SunGanges': (2019, 11, 15), \
'PK': (2018, 9, 6), \
'Phobia 2': (2018, 9, 5), \
'Super Monsters Save Halloween': (2018, 10, 5), \
'First and Last': (2018, 9, 7), \
'Out of Thin Air': (2017, 9, 29), \
'Shutter': (2018, 9, 5), \
'Long Shot': (2017, 9, 29), \
'FIGHTWORLD': (2018, 10, 12), \
"Monty Python's Almost the Truth": (2018, 10, 2), \
'3 Idiots': (2019, 8, 1)}, \
\
{'SunGanges': ['Naseeruddin Shah'], \
'PK': ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], \
'Phobia 2': ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], \
'Super Monsters Save Halloween': ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], \
'Shutter': ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], \
'FIGHTWORLD': ['Frank Grillo'], "Monty Python's Almost the Truth": ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], \
'3 Idiots': ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey']}, \
\
{'Documentaries': ['SunGanges', 'Out of Thin Air', 'Long Shot'], \
'International Movies': ['SunGanges', 'PK', 'Phobia 2', 'Out of Thin Air', 'Shutter', '3 Idiots'], \
'Comedies': ['PK', '3 Idiots'], \
'Dramas': ['PK', '3 Idiots'], 'Horror Movies': ['Phobia 2', 'Shutter'], \
'Children & Family Movies': ['Super Monsters Save Halloween'], \
'Docuseries': ['First and Last', 'FIGHTWORLD', "Monty Python's Almost the Truth"], \
'British TV Shows': ["Monty Python's Almost the Truth"]})
    '''
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    
    genre_to_movie = {}
    show_to_date = {}
    show_to_actors = {}
    
    file_handle = open(filename, 'r')
    next(file_handle)
    
    if file_handle == {}:
        return ({},{},{})
    
    
    for line in file_handle:
        line = line.strip()
        list_of_strings = line.split(',')
        actors = list_of_strings[INPUT_CAST]
        date = create_date(list_of_strings[INPUT_DATE])
        title = list_of_strings[INPUT_TITLE]
        show_to_date[title] = date
        catgories = list_of_strings[INPUT_CATEGORIES]
        indiv_catgories = catgories.split(':')
        print(indiv_catgories)
        
        if actors != '':
            act = list_of_strings[INPUT_CAST]
            act = act.strip()
            act = act.split(':')
            show_to_actors[list_of_strings[INPUT_TITLE]] = act
            
        for mtype in indiv_catgories:
            if mtype in genre_to_movie:
                genre_to_movie[mtype].append(title)
                
            else:
                genre_to_movie[mtype] = [title] 
        
    file_handle.close()
        
        
        
    return show_to_actors
        
        
        
        

    
    
def create_date(date_str: str) -> Date:
    '''takes a string representing a valid date and returns a date tuple 
    The string passed to the function is guaranteed to be in the following format: 'day-month-year' where,
    Day is a 2 digit integer representing a valid day of the month
    month is the first 3 letters of a valid month, where the first letter is uppercase
    year is a 2 digit integer representing a year in the 2000s
    
    >>> create_date('10-Jan-18') 
    (2018, 1, 10)
    
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    
    >>> create_date('24-Feb-00')
    (2000, 2, 24)
    '''
    d8 = date_str.split("-")
    if(d8[1] == "Jan"):
        d8[1] = 1
    elif(d8[1] == "Feb"):
        d8[1] = 2
    elif(d8[1] == "Mar"):
        d8[1] = 3  
    elif(d8[1] == "Apr"):
        d8[1] = 4
    elif(d8[1] == "May"):
        d8[1] = 5  
    elif(d8[1] == "Jun"):
        d8[1] = 6 
    elif(d8[1] == "Jul"):
        d8[1] = 7
    elif(d8[1] == "Aug"):
        d8[1] = 8
    elif(d8[1] == "Sep"):
        d8[1] = 9
    elif(d8[1] == "Oct"):
        d8[1] = 10
    elif(d8[1] == "Nov"):
        d8[1] = 11
    else:
        d8[1] = 12  
        
    return (int(d8[2])+START_YEAR,d8[1],int(d8[0]))
    
    
    
    




def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[str]:
    '''
    returns a list of sorted show titles of only shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'not found', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'Aamir Khan', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5),
    ['not found', 'not found either', 'Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dil Chahta Hai', 'Dil Dhadakne Do', 'PK', 'Zed Plus']
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dangal', 'Dhobi Ghat (Mumbai Diaries)', \
'Dil Chahta Hai', 'Dil Dhadakne Do', 'Lagaan', 'Madness in the Desert', 'PK', \
'Raja Hindustani', 'Rang De Basanti', 'Secret Superstar', 'Shutter', \
'Taare Zameen Par', 'Talaash', 'Zed Plus']
    '''
    
    movie_to_date,movie_to_actors,genre_to_movie = read_file(filename)
    lomovie = []
    movie_list = []
    if category in genre_to_movie:
        locatitle = genre_to_movie[category]
        
    else:
        return []
    
    for shows in locatitle:
        if shows in movie_to_actors:
            for act in actors:
                if act in movie_to_actors[shows]:
                    if shows not in lomovie:
                        lomovie.append(shows)
    for show in lomovie:
        if movie_to_date[show][YEAR] < date[YEAR] or movie_to_date[show][YEAR] == date[YEAR] and movie_to_date[show][MONTH] < date[MONTH]:
            movie_list.append(show)
            
        if movie_to_date[show][MONTH] == date[MONTH] or movie_to_date[show][DAY] < date[DAY]:
            movie_list.sort()
            
    return movie_list
            
            
        
    
    
    

    
    
        
    
    
    
    
    
   
