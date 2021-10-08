<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nouvelle réservation</title>
</head>
<body>
<form method="POST" action="{{ url_for('new_order') }}">
        <fieldset class="uk-fieldset">

            <legend>Réserver :</legend>

            <div>
                <input type="text" placeholder="Nom du livre" name='name'>
            </div>

            <div>
                <input type="text" placeholder="Auteur du livre" name='author'>
            </div>

        </fieldset>

        <!-- INPUT TO SUBMIT FOR ACTION CREATE BOOK -->
        <input type="submit" value="Valider le formulaire">
    </form>

</body>
</html>