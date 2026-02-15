#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analiza możliwości odchudzenia konstrukcji domku nad morzem
"""

# ============================================================================
# OBECNA KONSTRUKCJA - MASA BAZOWA
# ============================================================================

print("=" * 80)
print("ANALIZA MOŻLIWOŚCI ODCHUDZENIA KONSTRUKCJI DOMKU NAD MORZEM")
print("=" * 80)
print()

# Powierzchnie
powierzchnia_zabudowy = 28.0  # m²
powierzchnia_scian = 2 * (3.5 * 4.65) + 2 * (8.0 * 4.65) - 10.0  # m² (odjęte okna/drzwi)
powierzchnia_dachu = 28.0  # m²
powierzchnia_stropu_antresoli = 9.0  # m²
powierzchnia_podlogi = 28.0  # m²

print("POWIERZCHNIE:")
print(f"  Powierzchnia zabudowy: {powierzchnia_zabudowy} m²")
print(f"  Powierzchnia ścian: {powierzchnia_scian:.1f} m²")
print(f"  Powierzchnia dachu: {powierzchnia_dachu} m²")
print(f"  Powierzchnia stropu antresoli: {powierzchnia_stropu_antresoli} m²")
print(f"  Powierzchnia podłogi: {powierzchnia_podlogi} m²")
print()

# ============================================================================
# WARIANT BAZOWY - OSB
# ============================================================================

print("=" * 80)
print("WARIANT BAZOWY (obecny projekt)")
print("=" * 80)
print()

# OSB - gęstość 650 kg/m³, grubość 18 mm
gestosc_osb = 650  # kg/m³
grubosc_osb = 0.018  # m
masa_osb_m2 = gestosc_osb * grubosc_osb  # kg/m²

print(f"OSB 18 mm - masa jednostkowa: {masa_osb_m2:.1f} kg/m²")
print()

# Ściany - 2 warstwy OSB (zewnętrzna i wewnętrzna)
masa_osb_sciany = powierzchnia_scian * masa_osb_m2 * 2
print(f"  Ściany (2 warstwy): {powierzchnia_scian:.1f} m² × {masa_osb_m2:.1f} kg/m² × 2 = {masa_osb_sciany:.1f} kg")

# Dach - 2 warstwy OSB po 20 mm (razem 40 mm)
grubosc_osb_dach = 0.020  # m
masa_osb_dach_m2 = gestosc_osb * grubosc_osb_dach
masa_osb_dach = powierzchnia_dachu * masa_osb_dach_m2 * 2
print(f"  Dach (2×20 mm): {powierzchnia_dachu} m² × {masa_osb_dach_m2:.1f} kg/m² × 2 = {masa_osb_dach:.1f} kg")

# Strop antresoli - 1 warstwa OSB 18 mm
masa_osb_strop = powierzchnia_stropu_antresoli * masa_osb_m2
print(f"  Strop antresoli (1 warstwa): {powierzchnia_stropu_antresoli} m² × {masa_osb_m2:.1f} kg/m² = {masa_osb_strop:.1f} kg")

# Podłoga - 1 warstwa OSB 18 mm
masa_osb_podloga = powierzchnia_podlogi * masa_osb_m2
print(f"  Podłoga (1 warstwa): {powierzchnia_podlogi} m² × {masa_osb_m2:.1f} kg/m² = {masa_osb_podloga:.1f} kg")

masa_osb_total = masa_osb_sciany + masa_osb_dach + masa_osb_strop + masa_osb_podloga
print()
print(f"SUMA OSB: {masa_osb_total:.1f} kg")
print()

# ============================================================================
# WARIANT 1 - KROKWIE + DESKI (zamiast OSB na dachu i ścianach)
# ============================================================================

print("=" * 80)
print("WARIANT 1 - KROKWIE + DESKI (lżejsza konstrukcja)")
print("=" * 80)
print()

# Deski sosnowe - gęstość 500 kg/m³, grubość 25 mm
gestosc_deski = 500  # kg/m³
grubosc_deski = 0.025  # m
masa_deski_m2 = gestosc_deski * grubosc_deski  # kg/m²

print(f"Deski sosnowe 25 mm - masa jednostkowa: {masa_deski_m2:.1f} kg/m²")
print()

# ŚCIANY - deski zamiast OSB (tylko 1 warstwa wewnętrzna, zewnętrzna blacha bezpośrednio na słupach)
masa_deski_sciany = powierzchnia_scian * masa_deski_m2 * 1  # tylko wewnętrzna
print(f"  Ściany (1 warstwa desek wewn.): {powierzchnia_scian:.1f} m² × {masa_deski_m2:.1f} kg/m² = {masa_deski_sciany:.1f} kg")

# DACH - krokwie drewniane zamiast 2×OSB
# Krokwie 50×150 mm co 60 cm, długość 8 m
liczba_krokwi = int(3.5 / 0.6) + 1  # co 60 cm
dlugosc_krokwi = 8.0  # m
przekroj_krokwi = 0.05 * 0.15  # m²
objetosc_krokwi = liczba_krokwi * dlugosc_krokwi * przekroj_krokwi  # m³
masa_krokwi = objetosc_krokwi * gestosc_deski  # kg

# Deski na krokwie 25 mm (zamiast OSB)
masa_deski_dach = powierzchnia_dachu * masa_deski_m2

masa_dach_total = masa_krokwi + masa_deski_dach
print(f"  Dach - krokwie 50×150: {liczba_krokwi} szt. × {dlugosc_krokwi} m × {przekroj_krokwi:.4f} m² × {gestosc_deski} kg/m³ = {masa_krokwi:.1f} kg")
print(f"  Dach - deski 25 mm: {powierzchnia_dachu} m² × {masa_deski_m2:.1f} kg/m² = {masa_deski_dach:.1f} kg")
print(f"  Dach RAZEM: {masa_dach_total:.1f} kg")

# STROP ANTRESOLI - belki stalowe + deski (zamiast OSB)
masa_deski_strop = powierzchnia_stropu_antresoli * masa_deski_m2
print(f"  Strop antresoli (deski 25 mm): {powierzchnia_stropu_antresoli} m² × {masa_deski_m2:.1f} kg/m² = {masa_deski_strop:.1f} kg")

# PODŁOGA - pozostaje OSB (potrzebna sztywność)
masa_osb_podloga_v1 = masa_osb_podloga
print(f"  Podłoga (OSB 18 mm - bez zmian): {masa_osb_podloga_v1:.1f} kg")

masa_total_v1 = masa_deski_sciany + masa_dach_total + masa_deski_strop + masa_osb_podloga_v1
print()
print(f"SUMA WARIANT 1: {masa_total_v1:.1f} kg")
print()

oszczednosc_v1 = masa_osb_total - masa_total_v1
procent_v1 = (oszczednosc_v1 / masa_osb_total) * 100
print(f"OSZCZĘDNOŚĆ: {oszczednosc_v1:.1f} kg ({procent_v1:.1f}%)")
print()

# ============================================================================
# WARIANT 2 - MAKSYMALNE ODCHUDZENIE (sklejka zamiast OSB + krokwie)
# ============================================================================

print("=" * 80)
print("WARIANT 2 - MAKSYMALNE ODCHUDZENIE (sklejka + krokwie)")
print("=" * 80)
print()

# Sklejka wodoodporna - gęstość 550 kg/m³, grubość 12 mm
gestosc_sklejka = 550  # kg/m³
grubosc_sklejka = 0.012  # m
masa_sklejka_m2 = gestosc_sklejka * grubosc_sklejka  # kg/m²

print(f"Sklejka wodoodporna 12 mm - masa jednostkowa: {masa_sklejka_m2:.1f} kg/m²")
print()

# ŚCIANY - deski wewnętrzne (bez zmian)
masa_deski_sciany_v2 = masa_deski_sciany
print(f"  Ściany (deski 25 mm wewn.): {masa_deski_sciany_v2:.1f} kg")

# DACH - krokwie + sklejka (zamiast desek)
masa_sklejka_dach = powierzchnia_dachu * masa_sklejka_m2
masa_dach_total_v2 = masa_krokwi + masa_sklejka_dach
print(f"  Dach - krokwie 50×150: {masa_krokwi:.1f} kg")
print(f"  Dach - sklejka 12 mm: {powierzchnia_dachu} m² × {masa_sklejka_m2:.1f} kg/m² = {masa_sklejka_dach:.1f} kg")
print(f"  Dach RAZEM: {masa_dach_total_v2:.1f} kg")

# STROP ANTRESOLI - sklejka 12 mm
masa_sklejka_strop = powierzchnia_stropu_antresoli * masa_sklejka_m2
print(f"  Strop antresoli (sklejka 12 mm): {powierzchnia_stropu_antresoli} m² × {masa_sklejka_m2:.1f} kg/m² = {masa_sklejka_strop:.1f} kg")

# PODŁOGA - sklejka 18 mm (cieńsza niż OSB, ale wystarczająca)
grubosc_sklejka_podloga = 0.018  # m
masa_sklejka_podloga_m2 = gestosc_sklejka * grubosc_sklejka_podloga
masa_sklejka_podloga = powierzchnia_podlogi * masa_sklejka_podloga_m2
print(f"  Podłoga (sklejka 18 mm): {powierzchnia_podlogi} m² × {masa_sklejka_podloga_m2:.1f} kg/m² = {masa_sklejka_podloga:.1f} kg")

masa_total_v2 = masa_deski_sciany_v2 + masa_dach_total_v2 + masa_sklejka_strop + masa_sklejka_podloga
print()
print(f"SUMA WARIANT 2: {masa_total_v2:.1f} kg")
print()

oszczednosc_v2 = masa_osb_total - masa_total_v2
procent_v2 = (oszczednosc_v2 / masa_osb_total) * 100
print(f"OSZCZĘDNOŚĆ: {oszczednosc_v2:.1f} kg ({procent_v2:.1f}%)")
print()

# ============================================================================
# PODSUMOWANIE
# ============================================================================

print("=" * 80)
print("PODSUMOWANIE PORÓWNAWCZE")
print("=" * 80)
print()

print(f"{'Wariant':<30} {'Masa [kg]':<15} {'Oszczędność [kg]':<20} {'Oszczędność [%]':<15}")
print("-" * 80)
print(f"{'BAZOWY (OSB)':<30} {masa_osb_total:<15.1f} {'-':<20} {'-':<15}")
print(f"{'WARIANT 1 (krokwie+deski)':<30} {masa_total_v1:<15.1f} {oszczednosc_v1:<20.1f} {procent_v1:<15.1f}")
print(f"{'WARIANT 2 (krokwie+sklejka)':<30} {masa_total_v2:<15.1f} {oszczednosc_v2:<20.1f} {procent_v2:<15.1f}")
print()

# ============================================================================
# DODATKOWE MOŻLIWOŚCI ODCHUDZENIA
# ============================================================================

print("=" * 80)
print("DODATKOWE MOŻLIWOŚCI ODCHUDZENIA")
print("=" * 80)
print()

print("1. KONSTRUKCJA STALOWA - profil 80×80 mm zamiast 100×100 mm")
print("   Oszczędność: ok. 500-600 kg (wymaga przeliczenia nośności)")
print()

print("2. IZOLACJA - wełna mineralna 8 cm zamiast 10 cm")
masa_welna_bazowa = 554.4  # kg (z poprzednich obliczeń)
oszczednosc_welna = masa_welna_bazowa * 0.2  # 20% mniej
print(f"   Oszczędność: ok. {oszczednosc_welna:.1f} kg")
print()

print("3. WYKOŃCZENIE - płyty GK zamiast desek boazeryjnych")
masa_boazeria_bazowa = 1287.8  # kg
masa_gk_m2 = 8.0  # kg/m² (płyta GK 12.5 mm)
powierzchnia_wewnetrzna = powierzchnia_scian + powierzchnia_dachu  # przybliżenie
masa_gk = powierzchnia_wewnetrzna * masa_gk_m2
oszczednosc_wykończenie = masa_boazeria_bazowa - masa_gk
print(f"   Oszczędność: ok. {oszczednosc_wykończenie:.1f} kg")
print()

print("4. BLACHA ELEWACYJNA - 0.5 mm zamiast 0.7 mm")
masa_blacha_bazowa = 391.6  # kg
oszczednosc_blacha = masa_blacha_bazowa * 0.28  # 28% mniej (0.5/0.7)
print(f"   Oszczędność: ok. {oszczednosc_blacha:.1f} kg")
print()

# ============================================================================
# CAŁKOWITA MOŻLIWA OSZCZĘDNOŚĆ
# ============================================================================

print("=" * 80)
print("CAŁKOWITA MOŻLIWA OSZCZĘDNOŚĆ MASY")
print("=" * 80)
print()

masa_bazowa_total = 7291.8  # kg (z poprzednich obliczeń)

oszczednosc_max = oszczednosc_v2 + oszczednosc_welna + oszczednosc_wykończenie + oszczednosc_blacha
masa_min = masa_bazowa_total - oszczednosc_max
procent_max = (oszczednosc_max / masa_bazowa_total) * 100

print(f"Masa bazowa budynku: {masa_bazowa_total:.1f} kg")
print()
print(f"Możliwa oszczędność:")
print(f"  - Wariant 2 (krokwie+sklejka): {oszczednosc_v2:.1f} kg")
print(f"  - Izolacja 8 cm: {oszczednosc_welna:.1f} kg")
print(f"  - Płyty GK zamiast boazerii: {oszczednosc_wykończenie:.1f} kg")
print(f"  - Blacha 0.5 mm: {oszczednosc_blacha:.1f} kg")
print()
print(f"SUMA OSZCZĘDNOŚCI: {oszczednosc_max:.1f} kg ({procent_max:.1f}%)")
print(f"MASA MINIMALNA: {masa_min:.1f} kg")
print()

print("=" * 80)
print("KONIEC ANALIZY")
print("=" * 80)
