    '''
    >>> f = Frieze('frieze_1.txt')
    >>> f = Frieze('frieze_2.txt')
    >>> f = Frieze('frieze_3.txt')
    >>> f = Frieze('frieze_4.txt')
    >>> f = Frieze('frieze_5.txt')
    >>> f = Frieze('frieze_6.txt')
    >>> f = Frieze('frieze_7.txt')
    >>> f = Frieze('not_a_frieze_1.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('not_a_frieze_2.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('not_a_frieze_3.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('not_a_frieze_4.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('not_a_frieze_5.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('not_a_frieze_6.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('not_a_frieze_7.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Input does not represent a frieze. 
    >>> f = Frieze('incorrect_input_1.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Incorrect input. 
    >>> f = Frieze('incorrect_input_2.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Incorrect input. 
    >>> f = Frieze('incorrect_input_3.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Incorrect input. 
    >>> f = Frieze('incorrect_input_4.txt')
    Traceback (most recent call last):
    ...
    FriezeError: Incorrect input. 
    '''
    
    f.display()
