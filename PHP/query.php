<?php
    require('php_python.php');
    if($_POST['username'] == '' || $_POST['password'] == '')
    {
        echo("用户名或密码不能为空");
    }else
    {
        $ret = ppython("main::demo",$_POST['username'],$_POST['password'],$_POST['sel_mode']);
        var_dump($ret);
    }
?>
