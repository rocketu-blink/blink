'use strict';
angular.module("blink").config(function ($routeProvider) {
  $routeProvider
    .when("/search", {
      templateUrl: "app/views/main.html",
      controller: "MainController"
    })
    .when("/search/:search", {
      templateUrl: "app/views/search.html",
      controller: "SearchController"
    })
    .when("/movie/:id", {
      templateUrl: "app/views/movie.html",
      controller: "MovieController"
    })
    .when("/genre", {
      templateUrl: "app/views/genre.html",
      controller: "GenreController"
    })
    .when("/genre/:genre_id", {
      templateUrl: "app/views/detail_genre.html",
      controller: "GenreDetailController"
    })
    .when("/year", {
      templateUrl: "app/views/year.html",
      controller: "YearController"
    })
    .when("/year/:year_id", {
      templateUrl: "app/views/detail_year.html",
      controller: "YearDetailController"
    })
    .otherwise({redirectTo: "/search"})
});