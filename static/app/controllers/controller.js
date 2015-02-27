'use strict';
angular.module('blink')
  .controller('MainController', function ($scope, $http, $location) {
    $scope.collectData = function (data) {
      $scope.inputData = data
      if (data.length < 3) {
        $scope.movies = [];
      }
      if (data.length === 3) {
        var movies = $http.get("http://10.12.4.41:8000/results?search=" + $scope.inputData)
        movies.success(function (data) {
          $scope.all_data = data;
          $scope.movies = [];
          for (var i = 0; i < data.length; i++) {
            if (data[i]['release_year']) {
              $scope.movies.push(data[i]['title']+ ' ('+data[i]['release_year']+')');
            }
          }
        });
      };
    }
    $scope.searchTitle = function (data) {
      var length = data.length;
      var title = data.substring(0, length - 7);
      var year = data.substring(length - 5, length - 1);
      for (var i = 0; i < $scope.all_data.length; i++) {
        if (title === $scope.all_data[i]['title'] && parseInt(year) === $scope.all_data[i]["release_year"]) {
          var id = $scope.all_data[i]['id']
          $location.path("/movie/"+ id);
        }
      }      
    }
    $scope.searchInput = function () {
      if ($scope.inputData === undefined) {
        $scope.inputData = "";
      }
      $location.path('/search/'+ $scope.inputData);
    }
  })
  

  .controller('SearchController', function ($scope, $routeParams, $http) {
    $scope.loaded = false;
    $scope.searchTerm = $routeParams['search'];
    var searchResults = $http.get('http://10.12.4.41:8000/results?search=' + $scope.searchTerm.toString());
    searchResults.success(function (data) {
      $scope.results = data;
      $scope.loaded = true;
    })
  })

  .controller('MovieController', function ($scope, $routeParams, $http, $location, $anchorScroll) {
    $scope.movie_id = $routeParams['id'];
    var movie = $http.get('http://10.12.4.41:8000/content/' + $scope.movie_id);
    movie.success(function (data) {
      $scope.detail = data;
      $scope.date = new Date(data.release_date);
      $scope.dateString = $scope.date.toDateString().substring(3);      
    })
    $scope.gotoTop = function() {
      $location.hash('top');
      $anchorScroll();
    }
  })

  .controller('GenreController', function ($scope, $http) {
    
  })

  .controller('GenreController', function ($scope, $http) {
    $scope.genre = ['Crime', 'Drama', 'Comedy', 'Romance', 'Thriller', 'Animation', 'Adventure', 'War', 
    'Horror', 'Action', 'Sci-Fi', 'Family', 'Fantasy', 'Biography', 'Music', 'Mystery', 'Sport', 'History', 
    'Western', 'Musical', 'Adult', 'Film-Noir', 'News'];
  })

  .controller('GenreDetailController', function ($scope, $routeParams, $http) {
    $scope.genre = $routeParams['genre_id'];
    $scope.loaded = false;
    var genreDetail = $http.get('http://10.12.4.41:8000/genre?search=' + $scope.genre);
    genreDetail.success(function (data) {
      $scope.loaded = true;
      $scope.genreData = data;
    })
  })

  .controller('YearController', function ($scope, $http) {
    $scope.yearData = [];
    for (var i = 1900; i < 2016; i++) {
      $scope.yearData.push(i)
    }
  })

  .controller('YearDetailController', function ($scope, $http, $routeParams){
    $scope.year = $routeParams['year_id'];
    $scope.loaded = false;
    var yearDetail = $http.get('http://10.12.4.41:8000/year?search=' + $scope.year);
    yearDetail.success(function (data) {
      $scope.loaded = true;
      $scope.yearData = data;
    })
  })