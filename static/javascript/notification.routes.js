(function () {
  'use strict';

  angular
    .module('notification.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'NotificationController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/panel/register.html'
    }).otherwise('/');
  }
})();