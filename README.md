# civic-connect
# Projet : Civic Connect

## 1. Problème

Au Cameroun, les étudiants rencontrent plusieurs problèmes tels que :

* les coupures d'électricité ;
* l'accès aux informations fiables ;
* l'accès à la connexion Internet ;
* l'accès aux petites activités de commerce.

Le but de cette application est de permettre aux étudiants camerounais d'avoir accès aux points de connectivité, de signaler les perturbations et d'avoir accès aux services de commerce.

## 2. Cadrer le produit

### Que fait l'application ?

* Trouver des services utiles.
* Signaler les coupures et les perturbations.
* Accéder à des informations fiables.
* Trouver les points de connectivité.
* Suivre les petites annonces.

### Que ne fera-t-elle pas ?

* Pas de commerce.
* Pas d'échange entre les utilisateurs.

### Qui sont les utilisateurs ?

* Users(Les étudiants / clients)
* L'administrateur.

DIAGRAMME DE DOMAINE
<img width="901" height="627" alt="diagramme de domaine" src="https://github.com/user-attachments/assets/c13c71b1-044c-4362-a20a-c26944d089b7" />



## 3. Définir le MVP

* Création d'un compte utilisateur.
* Se connecter.
* Publier des services et des annonces.
* Supprimer des services.
* Modifier des services.
* Consulter la liste des services.
* Afficher les services disponibles.

## 4. Backlog

### Gestion des utilisateurs

* Créer la classe **Utilisateur**.
* Permettre l'inscription d'un utilisateur.
* Permettre la connexion.
* Créer une classe **Administrateur**.
* Modifier les informations d'un utilisateur.
* Supprimer un utilisateur.

### Gestion des localisations

* Créer la classe **Localisation**.
* Ajouter une localisation.
* Modifier une localisation.
* Associer une localisation à un utilisateur.

### Gestion des services

* Créer la classe **Service**.
* Publier un service.
* Modifier un service.
* Afficher la liste des services disponibles.
* Rechercher un service.
* Supprimer un service.

### Gestion des produits

* Créer la classe **Produit**.
* Ajouter un produit.
* Afficher la liste des produits.
* Supprimer un produit.
* Modifier un produit.

### Gestion des commandes

* Créer la classe **Commande**.
* Passer une commande.
* Afficher une commande.
* Annuler une commande.
* Changer le statut d'une commande.

### Gestion des signalements

* Créer une classe **Signalement** (ou **Report**).
* Signaler un service ou un produit.
* Afficher les signalements.
* Traiter les signalements.

### Interface

* Créer une fenêtre principale.
* Créer une fenêtre de connexion.
* Créer un formulaire d'ajout de services.
* Créer un formulaire de commande.
* Créer un menu de navigation.

### Base de données

* Créer les tables.
* Enregistrer les utilisateurs.
* Enregistrer les services.
* Enregistrer les produits.
* Enregistrer les commandes.
* Enregistrer les signalements.

### Tests

* Tester les classes Python.
* Tester les fonctions principales.
* Corriger les erreurs.
