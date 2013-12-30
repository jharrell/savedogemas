<?php
$url = 'http://dogechain.info/chain/Dogecoin/q/getreceivedbyaddress/DCCpdXmwD9TjqnXvmm7NrrBQt2nBKEPDSt';
$userAgent = 'SaveDogemas' ;

	$ch = curl_init($url);
    curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);       
    $kl = curl_exec($ch);
    curl_close($ch);
	
	$kl = number_format($kl, 0, '.', '');

	$totalreceived = floor(preg_replace('/\D/', '', $kl));
$progressbarwidth= ( $totalreceived / 15000000 ) * 100;
?>


	<h1 class="heading"> It's the year of the Doge. </h1>
	<p class="description">On Christmas Day, the spirit of Dogemas was damaged when hackers infiltrated Dogewallet and 					Instadoge, <b>stealing over Ɖ30,000,000 </b> from thousands of friendly shibes. The dogecoin community is coming together to reimburse as much of their losses as possible. <b>Thanks to your help, we have already<span class="raised"> raised Ð<?php echo 	number_format(preg_replace('/\D/', '', $totalreceived)); //THIS LINE WHEREVER YOU WANT THE NUMBER ?></span> for the cause.</b> We are looking to raise at least Ɖ15,000,000.</p>
	<?php echo $this->Html->link("Submit A Claim", array('controller' => 'Claims','action'=> 'add'), array( 'class' => 'button')) ?>
    <div class="progressbar">
        <div class="progressbar-inner" style="width: <?php echo $progressbarwidth; ?>%"></div>
    </div>
	<p class="info"><a href="http://dogechain.info/address/DCCpdXmwD9TjqnXvmm7NrrBQt2nBKEPDSt">Ð Donation Address:</a>  DCCpdXmwD9TjqnXvmm7NrrBQt2nBKEPDSt</p>
	<p>Please help your fellow shibes.<br />
	Questions and More Information can be found on <a href="http://www.reddit.com/r/dogecoin/comments/1tu0gs/officially_launching_savedogemas_the_dogecoin/">Reddit</a></p>
    
	<div class="sharing"><span class='st_facebook_hcount' displayText='Facebook'></span>
	<span class='st_twitter_hcount' displayText='Tweet' st_msg="#SaveDogemas" st_via=' '></span>
	<span class='st_linkedin_hcount' displayText='LinkedIn'></span>
	<span class='st_googleplus_hcount' displayText='Google +'></span>
	<span class='st_email_hcount' displayText='Email'></span>
	<span class='st_reddit_hcount' displayText='Reddit'></span></div>