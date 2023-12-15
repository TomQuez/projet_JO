Sécurité de l'application
=========================
**Généralités**
---------------
L'utilisation de Django permet de sécuriser l'application. Django est un framework sûr, extrêmement documenté, et disposant d'une communauté très solide. Aussi, Django est régulièrement maintenu et mis à jour, ce qui accentue sa sécurité.


**Authentification**
--------------------
Le site utilise le système intégré de Django. La sécurité des mots de passe a été renforcé en ajoutant des contraintes. Ainsi, un mot de passe devra faire au minimum 8 caractères comprenant au moins un chiffre, une minuscule, une majuscule et un caractère spécial.
L'authentification utilise l'email qui est par essence unique. Le modèle utilisateur ne permet pas d'avoir deux comptes utilisateurs avec le même email.  

**Autorisation**
----------------
Il y a deux groupes liés aux différentes autorisations : les administrateurs et les utilisateurs.
Les administrateurs ont accès à toutes les fonctionnalités, contrairement aux utilisateurs qui ne peuvent que consulter leurs données.

**Protection**
---------------
Les injections SQL et les attaques CSRF:
-----------------------------------------
En utilisant l'ORM de django et les jetons CSRF dans les formulaires, l'application est protégée contre ces actes malveillants.

Force brute : 
-------------
les mots de passe ont des contraintes fortes, qui rendent l'attaque par force brute plus compliqué. Aussi l'ajout d'un délai de 3 secondes entre chaque tentative de connexion rend l'attaque beaucoup plus longue.



