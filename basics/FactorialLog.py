import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of the program')

def factorial(n):
    logging.debug('start of the factorial('+str(n)+')')
    total = 1;
    for i in range(n+1):
        total *=i
        logging.debug('i is'+str(i)+ ', total is'+str(total))
    logging.debug('end of the factorial('+str(n)+')')
    return total

print(factorial(5))


logging.debug('start of the program')

