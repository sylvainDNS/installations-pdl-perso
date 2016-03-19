$(function() {
    $('#btnRecherche').on('click', function(e) {
        if(document.getElementById('recherche').value != ""){
            e.preventDefault();

            var r = document.getElementById('recherche').value;
            if(document.getElementById('choixRecherche1').checked == false){
                var c = 'activite';
            }else{
                var c = 'commune';
            }

            // var json1 = $.ajax({
            //     url: c + '/' + r,
            //     method: 'get'
            // });
            //
            // var json2 = $.ajax({
            //     url: c.str.split(' ').join('-') + '/' + r,
            //     method: 'get'
            // });
            //
            // var ajax = json1.concat(json2);

            var ajax = $.ajax({
                url: c + '/' + r,
                method: 'get'
            });

            ajax.done(function(data) {
                console.log('réponse reçue !');
                console.log(data);
            });

            ajax.fail(function() {
                console.log('erreur');
            })

        }
    })
});


// function recherche(){
//     var e = document.getElementById('recherche').value;
//     if(document.getElementById('choixRecherche1').checked = true){
//         var c = 'activite';
//     }else{
//         var c = 'commune';
//     }
//     document.location.href = c + '/' + e;
// }
