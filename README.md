# Gamayun Language Data Kits

There are more than 7,000 languages in the world, yet only a small proportion of them have language data presence in public. Translators without Borders’(TWB) Gamayun kits are a starting point for developing audio and text corpora for languages without pre-existing data resources. We create parallel data for a language by translating a pre-compiled set of general-domain sentences in English. If audio data is needed, these translated sentences are recorded by native speakers.

To scale corpus production, we offer four dataset versions:

- Mini-kit of 5,000 sentences (`kit5k`)
- Small-kit of 10,000 sentences (`kit10k`)
- Medium-kit of 15,000 sentences (`kit15k`)
- Large-kit of 30,000 sentences (`kit30k`)

Since each kit contains a unique set of sentences, it is possible to combine them to reach a maximum dataset size of 60,000 sentences. Recording these sentences result approximately in 75 hours of audio data.

## Source sentences (`core`)

Sentences in `core` directory are in English, French and Spanish and are sourced from the [Tatoeba repository](https://tatoeba.org). Sentence selection algorithm ensures representation of most frequently used words in the language. For more information, please refer to [corepus-gen repository](https://github.com/translatorswb/corepus-gen). `etc` directories contain sentence id's as used in the Tatoeba corpus. 

## Parallel corpora (`parallel`)

Translations of the kits are performed by professionals and volunteers of TWB's translator community. A complete list of translated sentences are:

| Language | Pair | # Segments | Source |
|------|--------|--------|--------|
| Hausa | English | 15,000 | Tatoeba |
| Kanuri | English | 5,000 | Tatoeba |
| Nande | French | 15,000 | Tatoeba |
| Rohingya | English | 5,000 | Tatoeba |
| Swahili (Coastal) | English | 5,000 | Tatoeba |
| Swahili (Congolese) | French | 25,302 | Tatoeba |

## Reference

More on [Gamayun, language equity initiative](https://translatorswithoutborders.org/gamayun/)

Gamayun kits are officially published in the [Gamayun portal](https://gamayun.translatorswb.org/data/). Conditions for use are described in `LICENSE.txt`. 

If you need to cite Gamayun kits: 

```
Alp Öktem, Muhannad Albayk Jaam, Eric DeLuca, Grace Tang
Gamayun –  Language Technology for Humanitarian Response
In: 2020 IEEE Global Humanitarian Technology Conference (GHTC)
2020 October 29 - November 1; Virtual.
Link: https://ieeexplore.ieee.org/document/9342939
```


