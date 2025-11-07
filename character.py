array_bi_dimensional = []
for i in range(3):
    char = []
    char_stats = ()

    char_name = input()
    char.append(char_name)
    char_attack_power = int(input())
    char_defense_power = int(input())
    char_stats = (char_attack_power, char_defense_power)
    char.append(char_stats)
    array_bi_dimensional.append(char[:])
    char.clear()

print(array_bi_dimensional)

highest_attack_char = max(array_bi_dimensional, key=lambda x: x[1][0])
print(f"Ataque {highest_attack_char[0]} {highest_attack_char[1][0]}")

highest_defense_char = max(array_bi_dimensional, key=lambda x: x[1][1])
print(f"Defesa {highest_defense_char[0]} {highest_defense_char[1][1]}")
