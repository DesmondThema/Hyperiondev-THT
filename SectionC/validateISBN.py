def isbn13(isbn):
    
    # check for length
    lenth = len(isbn)
    
    if (lenth == 10):
        
        # Computing weighted sum
        # of first 9 digits
        _sum = 0
        for i in range(9):
            if 0 <= int(isbn[i]) <= 9:
                _sum += int(isbn[i]) * (10 - i)
            else:
              return False
                
        # if last digit is X, add 10 to sum,
        # else add its value.
        _sum += 10 if isbn[9] == 'X' else int(isbn[9])
        
        if (_sum % 11 != 0):
            print('Invalid')
        else:
            isbn = '978' + isbn[0: lenth - 1]
            _sum = 0
            
            for i in range(12):
                number = 1 if i % 2 == 0 else 3
                _sum += int((isbn[i:i + 1])) * number
                
            lastDigit = str(10 - _sum % 10)
            print(isbn+lastDigit)
            
    if (lenth == 13):
        _sum = 0
        for i in range(13):
            number = 1 if i % 2 == 0 else 3
            _sum += int((isbn[i:i + 1])) * number
            
        if (_sum % 10 != 0):
            print('Invalid')
        else:
            print('Valid')

# Driver Code          

isbn13("9780316066525")
isbn13("0330301824")
isbn13("0316066524")

            