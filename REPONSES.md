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
```
 
- QUESTION 13 
```
```
 
- QUESTION 14 
```
```
 
- QUESTION 15
```
```
 
- QUESTION 16
```
```
 
- QUESTION 17
```
```
 