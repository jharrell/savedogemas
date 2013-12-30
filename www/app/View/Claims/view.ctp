<!-- File: /app/View/Posts/view.ctp -->

<h1>Claim for: <?php echo $claim['Claim']['contact_email']; ?></h1>

<p>Created: <?php echo $claim['Claim']['created']; ?></p>

        <p>Dogewallet Address: <?php echo $claim['Claim']['dogewallet_address']; ?></p>
        <p>Amount Lost: Ð<?php echo $claim['Claim']['estimated_amount_lost']; ?></p>
        <p>Reimburse Address: <?php echo $claim['Claim']['reimburse_addr']; ?></p>
        <p>Has the email been verified? <?php echo $claim['Claim']['email_verified']; ?></p>