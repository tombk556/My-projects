from data_storage import Store

allstocks = {'Amazon':'AMZ.DE', 'SiTime Inc.':'SITM', 
             'Biontech':'22UA.DE', 'Block':'SQ', 
             'Tesla': 'TL0.DE', 'Datagroup': 'D6H.DE', 
             'Rational AG': 'RAA.DE', 'Ferrari':'RACE', 
             'Alphabet': 'GOOG', 'Nestle':'NSRGY', 
             'LVMH':'MOH.F'}

Store(allstocks).fetch_and_store()