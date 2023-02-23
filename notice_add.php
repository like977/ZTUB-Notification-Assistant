<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
<title>校务通知添加数据</title>
<meta name="author" content="yinqi">
<link href="./css/bootstrap2.css" rel="stylesheet">
<link href="./css/materialdesignicons.css" rel="stylesheet">
<link href="./css/style2.css" rel="stylesheet">

<style>
.lyear-wrapper {
    position: relative;
}
.lyear-login {
    display: flex !important;
    min-height: 100vh;
    align-items: center !important;
    justify-content: center !important;
}
.login-center {
    background: #fff;
    min-width: 38.25rem;
    padding: 2.14286em 3.57143em;
    border-radius: 5px;
    margin: 2.85714em 0;
}
.login-header {
    margin-bottom: 1.5rem !important;
}
.login-center .has-feedback.feedback-left .form-control {
    padding-left: 38px;
    padding-right: 12px;
}
.login-center .has-feedback.feedback-left .form-control-feedback {
    left: 0;
    right: auto;
    width: 38px;
    height: 38px;
    line-height: 38px;
    z-index: 4;
    color: #dcdcdc;
}
.login-center .has-feedback.feedback-left.row .form-control-feedback {
    left: 15px;
}
</style>


</head>

<body>
<div class="row lyear-wrapper">
  <div class="lyear-login">
    <div class="login-center">
    <form action="" method="POST" class="form-horizontal">

      <div class="login-header text-center">
        <h3>新增数据</h3>
      </div>

        <div class="form-group has-feedback feedback-left">
          <input type="text" name="name" placeholder="姓名" class="form-control"/>
          <span class="mdi mdi-account form-control-feedback" aria-hidden="true"></span>
        </div>

        <div class="form-group has-feedback feedback-left">
          <input type="text" name="number" value="" placeholder="手机号(必填)" class="form-control"/>
          <span class="mdi mdi-account form-control-feedback" aria-hidden="true"></span>
        </div>

        <div class="form-group has-feedback feedback-left">
          <input type="text" name="token" placeholder="Token(必填)" class="form-control"/>
          <span class="mdi mdi-account form-control-feedback" aria-hidden="true"></span>
        </div>

        <div class="form-group has-feedback feedback-left row">

        <button class="btn btn-block btn-primary  type="submit" value="添加" name="updata_data">添加</button>
        </div>
    </div>
  </div>
</div>
<?php
    session_start();

    include("./config.php");
    $link = mysqli_connect($dbconfig['host'],$dbconfig['user'],$dbconfig['pwd'],$dbconfig['dbname'],$dbconfig['port']);

    if(!$link){
      exit('数据库连接失败！');
    }

    if(!empty($_POST["updata_data"])){
      $name = $_POST["name"];
      $number = $_POST["number"];
      $token = $_POST["token"];
      mysqli_query($link,"insert Notice (user,user_id,user_token) values ('$name','$number','$token')");
      echo '<script>
          if (confirm("添加成功！是否继续添加？") == true){
            location.href="index.php";
                                      }
          </script>';
    }
      mysqli_close($link);
?>
</form>
</body>
</html>