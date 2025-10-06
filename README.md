# 🍽️ Sistema di Gestione Elementi (SGE) – Python

## Titolo

**Sistema di Gestione Elementi per Food Management: applicazione Python per il monitoraggio di prodotti alimentari**

---

## Sommario Esecutivo

Progetto Python sviluppato per un'azienda fittizia del settore alimentare che richiede un sistema di gestione elementi (SGE) per i propri utenti. L'applicazione permette di gestire una collezione di prodotti alimentari attraverso un'interfaccia a menu interattivo con funzionalità di registrazione, ricerca avanzata e analisi statistica.

**Caratteristiche principali:**
- Gestione completa inventario con validazione input
- Ricerca semplice o con criteri multipli simultanei
- Statistiche automatiche su prodotti, categorie e prezzi
- Gestione date di scadenza con controlli di validità

---

## Problema Aziendale

L'azienda fittizia necessita di uno strumento per gestire efficacemente l'inventario di prodotti alimentari. Obiettivi principali:

- Registrare dettagli completi dei prodotti (nome, categoria, prezzo, quantità, scadenza, condizione)
- Monitorare prodotti scaduti o in scadenza
- Ottenere statistiche rapide su categorie, prezzi e quantità
- Ricercare prodotti tramite filtri singoli o combinati
- Identificare trend e ottimizzare le risorse

---

## Metodologia

### Architettura

Sistema modulare basato su lista di dizionari Python con funzioni specializzate per ogni operazione e menu interattivo per la navigazione.

### Funzionalità Principali

**1. Registrazione Elementi**
- Input guidato con validazione tipo dati (float per prezzi, int per quantità)
- Gestione date di scadenza formato GG-MM-AAAA con controlli logici
- Inserimento multiplo sequenziale

**2. Visualizzazione Elementi**
- Stampa formattata di tutti i prodotti con dettagli completi

**3. Ricerca Avanzata**
- Ricerca semplice su singolo attributo
- Ricerca multipla con criteri combinati (AND logico)
- Validazione automatica e conversione tipo dati

**4. Statistiche**
- Conteggio totale e distribuzione per categoria
- Categoria più frequente e prodotto con maggiore quantità
- Statistiche prezzi: massimo, minimo, medio

**5. Eliminazione**
- Rimozione prodotti per nome (case-insensitive)

### Tecniche Python

- Strutture dati: liste, dizionari, tuple
- List comprehension per filtraggio efficiente
- Gestione eccezioni try/except
- Validazione input con controlli formato e range
- Funzioni aggregate (max, min, sum) per statistiche

---

##Competenze

**Python:**
- Strutture dati complesse e modularizzazione codice
- List comprehension e gestione eccezioni
- F-strings e validazione tipo dati
- Algoritmi di ricerca e filtraggio

**Analisi Dati:**
- Calcoli statistici aggregati
- Comparazione multi-criterio
- Iterazione su strutture complesse

**User Experience:**
- Menu interattivo intuitivo
- Messaggi di errore descrittivi
- Validazione robusta degli input

---

## Risultati e Raccomandazioni

### Risultati

**Sistema Funzionale:**
- Applicazione completa con tutte le funzionalità richieste
- Interfaccia intuitiva con menu numerato
- Zero dipendenze esterne (solo libreria standard Python)

**Robustezza:**
- Validazione completa input previene errori runtime
- Gestione casi limite (liste vuote, attributi mancanti)
- Ricerca multipla permette query complesse

**Performance:**
- Operazioni istantanee anche con centinaia di elementi
- Ricerche efficienti tramite list comprehension

### Impatto

- **Riduzione sprechi**: monitoraggio scadenze previene perdite
- **Efficienza**: ricerca rapida riduce tempi di gestione
- **Decisioni informate**: statistiche supportano pianificazione acquisti

---

## 📂 Struttura Codice

```python
├── elementi = []                    # Lista principale
├── inserimento_elementi()           # Registrazione
├── visualizza_elementi()            # Visualizzazione
├── ricerca_elementi()               # Ricerca semplice/multipla
├── statistiche_elementi()           # Analytics
├── elimina_elemento()               # Rimozione
└── menu()                           # Interfaccia
```

---

## Utilizzo

1. Eseguire: `python gestione_elementi.py`
2. Selezionare operazione dal menu (1-6)
3. Seguire istruzioni a schermo

**Esempio:**
```
Aggiungi "Latte" → Categoria "Latticini", 2.50€, 10 unità
Visualizza → Vedi inventario completo
Statistiche → Totale prodotti, categoria più frequente, prezzo medio
Ricerca → Trova categoria "Latticini" con prezzo < 3€
```
