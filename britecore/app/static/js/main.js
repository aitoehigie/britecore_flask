var featureRequestModel = {
    featureTitle: ko.observable(""),
    featureDescription: ko.observable(""),
    clientValues: [
  {'id': 'A', 'name': 'Client A'},
 {'id': 'B', 'name': 'Client B'},
 {'id': 'C', 'name': 'Client C'},
 {'id': 'D', 'name': 'Client D'},
 {'id': 'E', 'name': 'Client E'},
 {'id': 'F', 'name': 'Client F'},
 {'id': 'G', 'name': 'Client G'},
 {'id': 'H', 'name': 'Client H'},
 {'id': 'I', 'name': 'Client I'},
 {'id': 'J', 'name': 'Client J'},
 {'id': 'K', 'name': 'Client K'},
 {'id': 'L', 'name': 'Client L'},
 {'id': 'M', 'name': 'Client M'},
 {'id': 'N', 'name': 'Client N'},
 {'id': 'O', 'name': 'Client O'},
 {'id': 'P', 'name': 'Client P'},
 {'id': 'Q', 'name': 'Client Q'},
 {'id': 'R', 'name': 'Client R'},
 {'id': 'S', 'name': 'Client S'},
 {'id': 'T', 'name': 'Client T'},
 {'id': 'U', 'name': 'Client U'},
 {'id': 'V', 'name': 'Client V'},
 {'id': 'W', 'name': 'Client W'},
 {'id': 'X', 'name': 'Client X'},
 {'id': 'Y', 'name': 'Client Y'},
 {'id': 'Z', 'name': 'Client Z'}
    ],
    selectedClient: ko.observable(1),
    priority: ko.observable(1),
    target: ko.observable(moment().format("YYYY-MM-DD")),
    areaValues: [
        { name: "Policies", id: "Policies" },
        { name: "Billings", id: "Billings" },
        { name: "Claims", id: "Claims" },
        { name: "Reports", id: "Reports" }
    ],
    selectedArea: ko.observable('policy'),
    create: function (formElement) {
        $(formElement).validate();
        $.ajax({
            url: '/createFeature',
            data: $(formElement).serialize(),
            type: 'POST',
            success: function (response) {
                window.location = "/";
            },
            error: function (error) {
                console.log(error);
            }
        });
    },
    deleteFeature: function (id, data, event) {
        $.ajax({
            url: '/delete/' + id,
            type: 'DELETE',
            success: function (response) {
                window.location = '/';
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
};
ko.applyBindings(featureRequestModel, document.getElementById("createFeature"));
