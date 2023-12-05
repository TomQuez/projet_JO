document.addEventListener("DOMContentLoaded", () => {
  const articleList = document.querySelector("#article-list");

  function loadData() {
    fetch("get_blog_articles/")
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        let collectionData = data.data;

        displayArticles(collectionData);
      });
  }
  loadData();
  function displayArticles(data) {
    articleList.innerHTML = "";
    const articleData = data;
    // console.log(articleData);
    articleData.forEach((article) => {
      console.log(article.thumbnail);
      articleList.innerHTML += `<div class="card m-auto my-2" style="width: 18rem;">
      <img src="${article.thumbnail}" class="card-img-top mt-3 p-2" alt="${article.title}">
      <div class="card-body">
        <h5 class="card-title">${article.title}</h5>
        <p class="card-text">${article.description}</p>
      </div>`;
    });
  }
});
