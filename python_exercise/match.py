score = input('Please input your score:')

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: #default
        print('score is ???.')
    
