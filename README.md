# TP JSON-LD (parties 1 et 2)

## Infos importants
- [L'adresse du repo Github utilisé](https://github.com/pchampin/sophia_rs)
- Le graphe RDF <b>est conforme</b> au modèle des shapes SHACL 

## Comment tester ?
### Télécharger les issues d'un répo Github
```
python3 import_github_trace.py pchampin/sophia_rs --out [filename].json
```

### Tester si le graphe RDF (obtenu à l'aide du context et les issues) conforme au graphe SHACL 
```
python3 main.py
```

## Dépendances
- Python3
- Pyld : `pip3 install pyld`
- RDFLib : `pip3 install rdflib`
- PySHACL : `pip3 install pyshacl`
- Requests : `pip3 install requests`
(Nécessaire uniquement pour importer la trace github)

## Travail de 
- Khaled ABDRABO p1713323 
- Jean BRIGNONE p1709655

Dynamique des connaissances M2IA - 2022