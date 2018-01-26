<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>信息查询结果</title>
<link rel="stylesheet" href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css">  
<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
 <style>
        body 
	{
          padding-top: 40px;
          padding-bottom: 40px;
          background-image: url("bg2.jpg");
	  background-size:100% 100% 
	}
        .form-signin 
	{
          max-width: 1024px;
          padding: 40px;
          margin: 0 auto;
        }		
    </style>
</head>
<body>

<?php
require('php_python.php');
if($_POST['username'] == '' || $_POST['password'] == '')
{
    echo("用户名或密码不能为空");
}else
{
    $ret = ppython("main::demo",$_POST['username'],$_POST['password'],$_POST['sel_mode']);
    //var_dump($ret);
}
?>
<div class="container">
	<div class="row clearfix">

		<div class="col-md-12 column form-signin ">
				<div class="panel panel-info">
    	<div class="panel-heading">
			<h2>
				信息查询结果Demo beta1.0
			</h2>
			<p><h3>
			</h3></p>
            <p><h5>
                <?php
                    echo("数据查询时间：".date("Y年m月d日 H时i分s秒",time()));
                ?>
            </h5></p>
        </div>
         <div class="panel-body">
			<table class="table table-responsive table-bordered">
				<thead>
                <?php
                    if($ret == NULL) {
                        echo("<h4>没有查询到您的成绩，请确认您的信息填写正确。</h4>");
                    }else{
                        $arrlen = count($ret[0]);
                        if($arrlen== 3){
                            $headstr = "<tr><td>时间</td><td>考试科目</td><td>分数</td></tr>";
                            print($headstr);
                        }else if($arrlen == 7 || (($arrlen - 7) % 5) == 0){
			    $arrlen = 7;
                            $headstr = "<tr><td>课程代号</td><td>课程名称</td><td>上课时间</td><td>周次</td><td>上课时间</td><td>上课地点</td><td>任课教师</td></tr>";
                            print($headstr);
                        }else if($arrlen == 10 || $arrlen == 11)
                        {
                            $headstr = "<tr><td>年度</td><td>季度</td><td>课程代号</td><td>课程名称</td><td>课程平台</td><td>课程性质</td><td>平时成绩</td><td>考核成绩</td><td>总评成绩</td><td>考试性质</td><td>考试状态</td></tr>";
                            print($headstr);
                        }else if($arrlen == 8){
                            $headstr ="<tr><td>课程代号</td><td>课程名称</td><td>年度</td><td>季度</td><td>成绩</td><td>等级</td><td>学分</td><td绩点</td></tr>";
                            print($headstr);
                        }
                    }
                ?>

				</thead>
               <tbody>
                <?php
                    if($ret == NULL)
                    {
                        return;
                    }else{
                  
                            for($i = 0;$i < count($ret);$i++){
                                $rowstr = "<tr>";
                                $colstr = "";
			        $countret = count($ret[$i]);
                                for($j = 0;$j < $countret;$j++){
                                    $tempstr = "<td>";
                                    if($arrlen == 7 && $j != 0 && $j % $arrlen == 0 )
				    { 
                                         //$colstr.=$tempstr; 
                                         print($rowstr.$colstr."</tr>");
                                         $colstr="<td>".$ret[$i][0]."</td><td>".$ret[$i][1]."</td>";
                                    }                                 
                                    if($arrlen == 8)
                                    {
                                        if($j == 1){
                                            $tempstr.= $ret[$i][2]."</td>";
                                            $colstr.= $tempstr;
                                            continue;
                                        }else if($j == 2){
                                            $tempstr.= $ret[$i][3]."</td>";
                                            $colstr.= $tempstr;
                                            continue;
                                        }else if($j == 3){
                                            $tempstr.= $ret[$i][4]."</td>";
                                            $colstr.= $tempstr;
                                            continue;
                                        }else if($j == 4){
                                            $tempstr.= $ret[$i][1]."</td>";
                                            $colstr.= $tempstr;
                                            continue;
                                        }

                                    }
                                    if(count($ret[$i]) == 10 && $j == 6){
                                        $tempstr.= " </td><td>";
                                    }
                                    if(count($ret[$i])==13 &&($j==7 || $j==8)){
                                        continue;
                                     }
                                    $tempstr.= $ret[$i][$j]."</td>";
                                    $colstr.= $tempstr;
                                }
                                $rowstr.=$colstr."<tr/>";
                                print($rowstr);
                            }
                      //  }
                    }
                ?>

				
				</tbody>
			</table>
		</div>
	</div>
</div>
</div>
</div>
</body>
</html>
