import React from 'react';
import TextField from '@material-ui/core/TextField';
import ArticleCardContainer from './ArticleCardContainer';

var Searchbar = React.createClass({

    getInitialState: function() {
        return {
            textFieldValue: ''
        };
    },

    _handleTextFieldChange: function(e) {
        this.setState({
            textFieldValue: e.target.value
        });
    },

    _handleOnClick: function (e) {
        var container = ArticleCardContainer();
    }

    render: function() {
        return (
            <div>
                <TextField value={this.state.textFieldValue} onChange={this._handleTextFieldChange} onclick={this._handleOnClick}/>
            </div>
        )
    }

});