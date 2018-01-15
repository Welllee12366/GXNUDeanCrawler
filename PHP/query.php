<?php
    header('Content-type: text/html; charset=GBK');
    function demo()
    {
        if($_POST['username'] == NULL || $_POST['password'] == NULL)
        {
            echo("用户名密码不能为空，请重试！\n");
        }else
        {
            $cmd = "C:\Users\WELLL\AppData\Local\Programs\Python\Python36\python.exe C:\Users\WELLL\PycharmProjects\DeanCrawler_beta0.1\python\main.py ".$_POST["username"]." ".$_POST["password"]." ".$_POST['sel_mode'];
            exec($cmd,$output,$status);
            var_dump($output);

        }
    }
    demo()
?>