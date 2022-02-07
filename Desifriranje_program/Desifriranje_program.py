# Janez Bučar, 35160122, IZJAVLJAM DA JE PROGRAM MOJE DELO, 26.12.2021


kode = [7446, 3290, 786, 9810, 12494, 12673, 16628, 9924, 341,
        16706, 5694, 8870, 14317, 16707, 11713, 4557, 2808, 11993,
        4836, 14318, 13910, 8914, 1808, 10509, 11858, 7243, 5698, 12537,
        11858, 7247, 3047, 2827, 4946, 4953, 13030, 1733, 8909, 12537, 3592,
        7532, 10350, 6867, 1306, 3046, 11511, 5785, 12537, 14000, 9822, 8229, 13331,
        9848, 11713, 2566, 13310, 10001, 340, 3191, 9924, 1548, 12291, 4851, 7438, 3206,
        11599, 3836, 8613, 2929, 7813, 4304, 13975, 3346, 83, 9913, 554, 8955, 2853, 13030,
        8495, 4853, 7449, 2058, 4953, 2041, 2529, 5891, 7438, 3150, 8333, 2135, 13030, 8481,
        13030, 11614, 9965, 3346, 3217, 7543, 4853, 2848, 11652, 13346, 8963, 4751, 13030, 16406,
        2318, 3893, 4853, 2734, 1372, 12291, 4847, 341, 14890, 9300, 9634, 9560, 9965, 3046, 15166,
        3503, 13975, 2796, 14033, 9494, 300, 13138, 6883, 4850, 7518, 15604, 10653, 4858, 5765, 3164,
        446, 15253, 12297]


abeceda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

desifriran_text = ''
mod = 0
stevec = 0


for koda in kode:

    temp = ''  # shranjevanje posameznih črk

    while koda > 0:

        stevec = stevec + 1     # števec koliko črk dobimo
        mod = koda % 26
        mod = int(mod)          # mod spremenimo v int...
        temp += abeceda[mod]    # ostanek pri računanju predstavlja črko
        koda = (koda - mod) / 26  # izračun za naslednjo črko

    if (stevec == 2):   #  če ne dobimo 3 črk, je na tem mestu 'a', ker pride do robnega primera.
        temp += 'a'

    stevec = 0

    desifriran_text += temp[::-1]  # tmp trojice črk nato zapišemo in shranimo v 'REVERSE' vrstnem redu

print(desifriran_text)  # izpis brez presledkov

