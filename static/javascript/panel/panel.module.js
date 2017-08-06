(function () {
  'use strict';

  angular
    .module('notification.panel', [
      'notification.panel.controllers',
      'notification.panel.services'
    ]);

  angular
    .module('notification.panel.controllers', []);

  angular
    .module('notification.panel.services', ['ngCookies']);
})();