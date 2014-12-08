(function () {
    'use strict';

    var website = openerp.website;

    website.snippet.animationRegistry.dashboard = website.snippet.Animation.extend({
        selector: ".common-list-holder",
        start: function (editable_mode) {
            var self = this;
            if (self.$target.data('model')) {
                openerp.jsonRpc('/dashboard/search_read', 'call', {
                    model: self.$target.data('model'),
                    domain: self.$target.data('domain'),
                    fields: self.$target.data('fields'),
                    limit: self.$target.data('limit'),
                    order: self.$target.data('order')
                }).always(function (data) {
                    //self.$target.find('div.caption').append(data.category.name);
                    _(data.results).each(function (result) {
                        //TODO:
                        self.$target.find('div.scroller').append(result.name)
                    });
                });
            }
        }
    });
})();
