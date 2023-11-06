import time

seconds = int(input("Digite o tempo em segundos: "))

def conversor(seconds):
    while seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins}:{secs}    '
        print(timer,end = '\r')
        time.sleep(1)
        seconds -=1
    
    
    
conversor(seconds)


