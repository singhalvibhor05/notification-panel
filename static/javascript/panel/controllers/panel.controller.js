/**
* Register controller
* @namespace notification.panel.controllers
*/
(function () {
  'use strict';

  angular
    .module('notification.panel.controllers')
    .controller('NotificationController', NotificationController);

  NotificationController.$inject = ['$location', '$scope', 'Notification'];

  /**
  * @namespace NotificationController
  */
  function NotificationController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    /**
    * @name register
    * @desc Register a new user
    * @memberOf thinkster.authentication.controllers.RegisterController
    */
    function register() {
      Notification.register(vm.header, vm.content, vm.image_url);
    }
  }
})();