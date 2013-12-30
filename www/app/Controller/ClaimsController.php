<?php
class ClaimsController extends AppController {
    public $helpers = array('Html', 'Form');

    public $components = array('Security');

    public function beforeFilter() {
       //$this->Security->$unlockedFields = array('dogewallet_address', 'estimated_amount_lost', 'contact_email', 'reimburse_addr');
    }

    public function index() {
        //$this->set('claims', $this->Claim->find('all'));
		return;
    }
	
	public function view($id = null,$hashcode = null) {
        if (!$id || !$hashcode) {
            throw new NotFoundException(__('Invalid ID or Hashcode'));
			return;
        }

        $claim = $this->Claim->findById($id);
		if ($claim['Claim']['email_hash'] == $hashcode){
       		$this->set('claim', $claim);
			if ( $claim['Claim']['email_verified'] == false) {
				$this->Claim->read(null, $id);
				$this->Claim->set('email_verified', true);
				$this->Claim->save();
				$this->Session->setFlash(__('Thank you for verifying your email, the status on your claim can be checked at this URL anytime.'));
			}
			
		}  else {
			throw new NotFoundException(__('Invalid ID or Hashcode'));
			return;
		}

    }

	
	public function add() {
		
        if ($this->request->is('post')) {

            $this->Claim->create($this->request->data);
			
            if ($this->Claim->save()) {
				$seed = '43tno3j333';
				$hash = substr(sha1(uniqid($seed . mt_rand(), true)), 0, 10);
				$this->Claim->saveField('email_hash',$hash);
				App::uses('CakeEmail', 'Network/Email');
				$Email = new CakeEmail();
				$Email->to($this->request->data('Claim.contact_email'))
			    ->from('no-reply@savedogemas.com')
				->subject('Please verify your SaveDogemas Email Address')
			    ->send("Thank you for signing up for the SaveDogemas program. For us to help you out, you need to first verify your email address by visiting the following URL: ".Router::url('/', true)."claims/view/".$this->Claim->id."/".$hash."  Once you have verified your email address, you may access your claim's status at any time by going to the above URL again.\r\n \r\nThanks!\r\nThe SaveDogemas Team");
				
                $this->Session->setFlash(__('Your claim has been added. Please check your email for the verification email. Make sure to check your spam folder.'));
                return $this->redirect(Router::url('/', true));
				
            }
            $this->Session->setFlash(__('Unable to add your claim.'));
        }
    }
}
?>