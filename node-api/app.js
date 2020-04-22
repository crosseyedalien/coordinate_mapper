import express from 'express';
import recipes from './db/db';
import bodyParser from 'body-parser';

//var recipes = require('./db/db');
//var express = require("express");

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

app.post("/newdata", (req, res) => {
    if (!req.body.title) {
        return res.status(400).send({
            success: 'false',
            message: 'title is required'
        });
    }

    const rec = {
        id: recipes.length + 1,
        title: req.body.title
    }

    recipes.push(rec);
    return res.status(201).send({
        success: 'true',
        message: 'added successfully'
    });
});

app.get("/recipes", (req, res, next) => {
    res.status(200).send({
        success: 'true',
        message: 'recipes retrieved',
        data: recipes 
    })
});

app.get('/recipes/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    recipes.map((recipe) => {
        if (recipe.id === id) {
            return res.status(200).send({
                success: 'true',
                message: 'recipe retrieved successfully',
                recipe,
            });
        }
    });
    return res.status(404).send({
        success: 'false',
        message: 'recipe does not exist',
    });
});

app.delete('/recipes/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    recipes.map((recipe, index) => {
        if (recipe.id === id) {
            recipes.splice(index, 1);
            return res.status(200).send({
                success: 'true',
                message: 'delete successful'
            });
        }
    });

    return res.status(404).send({
        success: 'false',
        message: 'recipe not found'
    });
});
 
const PORT = 5000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
