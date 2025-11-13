#!/usr/bin/env python3
"""
truth_hebrew.py - Analyse complète de mots hébreux
Affiche les conversions, propriétés mathématiques, hashs, etc.
"""

import math
import hashlib
import base64
import sys

# Alphabet hébreu complet
ALPHABET_HEBREU = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 11, 'ל': 12, 'מ': 13, 'נ': 14, 'ס': 15, 'ע': 16, 'פ': 17, 'צ': 18, 'ק': 19, 'ר': 20,
    'ש': 21, 'ת': 22,
    # Formes finales
    'ך': 11, 'ם': 13, 'ן': 14, 'ף': 17, 'ץ': 18
}

ALPHABET_INVERSE = {
    1: 'א', 2: 'ב', 3: 'ג', 4: 'ד', 5: 'ה', 6: 'ו', 7: 'ז', 8: 'ח', 9: 'ט', 10: 'י',
    11: 'כ', 12: 'ל', 13: 'מ', 14: 'נ', 15: 'ס', 16: 'ע', 17: 'פ', 18: 'צ', 19: 'ק', 20: 'ר',
    21: 'ש', 22: 'ת'
}

def encoder_mot_hebreu(mot):
    """Encode un mot hébreu en séquence numérique"""
    mot = mot.strip()
    resultat = []
    
    for lettre in mot:
        if lettre in ALPHABET_HEBREU:
            numero = ALPHABET_HEBREU[lettre]
            resultat.append(str(numero))
        elif lettre.isalpha():
            numero = ord(lettre.upper()) - ord('A') + 1
            resultat.append(str(numero))
    
    return '.'.join(resultat)

def decoder_sequence_hebreu(sequence):
    """Décode une séquence numérique en mot hébreu"""
    nombres = sequence.split('.')
    mot_decode = []
    
    for nombre in nombres:
        if nombre.isdigit():
            numero = int(nombre)
            if 1 <= numero <= 22:
                lettre = ALPHABET_INVERSE[numero]
                mot_decode.append(lettre)
            elif 1 <= numero <= 26:
                lettre = chr(numero + ord('A') - 1)
                mot_decode.append(lettre)
    
    return ''.join(mot_decode)

def mot_vers_nombre(mot):
    """Convertit un mot hébreu en nombre unique (somme des codes)"""
    mot = mot.strip()
    total = 0
    
    for lettre in mot:
        if lettre in ALPHABET_HEBREU:
            total += ALPHABET_HEBREU[lettre]
    
    return total

def analyser_mot_hebreu(mot):
    """Analyse complète d'un mot hébreu"""
    results = {}
    
    # Informations de base
    results['mot_original'] = mot
    results['longueur_mot'] = len(mot)
    
    # Encodage hébreu
    results['sequence_hebreu'] = encoder_mot_hebreu(mot)
    results['valeur_numerique'] = mot_vers_nombre(mot)
    
    # Décodage (pour vérification)
    results['mot_decode'] = decoder_sequence_hebreu(results['sequence_hebreu'])
    
    # Propriétés du texte
    results['est_palindrome'] = est_palindrome_hebreu(mot)
    results['nombre_lettres'] = compter_lettres_hebreu(mot)
    results['lettres_uniques'] = lettres_uniques_hebreu(mot)
    results['gematria'] = calculer_gematria(mot)
    
    # Analyse numérique basée sur la valeur totale
    nombre = results['valeur_numerique']
    results.update(analyser_nombre(nombre))
    
    return results

def analyser_nombre(nombre):
    """Analyse complète d'un nombre"""
    results = {}
    
    # Conversion de base
    results['decimal'] = nombre
    results['hexadecimal'] = hex(nombre)[2:].upper()
    results['binary'] = bin(nombre)[2:]
    results['octal'] = oct(nombre)[2:]
    
    # Propriétés mathématiques
    results['parity'] = "אי-זוגי (Odd)" if nombre % 2 else "זוגי (Even)"
    results['factors'] = factorize(nombre)
    results['prime_status'] = "ראשוני (Prime)" if is_prime(nombre) else "מרוכב (Composite)"
    results['digit_sum'] = sum(int(d) for d in str(nombre))
    results['digit_count'] = len(str(nombre))
    results['square'] = nombre ** 2
    results['cube'] = nombre ** 3
    if nombre >= 0:
        results['square_root'] = math.sqrt(nombre)
    else:
        results['square_root'] = float('nan')
    
    # Hash et cryptographie
    results['md5'] = hashlib.md5(str(nombre).encode()).hexdigest()
    results['sha256'] = hashlib.sha256(str(nombre).encode()).hexdigest()
    results['base64'] = base64.b64encode(str(nombre).encode()).decode()
    
    # Valeurs spéciales pour la culture hébraïque
    results['valeur_gematria'] = nombre
    results['signification_gematria'] = signification_gematria(nombre)
    
    return results

def est_palindrome_hebreu(mot):
    """Vérifie si le mot hébreu est un palindrome"""
    mot = mot.strip()
    mot_nettoye = ''.join(c for c in mot if c in ALPHABET_HEBREU)
    return mot_nettoye == mot_nettoye[::-1]

def compter_lettres_hebreu(mot):
    """Compte les lettres hébraïques dans le mot"""
    return sum(1 for lettre in mot if lettre in ALPHABET_HEBREU)

def lettres_uniques_hebreu(mot):
    """Retourne les lettres hébraïques uniques du mot"""
    lettres = [lettre for lettre in mot if lettre in ALPHABET_HEBREU]
    return ''.join(sorted(set(lettres), key=lambda x: ALPHABET_HEBREU[x]))

def calculer_gematria(mot):
    """Calcule la valeur Gematria complète"""
    mot = mot.strip()
    valeur_simple = mot_vers_nombre(mot)
    
    # Calcul additionnel pour Gematria (vous pouvez ajouter d'autres méthodes)
    return {
        'valeur_simple': valeur_simple,
        'valeur_miloui': valeur_simple,  # Version basique
        'description': f"Gematria: {valeur_simple}"
    }

def signification_gematria(nombre):
    """Retourne la signification Gematria du nombre"""
    significations = {
        1: "א - אחדות, אלוהים (Unité, Dieu)",
        2: "ב - ברכה, בית (Bénédiction, Maison)",
        3: "ג - גמול, גדולה (Récompense, Grandeur)",
        4: "ד - דעת, דלת (Connaissance, Porte)",
        5: "ה - הארה, חיים (Illumination, Vie)",
        6: "ו - וודאות, connection (Certitude, Connection)",
        7: "ז - זוהר, מזל (Brillance, Chance)",
        8: "ח - חיים, חסד (Vie, Grâce)",
        9: "ט - טוב, טהרה (Bonté, Pureté)",
        10: "י - יד, יסוד (Main, Fondation)",
        11: "כ - כוח, כבוד (Force, Honneur)",
        12: "ל - לימוד, לב (Étude, Cœur)",
        13: "מ - מים, מצוות (Eau, Commandements)",
        14: "נ - נשמה, נצח (Âme, Éternité)",
        15: "ס - סוד, סגולה (Secret, Vertu)",
        16: "ע - עין, עולם (Œil, Monde)",
        17: "פ - פה, פלא (Bouche, Merveille)",
        18: "צ - צדק, צמח (Justice, Plante)",
        19: "ק - קודש, קומה (Saint, Étage)",
        20: "ר - רוח, רחמים (Esprit, Miséricorde)",
        21: "ש - שלום, שמים (Paix, Cieux)",
        22: "ת - תורה, תשובה (Torah, Repentir)",
        26: "יהוה - Nom de Dieu",
        32: "32 chemins de la sagesse",
        42: "42 lettres du Nom Divin",
        72: "72 noms de Dieu"
    }
    
    return significations.get(nombre, "מספר כללי (Nombre général)")

def factorize(n):
    """Factorise un nombre"""
    if n < 2:
        return [n]
    
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    """Vérifie si un nombre est premier"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def afficher_table_hebreu():
    """Affiche la table de correspondance hébraïque"""
    print("\n" + "="*70)
    print("טבלת התאמות אלפבית עברי מלאה")
    print("Complete Hebrew Alphabet Correspondence Table")
    print("="*70)
    
    alphabet = list(ALPHABET_HEBREU.items())
    # Trier par valeur numérique (sans doublons pour les formes finales)
    alphabet_unique = []
    valeurs_vues = set()
    for lettre, valeur in alphabet:
        if valeur not in valeurs_vues:
            alphabet_unique.append((lettre, valeur))
            valeurs_vues.add(valeur)
    
    alphabet_unique.sort(key=lambda x: x[1])
    
    print("אלפבית בסיסי (Basic Alphabet):")
    for i in range(0, len(alphabet_unique), 5):
        ligne = alphabet_unique[i:i+5]
        for lettre, num in ligne:
            print(f"{lettre}={num:2d}", end="  ")
        print()
    
    print("\nצורות סופיות (Final Forms):")
    final_forms = [('ך', 11), ('ם', 13), ('ן', 14), ('ף', 17), ('ץ', 18)]
    for lettre, num in final_forms:
        print(f"{lettre}={num:2d}", end="  ")
    print()

def afficher_resultats(results):
    """Affiche les résultats de manière formatée"""
    print("="*80)
    print(f"ניתוח מלא של המילה העברית: '{results['mot_original']}'")
    print(f"COMPLETE ANALYSIS OF HEBREW WORD: '{results['mot_original']}'")
    print("="*80)
    
    print("\nמידע כללי (General Information)")
    print(f"    המילה המקורית : {results['mot_original']}")
    print(f"    אורך המילה : {results['longueur_mot']} תווים")
    print(f"    האם פלינדרום? : {'כן (Yes)' if results['est_palindrome'] else 'לא (No)'}")
    
    print("\nקידוד עברי (Hebrew Encoding)")
    print(f"    רצף מספרי : {results['sequence_hebreu']}")
    print(f"    מילה מפוענחת (לאימות) : {results['mot_decode']}")
    print(f"    ערך מספרי כולל : {results['valeur_numerique']}")
    
    print("\nגימטריה (Gematria)")
    print(f"    ערך גימטריה : {results['gematria']['valeur_simple']}")
    print(f"    משמעות : {results['signification_gematria']}")
    
    print("\nניתוח מספרי של הערך הכולל (Numeric Analysis)")
    print(f"    עשרוני : {results['decimal']}")
    print(f"    hexadecimal : {results['hexadecimal']}")
    print(f"    בינארי : {results['binary']}")
    print(f"    octal : {results['octal']}")
    
    print(f"\n    זוגיות : {results['parity']}")
    print(f"    גורמים : {', '.join(map(str, results['factors']))}")
    print(f"    ראשוני או מרוכב : {results['prime_status']}")
    print(f"    סכום ספרות : {results['digit_sum']}")
    
    print(f"\n    ריבוע : {results['square']}")
    print(f"    קובייה : {results['cube']}")
    if not math.isnan(results['square_root']):
        print(f"    שורש ריבועי : {results['square_root']:.4f}")
    
    print("\nהצפנה וחתימות (Encryption & Hashing)")
    print(f"    MD5 : {results['md5']}")
    print(f"    SHA-256 : {results['sha256']}")
    print(f"    Base64 : {results['base64']}")
    
    # Affichage détaillé de l'encodage
    print("\nפירוט קידוד אות-אות (Encoding Details Letter by Letter)")
    mot = results['mot_original']
    for i, lettre in enumerate(mot):
        if lettre in ALPHABET_HEBREU:
            code = ALPHABET_HEBREU[lettre]
            nom_lettre = nom_lettre_hebreu(lettre)
            print(f"    {i+1:2d}. {lettre} ({nom_lettre}) = {code:2d}")
        elif lettre.isalpha():
            code = ord(lettre.upper()) - ord('A') + 1
            print(f"    {i+1:2d}. {lettre} (לטיני/latin) = {code:2d}")

def nom_lettre_hebreu(lettre):
    """Retourne le nom de la lettre hébraïque"""
    noms = {
        'א': 'Aleph', 'ב': 'Bet', 'ג': 'Gimel', 'ד': 'Dalet', 'ה': 'He',
        'ו': 'Vav', 'ז': 'Zayin', 'ח': 'Chet', 'ט': 'Tet', 'י': 'Yod',
        'כ': 'Kaf', 'ל': 'Lamed', 'מ': 'Mem', 'נ': 'Nun', 'ס': 'Samech',
        'ע': 'Ayin', 'פ': 'Pe', 'צ': 'Tsadi', 'ק': 'Kof', 'ר': 'Resh',
        'ש': 'Shin', 'ת': 'Tav',
        'ך': 'Kaf Sofit', 'ם': 'Mem Sofit', 'ן': 'Nun Sofit', 
        'ף': 'Pe Sofit', 'ץ': 'Tsadi Sofit'
    }
    return noms.get(lettre, '?')

def main():
    if len(sys.argv) != 2:
        print("שימוש: python truth_hebrew.py <מילה_עברית>")
        print("Usage: python truth_hebrew.py <hebrew_word>")
        print("דוגמה: python truth_hebrew.py שלום")
        print("דוגמה: python truth_hebrew.py \"21.12.6.13\" (לפענוח)")
        sys.exit(1)
    
    entree = sys.argv[1].strip()
    
    try:
        # Vérifier si c'est une séquence numérique
        if '.' in entree and all(part.isdigit() for part in entree.split('.')):
            mot_decode = decoder_sequence_hebreu(entree)
            print(f"🔓 רצף מפוענח : {entree} → {mot_decode}")
            results = analyser_mot_hebreu(mot_decode)
        else:
            results = analyser_mot_hebreu(entree)
        
        afficher_resultats(results)
        afficher_table_hebreu()
        
    except Exception as e:
        print(f"❌ שגיאה (Error) : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
