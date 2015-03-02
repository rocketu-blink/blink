'use strict';
var app = angular.module('blink', ['ngRoute', 'autocomplete', 'angularUtils.directives.dirPagination']);

app.config(function(paginationTemplateProvider) {
    paginationTemplateProvider.setPath('app/views/dirPagination.tpl.html');
});