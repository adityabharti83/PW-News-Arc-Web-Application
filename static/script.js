// script.js

// Push Notifications - Mock function for demonstration
function sendNotification(message) {
    // This function would actually be connected to Firebase Cloud Messaging in production
    alert("New Notification: " + message);
}

// Event listener for search functionality
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const keyword = document.getElementById('searchInput').value;
    fetch(`/api/news?search=${keyword}`)
        .then(response => response.json())
        .then(data => {
            displayNews(data);
        })
        .catch(error => console.error('Error:', error));
});

// Function to display news articles dynamically
function displayNews(newsList) {
    const newsContainer = document.getElementById('newsContainer');
    newsContainer.innerHTML = ''; // Clear previous results
    newsList.forEach(news => {
        let article = document.createElement('div');
        article.classList.add('news-article');
        article.innerHTML = `
            <h3>${news.title}</h3>
            <p>${news.content}</p>
            <button onclick="likeArticle(${news.id})">Like</button>
            <button onclick="shareArticle('${news.title}', '${news.url}')">Share</button>
        `;
        newsContainer.appendChild(article);
    });
}

// Like functionality
function likeArticle(newsId) {
    fetch('/api/engage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ news_id: newsId, type: 'like' })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

// Social Media Sharing
function shareArticle(title, url) {
    const twitterUrl = `https://twitter.com/share?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}`;
    const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
    window.open(twitterUrl, '_blank');
    window.open(facebookUrl, '_blank');
}
