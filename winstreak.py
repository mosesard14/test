def winStreak(poin_awal, win_streak, poin_ws):
    if win_streak <= 1:
        return("anda tidak winstreak")
    elif win_streak > 1:
        for i in range(win_streak):
            poin_awal += poin_ws
            return(f'poin kamu: {poin_awal}')

            

print(winStreak(1000,5,100))