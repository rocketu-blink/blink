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
            $scope.movies.push(data[i]['title']+ ' ('+data[i]['release_year'].toString()+')');
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
    $scope.searchTerm = $routeParams['search'];
    var searchResults = $http.get('http://10.12.4.41:8000/results?search=' + $scope.searchTerm.toString());
    searchResults.success(function (data) {
      $scope.results = data;
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

  .controller('GenreDetailController', function ($scope, $routeParams, $http) {
    $scope.genre = $routeParams['genre_id'];
    var genreInfo = $http.get('test_json/test_genre.json');
    genreInfo.success(function (data) {
      $scope.genreInfo = data;
    })
    var genreDetail = $http.get('test_json/genre_movie_detail_test.json');
    genreDetail.success(function (data) {
      $scope.genreData = data;
    })
  })

  .controller('YearController', function ($scope, $http) {
    
  })

  .controller('YearDetailController', function ($scope, $http, $routeParams){
    $scope.year = $routeParams['year_id'];
    var yearDetail = $http.get('test_json/genre_movie_detail_test.json');
    yearDetail.success(function (data) {
      $scope.yearData = data;
    })
  })

