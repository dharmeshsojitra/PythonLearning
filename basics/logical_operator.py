bad_credit = input('press yes if user has bad credit: ')

if bad_credit == 'yes' :
    bad_credit = True
else:
    bad_credit = False

criminal_record = input('press yes if user has criminal record: ')
if criminal_record == 'yes' :
    criminal_record = True
else:
    criminal_record = False

if bad_credit and criminal_record :
    print('can not approve loan')
elif bad_credit and not criminal_record:
    print('submit bank guarantee')
else:
    print('loan granted')
