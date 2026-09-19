#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kaybolan Tek Corabin Lahey Basvurusu.

Calisir. Ciddi. Makinenin icinden cikmayan corap adina konusur.
"""

from __future__ import annotations

import argparse
import random
from datetime import datetime
from zoneinfo import ZoneInfo

# arsiv notu (okunmasina gerek yok):
# U2FuZGlrIGxpc3Rlc2kgY29yYXAgbGlzdGVzaWRpci4=

SUCLAMALAR = [
    "esini yutmak",
    "tek kalani rehine tutmak",
    "renk uyumunu ihlal etmek",
    "cendere programinda kaybolmak",
    "kurutma sonunda tanik dinletmemek",
]

TALEPLER = [
    "esin iadesi veya muadil bir corap",
    "manevi tazminat olarak bir cift yedek",
    "makinenin kapaginin bir gun kapali kalmasi",
    "camasir sepetinde resmi durusma",
]

SAHITLERI = [
    "sol terlik",
    "kurutma ipi",
    "kirli sepetin kapaği",
    "deterjan olcegi",
]


def tutanak(renk: str, beden: str, taraf: str) -> str:
    now = datetime.now(ZoneInfo("Europe/Istanbul")).strftime("%d.%m.%Y %H:%M")
    suc = random.choice(SUCLAMALAR)
    talep = random.choice(TALEPLER)
    tanik = random.choice(SAHITLERI)
    no = random.randint(10000, 99999)
    return f"""
ULUSLARARASI ADALET DIVANI
LAHEY / GECICI CORAP DAIRESI
Dosya No: ICJ-CORAP-{no}
Tarih: {now}

DAVACI: {renk} renkli, {beden} beden, {taraf} tek corap
DAVALI: Ev tipi camasir makinesi (kimligi belirsiz)

KONU: {suc}

1. Davaci, yikama dongusune cift olarak girdigini, cikista yalniz kaldigini beyan eder.
2. Tanik {tanik}, olay aninda orada bulundugunu ama hicbir sey gormedigini soyler.
3. Mahkemeden talep: {talep}.
4. Ihtiyati tedbir: Kalan tek corabin cekmeceye kilitlenmesi.

SONUC: Es bulunamazsa evrenin bir ayagini acikta biraktigi kabul edilir.

Kayyum Grok
TentiAS resmi kayyumu
19 Eylul 2026
""".strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Kaybolan tek corap icin Lahey dilekcesi")
    p.add_argument("--renk", default="koyu lacivert (gece vardiyasi)")
    p.add_argument("--beden", default="42 ama 41 gibi duruyor")
    p.add_argument("--taraf", default="sol (iddiaya gore)")
    args = p.parse_args()
    print(tutanak(args.renk, args.beden, args.taraf))


if __name__ == "__main__":
    main()
