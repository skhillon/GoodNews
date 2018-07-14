import React from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';
import Footer from './Footer';

function ArticleCardContainer() {
    if (this.state.loading) return (
      <p>Loading...</p>
    );

    return (
      <CardColumns>
        {this.state.articles.map((article, i) =>
          <Article
            key={i}
            url={article.url}
            urlToImage={article.urlToImage}
            title={article.title}
            description={article.description}
          />
        )}
      </CardColumns>
    );
}

ArticleCardContainer.propTypes = {
  location: PropTypes.object.isRequired //from React Router
};