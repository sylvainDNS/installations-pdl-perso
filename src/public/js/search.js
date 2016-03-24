$(function() {
    $('#btnRecherche').on('click', function(e) {
        if(document.getElementById('recherche').value != ""){
            e.preventDefault();

            var r = document.getElementById('recherche').value;
            if(document.getElementById('choixRecherche1').checked == false){
                var c = 'activite';
            }else{
                var c = 'ville';
            }

            var ajax = $.ajax({
                url: c + '/' + r,
                method: 'get'
            });

            ajax.done(function(data) {
                console.log('réponse reçue !');
                console.log(data);
                // $('#table_ville').show();
                $('#table_ville').DataTable();
            });

            ajax.fail(function() {
                console.log('erreur');
            })

        }
    })
});
