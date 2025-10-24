# Programming Exercise 9-1

def main():
    # Initialize dictionaries
    rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755,
             'NT110':1244, 'CM241':1411}

    instructors = {'CS101':'Haynes', 'CS102':'Alvarado',
                   'CS103':'Rich', 'NT110':'Burke',
                   'CM241':'Lee'}

    times = {'CS101':'8:00 am', 'CS102':'9:00 am',
             'CS103':'10:00 am', 'NT110':'11:00 am',
             'CM241':'12:00 pm'}

    course = input('Enter a course number: ')

    if course not in rooms:
        print(f'{course} is an invalid course number.')
    else:
        print(f'The details for course {course} are:')
        print(f'Room: {rooms[course]}')
        print(f'Instructor: {instructors[course]}')
        print(f'Time: {times[course]}')

# Call the main function.
if __name__ == '__main__':
    main()