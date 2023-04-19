import random

home_team = str(input("Írd be a hazai csapatot"))
away_team = str(input("Írd be a vendég csapatot"))

home_goals = random.randint(0, 5)
away_goals = random.randint(0, 5)

# Az első gól percben
first_goal_minute = random.randint(1, 90)

# A további gólok és időpontok listája
goal_minutes = []

for i in range(home_goals):
    goal_minutes.append(random.randint(1, 90))

for i in range(away_goals):
    goal_minutes.append(random.randint(1, 90))

# Az időpontokat növekvő sorrendbe rendezzük
goal_minutes.sort()

print(f"{home_team} {home_goals} - {away_goals} {away_team}")


# Az összes gól kiírása
if len(goal_minutes) == 0:
    print("Nem született több gól a meccsen.")
else:
    print("Gólok: ")
    for minute in goal_minutes:
        if minute == first_goal_minute:
            continue
        team = home_team if minute in goal_minutes[:home_goals] else away_team
        print(f"{minute}. perc: {team}")
