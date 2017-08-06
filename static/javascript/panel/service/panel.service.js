/**
* Notification
* @namespace notification.panel.services
*/
(function () {
  'use strict';

  angular
    .module('notification.panel.services')
    .factory('Notification', Notification);

  Notification.$inject = ['$cookies', '$http'];

  /**
  * @namespace notification.panel.services
  * @returns {Factory}
  */
  function Notification($cookies, $http) {
    /**
    * @name Notification
    * @desc The Factory to be returned
    */
    var Notification = {
      register: register
    };

    return Notification;

    ////////////////////

    /**
    * @name register
    * @desc Try to create a notification
    * @param {string} header The username entered by the user
    * @param {string} content The password entered by the user
    * @param {string} image_url The email entered by the user
    * @returns {Promise}
    * @memberOf notification.panel.services
    */
    function register(header, content, image_url) {
      return $http.post('/api/v1/panel/', {
        header: header,
        content: content,
        image_url: image_url
      });
    }
  }
})();