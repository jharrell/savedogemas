<h1>Submit Claim</h1>
<p>Please submit your reimbursement claim from the DogeWallet Hack. Please note that it might take a while for the payments to be sent, as there are many logistics to this whole thing. Please enter your DogeWallet Account email, and address to the best of your knowledge. <b>We will be verifying this information before payments are made.</b></p>

<p> If you have multiple addresses you would like to claim with, open up a claim for each address with the same email attached to the DogeWallet account. Thanks! - SaveDogeMas Team </p>

<p>If you are a InstaDoge user, we will update with options for you to make a claim by tomorrow. Sorry for the Delay!</p>
<?php

echo $this->Form->create('Claim');
echo $this->Form->input('contact_email', array('label' => 'DogeWallet Email'));
echo $this->Form->input('dogewallet_address', array('label' => 'DogeWallet Address'));
echo $this->Form->input('estimated_amount_lost', array('label' => 'Amount Ð Lost'));
echo $this->Form->input('reimburse_addr', array('label' => 'Ð Address to Reimburse to'));
echo $this->Form->end('Submit Claim');

?>