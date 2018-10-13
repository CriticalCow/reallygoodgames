import time

print(r'welcome to CriticalCows super fun game!')                              
time.sleep(2)                                                                  
print('HOW TO PLAY')                                                           
print('-----------')                                                           
print('do the math problems that come up on the screen!')                      
choice = raw_input('if your ready type READY  -->  ')                          
if choice == 'READY':                                                          
  print('ok lets start this super fun game!')                                  
  time.sleep(1)                                                                
  choice_2 = raw_input('1  -->  ')                                             
if choice_2 == '1':                                                            
  print('wow you can read or count or whatever!')
else: print('can you count')
choice_3 = raw_input('1 + 1  -->  ')                                           
if choice_3 == '2':                                                            
  print('ok i guess')                                                          
  choice_4 = raw_input('1 * 1  -->  ')                                         
if choice_4 == '1':
  print('sure')
else: print('no get it right, 1 times 1 is always 1')
time.sleep(1)
choice_5 = raw_input('10 * 10  -->  ')                                         
if choice_5 == '100':
  print('gud job you can count!')
  print(r'your reward:')
  time.sleep(1)
  print('nothing! ofc')
  time.sleep(1)
  choice_6 = raw_input('lets keep going ok? ')
if choice_6 == 'ok':
  time.sleep(1)
  choice_7 = raw_input('5 * 5  -->  ')
if choice_7 == '25':
  print('ok')
  print('im still making this really good game just wait')                                      
  print('this is the end')
  print('---------------')
