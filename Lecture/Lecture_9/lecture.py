from stack_adt import *

def checks_parenthesis_are_balenced(expression):
    '''
    >>> checks_parenthesis_are_balenced('')
    True
    >>> checks_parenthesis_are_balenced('{1+2+[(1+2)+(3+4)]}')
    True
    >>> checks_parenthesis_are_balenced('{1+2+[(1+2)+(3+4)]')
    False
    >>> checks_parenthesis_are_balenced('{1+3}')
    True
    '''

    kinds_of_parenthesis = {')':'(', ']':'[', '}':'{'}
    stack = Stack()
    for s in expression:
        if s in '([{':
            stack.push(s)
        elif s in ')]}':
            '''
            # if stack is empty: imbalenced
            if stack.is_empty():
                return False
            # if ) top of stack should contain (
            # if ] top of stack should contain [
            # if } top of stack should contain {
            if kinds_of_parenthesis != stack.peek():
                return False
            '''
            try:
                if kinds_of_parenthesis[s] != stack.peek():
                    return False
            except EmptyStackError:
                return False
            # pop corresponding opening bracket from stack
            stack.pop()
    return stack.is_empty()

def evaluate(expression):
    '''
    >>> evaluate('20')
    20
    >>> evaluate('2')
    2
    >>> evaluate('1 2+')
    3
    '''
    operations = {'+': lambda x, y: x + y,\
                  '-': lambda x, y: y - x,\
                  '*': lambda x, y: x * y,\
                  '/': lambda x, y: y / x }
    stack = Stack()
    processing_number = False
    for s in expression:
        if s.isdigit():
            if not processing_number:
                processing_number = True
                # push the first digit in a number that is possibly
                # many digits long.
                stack.push(int(s))
            else:
                # s is another digit as part of a number whose previous
                # digits have been processed and 'assembled' into a number 
                # which is now on top of our stack
                stack.push(stack.pop() * 10 + int(s))
        else:
            # Either we just stop processing a number,
            # or we stopped before; in any case, processing number
            # becomes False or it is False already 
            processing_number = False
            if s in operations:
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.push(operations[s](arg1, arg2))
    result = stack.pop()
    if not stack.is_empty():
        print('Expression incorrect!')
    return result





if __name__ == '__main__':
    import doctest
    doctest.testmod()

