document.addEventListener("DOMContentLoaded", () => {
  const articleList = document.querySelector("#article-list");
  const offerList = document.querySelector("#offers-list");

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

  function displayArticles(data) {
    articleList.innerHTML = "";
    const articleData = data;
    // console.log(articleData);
    articleData.forEach((article) => {
      // console.log(article.thumbnail);
      articleList.innerHTML += `<div class="card m-auto my-2" style="width: 18rem;">
      <img src="${article.thumbnail}" class="card-img-top mt-3 p-2" alt="${article.title}">
      <div class="card-body">
        <h5 class="card-title">${article.title}</h5>
        <p class="card-text">${article.description}</p>
        
      </div>`;
    });
  }
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

  function displayOffers(data) {
    offerList.innerHTML = "";
    const offerData = data;
    // console.log(articleData);
    offerData.forEach((offer) => {
      // console.log(offer.thumbnail);
      offerList.innerHTML += `<div class="card m-auto my-2" style="width: 18rem;">
      <img src="${offer.thumbnail}" class="card-img-top mt-3 p-2" alt="${offer.name}">
      <div class="card-body">
        <h5 class="card-title">${offer.name}</h5>
        <p class="card-text">${offer.description}</p>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">Prix : ${offer.price} €</li>
          
          <li class="list-group-item">Billets disponibles : ${offer.stock} </li>
          </ul>
      </div>`;
    });
  }
});
