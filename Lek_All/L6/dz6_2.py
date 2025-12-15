# Ваше завдання — написати програму
# яка переводить число у формат часу у читальному вигляді.
#seconds = int(input("Введіть кількість секунд: "))

#days, ostat = divmod(seconds, 86400)
#hours, ostat = divmod(ostat, 3600)
#minutes, seconds = divmod(ostat, 60)

#print(f"{days} днів, {hours:02}:{minutes:02}:{seconds:02}")

seconds = int(input("Введіть число (від 0 до 8640000): "))

if 0 <= seconds < 8640000:
    days, ostat = divmod(seconds, 86400)
    hours, ostat = divmod(ostat, 3600)
    minutes, secs = divmod(ostat, 60)

    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"
    day_s = "день" if days % 10 == 1 and days % 100 != 11 else \
               "дні" if 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14) else "днів"

    print(f"{days} {day_s}, {time_str}")
else:
    print("Error: число повинно бути від 0 до 8639999 включно.")
