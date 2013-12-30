<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style>
html{
  height: 100%;
}
body {
	background-attachment:fixed;
	background-image: -webkit-gradient(
	linear,
	right bottom,
	left top,
	color-stop(0, #38B35B),
	color-stop(1, #69FF94)
);
background-image: -o-linear-gradient(left top, #38B35B 0%, #69FF94 100%);
background-image: -moz-linear-gradient(left top, #38B35B 0%, #69FF94 100%);
background-image: -webkit-linear-gradient(left top, #38B35B 0%, #69FF94 100%);
background-image: -ms-linear-gradient(left top, #38B35B 0%, #69FF94 100%);
background-image: linear-gradient(to left top, #38B35B 0%, #69FF94 100%);
	font-family:"Century Gothic","Lucida Grande",Arial,sans-serif;
    font-weight:normal;
	margin:0;
 	text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
	height: 100%;
}
.heading{
	margin-top: 3em;
}

.info, .info a{
	font-weight:bold;
}

a.button {
    color: #FFF;
    font: bold 12px Helvetica, Arial, sans-serif;
    text-decoration: none;
    padding: 7px 12px;
    position: relative;
    display: inline-block;
    text-shadow: 0 1px 0 #063;
    -webkit-transition: border-color .218s;
    -moz-transition: border .218s;
    -o-transition: border-color .218s;
    transition: border-color .218s;
    background: #38B35B;
    border: solid 1px #dcdcdc;
    border-radius: 2px;
    -webkit-border-radius: 2px;
    -moz-border-radius: 2px;
    margin-right: 20px;
    cursor:pointer;
}
a.button:hover{
    color: #FFF;
    border-color: #999;
    -moz-box-shadow: 0 2px 0 rgba(0, 0, 0, 0.2); 
-webkit-box-shadow:0 2px 5px rgba(0, 0, 0, 0.2);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.15);
}
a.button:active {
    color: #000;
    border-color: #444;
}

.raised{

}

.logo{
display: block;
margin: 0 auto;
}

.container{
	background: #fff;
	max-width: 725px;
	margin-left:auto;
	margin-right:auto;
	text-align: center ;
	padding: 15px;
	border-radius: 45px;
	-webkit-box-shadow: 1px 2px 10px rgba(0,0,0,.5);
	-moz-box-shadow: 1px 2px 10px rgba(0,0,0,.5);
	box-shadow: 1px 2px 10px rgba(0,0,0,.5);
}

.progressbar{
    width:700px;
    height:16px;
    margin:20px auto 20px auto;
    padding:0px;
    background:#cfcfcf;
    border-width:1px;
    border-style:solid;
    border-color: #aaa #bbb #fff #bbb;    
    box-shadow:inset 0px 2px 3px #bbb;    
}

.progressbar,
.progressbar-inner{
    border-radius:4px;
    -moz-border-radius:4px;
    -webkit-border-radius:4px;
    -o-border-radius:4px;
}

.progressbar-inner{
    height:100%;
    background:#999;
    background-color:red;
    background-size:18px 18px;
    background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 1) 25%, transparent 25%,
                        transparent 50%, rgba(255, 255, 255, 1) 50%, rgba(255, 255, 255, 1) 75%,
                        transparent 75%, transparent);
    background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 1) 25%, transparent 25%,
                        transparent 50%, rgba(255, 255, 255, 1) 50%, rgba(255, 255, 255, 1) 75%,
                        transparent 75%, transparent);
    background-image: -ms-linear-gradient(45deg, rgba(255, 255, 255, 1) 25%, transparent 25%,
                        transparent 50%, rgba(255, 255, 255, 1) 50%, rgba(255, 255, 255, 1) 75%,
                        transparent 75%, transparent);
    background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 1) 25%, transparent 25%,
                        transparent 50%, rgba(255, 255, 255, 1) 50%, rgba(255, 255, 255, 1) 75%,
                        transparent 75%, transparent);
    background-image: linear-gradient(45deg, rgba(255, 255, 255, 1) 25%, transparent 25%,
                        transparent 50%, rgba(255, 255, 255, 1) 50%, rgba(255, 255, 255, 1) 75%,
                        transparent 75%, transparent);
    box-shadow:inset 0px 2px 8px rgba(255, 255, 255, .8), inset -1px -1px 0px rgba(0, 0, 0, .2);
}


</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>SaveDogemas - Helping Shibes In Need</title>
<script type="text/javascript">var switchTo5x=true;</script>
<script type="text/javascript" src="http://w.sharethis.com/button/buttons.js"></script>
<script type="text/javascript">stLight.options({publisher: "7fc94272-a486-47bf-936d-1d6d9e926960", doNotHash: true, doNotCopy: false, hashAddressBar: false});</script>
	<?php
		echo $this->Html->meta('icon');

		echo $this->Html->css('cake.generic');

		echo $this->fetch('meta');
		echo $this->fetch('css');
		echo $this->fetch('script');
	?>

<!-- HTML made by hand in Dreamweaver by Gabriel Medine for SaveDogemas.com. It was a pain in the ass.  -->
</head>
<body>
<a href="http://savedogemas.com/"><img class="logo" src="http://savedogemas.com/logo.png"></a>
<div class="container">
<!--nocache-->
   		<?php echo $this->Session->flash(); ?>
<!--/nocache-->

			<?php echo $this->fetch('content'); ?>
</div>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-46769426-1', 'savedogemas.com');
  ga('send', 'pageview');

</script>
</body>
</html>
