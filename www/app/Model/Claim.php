<?php
class Claim extends AppModel {
	
    public $validate = array(
        'contact_email' => array(
            'rule' => 'email',
			'required' => true,
            'message'  => 'Must be a Valid Email Address'
        ),
        'dogewallet_address' => array(
            'rule' => 'alphaNumeric',
			'message'  => 'Not A Valid Dogecoin Address'
        ),
		'estimated_amount_lost' => array(
            'rule' => 'decimal',
			'message'  => 'Not a number'
        ),
		'reimburse_addr' => array(
            'rule' => 'alphaNumeric',
			'message'  => 'Not A Valid Dogecoin Address'
        ),
    );

}
?>