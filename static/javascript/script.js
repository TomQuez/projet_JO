document.addEventListener("DOMContentLoaded", () => {
  const articleList = document.querySelector("#article-list");
  const offerList = document.querySelector("#offers-list");
  let currentPath = window.location.pathname;
  let navLinks = document.querySelectorAll("#nav-link");
  /**
   * Ajout de la classe active sur le lien de la page courante.
   * @param {string} currentPath
   * @param {array} navLinks
   *
   */
  navLinks.forEach((link) => {
    if (link.getAttribute("href") == currentPath) {
      link.classList.add("active");
    }
  });

  /**
   * Fonction qui récupère les articles de blog au format Json et les affiche dans la page d'accueil.
   * La fonction fait appel à une autre fonction : displayArticles.
   *
   *
   */

  function loadArticles() {
    fetch("get_blog_articles/")
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        let collectionData = data.data;

        displayArticles(collectionData);
      });
  }

  if (articleList !== null) {
    loadArticles();
  }
  /**
   * Fonction qui affiche les articles de blog dans la page d'accueil index.html.
   * @param {*} data
   */
  function displayArticles(data) {
    articleList.innerHTML = "";
    const articleData = data;

    articleData.forEach((article) => {
      articleList.innerHTML += `<div class="card m-auto my-2" style="width: 24rem;">
      <img src="${article.thumbnail}" class="card-img-top mt-3 p-2" alt="${article.title}">
      <div class="card-body">
        <h5 class="card-title">${article.title}</h5>
        <p class="card-text">${article.description}</p>
        
      </div>`;
    });
  }

  /**
   * Fonction qui récupère les offres au format Json et les affiche dans la page d'accueil.
   * Cette fonction fait appel à une autre fonction : displayOffers.
   *
   */

  function loadOffers() {
    fetch("/get_offers_data/")
      .then((response) => response.json())
      .then((data) => {
        let collectionOffers = data.data;

        displayOffers(collectionOffers);
      });
  }
  if (offerList !== null) {
    loadOffers();
  }

  /**
   * Fonction qui affiche les offres dans le template offers.html
   * @param {*} data
   */

  function displayOffers(data) {
    offerList.innerHTML = "";
    const offerData = data;

    offerData.forEach((offer) => {
      offerList.innerHTML += `<div class="card m-auto my-2" style="width: 18rem;">
      <img src="${offer.thumbnail}" class="card-img-top mt-3 p-2" alt="${offer.name}">
      <div class="card-body">
        <h5 class="card-title">${offer.name}</h5>
        <p class="card-text">${offer.description}</p>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">Prix : ${offer.price} €</li>
          
          <li class="list-group-item">Billets disponibles : ${offer.stock} </li>
         <li class ="list-group-item"><a href="/offers/${offer.slug}/">Voir l'offre</a></li>
          </ul>
      </div>`;
    });
  }
});
