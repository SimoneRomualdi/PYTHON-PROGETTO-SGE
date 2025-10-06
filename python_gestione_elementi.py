# Struttura dati per conservare gli elementi
elementi = []

# Funzione per inserimento elementi
def inserimento_elementi():
    while True:
        nome = input('Inserisci nome: ')
        categoria = input('Inserisci categoria: ')

        # Controllo dell'input corretto del prezzo e quantità
        while True:
            try:
                prezzo = float(input('Inserisci prezzo: '))
                break
            except ValueError:
                print('Errore: Inserisci un numero valido: ')

        while True:
            try:
                quantità = int(input('Inserisci quantità: '))
                break
            except ValueError:
                print('Errore: Inserisci un numero valido per la quantità: ')

        condizione = input('Qual è la condizione? (scaduto, difetti estetici ecc..): ')

        scadenza = None
        anno_corrente = 2025

        if 'scaduto' in condizione.lower():
            while True:
                scadenza = input('Quando scade il prodotto? (Formato GG-MM-AAAA): ')

                if len(scadenza) == 10 and scadenza[2] == '-' and scadenza[5] == '-' and scadenza.replace('-', '').isdigit():
                    giorno, mese, anno = map(int, scadenza.split('-'))

                    if 1 <= giorno <= 31 and 1 <= mese <= 12 and anno <= anno_corrente:
                        break
                    else:
                        print('Errore! La data deve essere nel passato o oggi.')
                else:
                    while True:
                        scadenza = input('Il prodotto non è scaduto, quando scade? (Formato GG-MM-AAAA, lascia vuoto se non applicabile): ').strip()

                        if scadenza == '':
                            scadenza = None
                            break

                        if len(scadenza) == 10 and scadenza[2] == '-' and scadenza[5] == '-' and scadenza.replace('-', '').isdigit():
                            giorno, mese, anno = map(int, scadenza.split('-'))

                            if 1 <= giorno <= 31 and 1 <= mese <= 12 and anno >= anno_corrente:
                                break
                            else:
                                print('Errore! Inserisci una data futura valida.')
                        else:
                            print('Errore! Inserisci la data nel formato corretto.')
                    break

        # Creazione dizionario elementi
        cibo = {
            'nome': nome,
            'categoria': categoria,
            'prezzo': prezzo,
            'quantità': quantità,
            'scadenza': scadenza,
            'condizione': condizione
        }

        elementi.append(cibo)
        print(f'{nome} aggiunto correttamente')

        elemento_aggiuntivo = input('Vuoi aggiungere un altro elemento? (si/no): ').strip().lower()
        if elemento_aggiuntivo not in ['si', 'sì']:
            break

# Funzione per visualizzazione elementi
def visualizza_elementi():
    if len(elementi) == 0:
        print('Non ci sono elementi registrati')
    else:
        for cibo in elementi:
            print('\nDettagli cibo')
            print(f"Nome: {cibo['nome']}")
            print(f"Categoria: {cibo['categoria']}")
            print(f"Prezzo: {cibo['prezzo']}")
            print(f"Quantità: {cibo['quantità']}")
            print(f"Scadenza: {cibo['scadenza']}")
            print(f"Condizione: {cibo['condizione']}")

# Funzione ricerca elementi
def ricerca_elementi():
    attributi_validi = ['nome', 'categoria', 'prezzo', 'quantità', 'scadenza', 'condizione']

    scelta = input('Vuoi fare una ricerca con uno o più attributi? (uno/multipli): ').lower()

    if scelta == 'uno':
        attributo = input("Inserisci l'attributo per la ricerca (nome/categoria/prezzo/quantità/scadenza/condizione): ").lower()
        valore = input(f"Inserisci il valore per l'attributo {attributo}: ")

        if attributo not in attributi_validi:
            print('Errore! Attributo non presente')
            return

        if attributo in ['prezzo', 'quantità']:
            try:
                if attributo == 'prezzo':
                    valore = float(valore)
                else:
                    valore = int(valore)
            except ValueError:
                print(f'Errore! {attributo} deve essere un numero valido (int/float).')
                return

        risultati = [cibo for cibo in elementi if cibo.get(attributo) == valore]

    elif scelta == 'multipli':
        criteri = []
        risultati = []

        while True:
            attributo = input('Inserisci un attributo per la ricerca (nome/categoria/prezzo/quantità/scadenza/condizione): ').lower()
            valore = input(f"Inserisci un valore per l'attributo {attributo}: ")

            if attributo not in attributi_validi:
                print('Errore, attributo non presente')
                continue

            if attributo in ['prezzo', 'quantità']:
                try:
                    if attributo == 'prezzo':
                        valore = float(valore)
                    else:
                        valore = int(valore)
                except ValueError:
                    print(f'Errore! {attributo} deve essere un numero valido (int/float).')
                    continue

            criteri.append((attributo, valore))

            altro = input('Vuoi aggiungere un altro valore di ricerca? (si/no): ').lower()
            if altro != 'si':
                break

        for cibo in elementi:
            corrisponde = True
            for attributo, valore in criteri:
                if cibo[attributo] != valore:
                    corrisponde = False
                    break

            if corrisponde:
                risultati.append(cibo)

    else:
        print('Scelta non valida. Riprova')
        return

    if risultati:
        print('\nElementi trovati:')
        for cibo in risultati:
            print(f"\nNome: {cibo['nome']}")
            print(f"Categoria: {cibo['categoria']}")
            print(f"Prezzo: {cibo['prezzo']}")
            print(f"Quantità: {cibo['quantità']}")
            print(f"Scadenza: {cibo['scadenza']}")
            print(f"Condizione: {cibo['condizione']}")
    else:
        print('Nessun elemento trovato.')


def statistiche_elementi():
    if not elementi:
        print('Nessun elemento registrato')
        return

    totale_elementi = len(elementi)
    print(f'Il totale degli elementi registrati è {totale_elementi}')

    conta_categorie = {}

    for elemento in elementi:
        categoria = elemento.get('categoria', 'sconosciuta')
        conta_categorie[categoria] = conta_categorie.get(categoria, 0) + 1

    print('\nDistribuzione per categoria: ')
    for categoria, conteggio in conta_categorie.items():
        print(f'{categoria}, {conteggio}')

    categoria_piu_frequente = max(conta_categorie, key=conta_categorie.get)
    print(f'\nCategoria più frequente: {categoria_piu_frequente}, {conta_categorie[categoria_piu_frequente]} elementi')

    def max_quantita(elemento):
        return elemento['quantità']

    cibo_piu_presente = max(elementi, key=max_quantita)
    print(f'\nIl cibo più presente è: {cibo_piu_presente["nome"]}, {cibo_piu_presente["quantità"]}')

    prezzi = [e['prezzo'] for e in elementi]

    prezzo_massimo = max(prezzi)
    prezzo_minimo = min(prezzi)
    prezzo_medio = sum(prezzi) / len(prezzi)

    print('\nStatistiche sui prezzi:')
    print(f'Il prezzo massimo è {prezzo_massimo:.2f}')
    print(f'Il prezzo minimo è {prezzo_minimo:.2f}')
    print(f'Il prezzo medio è {prezzo_medio:.2f}')

def elimina_elemento():
    nome = input('Inserisci il nome dell\'elemento da eliminare: ')
    elementi[:] = [e for e in elementi if e['nome'].lower() != nome.lower()]
    print(f"Elemento '{nome}' eliminato con successo.")

def menu():
    while True:
        print("\n--- Sistema di Gestione Elementi ---")
        print("1. Aggiungi elemento")
        print("2. Visualizza elementi")
        print("3. Ricerca elemento")
        print("4. Statistiche elementi")
        print("5. Elimina elemento")
        print("6. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            inserimento_elementi()
        elif scelta == "2":
            visualizza_elementi()
        elif scelta == "3":
            ricerca_elementi()
        elif scelta == "4":
            statistiche_elementi()
        elif scelta == "5":
            elimina_elemento()
        elif scelta == "6":
            print("Uscita dal sistema.")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == '__main__':
    menu()
