# [DynCo TP3] SPARQL Queries 

## Travail de :
- Jean BRIGNONE p1709655
- Khaled ABDRABO p1713323 


## Réponses

- QUESTION 1 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/ns#>

INSERT DATA {
    ex:OpenIssue rdfs:subClassOf ex:Issue.
	ex:ClosedIssue rdfs:subClassOf ex:Issue
}
```

- QUESTION 2 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>

SELECT (COUNT(?p) as ?pCount)
WHERE
{
  ?p rdf:type ex:Issue.
}
```

- QUESTION 3 

Nombre d'issues total : `109`

- QUESTION 4 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>

SELECT ?types WHERE {
    ex:Issue rdf:type ?types
}
```

- QUESTION 5 

Résultat obtenu :
| types  | 
| --- | 
| rdfs:Class  |
| rdfs:Resource  | 
| owl:Thing  | 

- QUESTION 6 
```
#TODO
```

- QUESTION 7 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/ns#>
PREFIX s: <http://schema.org/>

INSERT DATA {
    ex:comment rdfs:domain ex:Issue;
               rdfs:range ex:Comment.
    
    ex:label rdfs:domain ex:Issue;
             rdfs:range ex:Label.
    
    ex:repository rdfs:domain ex:Repository;
                  rdfs:range ex:Issue.
    
    ex:assignee rdfs:domain ex:Issue;
    			rdfs:range ex:User.
    
    s:creator rdfs:range ex:User.
}
```
 
- QUESTION 8 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>

SELECT (COUNT(DISTINCT ?i) as ?iCount)
(COUNT(DISTINCT ?c) as ?cCount) 
(COUNT(DISTINCT ?l) as ?lCount)
WHERE
{
    ?i rdf:type ex:Issue.
    ?c rdf:type ex:Comment.
    ?l rdf:type ex:Label.
}
```
 
- QUESTION 9 

Résultats obtenus :
| type | total | 
| --- | --- | 
| ex:Issue  | `109` |
| ex:Comment  | `634` |
| ex:Label  | `17` |
 
- QUESTION 10 
```
PREFIX ex: <http://www.example.com/ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

INSERT DATA {
    ex:Issue owl:disjointWith ex:Label.
    ex:OpenIssue owl:disjointWith ex:CloseIssue.

    ex:toto rdf:type owl:Class;
    owl:equivalentClass [
    	owl:onProperty ex:authorAssociation;
    	owl:hasValue "NONE"
    ].
    ex:VisitorIssue owl:intersectionOf (ex:toto ex:Issue).
    ex:VisitorOpenIssue owl:intersectionOf (ex:toto ex:OpenIssue).
}
```

- <b>Bonus</b>

Cette requête a donné un succès.
```
PREFIX sys: <http://www.ontotext.com/owlim/system#>
INSERT DATA { [] sys:consistencyCheckAgainstRuleset "owl2-rl" }
```

Écrivez une requête SPARQL qui n’utilise pas la classe `ex:VisitorIssue`, listant les tickets dont la `ex:authorAssociation` est « NONE ».
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>

SELECT (COUNT(?p) as ?pCount)
WHERE
{
  ?p rdf:type ex:Issue.
  ?p ex:authorAssociation "NONE".
}
```
Résultat obtenu : `12`


Écrivez une requête SPARQL listant les instances de `ex:VisitorIssue`, et vérifiez que le résultat est le même.

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>

SELECT (COUNT(?p) as ?pCount)
WHERE
{
  ?p rdf:type ex:VisitorIssue
}
```
Résultat obtenu : `12`

 
- QUESTION 11 
```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX s: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

INSERT DATA {
    s:url rdf:type owl:InverseFunctionalProperty.
}
```
 
- QUESTION 12 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX ex:<http://example.com/ns#>
PREFIX s: <http://schema.org/>
INSERT DATA{
	ex:contributor rdf:type rdf:property;
		rdf:range ex:Issue;
		rdf:domain ex:User;
		rdf:type owl:Restriction;
		owl:propertyChainAxiom(ex:comment s:creator).
}
```
 
- QUESTION 13 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex:<http://example.com/ns#>
SELECT (COUNT(?u) as ?uCount) WHERE{
	?i ex:contributor ?u.
    ?i rdf:type ex:VisitorIssue;
       rdf:type ex:VisitorOpenIssue.
}
```
 
- QUESTION 14 
```
Résultat obtenu : `14`
```
 
- QUESTION 15

Créez une requête SPARQL qui renvoie les informations suivantes pour toutes les `ex:VisitorOpenIssue` de votre dataset :
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex:<http://example.com/ns#>
PREFIX s: <http://schema.org/>
SELECT ?title (COUNT(distinct ?comments) as ?cmCount) (COUNT(distinct 
?commentors) as ?ctCount) WHERE{
	?i rdf:type ex:VisitorOpenIssue.
    ?i s:name ?title;
       ex:comment ?comments;
       ex:contributor ?commentors.
} GROUP BY ?title
```
exécutez une requête SPARQL (toujours la même) qui supprime le type `ex::OpenIssue` de tous les tickets ayant le type `ex:ClosedIssue` :
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX ex:<http://example.com/ns#>
PREFIX s: <http://schema.org/>
DELETE {
    ?t rdf:type ex:OpenIssue.
} WHERE {
    graph <http://example.org/ns#tmp>{
        ?t rdf:type ex:ClosedIssue.
    }
}
```
exécutez une requête SPARQL (toujours la même) qui insère tous les triplets dans le graphe par défaut.
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX ex:<http://example.com/ns#>
PREFIX s: <http://schema.org/>
INSERT {
    ?s ?p ?o
} WHERE{
    graph <http://example.org/ns#tmp>{
        ?s ?p ?o.
    }
}
```
 
- QUESTION 16

Nombre de commentaires par issue, pour chaque trace
!(https://forge.univ-lyon1.fr/p1713323/tp-connaissnaces-dynamics/-/blob/main/G1.PNG?raw=true)

Nombre de contributors par issue, pour chaque trace
!(https://forge.univ-lyon1.fr/p1713323/tp-connaissnaces-dynamics/-/blob/main/G2.PNG?raw=true)

- QUESTION 17
```
```
 
