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
                method: 'get',
                dataType : 'json'
            });

            ajax.done(function(data) {
                $('#table_activite').DataTable().destroy();
                $('#table_ville').DataTable().destroy();
                if(c == 'activite'){
                    $('#ville').hide();
                }else{
                    $('#activite').hide();
                }

                $("#" + c).show();
                $('#table_' + c).DataTable( {
                    data: data
                });
            });

            ajax.fail(function() {
                console.log('erreur');
            })

        }
    })
});
