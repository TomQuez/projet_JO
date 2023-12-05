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
      const articleTitle = document.createElement("h2");
      articleTitle.textContent = article.title;
      articleList.appendChild(articleTitle);
    });
  }
});
