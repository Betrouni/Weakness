# By HappySylveon :)

import time


def typeListToString(list):
    sentence = ''
    for word in list:
        sentence += word + ' '
    return sentence


def replaceLetterE(s: str) -> str:
    # On parcourt chaque caractère de la chaîne de caractères
    if s[0] == "E":
        s = "É" + s[1:]
        return s
    else:
        s = s.replace('e', 'é')
        return s


def findWeakness(typesInput):
    a = ("normal")
    b = ("fighting")
    c = ("flying")
    d = ("poison")
    e = ("ground")
    f = ("rock")
    g = ("bug")
    h = ("ghost")
    i = ("steel")
    j = ("fire")
    k = ("water")
    l = ("grass")
    m = ("electric")
    n = ("psychic")
    o = ("ice")
    p = ("dragon")
    q = ("dark")
    r = ("fairy")

    types = (
        "Normal", "Combat", "Vol", "Poison", "Sol", "Roche", "Insecte", "Spectre", "Acier", "Feu", "Eau", "Plante",
        "Electrik", "Psy", "Glace", "Dragon", "Ténèbres", "Fée")

    # type = ['Normal', 'Vol']
    # print(type[1] + ' ' + type[0])

    owo = typesInput

    if owo == a:
        print("Faiblesses: Combat", "\nResistances: none", "\nImmunité: Spectre")
    elif owo == b:
        print("Faiblesses: Fée, Vol, Psy", "\nResistances: Insecte, Ténèbres, Roche", "\nImmunité: None")
    elif owo == c:
        print("Faiblesses: Electrik, Glace, Roche", "\nResistances: Insecte, Combat, Plante", "\nImmunité: Sol")
    elif owo == d:
        print("Faiblesses: Sol, Psy", "\nResistances: Insecte, Fée, Combat, Plante, Poison",
              "\nImmunité: None")
    elif owo == e:
        print("Faiblesses: Plante, Glace, Eau", "\nResistances: Poison, Roche", "\nImmunité: Electrik")
    elif owo == f:
        print("Faiblesses: Combat, Plante, Sol, Acier, Eau", "\nResistances: Feu, Vol, Normal, Poison",
              "\nImmunité: None")
    elif owo == g:
        print("Faiblesses: Feu, Vol, Roche", "\nResistances: Combat, Plante, Sol", "\nImmunité: None")
    elif owo == h:
        print("Faiblesses: Ténèbres, Spectre", "\nResistances: Insecte, Poison", "\nImmunité: Combat, Normal")
    elif owo == i:
        print("Faiblesses: Combat, Feu, Sol",
              "\nResistances: Insecte, Dragon, Fée, Vol, Plante, Glace, Normal, Psy, Roche, Acier",
              "\nImmunité: Poison")
    elif owo == j:
        print("Faiblesses: Sol, Roche, Eau", "\nResistances: Insecte, Fée, Feu, Plante, Glace, Acier",
              "\nImmunité: None")
    elif owo == k:
        print("Faiblesses: Electrik, Plante", "\nResistances: Feu, Glace, Acier, Eau", "\nImmunité: None")
    elif owo == l:
        print("Faiblesses: Insecte, Feu, Vol, Glace, Poison", "\nResistances: Electrik, Plante, Sol, Eau",
              "\nImmunité: None")
    elif owo == m:
        print("Faiblesses: Sol", "\nResistances: Electrik, Vol, Acier", "\nImmunité: None")
    elif owo == n:
        print("Faiblesses: Insecte, Ténèbres, Spectre", "\nResistances: Combat, Psy", "\nImmunité: None")
    elif owo == o:
        print("Faiblesses: Combat, Feu, Roche, Acier", "\nResistances: Glace", "\nImmunité: None")
    elif owo == p:
        print("Faiblesses: Dragon, Fée, Glace", "\nResistances: Electrik, Feu, Plante, Eau", "\nImmunité: None")
    elif owo == q:
        print("Faiblesses: Insecte, Fée, Combat", "\nResistances: Ténèbres, Spectre", "\nImmunité: Psy")
    elif owo == r:
        print("Faiblesses: Poison, Acier", "\nResistances: Insecte, Ténèbres, Combat", "\nImmunité: Dragon")
    elif owo == (a + " " + b) or owo == (b + " " + a):
        print("Faiblesses: Fée, Combat, Vol, Psy", "\nResistances: Insecte, Ténèbres, Roche",
              "\nImmunité: Spectre")
    elif owo == (a + " " + c) or owo == (c + " " + a):
        print("Faiblesses: Electrik, Glace, Roche", "\nResistances: Insecte, Plante", "\nImmunité: Spectre, Sol")
    elif owo == (a + " " + d) or owo == (d + " " + a):
        print("Faiblesses: Sol, Psy", "\nResistances: Plante, Poison, Insecte, Fée", "\nImmunité: Spectre")
    elif owo == (a + " " + e) or owo == (e + " " + a):
        print("Faiblesses: Combat, Plante, Glace, Eau", "\nResistances: Poison, Roche",
              "\nImmunité: Electrik, Spectre")
    elif owo == (a + " " + f) or owo == (f + " " + a):
        print("Faiblesses: Eau, Plante, Combat, Sol", "\nResistances: Normal, Feu, Poison, Vol",
              "\nImmunité: Spectre")
    elif owo == (a + " " + g) or owo == (g + " " + a):
        print("Faiblesses: Feu, Vol, Roche", "\nResistances: Plante, Sol", "\nImmunité: Spectre")
    elif owo == (a + " " + h) or owo == (h + " " + a):
        print("Faiblesses: Ténèbres", "\nResistances: Poison, Insecte", "\nImmunité: Normal, Combat, Spectre")
    elif owo == (a + " " + i) or owo == (i + " " + a):
        print("Faiblesses: Feu, Combat, Sol",
              "\nResistances: Feu, Plante, Glace, Vol, Psy, Insecte, Roche, Dragon, Acier, Fée",
              "\nImmunité: Poison, Normal")
    elif owo == (a + " " + j) or owo == (j + " " + a):
        print("Faiblesses: Combat, Sol, Roche, Eau", "\nResistances: Insecte, Fée, Feu, Plante, Glace, Acier",
              "\nImmunité: Spectre")
    elif owo == (a + " " + k) or owo == (k + " " + a):
        print("Faiblesses: Electrik, Combat, Plante", "\nResistances: Feu, Glace, Acier, Eau",
              "\nImmunité: Spectre")
    elif owo == (a + " " + l) or owo == (l + " " + a):
        print("Faiblesses: Insecte, Combat, Feu, Vol, Glace, Poison",
              "\nResistances: Electrik, Plante, Sol, Eau", "\nImmunité: Spectre")
    elif owo == (a + " " + m) or owo == (m + " " + a):
        print("Faiblesses: Combat, Sol", "\nResistances: Electrik, Vol, Acier", "\nImmunité: Spectre")
    elif owo == (a + " " + m) or owo == (m + " " + a):
        print("Faiblesses: Combat, Sol", "\nResistances: Electrik, Vol, Acier", "\nImmunité: Spectre")
    elif owo == (a + " " + n) or owo == (n + " " + a):
        print("Faiblesses: Insecte, Ténèbres", "\nResistances: Psy", "\nImmunité: Spectre")
    elif owo == (a + " " + o) or owo == (o + " " + a):
        print("Faiblesses: Feu, Combat, Roche, Acier", "\nResistances: Glace", "\nImmunité: Spectre")
    elif owo == (a + " " + p) or owo == (p + " " + a):
        print("Faiblesses: Dragon, Fée, Combat, Glace", "\nResistances: Electrik, Feu, Plante, Eau",
              "\nImmunité: Spectre")
    elif owo == (a + " " + q) or owo == (q + " " + a):
        print("Faiblesses: Insecte, Fée, Combat", "\nResistances: Ténèbres", "\nImmunité: Spectre, Psy")
    elif owo == (a + " " + r) or owo == (r + " " + a):
        print("Faiblesses: Poison, Acier", "\nResistances: Insecte, Ténèbres", "\nImmunité: Dragon, Spectre")
    elif owo == (b + " " + c) or owo == (c + " " + b):
        print("Faiblesses: Electrik, Fée, Vol, Glace, Psy", "\nResistances: Insecte, Ténèbres, Combat, Plante",
              "\nImmunité: Sol")
    elif owo == (b + " " + d) or owo == (d + " " + b):
        print("Faiblesses: Vol, Sol, Psy", "\nResistances: Insecte, Ténèbres, Combat, Plante, Poison, Roche",
              "\nImmunité: None")
    elif owo == (b + " " + e) or owo == (e + " " + b):
        print("Faiblesses: Eau, Plante, Glace, Vol, Psy, Fée", "\nResistances: Poison, Insecte, Roche, Ténèbres",
              "\nImmunité: Electrik")
    elif owo == (b + " " + f) or owo == (f + " " + b):
        print("Faiblesses: Fée, Combat, Plante, Sol, Psy, Acier, Eau",
              "\nResistances: Insecte, Ténèbres, Feu, Normal, Poison, Roche", "\nImmunité: None")
    elif owo == (b + " " + g) or owo == (g + " " + b):
        print("Faiblesses: Fée, Feu, Vol, Psy", "\nResistances: Insecte, Ténèbres, Combat, Plante, Sol",
              "\nImmunité: None")
    elif owo == (b + " " + h) or owo == (h + " " + b):
        print("Faiblesses: Fée, Vol, Spectre, Psy", "\nResistances: Insecte, Poison, Roche",
              "\nImmunité: Combat, Normal")
    elif owo == (b + " " + i) or owo == (i + " " + b):
        print("Faiblesses: Combat, Feu, Sol",
              "\nResistances: Insecte, Ténèbres, Dragon, Plante, Glace, Normal, Roche, Acier", "\nImmunité: Poison")
    elif owo == (b + " " + j) or owo == (j + " " + b):
        print("Faiblesses: Vol, Sol, Psy, Eau", "\nResistances: Insecte, Ténèbres, Feu, Plante, Glace, Acier",
              "\nImmunité: None")
    elif owo == (b + " " + k) or owo == (k + " " + b):
        print("Faiblesses: Electrik, Fée, Vol, Plante, Psy",
              "\nResistances: Insecte, Ténèbres, Feu, Glace, Roche, Acier, Eau", "\nImmunité: None")
    elif owo == (b + " " + l) or owo == (l + " " + b):
        print("Faiblesses: Fée, Feu, Vol, Glace, Poison, Psy",
              "\nResistances: Ténèbres, Electrik, Plante, Sol, Roche, Eau", "\nImmunité: None")
    elif owo == (b + " " + m) or owo == (m + " " + b):
        print("Faiblesses: Sol, Psy, Fée", "\nResistances: Electrik, Insecte, Roche, Ténèbres, Acier",
              "\nImmunité: None")
    elif owo == (b + " " + n) or owo == (n + " " + b):
        print("Faiblesses: Fée, Vol, Spectre", "\nResistances: Combat, Roche", "\nImmunité: None")
    elif owo == (b + " " + o) or owo == (o + " " + b):
        print("Faiblesses: Fée, Combat, Feu, Vol, Psy, Acier", "\nResistances: Insecte, Ténèbres, Glace",
              "\nImmunité: None")
    elif owo == (b + " " + p) or owo == (p + " " + b):
        print("Faiblesses: Dragon, Fée, Vol, Glace, Psy",
              "\nResistances: Insecte, Ténèbres, Electrik, Feu, Plante, Roche, Eau", "\nImmunité: None")
    elif owo == (b + " " + q) or owo == (q + " " + b):
        print("Faiblesses: Fée, Combat, Vol", "\nResistances: Ténèbres, Spectre, Roche", "\nImmunité: Psy")
    elif owo == (b + " " + r) or owo == (r + " " + b):
        print("Faiblesses: Poison, Vol, Psy, Acier, Fée", "\nResistances: Combat, Insecte, Roche, Ténèbres",
              "\nImmunité: Dragon")
    elif owo == (c + " " + d) or owo == (d + " " + c):
        print("Faiblesses: Electrik, Glace, Psy, Roche", "\nResistances: Insecte, Fée, Combat, Plante, Poison",
              "\nImmunité: Sol")
    elif owo == (c + " " + e) or owo == (e + " " + c):
        print("Faiblesses: Glace, Eau", "\nResistances: Insecte, Combat, Poison", "\nImmunité: Electrik, Sol")
    elif owo == (c + " " + f) or owo == (f + " " + c):
        print("Faiblesses: Electrik, Glace, Roche, Acier, Eau", "\nResistances: Insecte, Feu, Vol, Normal, Poison",
              "\nImmunité: Sol")
    elif owo == (c + " " + g) or owo == (g + " " + c):
        print("Faiblesses: Electrik, Feu, Vol, Glace, Roche", "\nResistances: Insecte, Combat, Plante",
              "\nImmunité: Sol")
    elif owo == (c + " " + h) or owo == (h + " " + c):
        print("Faiblesses: Ténèbres, Electrik, Spectre, Glace, Roche", "\nResistances: Insecte, Plante, Poison",
              "\nImmunité: Combat, Sol, Normal")
    elif owo == (c + " " + i) or owo == (i + " " + c):
        print("Faiblesses: Electrik, Feu",
              "\nResistances: Insecte, Dragon, Fée, Vol, Plante, Normal, Psy, Acier",
              "\nImmunité: Sol, Poison")
    elif owo == (c + " " + j) or owo == (j + " " + c):
        print("Faiblesses: Electrik, Roche, Eau", "\nResistances: Insecte, Fée, Combat, Feu, Plante, Acier",
              "\nImmunité: Sol")
    elif owo == (c + " " + k) or owo == (k + " " + c):
        print("Faiblesses: Electrik, Roche", "\nResistances: Insecte, Combat, Feu, Acier, Eau",
              "\nImmunité: Sol")
    elif owo == (c + " " + l) or owo == (l + " " + c):
        print("Faiblesses: Feu, Vol, Glace, Poison, Roche", "\nResistances: Combat, Plante, Eau",
              "\nImmunité: Sol")
    elif owo == (c + " " + m) or owo == (m + " " + c):
        print("Faiblesses: Glace, Roche", "\nResistances: Insecte, Combat, Vol, Plante, Acier", "\nImmunité: Sol")
    elif owo == (c + " " + n) or owo == (n + " " + c):
        print("Faiblesses: Ténèbres, Electrik, Spectre, Glace, Roche", "\nResistances: Combat, Plante, Psy",
              "\nImmunité: Sol")
    elif owo == (c + " " + o) or owo == (o + " " + c):
        print("Faiblesses: Electrik, Feu, Roche, Acier", "\nResistances: Insecte, Plante", "\nImmunité: Sol")
    elif owo == (c + " " + p) or owo == (p + " " + c):
        print("Faiblesses: Dragon, Fée, Glace, Roche", "\nResistances: Insecte, Combat, Feu, Plante, Eau",
              "\nImmunité: Sol")
    elif owo == (c + " " + q) or owo == (q + " " + c):
        print("Faiblesses: Electrik, Fée, Glace, Roche", "\nResistances: Ténèbres, Spectre, Plante",
              "\nImmunité: Sol, Psy")
    elif owo == (c + " " + r) or owo == (r + " " + c):
        print("Faiblesses: Electrik, Glace, Poison, Roche, Acier", "\nResistances: Insecte, Ténèbres, Combat, Plante",
              "\nImmunité: Dragon, Sol")
    elif owo == (d + " " + e) or owo == (e + " " + d):
        print("Faiblesses: Sol, Glace, Psy, Eau", "\nResistances: Insecte, Fée, Combat, Poison, Roche",
              "\nImmunité: Electrik")
    elif owo == (d + " " + f) or owo == (f + " " + d):
        print("Faiblesses: Sol, Psy, Acier, Eau",
              "\nResistances: Insecte, Fée, Feu, Vol, Normal, Poison", "\nImmunité: None")
    elif owo == (d + " " + g) or owo == (g + " " + d):
        print("Faiblesses: Feu, Vol, Psy, Roche", "\nResistances: Insecte, Fée, Combat, Plante, Poison",
              "\nImmunité: None")
    elif owo == (d + " " + h) or owo == (h + " " + d):
        print("Faiblesses: Ténèbres, Spectre, Sol, Psy", "\nResistances: Insecte, Fée, Plante, Poison",
              "\nImmunité: Combat, Normal")
    elif owo == (d + " " + i) or owo == (i + " " + d):
        print("Faiblesses: Feu, Sol",
              "\nResistances: Normal, Plante, Glace, Vol, Insecte, Roche, Dragon, Acier, Fée", "\nImmunité: Poison")
    elif owo == (d + " " + j) or owo == (j + " " + d):
        print("Faiblesses: Sol, Psy, Roche, Eau",
              "\nResistances: Insecte, Fée, Combat, Feu, Plante, Glace, Poison, Acier", "\nImmunité: None")
    elif owo == (d + " " + k) or owo == (k + " " + d):
        print("Faiblesses: Electrik, Sol, Psy",
              "\nResistances: Insecte, Fée, Combat, Feu, Glace, Poison, Acier, Eau", "\nImmunité: None")
    elif owo == (d + " " + l) or owo == (l + " " + d):
        print("Faiblesses: Feu, Vol, Glace, Psy", "\nResistances: Electrik, Fée, Combat, Plante, Eau",
              "\nImmunité: None")
    elif owo == (d + " " + m) or owo == (m + " " + d):
        print("Faiblesses: Sol, Psy",
              "\nResistances: Electrik, Plante, Combat, Poison, Vol, Insecte, Acier, Fée", "\nImmunité: None")
    elif owo == (d + " " + n) or owo == (n + " " + d):
        print("Faiblesses: Sol, Spectre, Ténèbres", "\nResistances: Plante, Combat, Poison, Fée",
              "\nImmunité: None")
    elif owo == (d + " " + o) or owo == (o + " " + d):
        print("Faiblesses: Feu, Sol, Psy, Roche, Acier", "\nResistances: Plante, Glace, Poison, Insecte, Fée",
              "\nImmunité: None")
    elif owo == (d + " " + p) or owo == (p + " " + d):
        print("Faiblesses: Dragon, Sol, Glace, Psy",
              "\nResistances: Insecte, Electrik, Combat, Feu, Plante, Poison, Eau", "\nImmunité: None")
    elif owo == (d + " " + q) or owo == (q + " " + d):
        print("Faiblesses: Sol", "\nResistances: Ténèbres, Spectre, Plante, Poison", "\nImmunité: Psy")
    elif owo == (d + " " + r) or owo == (r + " " + d):
        print("Faiblesses: Sol, Psy, Acier", "\nResistances: Plante, Combat, Insecte, Ténèbres, Fée",
              "\nImmunité: Dragon")
    elif owo == (e + " " + f) or owo == (f + " " + e):
        print("Faiblesses: Combat, Plante, Sol, Glace, Acier, Eau",
              "\nResistances: Feu, Vol, Normal, Poison, Roche", "\nImmunité: Electrik")
    elif owo == (e + " " + g) or owo == (g + " " + e):
        print("Faiblesses: Feu, Vol, Glace, Eau", "\nResistances: Combat, Sol, Poison",
              "\nImmunité: Electrik")
    elif owo == (e + " " + h) or owo == (h + " " + e):
        print("Faiblesses: Ténèbres, Spectre, Plante, Glace, Eau", "\nResistances: Insecte, Poison, Roche",
              "\nImmunité: Electrik, Combat, Normal")
    elif owo == (e + " " + i) or owo == (i + " " + e):
        print("Faiblesses: Combat, Feu, Sol, Eau",
              "\nResistances: Insecte, Dragon, Fée, Vol, Normal, Psy, Roche, Acier",
              "\nImmunité: Electrik, Poison")
    elif owo == (e + " " + j) or owo == (j + " " + e):
        print("Faiblesses: Sol, Eau", "\nResistances: Insecte, Fée, Feu, Poison, Acier",
              "\nImmunité: Electrik")
    elif owo == (e + " " + k) or owo == (k + " " + e):
        print("Faiblesses: Plante", "\nResistances: Feu, Poison, Roche, Acier", "\nImmunité: Electrik")
    elif owo == (e + " " + l) or owo == (l + " " + e):
        print("Faiblesses: Insecte, Feu, Vol, Glace", "\nResistances: Sol, Roche", "\nImmunité: Electrik")
    elif owo == (e + " " + m) or owo == (m + " " + e):
        print("Faiblesses: Plante, Sol, Glace, Eau", "\nResistances: Vol, Poison, Roche, Acier",
              "\nImmunité: Electrik")
    elif owo == (e + " " + n) or owo == (n + " " + e):
        print("Faiblesses: Insecte, Ténèbres, Spectre, Plante, Glace, Eau", "\nResistances: Combat, Poison, Psy, Roche",
              "\nImmunité: Electrik")
    elif owo == (e + " " + o) or owo == (o + " " + e):
        print("Faiblesses: Combat, Feu, Plante, Acier, Eau", "\nResistances: Poison", "\nImmunité: Electrik")
    elif owo == (e + " " + p) or owo == (p + " " + e):
        print("Faiblesses: Dragon, Fée, Glace", "\nResistances: Feu, Poison, Roche", "\nImmunité: Electrik")
    elif owo == (e + " " + q) or owo == (q + " " + e):
        print("Faiblesses: Insecte, Fée, Combat, Plante, Glace, Eau", "\nResistances: Ténèbres, Spectre, Poison, Roche",
              "\nImmunité: Electrik, Psy")
    elif owo == (e + " " + r) or owo == (r + " " + e):
        print("Faiblesses: Eau, Plante, Glace, Acier", "\nResistances: Combat, Insecte, Roche, Ténèbres",
              "\nImmunité: Electrik, Dragon")
    elif owo == (f + " " + g) or owo == (g + " " + f):
        print("Faiblesses: Roche, Acier, Eau", "\nResistances: Normal, Poison", "\nImmunité: None")
    elif owo == (f + " " + h) or owo == (h + " " + f):
        print("Faiblesses: Eau, Plante, Sol, Spectre, Ténèbres, Acier", "\nResistances: Feu, Poison, Vol, Insecte",
              "\nImmunité: Normal, Combat")
    elif owo == (f + " " + i) or owo == (i + " " + f):
        print("Faiblesses: Combat, Sol, Eau",
              "\nResistances: Insecte, Dragon, Fée, Vol, Glace, Normal, Psy, Roche", "\nImmunité: Poison")
    elif owo == (f + " " + j) or owo == (j + " " + f):
        print("Faiblesses: Combat, Sol, Roche, Eau",
              "\nResistances: Insecte, Fée, Feu, Vol, Glace, Normal, Poison", "\nImmunité: None")
    elif owo == (f + " " + k) or owo == (k + " " + f):
        print("Faiblesses: Electrik, Combat, Plante, Sol", "\nResistances: Feu, Vol, Glace, Normal, Poison",
              "\nImmunité: None")
    elif owo == (f + " " + l) or owo == (l + " " + f):
        print("Faiblesses: Insecte, Combat, Glace, Acier", "\nResistances: Electrik, Normal", "\nImmunité: None")
    elif owo == (f + " " + m) or owo == (m + " " + f):
        print("Faiblesses: Combat, Plante, Sol, Eau", "\nResistances: Electrik, Feu, Vol, Normal, Poison",
              "\nImmunité: None")
    elif owo == (f + " " + n) or owo == (n + " " + f):
        print("Faiblesses: Insecte, Ténèbres, Spectre, Plante, Sol, Acier, Eau",
              "\nResistances: Feu, Vol, Normal, Poison, Psy", "\nImmunité: None")
    elif owo == (f + " " + o) or owo == (o + " " + f):
        print("Faiblesses: Combat, Plante, Sol, Roche, Acier, Eau",
              "\nResistances: Vol, Glace, Normal, Poison", "\nImmunité: None")
    elif owo == (f + " " + p) or owo == (p + " " + f):
        print("Faiblesses: Dragon, Fée, Combat, Sol, Glace, Acier",
              "\nResistances: Electrik, Feu, Vol, Normal, Poison", "\nImmunité: None")
    elif owo == (f + " " + q) or owo == (q + " " + f):
        print("Faiblesses: Insecte, Fée, Combat, Plante, Sol, Acier, Eau",
              "\nResistances: Ténèbres, Feu, Vol, Spectre, Normal, Poison", "\nImmunité: Psy")
    elif owo == (f + " " + r) or owo == (r + " " + f):
        print("Faiblesses: Plante, Sol, Acier, Eau", "\nResistances: Insecte, Ténèbres, Feu, Vol, Normal",
              "\nImmunité: Dragon")
    elif owo == (g + " " + h) or owo == (h + " " + g):
        print("Faiblesses: Ténèbres, Feu, Vol, Spectre, Roche", "\nResistances: Insecte, Plante, Sol, Poison",
              "\nImmunité: Combat, Normal")
    elif owo == (g + " " + i) or owo == (i + " " + g):
        print("Faiblesses: Feu", "\nResistances: Insecte, Dragon, Fée, Plante, Glace, Normal, Psy, Acier",
              "\nImmunité: Poison")
    elif owo == (g + " " + j) or owo == (j + " " + g):
        print("Faiblesses: Vol, Roche, Eau", "\nResistances: Insecte, Fée, Combat, Plante, Glace, Acier",
              "\nImmunité: None")
    elif owo == (g + " " + k) or owo == (k + " " + g):
        print("Faiblesses: Electrik, Vol, Roche", "\nResistances: Combat, Sol, Glace, Acier, Eau",
              "\nImmunité: None")
    elif owo == (g + " " + l) or owo == (l + " " + g):
        print("Faiblesses: Insecte, Feu, Vol, Glace, Poison, Roche",
              "\nResistances: Electrik, Combat, Plante, Sol, Eau", "\nImmunité: None")
    elif owo == (g + " " + m) or owo == (m + " " + g):
        print("Faiblesses: Feu, Roche", "\nResistances: Electrik, Combat, Plante, Acier", "\nImmunité: None")
    elif owo == (g + " " + n) or owo == (n + " " + g):
        print("Faiblesses: Feu, Vol, Insecte, Roche, Spectre, Ténèbres", "\nResistances: Plante, Combat, Sol, Psy",
              "\nImmunité: None")
    elif owo == (g + " " + o) or owo == (o + " " + g):
        print("Faiblesses: Feu, Vol, Roche, Acier", "\nResistances: Plante, Glace, Sol", "\nImmunité: None")
    elif owo == (g + " " + p) or owo == (p + " " + g):
        print("Faiblesses: Glace, Vol, Roche, Dragon, Fée", "\nResistances: Eau, Electrik, Combat, Sol",
              "\nImmunité: None")
    elif owo == (g + " " + q) or owo == (q + " " + g):
        print("Faiblesses: Feu, Vol, Insecte, Roche, Fée", "\nResistances: Plante, Sol, Spectre, Ténèbres",
              "\nImmunité: Psy")
    elif owo == (g + " " + r) or owo == (r + " " + g):
        print("Faiblesses: Feu, Vol, Poison, Roche, Acier", "\nResistances: Insecte, Ténèbres, Combat, Plante, Sol",
              "\nImmunité: Dragon")
    elif owo == (h + " " + i) or owo == (i + " " + h):
        print("Faiblesses: Ténèbres, Feu, Spectre, Sol",
              "\nResistances: Insecte, Dragon, Fée, Vol, Plante, Glace, Psy, Roche, Acier",
              "\nImmunité: Combat, Normal, Poison")
    elif owo == (h + " " + j) or owo == (j + " " + h):
        print("Faiblesses: Ténèbres, Spectre, Sol, Roche, Eau",
              "\nResistances: Insecte, Fée, Feu, Plante, Glace, Poison, Acier", "\nImmunité: Combat, Normal")
    elif owo == (h + " " + k) or owo == (k + " " + h):
        print("Faiblesses: Ténèbres, Electrik, Spectre, Plante",
              "\nResistances: Insecte, Feu, Glace, Poison, Acier, Eau",
              "\nImmunité: Combat, Normal")
    elif owo == (h + " " + l) or owo == (l + " " + h):
        print("Faiblesses: Ténèbres, Feu, Vol, Spectre, Glace", "\nResistances: Electrik, Plante, Sol, Eau",
              "\nImmunité: Combat, Normal")
    elif owo == (h + " " + m) or owo == (m + " " + h):
        print("Faiblesses: Ténèbres, Spectre, Sol", "\nResistances: Insecte, Electrik, Vol, Poison, Acier",
              "\nImmunité: Combat, Normal")
    elif owo == (h + " " + n) or owo == (n + " " + h):
        print("Faiblesses: Ténèbres, Spectre", "\nResistances: Poison, Psy", "\nImmunité: Combat, Normal")
    elif owo == (h + " " + o) or owo == (o + " " + h):
        print("Faiblesses: Ténèbres, Feu, Spectre, Roche, Acier", "\nResistances: Insecte, Glace, Poison",
              "\nImmunité: Combat, Normal")
    elif owo == (h + " " + p) or owo == (p + " " + h):
        print("Faiblesses: Ténèbres, Dragon, Fée, Spectre, Glace",
              "\nResistances: Insecte, Electrik, Feu, Plante, Poison, Eau", "\nImmunité: Combat, Normal")
    elif owo == (h + " " + q) or owo == (q + " " + h):
        print("Faiblesses: Fée", "\nResistances: Poison", "\nImmunité: Combat, Normal, Psy")
    elif owo == (h + " " + r) or owo == (r + " " + h):
        print("Faiblesses: Spectre, Acier", "\nResistances: Insecte", "\nImmunité: Dragon, Combat, Normal")
    elif owo == (i + " " + j) or owo == (j + " " + i):
        print("Faiblesses: Combat, Sol, Eau",
              "\nResistances: Insecte, Dragon, Fée, Vol, Plante, Glace, Normal, Psy, Acier",
              "\nImmunité: Poison")
    elif owo == (i + " " + k) or owo == (k + " " + i):
        print("Faiblesses: Electrik, Combat, Sol",
              "\nResistances: Insecte, Dragon, Fée, Vol, Glace, Normal, Psy, Roche, Acier, Eau",
              "\nImmunité: Poison")
    elif owo == (i + " " + l) or owo == (l + " " + i):
        print("Faiblesses: Combat, Feu",
              "\nResistances: Dragon, Electrik, Fée, Plante, Normal, Psy, Roche, Acier, Eau",
              "\nImmunité: Poison")
    elif owo == (i + " " + m) or owo == (m + " " + i):
        print("Faiblesses: Combat, Feu, Sol",
              "\nResistances: Insecte, Dragon, Electrik, Fée, Vol, Plante, Glace, Normal, Psy, Roche, Acier",
              "\nImmunité: Poison")
    elif owo == (i + " " + n) or owo == (n + " " + i):
        print("Faiblesses: Ténèbres, Feu, Spectre, Sol",
              "\nResistances: Dragon, Fée, Vol, Plante, Glace, Normal, Psy, Roche, Acier",
              "\nImmunité: Poison")
    elif owo == (i + " " + o) or owo == (o + " " + i):
        print("Faiblesses: Combat, Feu, Sol",
              "\nResistances: Insecte, Dragon, Fée, Vol, Plante, Glace, Normal, Psy", "\nImmunité: Poison")
    elif owo == (i + " " + p) or owo == (p + " " + i):
        print("Faiblesses: Combat, Sol",
              "\nResistances: Insecte, Electrik, Vol, Plante, Normal, Psy, Roche, Acier, Eau",
              "\nImmunité: Poison")
    elif owo == (i + " " + q) or owo == (q + " " + i):
        print("Faiblesses: Combat, Feu, Sol",
              "\nResistances: Ténèbres, Dragon, Vol, Spectre, Plante, Glace, Normal, Roche, Acier",
              "\nImmunité: Poison, Psy")
    elif owo == (i + " " + r) or owo == (r + " " + i):
        print("Faiblesses: Feu, Sol",
              "\nResistances: Insecte, Ténèbres, Fée, Vol, Plante, Glace, Normal, Psy, Rochel",
              "\nImmunité: Dragon, Poison")
    elif owo == (j + " " + k) or owo == (k + " " + j):
        print("Faiblesses: Electrik, Sol, Roche", "\nResistances: Insecte, Fée, Feu, Glace, Acier",
              "\nImmunité: None")
    elif owo == (j + " " + l) or owo == (l + " " + j):
        print("Faiblesses: Poison, Vol, Roche", "\nResistances: Electrik, Plante, Acier, Fée",
              "\nImmunité: None")
    elif owo == (j + " " + m) or owo == (m + " " + j):
        print("Faiblesses: Sol, Roche, Eau",
              "\nResistances: Insecte, Electrik, Fée, Feu, Vol, Plante, Glace, Acier", "\nImmunité: None")
    elif owo == (j + " " + n) or owo == (n + " " + j):
        print("Faiblesses: Ténèbres, Spectre, Sol, Roche, Eau",
              "\nResistances: Fée, Combat, Feu, Plante, Glace, Psy, Acier", "\nImmunité: None")
    elif owo == (j + " " + o) or owo == (o + " " + j):
        print("Faiblesses: Eau, Combat, Sol, Roche", "\nResistances: Plante, Glace, Insecte, Fée",
              "\nImmunité: None")
    elif owo == (j + " " + p) or owo == (p + " " + j):
        print("Faiblesses: Dragon, Sol, Roche", "\nResistances: Insecte, Electrik, Feu, Plante, Acier",
              "\nImmunité: None")
    elif owo == (j + " " + q) or owo == (q + " " + j):
        print("Faiblesses: Combat, Sol, Roche, Eau", "\nResistances: Ténèbres, Feu, Spectre, Plante, Glace, Acier",
              "\nImmunité: Psy")
    elif owo == (j + " " + r) or owo == (r + " " + j):
        print("Faiblesses: Eau, Poison, Sol, Roche",
              "\nResistances: Feu, Plante, Glace, Combat, Insecte, Ténèbres, Fée", "\nImmunité: Dragon")
    elif owo == (k + " " + l) or owo == (l + " " + k):
        print("Faiblesses: Insecte, Vol, Poison", "\nResistances: Sol, Acier, Eau", "\nImmunité: None")
    elif owo == (k + " " + m) or owo == (m + " " + k):
        print("Faiblesses: Plante, Sol", "\nResistances: Feu, Vol, Glace, Acier, Eau", "\nImmunité: None")
    elif owo == (k + " " + n) or owo == (n + " " + k):
        print("Faiblesses: Insecte, Ténèbres, Electrik, Spectre, Plante",
              "\nResistances: Combat, Feu, Glace, Psy, Acier, Eau", "\nImmunité: None")
    elif owo == (k + " " + o) or owo == (o + " " + k):
        print("Faiblesses: Electrik, Combat, Plante, Roche", "\nResistances: Glace, Eau", "\nImmunité: None")
    elif owo == (k + " " + p) or owo == (p + " " + k):
        print("Faiblesses: Dragon, Fée", "\nResistances: Feu, Acier, Eau", "\nImmunité: None")
    elif owo == (k + " " + q) or owo == (q + " " + k):
        print("Faiblesses: Insecte, Electrik, Fée, Combat, Plante",
              "\nResistances: Ténèbres, Feu, Spectre, Glace, Acier, Eau", "\nImmunité: Psy")
    elif owo == (k + " " + r) or owo == (r + " " + k):
        print("Faiblesses: Electrik, Plante, Poison", "\nResistances: Insecte, Ténèbres, Combat, Feu, Glace, Eau",
              "\nImmunité: Dragon")
    elif owo == (l + " " + m) or owo == (m + " " + l):
        print("Faiblesses: Insecte, Feu, Glace, Poison", "\nResistances: Electrik, Plante, Acier, Eau",
              "\nImmunité: None")
    elif owo == (l + " " + n) or owo == (n + " " + l):
        print("Faiblesses: Insecte, Ténèbres, Feu, Vol, Spectre, Glace, Poison",
              "\nResistances: Electrik, Combat, Plante, Sol, Psy, Eau", "\nImmunité: None")
    elif owo == (l + " " + o) or owo == (o + " " + l):
        print("Faiblesses: Insecte, Combat, Feu, Vol, Poison, Roche, Acier",
              "\nResistances: Electrik, Plante, Sol, Eau", "\nImmunité: None")
    elif owo == (l + " " + p) or owo == (p + " " + l):
        print("Faiblesses: Insecte, Dragon, Fée, Vol, Glace, Poison",
              "\nResistances: Electrik, Plante, Sol, Eau", "\nImmunité: None")
    elif owo == (l + " " + q) or owo == (q + " " + l):
        print("Faiblesses: Insecte, Fée, Combat, Feu, Vol, Glace, Poison",
              "\nResistances: Ténèbres, Electrik, Spectre, Plante, Sol, Eau", "\nImmunité: Psy")
    elif owo == (l + " " + r) or owo == (r + " " + l):
        print("Faiblesses: Feu, Vol, Glace, Poison, Acier",
              "\nResistances: Ténèbres, Electrik, Combat, Plante, Sol, Eau", "\nImmunité: Dragon")
    elif owo == (m + " " + n) or owo == (n + " " + m):
        print("Faiblesses: Insecte, Ténèbres, Spectre, Sol", "\nResistances: Electrik, Combat, Vol, Psy, Acier",
              "\nImmunité: None")
    elif owo == (m + " " + o) or owo == (o + " " + m):
        print("Faiblesses: Combat, Feu, Sol, Roche", "\nResistances: Electrik, Vol, Glace",
              "\nImmunité: None")
    elif owo == (m + " " + p) or owo == (p + " " + m):
        print("Faiblesses: Dragon, Fée, Sol, Glace",
              "\nResistances: Electrik, Feu, Vol, Plante, Acier, Eau", "\nImmunité: None")
    elif owo == (m + " " + q) or owo == (q + " " + m):
        print("Faiblesses: Combat, Sol, Insecte, Fée", "\nResistances: Electrik, Vol, Spectre, Ténèbres",
              "\nImmunité: Psy")
    elif owo == (m + " " + r) or owo == (r + " " + m):
        print("Faiblesses: Sol, Poison", "\nResistances: Insecte, Ténèbres, Electrik, Combat, Vol",
              "\nImmunité: Dragon")
    elif owo == (n + " " + o) or owo == (o + " " + n):
        print("Faiblesses: Insecte, Ténèbres, Feu, Spectre, Roche, Acier", "\nResistances: Glace, Psy",
              "\nImmunité: None")
    elif owo == (n + " " + p) or owo == (p + " " + n):
        print("Faiblesses: Insecte, Ténèbres, Dragon, Fée, Spectre, Glace",
              "\nResistances: Electrik, Combat, Feu, Plante, Psy, Eau", "\nImmunité: None")
    elif owo == (n + " " + q) or owo == (q + " " + n):
        print("Faiblesses: Insecte, Fée", "\nResistances: None", "\nImmunité: Psy")
    elif owo == (n + " " + r) or owo == (r + " " + n):
        print("Faiblesses: Spectre, Poison, Acier", "\nResistances: Combat, Psy", "\nImmunité: Dragon")
    elif owo == (o + " " + p) or owo == (p + " " + o):
        print("Faiblesses: Dragon, Fée, Combat, Roche, Acier", "\nResistances: Electrik, Plante, Eau",
              "\nImmunité: None")
    elif owo == (o + " " + q) or owo == (q + " " + o):
        print("Faiblesses: Insecte, Fée, Combat, Feu, Roche, Acier", "\nResistances: Ténèbres, Spectre, Glace",
              "\nImmunité: Psy")
    elif owo == (o + " " + r) or owo == (r + " " + o):
        print("Faiblesses: Feu, Poison, Roche, Acier", "\nResistances: Insecte, Ténèbres, Glace", "\nImmunité: Dragon")
    elif owo == (p + " " + q) or owo == (q + " " + p):
        print("Faiblesses: Insecte, Dragon, Fée, Combat, Glace",
              "\nResistances: Ténèbres, Electrik, Feu, Spectre, Plante, Eau", "\nImmunité: Psy")
    elif owo == (p + " " + r) or owo == (r + " " + p):
        print("Faiblesses: Fée, Glace, Poison, Acier",
              "\nResistances: Insecte, Ténèbres, Electrik, Combat, Feu, Plante, Eau", "\nImmunité: Dragon")
    elif owo == (q + " " + r) or owo == (r + " " + q):
        print("Faiblesses: Poison, Acier, Fée", "\nResistances: Spectre, Ténèbres", "\nImmunité: Psy, Dragon")
    elif owo == ("types"):
        print(types)
    elif owo == ("who"):
        print("Made by HappySylveon")


