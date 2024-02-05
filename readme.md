# Projet site e-commerce pour vente de ticket sportif JO 2024

## Description

Ce projet est un site e-commerce pour la vente de ticket sportif pour les JO 2024. Il permettra aux utilisateurs de consulter les différents sports et les différentes épreuves qui auront lieu lors des JO 2024. Ils pourront également acheter des tickets pour les épreuves de leur choix.

## Installation

Pour installer le projet, il suffit de cloner le dépôt git sur votre machine.Ensuite, vous devrez installer les dépendances du projet :

```bash
git clone https://github.com/TomQuez/projet_JO.git
cd projet_JO
pip install -r requirements.txt
```

## Congiguration

Pour configurer le projet, vous devrez créer un fichier .env à la racine du projet. Vous devrez y ajouter les variables d'environnement suivantes :

```bash
SECRET_KEY=VotreCleSecrete
DEBUG=True
```

Vous pourriez être amené à ajouter d'autres variables d'environnement en fonction de votre configuration et du type de déploiement que vous souhaitez faire.

## Utilisation

Pour utiliser le projet, vous devrez lancer le serveur de développement de Django :

```bash
python manage.py runserver
```

## Fonctionnalités

- Consultation des sports et des épreuves
- Achat de tickets
- Historique des achats
- Gestion des utilisateurs

## Technologies

- Python
- Django
- HTML
- CSS
- Bootstrap
- JavaScript
- PostgreSQL

## Structure du projet

Le projet est structuré de la manière suivante :
.
├── Shop
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
| ├── asgi.py
| ├── .env
├── Store
│ ├── templates
│ │ ├── cart.html
│ │ ├── checkout.html
│ │ ├── index.html
│ │ ├── offer_detail.html
│ │ ├── offers.html
│ │ ├── orders_paid.html
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── static
│ ├── css
│ │ ├── style.css
│ ├── images
| ├── javascript
| | |── script.js
